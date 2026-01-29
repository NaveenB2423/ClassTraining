import razorpay
from django.conf import settings
client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

def initiate_payment(amount, currency='INR'):
   data = {
       'amount': amount * 100, # Amount in paise
       'currency': currency,
       'payment_capture': '1'
   }
   response = client.order.create(data=data)
   return response['id']


