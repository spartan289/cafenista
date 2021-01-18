from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from telusko.settings import EMAIL_HOST_USER
import random

# Create your views here.
l = ['vmrqea', 'ugnhlg', 'ffjiov', 'zndudf', 'oavysn', 'efqnvl', 'nfpwuw', 'tpgnlk', 'xtdxnt', 'phsvsn', 'lhzxzp', 'basinb', 'hqcpai', 'vzktji', 'sbdtqa', 'samnjg', 'tdherk', 'zuaalc', 'lqovmz', 'gngawo', 'lgyljd', 'orzucb', 'shgtya', 'ufdixa', 'aztjnr', 'wxzjjx', 'ucwpwr', 'htlulr', 'oqszpz', 'npgkkz', 'isivvm', 'anouxk', 'hwgpfv', 'vbjtyd', 'xguqzz', 'fuchir', 'bjvklu', 'bmloxk', 'xgmohy', 'qgvqgw', 'nmbryl', 'txmamg', 'kjgelx', 'atclpq', 'magdsv', 'stdljf', 'zqcfia', 'ndausm', 'tiosan', 'hdeimt', 'olsxoa', 'zilhen', 'mgspeh', 'mdxfkl', 'felmsv', 'fqivvh', 'pvugfj', 'bynhyt', 'nrhxho', 'zxkxst', 'vrbqaa', 'dwluyo', 'pcnjzm', 'ibblcs', 'kqigdq', 'fulxow', 'klkccb', 'ipfqrc', 'wendqt', 'ztukhj', 'szguwq', 'mbhyuj', 'neuhhn', 'gpqdoj', 'xqgxwh', 'cvibuz', 'yswbnh', 'wcalkg', 'oxxbmy', 'kyehhc', 'asinzr', 'rhkyxq', 'limnqx', 'qdrwwb', 'vsjuur', 'slixup', 'efbgxx', 'mstkyp', 'vatamp', 'tlerlf', 'ltiooo', 'kwsgoz', 'aobels', 'rphvsp', 'wzpzvg', 'dpaiev', 'rzlobd', 'vquhfp', 'mkiygj', 'hhsslb']

x = random.choice(l) 


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
            else:
                user = User.objects.create_user(username=username, password = password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def forget_pass(request):
    if request.method == 'POST':
        
        email = request.POST['email']
        request.session['email'] = email
        subject = 'Welcome to dupost'
        message = 'Enter the code {} '.format(x)

        send_mail(subject,message, EMAIL_HOST_USER, [email], fail_silently=False)
        messages.info(request,'Message sent')
        return redirect('verify')
    else:       
        return render(request,'forget.html')
 
def verify(request):
    if request.method == 'POST':
        verification = request.POST['verification']

        for i in l:
            if verification == i:
                 messages.info(request,'Verified')
        return redirect('reset')
    else:
        return render(request,'verify.html')
def reset(request):
        if request.method == 'POST':
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.session['email']
            print(email)
            if password1 == password2:
                a = User.objects.get(email=email)
                a.set_password(password1)
                a.save()
                
                
                return redirect('/')
        else:
            return render(request, 'reset.html')


    


    