from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Account_Details, Birthday_cake,Anniversary_cake,Designer_cake,Normal_cake,Eggless_cake, Order,Trend_cake,Photo_cake,Passion_cake,Cartoon_cake
from .models import Filmy_cake,Chocolate_cake,Venilla_cake,Black_cur_cake,Pine_cake,Red_cake,Blue_cake
from  django .contrib import messages


def index(request):
  return render(request, 'index.html')

def normal_cake(request):
  return render(request, 'normal_cake.html')

def eggless(request):
  return render(request, 'eggless.html')

def contact(request):
  return render(request, 'contact.html')

def birth(request):
  return render(request, 'birth.html')

def anniversary(request):
  return render(request, 'anniversary.html')

def design(request):
  return render(request, 'design.html')

def trend(request):
  return render(request, 'trend.html')

def photo(request):
  return render(request, 'photo.html')

def passion(request):
  return render(request, 'passion.html')

def cartoon(request):
  return render(request, 'cartoon.html')

def filmy(request):
  return render(request, 'filmy.html')

def chocolate(request):
  return render(request, 'chocolate.html')

def venilla(request):
  return render(request, 'venilla.html')

def black_cur(request):
  return render(request, 'black_cur.html')

def pine(request):
  return render(request, 'pine.html')

def red(request):
  return render(request, 'red.html')

def blue(request):
  return render(request, 'blue.html')

def order(request):
  if request.method == 'POST':
        # Process the form submission here
        # ...

        # Redirect to the order page with a success flag
        return HttpResponseRedirect(f"{reverse('order')}?success=true")

  return render(request, 'order.html')

def login(request):
  return render(request, 'login.html')

def welcome(request):
  return render(request, 'welcome.html')


def normal_cake(request):
  normal_cake_var=Normal_cake.objects.all()
  return render(request, 'normal_cake.html', {'normal_cake_var': normal_cake_var})

def eggless(request):
  eggless_cake_var=Eggless_cake.objects.all()
  return render(request, 'eggless.html', {'eggless_cake_var': eggless_cake_var})

def birth(request):
  birthday_cake_var=Birthday_cake.objects.all()
  return render(request, 'birth.html', {'birthday_cake_var': birthday_cake_var})

def anniversary(request):
  anniversary_cake_var=Anniversary_cake.objects.all()
  return render(request, 'anniversary.html', {'anniversary_cake_var': anniversary_cake_var})

def design(request):
  designer_cake_var=Designer_cake.objects.all()
  return render(request, 'design.html', {'designer_cake_var': designer_cake_var})

def trend(request):
  trend_cake_var=Trend_cake.objects.all()
  return render(request, 'trend.html', {'trend_cake_var': trend_cake_var})

def photo(request):
  photo_cake_var=Photo_cake.objects.all()
  return render(request, 'photo.html', {'photo_cake_var': photo_cake_var})

def passion(request):
  passion_cake_var=Passion_cake.objects.all()
  return render(request, 'passion.html', {'passion_cake_var': passion_cake_var})

def cartoon(request):
  cartoon_cake_var=Cartoon_cake.objects.all()
  return render(request, 'cartoon.html', {'cartoon_cake_var': cartoon_cake_var})

def filmy(request):
  filmy_cake_var=Filmy_cake.objects.all()
  return render(request, 'filmy.html', {'filmy_cake_var': filmy_cake_var})

def chocolate(request):
  chocolate_cake_var=Chocolate_cake.objects.all()
  return render(request, 'chocolate.html', {'chocolate_cake_var': chocolate_cake_var})

def venilla(request):
  venilla_cake_var=Venilla_cake.objects.all()
  return render(request, 'venilla.html', {'venilla_cake_var': venilla_cake_var})

def black_cur(request):
  black_cur_cake_var=Black_cur_cake.objects.all()
  return render(request, 'black_cur.html', {'black_cur_cake_var': black_cur_cake_var})

def pine(request):
  pine_cake_var=Pine_cake.objects.all()
  return render(request, 'pine.html', {'pine_cake_var': pine_cake_var})

def red(request):
  red_cake_var=Red_cake.objects.all()
  return render(request, 'red.html', {'red_cake_var': red_cake_var})

def blue(request):
  blue_cake_var=Blue_cake.objects.all()
  return render(request, 'blue.html', {'blue_cake_var': blue_cake_var})

def SignInSuccess(request):
    return render(request,'sign_in_success.html')

def SignUnSuccess(request):
    return render(request,'sign_in_unsuccess.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
       
        
        account_details = Account_Details(
            name=name,
            Email=email,
            Contact_no=contact,
            Password=password
        )
        
        account_details.save()
        \
        return redirect(index)
    
    return render(request, 'sign_up.html')



def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(name, password)
        try:
            account = Account_Details.objects.get(name=name,Password=password)
            print(account)
        except Account_Details.DoesNotExist:
            account = None
        if account is not None and account.Password == password:
            return render(request, 'index.html')
        else:
            messages.error(request,'Invaid Login')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def order(request):
    if request.method == 'POST':
        print(request.POST)  # Print form data for debugging

        cake_name = request.POST.get('cake_name')
        cake_price = request.POST.get('cake_price')
        name=request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')

        print(cake_name, cake_price, contact, address)  # Print extracted data for debugging

        # Save the order to the database
        Order.objects.create(
            cake_name=cake_name,
            cake_price=cake_price,
            name=name,
            contact=contact,
            address=address
        )

        # Redirect to the order page with a success flag
        return redirect('order')

    return render(request, 'order.html')
  

