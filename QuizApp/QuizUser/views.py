from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import quiz_que


# Create your views here.
def home(request):
	return render(request, 'QuizUser/home.html')

def quiz(request):
    questions = quiz_que.objects.filter(qno='1')
    return render(request, 'QuizUser/quiz.html', {'questions':questions})


    

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        password2 = request.POST.get('psw2')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username has been taken')
                return render(request,'QuizUser/login.html')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email has been taken')
                return render(request, 'QuizUser/register.html')
                
            else:
                Data = User.objects.create_user(username=username, email=email, password=password)
                Data.save()
                messages.info(request, 'Account has been created')
                return render(request, 'QuizUser/login.html')
        else:
            messages.info(request,'Passwords are not same, please try again')
            return render(request, 'QuizUser/register.html')
    else:
        return render(request,'QuizUser/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,'QuizUser/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')