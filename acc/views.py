from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password
from .models import User
from django.contrib import messages

# Create your views here.

def ckpw(request):
    u = request.user
    ck = request.POST.get("ckpw")
    if check_password(ck, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        pass        # 20 일차 메세지
    return redirect("acc:profile")

def changepw(request):
    cp = request.POST.get("cpass")
    if check_password(cp, request.user.password):
        np = request.POST.get("npass")
        request.user.set_password(np)
        request.user.save()
        return redirect("acc:login")
    else:
        messages.info(request, "패스워드가 바꼈습니다. 다시 로그인해주세요")
    return redirect("acc:update")

def update(request):
    if request.method == "POST":
        u = request.user
        ue = request.POST.get("umail")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        u.email, u.comment = ue, uc
        if pi:
            u.pic.delete()
            u.pic = pi
        u.save()
        return redirect("acc:profile")
    return render(request, "acc/update.html")

def profile(request):
    return render(request, "acc/profile.html")

def signup(request):
    if request.method=="POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucom")
        upi = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, comment=uc, pic=upi).save()
            return redirect("acc:login")
        except:
            pass
    return render(request, "acc/signup.html")

def userlogout(request):
    logout(request)     # request 에서 레코드 빼냄
    return redirect("acc:index")

def index(request):
    return render(request, "acc/index.html")

def userlogin(request):
    if request.method=="POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:       # 로그인 성공시
            login(request, u)       # request 에 u 레코드를 실어줌
            messages.success(request, f"{u}!! WELCOME")
            return redirect("acc:index")
        else:
            messages.error(request, "LOGIN FAILURE")
    return render(request, "acc/login.html")