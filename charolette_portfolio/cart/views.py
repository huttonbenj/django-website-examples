from django.shortcuts import render, redirect
from .models import Cart, CartBackground
from header.models import Header
from charolette_portfolio import settings
from django.contrib.auth.models import User
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.
def cart(request, *args, **kwargs):

    # Stripe Key
    stripe_key = settings.STRIPE_PUBLISHABLE_KEY

    #### CART HEADER ####
    cart_background_header = CartBackground.objects.all()

    # Cart Items
    image_url = request.GET.get('image_url')
    image_title = request.GET.get('image_title')
    image_price = request.GET.get('image_price')
    image_category = request.GET.get('image_category')
    image_sub_category = request.GET.get('image_sub_category')
    image_description = request.GET.get('image_description')

    cart_link = str(request.GET.get('cart_link'))
    keep_shopping = str(request.GET.get('keep_shopping'))
    checkout = str(request.GET.get('checkout'))
    login_redirect_url = str(request.GET.get('previous_url'))
    login_item = request.GET.get('item')


    remove = request.POST.get('remove')
    remove_item = request.GET.get('remove_item')

    image_category = None if image_category == None else image_category.split('-')[0]
    item = [image_url, image_title, image_price,
            image_category, image_sub_category, image_description]

    #### GET PREVIOUS URL ####
    referrer = request.META.get('HTTP_REFERER')
    previous_url = None if referrer == None else referrer.split('/')
    previous_url = None if previous_url == None else [s for s in previous_url if s == 'artwork' or s == 'originals' or s == 'oil' or s == 'watercolor' or s == 'prints' or s == 'framed' or s == 'unframed' or s == 'login' or s == 'register' or s == 'cart']
    if not previous_url == None:
        previous_url = 'home' if previous_url == [] else previous_url[0]

    if previous_url == 'cart':
        if not remove == None:
            rm_item = Cart.objects.filter(image_url=remove)
            rm_item.delete()
            return redirect(f'/?remove={remove}')
        if remove_item == 'True':
            cart_link = 'True'
        elif remove == None:
            pass

    #### AUTHENTICATED ####
    if request.user.is_authenticated:

        #### NOT CART LINK ####
        if not cart_link == 'True':

            #### GET USERS CART ITEMS ####
            usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
            duplicate = [s.image_url for s in usr_cart_items if s.image_url == image_url]
            if len(duplicate) == 0 and not image_url == None:
                item = Cart(image_url=image_url, image_title=image_title, image_price=image_price, image_category=image_category, image_sub_category=image_sub_category, image_description=image_description, usr=request.user)
                item.save()
            usr_cart_items = Cart.objects.filter(usr_id=request.user.id)

            #### GET TOTAL PRICE ####
            if len(usr_cart_items) > 0:
                total = 0
                for i in usr_cart_items:
                    total += float(i.image_price)
                total = ("%.2f" % total)
            elif len(usr_cart_items) == 0: total = 0
            payment_total = float(total)*100

            #### KEEP SHOPPING ####
            if keep_shopping == 'True':
                if not previous_url == 'login' and not previous_url == 'register':
                    usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
                    duplicate = [s.image_url for s in usr_cart_items if s.image_url == image_url]
                    if len(duplicate) == 0 and not image_url == None:
                        item = Cart(image_url=image_url, image_title=image_title, image_price=image_price, image_category=image_category, image_sub_category=image_sub_category, image_description=image_description, usr=request.user)
                        item.save()

                    return redirect(previous_url)

                elif previous_url == 'login' or previous_url == 'register':
                    login_item = login_item.split(',')
                    image_url = login_item[0].split("'")[1]
                    image_title = login_item[1].split("'")[1]
                    image_price = login_item[2].split("'")[1]
                    image_category = login_item[3].split("'")[1]
                    image_sub_category = login_item[4].split("'")[1]
                    image_description = login_item[5].split("'")
                    image_description = [s for s in image_description if not s == '' and not s == ' ' and not s == ']']
                    image_description = image_description[0]
                    usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
                    duplicate = [s.image_url for s in usr_cart_items if s.image_url == image_url]

                    if len(duplicate) == 0 and not image_url == None:
                        item = Cart(image_url=image_url, image_title=image_title, image_price=image_price, image_category=image_category,
                                    image_sub_category=image_sub_category, image_description=image_description, usr=request.user)
                        item.save()
                        usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
                        if len(usr_cart_items) > 0:
                            total = 0
                            for i in usr_cart_items:
                                total += float(i.image_price)
                            total = ("%.2f" % total)
                        elif len(usr_cart_items) == 0: total = 0
                        payment_total = float(total)*100
                    return redirect(login_redirect_url)

            #### CHECKOUT ####
            if checkout == 'True':
                if not previous_url == 'login' and not previous_url == 'register':
                    usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
                    duplicate = [s.image_url for s in usr_cart_items if s.image_url == image_url]
                    if len(duplicate) == 0 and not image_url == None:
                        item = Cart(image_url=image_url, image_title=image_title, image_price=image_price, image_category=image_category, image_sub_category=image_sub_category, image_description=image_description, usr=request.user)
                        item.save()
                        usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
                    return render(request, 'cart/cart.html', {
                        'background': cart_background_header,
                        'cart_items': usr_cart_items,
                        'total': total,
                        'payment_total': payment_total,
                        'stripe_key': stripe_key
                    })

                elif previous_url == 'login' or previous_url == 'register':
                    login_item = login_item.split(',')
                    image_url = login_item[0].split("'")[1]
                    image_title = login_item[1].split("'")[1]
                    image_price = login_item[2].split("'")[1]
                    image_category = login_item[3].split("'")[1]
                    image_sub_category = login_item[4].split("'")[1]
                    image_description = login_item[5].split("'")
                    image_description = [s for s in image_description if not s == '' and not s == ' ' and not s == ']']
                    image_description = image_description[0]

                    usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
                    duplicate = [s.image_url for s in usr_cart_items if s.image_url == image_url]

                    if len(duplicate) == 0 and not image_url == None:
                        item = Cart(image_url=image_url, image_title=image_title, image_price=image_price, image_category=image_category,
                                    image_sub_category=image_sub_category, image_description=image_description, usr=request.user)
                        item.save()
                        usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
                        if len(usr_cart_items) > 0:
                            total = 0
                            for i in usr_cart_items:
                                total += float(i.image_price)
                            total = ("%.2f" % total)
                        elif len(usr_cart_items) == 0:
                            total = 0
                        payment_total = float(total)*100
                    return render(request, 'cart/cart.html', {
                        'background': cart_background_header,
                        'cart_items': usr_cart_items,
                        'total': total,
                        'payment_total': payment_total,
                        'stripe_key': stripe_key
                    })

            #### LOGIN ####
            if previous_url == 'login' or previous_url == 'register':
                usr_cart_items = Cart.objects.filter(usr_id=request.user.id)
                #### GET TOTAL PRICE ####
                if len(usr_cart_items) > 0:
                    total = 0
                    for i in usr_cart_items:
                        total += float(i.image_price)
                    total = ("%.2f" % total)
                elif len(usr_cart_items) == 0: total = 0
                payment_total = float(total)*100

                return render(request, 'cart/cart.html', {
                    'background': cart_background_header,
                    'cart_items': usr_cart_items,
                    'total': total,
                    'payment_total': payment_total,
                    'stripe_key': stripe_key
                })

        #### CART LINK ####
        elif cart_link == 'True':
            usr_cart_items = Cart.objects.filter(usr_id=request.user.id)

            #### GET TOTAL PRICE ####
            if len(usr_cart_items) > 0:
                total = 0
                for i in usr_cart_items:
                    total += float(i.image_price)
                total = ("%.2f" % total)
            elif len(usr_cart_items) == 0: total = 0
            payment_total = float(total)*100

            return render(request, 'cart/cart.html', {
                'background': cart_background_header,
                'cart_items': usr_cart_items,
                'total': total,
                'payment_total':payment_total,
                'stripe_key': stripe_key
            })


    #### NOT AUTHENTICATED ####
    elif not request.user.is_authenticated:

        #### NOT CART LINK ####
        if not cart_link == 'True':
            return redirect(f'/login/?previous_url={previous_url}&keep_shopping={keep_shopping}&checkout={checkout}&item={item}')

        #### CART LINK ####
        if cart_link == 'True': return redirect(f'/login/?previous_url=cart&cart_link=True')



def checkout(request):
    if request.method == 'POST':
        total = request.GET.get('total')
        total = int(float(total))*100

        charge = stripe.Charge.create(
            amount=total,
            currency='usd',
            description='Charolette Meadows',
            source=request.POST['stripeToken']
        )

        all_items = Cart.objects.all()

        usr_cart_items = Cart.objects.filter(usr_id=request.user.id)

        usr_images = [s.image_url for s in usr_cart_items]
        all_images = [s for s in all_items if s.image_url in usr_images]

        remove_others_items = [s.delete() for s in all_images]
        remove_usr_items = [s.delete() for s in usr_cart_items]

        return render(request, 'cart/checkout.html')
