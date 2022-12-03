from .serializers import UserSerializer
from rest_framework import routers, serializers, viewsets
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .models import *

from django.contrib.auth.hashers import make_password, check_password


def index(request):
    if request.method == "POST":
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus')

        cart_id = request.session.get('cart')
        print("-------------", cart_id)

        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity - 1
                else:
                    cart_id[product_id] = quantity + 1

            else:
                cart_id[product_id] = 1
        else:
            cart_id = {}
            cart_id[product_id] = 1

        request.session["cart"] = cart_id
        print("------------", request.session['cart'])

    cat_id = request.GET.get('cat_id')

    cate = category.objects.all()

    if cat_id:
        pro = Product.objects.filter(category=cat_id)
    else:

        pro = Product.objects.all()

    context = {
        'category': cate,
        'pro': pro
    }

    return render(request, 'home.html', context=context)


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == "POST":
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('Email')
        password = request.POST.get('pwd')
        mobile = request.POST.get('mbl')
        gender = request.POST.get('gen')

        s = Registration(
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=make_password(password),
            mobile=mobile,
            gender=gender
        )

        s.save()
        return HttpResponse("data saved successfully")


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')

        try:
            fetch_obj = Registration.objects.get(email=email)
            # if check_password(password, fetch_obj.password):
            request.session['name'] = fetch_obj.first_name
            request.session['customer_id'] = fetch_obj.id

            return redirect('home')

            return HttpResponse("login successfull")
            # else:
            # return HttpResponse('enter a vlid password')

        except:
            return HttpResponse("please enter a valid email.....")


def Logout(request):
    request.session.clear()
    return redirect('home')


def cart_info(request):

    keys = list(request.session['cart'].keys())
    c = Product.objects.filter(id__in=keys)
    return render(request, 'cart.html', {'cartdt': c})


def checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        mobile = request.POST.get('mbl')
        customer_id = request.session.get('customer_id')
        if not customer_id:
            return HttpResponse("please login")
        cart = request.session.get('cart')
        products = Product.objects.filter(id__in=list(cart.keys()))
        for i in products:
            obj = Order_details(
                address=address,
                mobile=mobile,
                customer=Registration(id=customer_id),
                price=i.price,
                product=Product(id=i.id),
                Quantity=cart.get(str(i.id)),


            )
            obj.save()
        request.session['cart']

        return redirect('order')


def order(request):
    id = request.session.get('customer_id')

    fetch_pro = Order_details.objects.filter(customer=id)

    tp = 0

    for i in fetch_pro:
        tp = tp + (i.price * i.Quantity)

    return render(request, 'order.html', {'fetch_product': fetch_pro, 'tp': tp})


class UserViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = UserSerializer
