import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.core.mail import send_mail
from django.contrib.auth import logout


# Create your views here.
def register(request):
    if request.method == 'POST':
        a = regform1(request.POST, request.FILES)
        if a.is_valid():
            fn = a.cleaned_data['fname']
            ln = a.cleaned_data['lname']
            un = a.cleaned_data['uname']
            nm = a.cleaned_data['num']
            em = a.cleaned_data['em']
            im = a.cleaned_data['im']
            ps = a.cleaned_data['pin']
            cps = a.cleaned_data['cpin']
            ac_num = int("15" + str(nm))  # concantination
            if ps == cps:
                b = regmod1(fname=fn, lname=ln, uname=un, num=nm, em=em, im=im, pin=ps, balance=0, ac_num=ac_num)
                b.save()
                subject = '$$$ YOUR ACCOUNT HAS BEEN CREATED $$$'
                message = f'YOUR NEW ACCOUNT NUMBER IS {ac_num}'  # formatter used for variable recognition
                email_from = "techymech23@gmail.com"
                email_to = 'bensonpm333@gmail.com'
                send_mail(subject, message, email_from, [email_to])
                return redirect(login)
            else:
                return HttpResponse('PASSWORD MISMATCH !')
        else:
            return HttpResponse('REGISTRATION FAILED !!!')
    return render(request, 'reg.html')


def login(request):
    if request.method == 'POST':
        a = logform1(request.POST)
        if a.is_valid():
            un = a.cleaned_data['uname']
            ps = a.cleaned_data['pswd']

            b = regmod1.objects.all()
            for i in b:
                if i.uname == un and i.pin == ps:
                    request.session['id'] = i.id  # global calling  (global variable-->request.session['id])
                    return redirect(profile)
            else:
                return HttpResponse('Password missmatch')
        else:
            return HttpResponse('INVALID')
    return render(request, 'login.html')


def ind(request):
    return render(request, 'index.html')


def profile(request):
    try:
        id1 = request.session['id']
        a = regmod1.objects.get(id=id1)
        im = str(a.im).split('/')[-1]  # splitting file path
        return render(request, 'profile.html', {'a': a, 'im': im})
    except:
        return redirect(login)


# register cheyth login cheythaal maathrai work aaku  ****


def editbank(request, id):
    a = regmod1.objects.get(id=id)
    if request.method == 'POST':
        a.fname = request.POST.get('fname')
        a.lname = request.POST.get('lname')
        a.uname = request.POST.get('uname')
        a.num = request.POST.get('num')
        a.em = request.POST.get('em')
        a.pin = request.POST.get('pin')
        a.save()
        return redirect(profile)
    return render(request, 'bankedit.html', {'a': a})


def editim(request, id):
    a = regmod1.objects.get(id=id)
    im = str(a.im).split('/')[-1]
    if request.method == 'POST':
        a.uname = request.POST.get('uname')
        if len(request.FILES) != 0:
            if len(a.im) > 0:
                os.remove(a.im.path)
            a.im = request.FILES['im']
        a.save()
        # return redirect(profile)
    return render(request, 'imgedit.html', {'a': a, 'im': im})


def addmoney(request, id):
    x = regmod1.objects.get(id=id)
    if request.method == 'POST':
        am = request.POST.get('amount')
        request.session['am'] = am

        request.session['ac_num'] = x.ac_num

        x.balance += int(am)
        x.save()

        b = addamount(amount=am, uid=request.session['id'])  # ministatement
        b.save()

        pin = request.POST.get('pin')
        if pin == x.pin:  # converting pin to integer field here ### nomore needed
            return redirect(success)
        else:
            return HttpResponse('AMOUNT ADDED FAILURE....!')
    return render(request, 'addamount.html')


def success(request):
    am = request.session['am']
    ac = request.session['ac_num']
    return render(request, 'success.html', {'am': am, 'ac_num': ac})


def widrawmoney(request, id):
    x = regmod1.objects.get(id=id)
    if request.method == 'POST':
        am = request.POST.get('amount')  # withot form
        request.session['am'] = am
        request.session['ac'] = x.ac_num
        if (x.balance >= int(am)):
            x.balance -= int(am)
            x.save()
            b = withdrawamount(amount=am, uid=request.session['id'])
            b.save()
            pin = request.POST.get('pin')
            if pin == x.pin:

                return redirect(widrawsuccess)
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse('Insufficient Balance')

    return render(request, 'withdrawamount.html')


def widrawsuccess(request):
    am = request.session['am']
    ac = request.session['ac_num']
    return render(request, 'withdraw success.html', {'am': am, 'ac_num': ac})


def balance(request, id):
    a = regmod1.objects.get(id=id)
    if request.method == 'POST':
        request.session['balance'] = a.balance
        request.session['ac_num'] = a.ac_num
        pin = request.POST.get('pin')
        if pin == a.pin:
            return redirect(baldis)
        else:
            return HttpResponse('Invalid!!!')

    return render(request, 'checkbalance.html')


def baldis(request):
    balance = request.session['balance']
    ac_num = request.session['ac_num']
    return render(request, 'balancedisplay.html', {'ac_num': ac_num, 'balance': balance})


def ministatement(request, id):
    x = regmod1.objects.get(id=id)
    pin = request.POST.get('pin')
    if request.method == 'POST':
        if pin == x.pin:
            choice = request.POST.get('statement')
            if choice == 'deposit':
                return redirect(deposit)
            elif choice == 'withdraw':
                return redirect(withdrawmini)
        else:
            return HttpResponse('PASSWORD INCORRECT !!!')

    return render(request, 'mini.html')


def deposit(request):
    x = addamount.objects.all()
    id = request.session['id']
    return render(request, 'depo.html', {'x': x, 'id': id})


def withdrawmini(request):
    x = withdrawamount.objects.all()
    id = request.session['id']
    return render(request, 'widmini.html', {'x': x, 'id': id})


def news(request):
    if request.method == 'POST':
        a = newsform(request.POST, request.FILES)
        if a.is_valid():
            to = a.cleaned_data['topic']
            cnt = a.cleaned_data['content']
            b = newsmodel(topic=to, content=cnt)
            b.save()
            return redirect(newsdisp)
        else:
            return HttpResponse('FAILURE!!!')
    return render(request, 'news.html')


def adminlogin(request):
    if request.method == 'POST':
        a = adminform(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']

            ps = a.cleaned_data['password']
            user = authenticate(request, username=us, password=ps)
            if user is not None:
                return redirect(adminprofile)
            else:
                return HttpResponse('Failed !!')

    return render(request, 'adminlogin.html')


def adminprofile(request):
    return render(request, 'adminprofile.html')


def newsdisp(request):  # admin
    a = newsmodel.objects.all()
    return render(request, 'newsdisp.html', {'a': a})


def newsuser(request):
    a = newsmodel.objects.all()
    return render(request, 'newsuser.html', {'a': a})


def newsedit(request, id):
    a = newsmodel.objects.get(id=id)
    if request.method == 'POST':
        a.topic = request.POST.get('topic')
        a.content = request.POST.get('content')
        a.save()
        return redirect(newsdisp)
    return render(request, 'newsedit.html', {'a': a})


def newsdelete(request, id):
    a = newsmodel.objects.get(id=id)
    a.delete()
    return redirect(newsdisp)


def tablesearch(request):
    if request.method == 'POST':
        a = tablesform(request.POST, request.FILES)
        if a.is_valid():
            nm = a.cleaned_data['name']
            ag = a.cleaned_data['age']
            num = a.cleaned_data['number']
            b = tablesmod(name=nm, age=ag, number=num)
            b.save()
            return redirect(tabledisp)
        else:
            return HttpResponse('FAILURE!!!')
    return render(request, 'table search.html')


def tabledisp(request):
    x = tablesmod.objects.all()
    id = request.session['id']
    return render(request('tabledisplay.html', {'x': x, 'id': id}))


def wish(request, id):
    a = newsmodel.objects.get(id=id)
    a1 = wishlist.objects.all()
    for i in a1:
        if i.newsid == a.id and i.uid == request.session[
            'id']:  # wishlist ilai item equal aanennum athinte uid um login cheytha uid um equal aayaal mathram msg kaanichaal mathi
            return HttpResponse('Item already in wishlist')
    b = wishlist(topic=a.topic, content=a.content, date=a.date, newsid=a.id, uid=request.session['id'])
    b.save()
    return HttpResponse('added to wishlist')


def wishdis(request):
    try:
        a = wishlist.objects.all()
        id = request.session['id']
        return render(request, 'wishlist.html', {'a': a, 'id': id})
    except:
        return redirect(login)


# from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect(ind)


def forgot_password(request):
    a=regmod1.objects.all()
    if request.method=='POST':
        em= request.POST.get('em')
        ac= request.POST.get('ac')
        for i in a:
            if(i.em==em and i.ac_num==int(ac)):

                id=i.id
                subject="Password Change"
                message=f"http://127.0.0.1:8000/bank_app/change/{id}"
                # message="Renew your password"
                frm="techymech23@gmail.com"
                to=em
                send_mail(subject,message,frm,[to])
                return HttpResponse("Check Your E-mail")
        else:
            return HttpResponse("Sorry, Some Error Occured")
    return render(request,'forgotpassword.html')


def change_password(request,id):
    a=regmod1.objects.get(id=id)
    if request.method=='POST':
        p1=request.POST.get('pin')
        p2=request.POST.get('repin')
        if p1==p2:
            a.pin=p1
            a.save()
            return HttpResponse('Password changed')
        else:
            return HttpResponse('Sorry!!')
    return render(request,'change.html')

