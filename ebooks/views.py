from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe

def index(request):
    return render(request, 'index.html')

def thanks(request):
    return render(request, 'thanks.html')

@csrf_exempt
def checkout(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1Gzv86HRBy35qivl4wrURNpK',
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('thanks')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('index')),
    )

    return JsonResponse({
        'session_id': session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY
    })