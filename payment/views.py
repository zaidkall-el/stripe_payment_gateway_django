from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
import stripe
stripe.api_key=''
@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        print(request.data['price'])
        price = request.data['price']
        print(request.data['productName'])
        YOUR_DOMAIN='http://localhost:4200'
        productName = request.data['productName']
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': price,
                        'product_data': {
                            'name': productName,
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )

        return JsonResponse({'sessionId': checkout_session.url}, status=status.HTTP_200_OK)
