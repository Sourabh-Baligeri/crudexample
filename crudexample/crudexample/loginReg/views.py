from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def register(request):
    if request.method == "POST":
        # To Create a User
        if request.POST['password'] == request.POST['passwordagain']:
            # Both the password matched
            # check if a previous user exists
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'register.html',{'error':"Email already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                return redirect('/')
        else:
            return render(request, 'register.html',{'error':"Password not match"})


    return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get['username']
        password = request.POST.get['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/welcome')
        else:
            return render(request, 'login.html',{'error':"Invalid Credentials, Please TryAgain"})
    return render(request, 'login.html')
def welcomepage(request):
    return render(request, 'welcome.html')