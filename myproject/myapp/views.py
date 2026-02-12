from django.shortcuts import render,redirect
from myapp.models import Book
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def register_Book(request):
    if request.method == 'POST':
        if request.POST.get('Register') == 'Register':
            name = request.POST.get('USERNAME')
            password = request.POST.get('PASSWORD')
            
            if User.objects.filter(username = name).exists():
                return redirect('register')
            
            User.objects.create_user(username=name,password=password)
            return redirect('login')

    return render(request,'register.html')

def login_book(request):
    if request.method == 'POST':
        if request.POST.get('Login') == 'Login':
             name = request.POST.get('USERNAME')
             password = request.POST.get('PASSWORD')

             if not User.objects.filter(username=name):
                 return redirect('login')
             
             userdetail = authenticate(request,username = name,password=password)

             if userdetail is None:
                 return redirect('login')
             else:
                 login(request,userdetail)
                 return redirect('index')

    return render(request,'login.html')


def logout_book(request):
    if request.method == 'POST':
        if request.POST.get('Logout')=='Logout':
            print('hello i m inside')
            logout(request)
    
    return redirect('index')

    


@login_required(login_url='login')
def showBook(request):
    if request.method == 'POST':
        if request.POST.get('Add') == 'Add':
            firstname= request.POST.get('name')
            secondname = request.POST.get('author')
            thirdname = request.POST.get('price')
            Book.objects.create(bookName=firstname,bookAuthor=secondname,bookPrice=thirdname)

        if request.POST.get('delete') == 'Delete ALL':
            Book.objects.all().delete()


    
    books = Book.objects.all()
    return render(request,'index.html',{'Books':books})

@login_required(login_url='login')
def deleteBook(request,id):
    if request.method == 'POST':
         Book.objects.filter(id=id).delete()
    return redirect('index')

@login_required(login_url='login')
def updateBook(request,id):
    if request.method == 'POST':    
        firstname= request.POST.get('name')
        secondname = request.POST.get('author')
        thirdname = request.POST.get('price')
        Book.objects.filter(id=id).update(bookName=firstname,bookAuthor=secondname,bookPrice=thirdname)
        return redirect('index')
    
    books = Book.objects.filter(id=id).get()
    return render(request,'update.html',{'Books':books})