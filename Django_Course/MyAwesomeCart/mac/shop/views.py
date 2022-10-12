from django.shortcuts import render
from django.http import HttpResponse, response
from  .models import Product, Contact, Order, OrderUpdate
from math import  ceil
import json
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
MERCHANT_KEY = "W@%XCqu%6e_Y7j3K"


# Create your views here.
def index(request):
    # return HttpResponse("keyur chanchad")
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) + (n // 4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # print(products)
    # allprods = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides],]
    allprods = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prods = Product.objects.filter(category = cat)
        n = len(prods)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prods, range(1, nSlides), nSlides])  
    params = {'allprods': allprods}
    return render(request, 'shop/index.html', params)

def searchMatch(query, item):
    ''' return true only if query mathches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:   
        return False

def search(request):
    query = request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category = cat)
        prod = [item for item in prodtemp if searchMatch(query, item) ]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nSlides), nSlides])  
    params = {'allprods': allprods, 'msg': ""}
    if len(allprods) == 0 or len(query) < 3:
        params['msg'] = "Results not found. Please enter valid search."
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    #if request method is post
    if(request.method == 'POST'):
        fname = request.POST.get('fname')
        lname= request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(fname=fname, lname=lname, email=email, phone=phone, desc=desc)
        contact.save()
        post = True
        return render(request, 'shop/contact.html', {'post': post, 'name': fname})

    #if request method is get
    return render(request, 'shop/contact.html')



def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id = orderId, email = email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id = orderId)
                updates = []
                for item in update:
                    updates.append( {'text' : item.update_desc, 'time' : item.timeStamp} )
                    response = json.dumps( {"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str )
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
            
    return render(request, 'shop/tracker.html')



def productView(request, myid):
    #Fetch the product using the id
    product=Product.objects.filter(product_id = myid)
    return render(request, "shop/productView.html", {'product':product[0]})


def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('items_json', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        
        order = Order(items_json= items_json, name=name, phone=phone, email=email, address= address, city = city, state=state, zip_code=zip_code, amount=amount)
        order.save()

        orderupdate = OrderUpdate(order_id = order.order_id, update_desc = "This is update description.")
        orderupdate.save()

        post = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'post':post, 'id':id})

        # Request Paytm to transfer amount to your account after Payment by user.
        param_dict={
            'MID': 'SOoCXc73428937701541',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': str(email),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHAS'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/payment.html', {'param_dict' : param_dict})

    return render(request, 'shop/checkout.html')

# To by pass the csrf token
@csrf_exempt
def handlerequest(request):
    # Paytm will send you post request here.
    form = request.post
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHAS':
            checksum = form[i]
    
    varify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if varify:
        if response_dict['RESPCODE'] == '01':
            print('order sucessful')
        else:
            print('order not successful ' + response_dict['RESPMEG'])

    return render(request, '/shop/paymentStatus.html', {'response': response_dict})


 