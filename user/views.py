from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import authenticate,login, decorators, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm
from .models import User
from order.models import Order, Cart, Voucher, Shipment, Payment, Credit, Cash, Tranfer
from shoes.models import ShoesItem
from book.models import BookItem
from electronic.models import ElectronicItem
# Create your views here.


class LoginClass(View):
    def get(self, request):
        return render(request, 'page/login.html')
    def post(self, request):
        username = request.POST.get('username')
        matkhau = request.POST.get('password')
        my_user = authenticate(username=username, password=matkhau)
        if my_user is None:
            return render(request, 'page/login.html', {'msg' : 'Sai tai khoan hoac mat khau'})
        login(request, my_user)
        return redirect('/')


class IndexClass(View):
    def get(self, request):
        listBook = BookItem.objects.filter(isPay = 'False').order_by('-id')[0:18]
        listElectronic = ElectronicItem.objects.filter(isPay = 'False').order_by('-id')[0:18]
        listShoes = ShoesItem.objects.filter(isPay = 'False').order_by('-id')[0:18]
        if request.user.id is not None:
            order = Order.objects.get(user_id=request.user.id, status='new')
            cart = Cart.objects.get(order_id=order.id)
            return render(request, 'page/index.html', {'listBook': listBook, 'listElectronic': listElectronic,
                                                       'listShoes':listShoes, 'cart': cart})
        else:
            return render(request, 'page/index.html', {'listBook': listBook, 'listElectronic': listElectronic,
                                                       'listShoes': listShoes})


class RegisterClass(View):
    def get(self, request):
        return render(request, 'page/register.html')
    def post(self, request):
        f = RegisterForm(request.POST)
        if not f.is_valid():
            return render(request, 'page/register.html', {'msg':"Nhap sai thong tin!"})
        password = request.POST.get('password')
        rePassword = request.POST.get('rePassword')
        if password != rePassword:
            return render(request, 'page/register.html', {'msg':"Mat Khau Khong Khop!"})
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        username = request.POST.get('username')
        user = User.objects.create_user(
            first_name = firstname,
            last_name = lastname,
            phone = phone,
            username = username,
            password = password,
        )
        order = Order.objects.create(
            status = 'new',
            user = user
        )
        cart = Cart.objects.create(
            order = order
        )
        login(request, user)
        return redirect('/')


class LogoutClass(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class ProductClass(View, type):
    def get(self, request):
        if type == "bookitem":
            listBook = BookItem.objects.all()
            return render(request, 'page/product.html', {'product': listBook})
        if type == "electronicitem":
            listElectronic = ElectronicItem.objects.all()
            return render(request, 'page/product.html', {'product': listElectronic})
        if type == "bookitem":
            listShoes = ShoesItem.objects.all()
            return render(request, 'page/product.html',{'product': listShoes})


@decorators.login_required(login_url='/login/')
def addItemToCart(request, type, id):
    order = Order.objects.get(user_id=request.user.id, status='new')
    cart = Cart.objects.get(order_id=order.id)
    kt = 0
    if type == 'shoesitem':
        listShoes = ShoesItem.objects.filter(cart=cart, pk=id)
        if len(listShoes) > 0:
            kt = 2
        else:
            shoesItem = ShoesItem.objects.get(pk=id)
            cart.shoesItem.add(shoesItem)
            cart.quantity = cart.quantity+1
            cart.totalPrice = cart.totalPrice + shoesItem.price*(1-shoesItem.discount)
            cart.save()
            kt = 1
    if type == 'electronicitem':
        listElectronicItem = ElectronicItem.objects.filter(cart = cart, pk=id)
        if len(listElectronicItem) > 0:
            kt = 2
        else:
            electronicItem = ElectronicItem.objects.get(pk=id)
            cart.electronicItem.add(electronicItem)
            cart.quantity = cart.quantity + 1
            cart.totalPrice = cart.totalPrice + electronicItem.price*(1-electronicItem.discount)
            cart.save()
            kt = 1
    if type == 'bookitem':
        listBook = BookItem.objects.filter(cart=cart, pk=id)
        if len(listBook) > 0:
            kt = 2
        else:
            bookItem = BookItem.objects.get(pk=id)
            cart.bookItem.add(bookItem)
            cart.quantity = cart.quantity + 1
            cart.totalPrice = cart.totalPrice + bookItem.price*(1-bookItem.discount)
            cart.save()
            kt = 1
    listBook = BookItem.objects.filter(isPay='False').order_by('-id')[0:18]
    listElectronic = ElectronicItem.objects.filter(isPay='False').order_by('-id')[0:18]
    listShoes = ShoesItem.objects.filter(isPay='False').order_by('-id')[0:18]
    order = Order.objects.get(user_id=request.user.id, status='new')
    cart = Cart.objects.get(order_id=order.id)
    return render(request, 'page/index.html', {'listBook': listBook, 'listElectronic': listElectronic,
                                               'listShoes': listShoes, 'cart': cart, 'kt': kt})

class CartClass(View):
    def get(self, request):
        order = Order.objects.get(user_id=request.user.id, status='new')
        cart = Cart.objects.get(order_id=order.id)
        listBookItem = BookItem.objects.filter(cart = cart).order_by('isPay');
        listElectronicItem = ElectronicItem.objects.filter(cart = cart).order_by('isPay');
        listShoesItem = ShoesItem.objects.filter(cart = cart).order_by('isPay');
        totalProduct = cart.quantity
        totalPrice = cart.totalPrice
        return render(request, 'page/cart.html', {'listBook': listBookItem, 'listElectronic': listElectronicItem,
                                                   'listShoes': listShoesItem, 'totalProduct': totalProduct,
                                                  'totalPrice': totalPrice})


def deleteItemFromCart(request, type, id):
    order = Order.objects.get(user_id=request.user.id, status='new')
    cart = Cart.objects.get(order_id=order.id)
    kt = 0
    if cart.quantity > 0:
        if type == 'shoesitem':
            list = ShoesItem.objects.filter(cart=cart, pk=id)
            if len(list) > 0:
                shoesItem = ShoesItem.objects.get(pk=id)
                cart.shoesItem.remove(shoesItem)
                if shoesItem.isPay == False:
                    cart.quantity = cart.quantity - 1
                    cart.totalPrice = cart.totalPrice - shoesItem.price * (1 - shoesItem.discount)
                cart.save()
                kt = 1
        if type == 'electronicitem':
            list = ElectronicItem.objects.filter(cart=cart, pk=id)
            if len(list) > 0:
                electronicItem = ElectronicItem.objects.get(pk=id)
                cart.electronicItem.remove(electronicItem)
                if electronicItem.isPay == False:
                    cart.quantity = cart.quantity - 1
                    cart.totalPrice = cart.totalPrice - electronicItem.price * (1 - electronicItem.discount)
                cart.save()
                kt = 1
        if type == 'bookitem':
            list = BookItem.objects.filter(cart=cart, pk=id)
            if len(list) > 0:
                bookItem = BookItem.objects.get(pk=id)
                cart.bookItem.remove(bookItem)
                if bookItem.isPay == False:
                    cart.quantity = cart.quantity - 1
                    cart.totalPrice = cart.totalPrice - bookItem.price * (1 - bookItem.discount)
                cart.save()
                kt = 1
    listBookItem = BookItem.objects.filter(cart=cart)
    listElectronicItem = ElectronicItem.objects.filter(cart=cart)
    listShoesItem = ShoesItem.objects.filter(cart=cart)
    totalProduct = cart.quantity
    totalPrice = cart.totalPrice
    return render(request, 'page/cart.html', {'listBook': listBookItem, 'listElectronic': listElectronicItem,
                                              'listShoes': listShoesItem, 'totalProduct': totalProduct,
                                              'totalPrice': totalPrice, 'kt': kt})


class DiscountClass(View):
    def get(self, request):
        id = request.GET.get("exits")
        order = Order.objects.get(user_id=request.user.id, status='new')
        voucher = Voucher.objects.get(pk = id)
        if (voucher is not None) and (voucher.order is None):
            return HttpResponse(voucher.discountPercent)
        else:
            return HttpResponse(0)


class Create_Order_class(View):
    def get(self, request):
        order = Order.objects.get(user_id=request.user.id, status='new')
        cart = Cart.objects.get(order_id=order.id)
        listBookItem = BookItem.objects.filter(cart=cart, isPay = False)
        listElectronicItem = ElectronicItem.objects.filter(cart=cart, isPay = False)
        listShoesItem = ShoesItem.objects.filter(cart=cart, isPay = False)
        totalProduct = cart.quantity
        totalPrice = cart.totalPrice
        return render(request, 'page/create_order.html',
                      {'listBook': listBookItem, 'listElectronic': listElectronicItem,
                       'listShoes': listShoesItem, 'totalProduct': totalProduct,
                       'totalPrice': totalPrice})
    def post(self, request):
        order = Order.objects.get(user_id=request.user.id, status='new')
        cart = Cart.objects.get(order_id=order.id)
        address = request.POST.get("address")
        shipmentType = request.POST.get("shipmentType")
        shippingFee = 0
        if shipmentType == 'fast':
            shippingFee = 50000
            shipmentType = "Vận chuyển siêu tốc"
        if shipmentType == 'quick':
            shippingFee = 40000
            shipmentType = "Vận chuyển nhanh"
        if shipmentType == 'normal':
            shippingFee = 30000
            shipmentType = "Vận chuyển tiết kiệm"
        paymentMethod = request.POST.get("paymentMethod")
        discountID = request.POST.get("discountID")
        voucher = None
        if discountID != '':
            voucher = Voucher.objects.get(pk = discountID)
        if paymentMethod == 'cash':
            paymentMethod = 'Thanh toán bằng tiền mặt'
            cashTendered = 0
            if (voucher is not None) and (voucher.order is None):
                voucher.order = order
                voucher.save()
                cashTendered += cart.totalPrice - cart.totalPrice * voucher.discountPercent + shippingFee
            else:
                cashTendered += cart.totalPrice + shippingFee
            Cash.objects.create(cashier = 'Người vận chuyển', cashTendered = cashTendered, order = order)
            Shipment.objects.create(type=shipmentType, cost=shippingFee, address=address, order=order)
            order.status = 'successful'
            order.totalAmount = cashTendered
            order.save()
            for item in BookItem.objects.filter(cart = cart):
                if item.isPay == True:
                    cart.bookItem.remove(item)
                    cart.save()
                else:
                    item.isPay = True
                    item.save()
                    listCart = Cart.objects.filter(bookItem = item)
                    for c in listCart:
                        if(c.id != cart.id):
                            c.totalPrice = c.totalPrice - item.price*(1-item.discount)
                            c.quantity = c.quantity - 1
                            c.save()
            for item in ElectronicItem.objects.filter(cart = cart):
                if item.isPay == True:
                    cart.electronicItem.remove(item)
                    cart.save()
                else:
                    item.isPay = True
                    item.save()
                    listCart = Cart.objects.filter(electronicItem=item)
                    for c in listCart:
                        if (c.id != cart.id):
                            c.totalPrice = c.totalPrice - item.price*(1-item.discount)
                            c.quantity = c.quantity - 1
                            c.save()
            for item in ShoesItem.objects.filter(cart = cart):
                if item.isPay == True:
                    cart.shoesItem.remove(item)
                    cart.save()
                else:
                    item.isPay = True
                    item.save()
                    listCart = Cart.objects.filter(shoesItem=item)
                    for c in listCart:
                        if (c.id != cart.id):
                            c.totalPrice = c.totalPrice - item.price*(1-item.discount)
                            c.quantity = c.quantity - 1
                            c.save()
            bookitem = BookItem.objects.filter(cart=cart)
            electronicitem = ElectronicItem.objects.filter(cart=cart)
            shoesitem = ShoesItem.objects.filter(cart=cart)
            fullname = request.user.last_name + " " + request.user.first_name
            totalprice = cart.totalPrice
            totalAmount = order.totalAmount
            order = Order.objects.create(
                status='new',
                user=request.user
            )
            Cart.objects.create(
                order=order
            )
        return render(request, 'page/order_detail.html', {'fullname': fullname, 'address': address, 'shipmentType': shipmentType,
                                                          'bookitem': bookitem, 'electronicitem': electronicitem, 'shoesitem': shoesitem,
                                                          'totalprice': totalprice, 'shippingFee': shippingFee, 'voucher': voucher,
                                                          'totalAmount': totalAmount, 'paymentMethod': paymentMethod})





