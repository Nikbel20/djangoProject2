import asyncio
import random
from turtle import pd

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django import forms

from acs.forms import ImageForm
from acs.models import ModelReg, Img



@csrf_exempt
def index(request):
    if request.method == 'POST':pass
       # asyncio.run(main()) #запуск бота
    return render(request, 'index.html')

user_info = {"":False}

@csrf_exempt
def register(request):
    reg = ModelReg()

    if request.method == 'POST':
        data = ModelReg.objects.all()
        for i in data:
            if request.POST['email'] == i.email:
                return render(request, 'index.html', {"err": f'Email: {i.email} занят другим пользователем'})
        reg.email = request.POST['email']
        reg.password = request.POST['password']
        reg.login = request.POST['login']
        reg.save()
        return HttpResponse(f'Пользователь с Email: {reg.email} успешно зарегистрирован!')
    return render(request, 'login.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = ModelReg.objects.all()
        print(data)
        print(f"Из пост запроса. Почта: {request.POST['email']} Pass: {request.POST['password']}")
        for i in data:
            print(f'Текущий объект из базы данных. Почта: {i.email} Pass: {i.password}')
            if request.POST['email'] == i.email and request.POST['password'] == i.password:
                user_login = request.POST['email']
                user_info[user_login] = True
                html = redirect('/profile', {'user': user_login})
                html.set_cookie('isAuth', user_login)
                return html

        return render(request, 'index.html', {'err': 'авторизация не пройдена'})
    return render(request, 'author.html')

@csrf_exempt
def testo(request):
    if request.method == 'POST':
        if request.POST['login'] == 'Egor' and request.POST['pass'] == '123123':
            return render(request, 'testo2.html', {'form': 'Авторизация пройдена!'})
        else:
            return render(request, 'testo2.html', {'form': 'Неверный логин или пароль!'})
    else:
        form = ImageForm()
    regs = ModelReg.objects.all().values() #получаем все значение у строк из таблицы бд
    arr = [random.randint(1, 100) for i in range(10)]
    return render(request, 'testo2.html', {'name': regs})

@csrf_exempt
def profile(request):
    if request.method == 'POST':
        html = redirect('/')
        html.delete_cookie('isAuth')
        return html
    r = ''
    try: r = request.COOKIES['isAuth']
    except: return redirect('/')
    return render(request, 'profile.html', {'user':request.COOKIES['isAuth']})

class ImageForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ('img', 'name')

@csrf_exempt
def img_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            fname = request.FILES['img'].name
            form.save()
            added_image = Img.objects.last()
            df = pd.DataFrame(Img.objects.all().values())
            df.to_excel('./images.xlsx')

            return render(request, 'form.html', {'form': form, 'image': added_image, 'fname': fname})
    else:
        form = ImageForm()
    return render(request, 'form.html', {'form': form})
