from .models import Destination
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from telusko.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def index(request):
    dests = Destination.objects.all()


    return render(request, 'index.html', {'dests': dests})

def ex_list(request):
    
    ls=[]
    y=0
    if request.POST:
            selected_values = request.POST.getlist('exlist[]')
            
            quantity = request.POST.getlist('quantity')
            print(selected_values)
            print(quantity)
            
            
            name=[]
            price=[]
            q=[]

            for i in selected_values:
                dest = Destination.objects.filter(price=i).order_by('id').first()
                name.append(dest.name)
                price.append(dest.price)
                for j in range(len(quantity)):
                    if j==dest.pk:
                        q.append(quantity[j])
                        x = int(i)
                        y = y+x*int(quantity[j])
            
            team_info = zip(name, price, q)
            html_message = render_to_string('table.html', {'dest': dest, 'team_info':team_info,'y': y})
            print(y)
            print(ls)
            if User.is_active:
                subject='Your total food value is {}'.format(y)
                plain_message = strip_tags(html_message)
                message = 'List Sended'
                send_mail(subject,plain_message, EMAIL_HOST_USER, [request.user.email],html_message=html_message, fail_silently=False)
       
            
            return redirect('email_to_be_sent')
            
    return render(request, 'index.html')
def email_to_be_sent(request):
    return render(request, 'emails.html')
        
            