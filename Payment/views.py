from django.shortcuts import render
from django.http import HttpResponse
from instamojo_wrapper import Instamojo
# Create your views here.
API_KEY="test_e4152152589c3c8954a56998ef1"
AUTH_TOKEN ="test_16d4fce2079a45ec988e3655747"
api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

def pay(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        purpose = request.POST.get('purpose')
        email = request.POST.get('email')
        amount = request.POST.get('amount')

        response = api.payment_request_create(
        amount=amount,
        purpose=purpose,
        buyer_name=name,
        send_email=True,
        email=email,
        redirect_url="http://localhost:8000/"
        )
        return render(request,'payment.html')

    return render(request,'payment.html')
