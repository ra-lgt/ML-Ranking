import firebase_admin
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from instamojo_wrapper import Instamojo
from .forms import *
import smtplib
from journey_begins import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from firebase_admin import firestore
from firebase_admin import credentials
import random
from django.shortcuts import redirect
from django.contrib import messages
import requests
import pyrebase
from django.views.decorators.csrf import csrf_exempt
from Bus import views

# Create your views here.
url="https://test.cashfree.com/api/v1/order/create"
API_KEY="258402db0c10ba8cb3e7ad13a2204852"
AUTH_TOKEN="47a0337a632177ce686619461542259f9a16796d"

response=""



firebaseConfig = {
        "apiKey": "AIzaSyAEzl4aWGVQnTb4Sk9pMNRhzNCxe3MFAmw",

        "authDomain": "sece-hackathon-390a0.firebaseapp.com",

        "projectId": "sece-hackathon-390a0",

        "storageBucket": "sece-hackathon-390a0.appspot.com",

        "databaseURL":"https://sece-hackathon-390a0-default-rtdb.firebaseio.com/",

        "messagingSenderId": "772188818031",

        "appId": "1:772188818031:web:1d02b48b391ce1602b9b9a",

        "measurementId": "G-Y5YXYRMD9M"

    }

#firestore

#database and auth
firebase=pyrebase.initialize_app(firebaseConfig)
authorize=firebase.auth()
storage=firebase.storage()
database=firebase.database()
session=""
email=""
Member_ship_type=""

#membership
member_email=""
f_name=""
l_name=""
mobile=""
age=""


def login_signup(request):

    return render(request,'login.html')
def home(request):

    global session
    global email

    if (request.method == 'POST'):
        emails=["@outlook.com","@gmail.com","@yahoo.com"]
        form = Login(request.POST)

        if (form.is_valid()):
            email = form.cleaned_data['email_id']
            passwd = form.cleaned_data['passwd']
            i=email.index("@")
            string=email[i:]
            print(string)

            try:
                user_auth=authorize.sign_in_with_email_and_password(email, passwd)
                session+=user_auth['idToken']

                return render(request, 'home.html', {'option': email.replace(string,""),'session':session})
            except Exception:
                return HttpResponse("Try again turn on wifi or user doesn't exists")
        else:
            return HttpResponse("Login Failed")
    else:
        return render(request,'home.html',{'option': email.replace("@gmail.com",""),'session':session})

def register(request):
    if(request.method=='POST'):
        form=Register(request.POST)
        if(form.is_valid()):

            emails=form.cleaned_data['email_id']
            passwd=form.cleaned_data['passwd']
            re_passwd=form.cleaned_data['re_password']
            username=form.cleaned_data['username']

            if(passwd==re_passwd):
                try:
                    authorize.create_user_with_email_and_password(emails,passwd)
                except:
                    return HttpResponse("user already exists")
                message=MIMEMultipart('alternative')
                message['subject']="Thanks for registering"
                message["from"]="raviajay9344@gmail.com"
                message["to"]=emails

                html="""\
                <html>
                <head>
                    <link href="https://fonts.googleapis.com/css?family=Kaushan+Script|Source+Sans+Pro" rel="stylesheet">
                    <style>
                    body {
                        background: #e2e1e0;
                        text-align: center;
                      }

                      .card {
                        background: #fff;
                        border-radius: 2px;
                        display: inline-block;
                        height: 600px;
                        margin: 1rem;
                        position: relative;
                        width: 800px;
                      }.card-5 {
                        box-shadow: 0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(245, 157, 6, 0.866);
                      }
                      h1{
                        font-family: 'Kaushan Script', cursive;
                      font-size:4em;
                      letter-spacing:3px;
                      color: rgba(245, 157, 6, 0.866);
                      margin:0;
                      margin-bottom:20px;
                    }
                    </style>
                </head>
                <body>

                    <div class="card card-5">
                        <h1>Your Journey Begins !</h1>
                        <p style="font-weight:bold;text-align:left;padding-left:40px;padding-top:30px;font-size:20px;">Hi user,</p>
                        <p style="padding-left:60px;padding-top:10px;font-size:20px;">We're so happy to have you on board! Be sure to stay logged in for effortless<br><p style="padding-right:380px;font-size:20px;">booking experience.</p></p>
                        <p style="padding-right:600px;padding-top:30px;font-weight:bold;font-size:18px;">Regards,</p>
                        <p style="padding-right:550px;font-weight:bold;font-size:18px;">Journey Begins !</p>
                        <p style="font-weight:300;padding-top:50px;padding-right:50px">Please do not hesitate to call us on at +91-9244262900(Mon-Fri 10AM - 6.30PM, Sat 10AM - 4.00PM)</p>
                        <p style="font-weight:300;padding-bottom:70px;padding-right:130px">or email customercare@journeybegins.com if have any questions at all regarding the above.</p>
                    </div>
                    </body>
                    </html>
                """
                html_mail=MIMEText(html,'html')
                message.attach(html_mail)

                server=smtplib.SMTP_SSL("smtp.gmail.com",465)
                server.login("raviajay9344@gmail.com","vmrxmwpnrruyonus")
                server.sendmail("raviajay9344@gmail.com",emails,message.as_string())

                server.quit()
                return HttpResponse("<script>alert('Registered successfully')</script>")
            else:
                return HttpResponse("<script>alert('password does not match')</script>")
def signout(request):
    global email
    email=""
    global session
    session=""
    return render(request,'home.html',{'option': email,'session':session})


def cancel_reservation(request):
    #if(session==""):
     #   return HttpResponse("Login to cancel_reservation :)")
    #if(request.method=='POST'):

    if(request.method=='POST'):
        user_name=request.POST.get('name')

        emails = request.POST.get('emails')
        bus = request.POST.get('bus')
        desc = request.POST.get('desc')

        data={
            'name':user_name,
            'bus':bus,
            'email':emails,
            'desc':desc
        }
        database.push(data)
    return render(request,'cancel_reservation.html')

def contactus(request):
    if(request.method=='POST'):
        #name=request.POST.get('name')
        #num=request.Post.get('num')
        #emails=request.Post.get('email')
        #subject=request.Post.get('subject')
        #message=request.Post.get('message')

        return HttpResponse("""<h1>We will shortly contact you</h1>""")


    return render(request,'contact_us.html')

def subscription(request):
    return render(request,'subscription.html')


def gold_membership(request):
    orderId=random.randint(0,100)

    global insta_mojo,member_email,f_name,l_name,mobile,age,Member_ship_type,response
    if(request.method=='POST'):
        member_email=request.POST.get('email')
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        mobile=request.POST.get('mobile')
        age=request.POST.get('age')
        Member_ship_type="GOLD Membership"
        payload={
            "appId":API_KEY,
            "secretKey":AUTH_TOKEN,
            "orderId":orderId,
            "orderAmount":"7500",
            "orderCurrency":"INR",
            "orderNote":"Tickets",
            "customerName":f_name,
            "customerEmail":member_email,
            "customerPhone":mobile,
            "returnUrl":"http://127.0.0.1:8000/"
        }
        res=requests.request("POST",url,data=payload)
        text=(res.text)
        response=text[30:len(text)-3]

        data = {
                'f_name': f_name,
                'l_name': l_name,
                'member_email': member_email,
                'mobile': mobile,
                'age': age,
                'Membership':Member_ship_type
            }

        settings.fire.collection('membership').add(data)
        return redirect(response)

        #return render(request,'membership.html',context={'url':response,'amount':7500})

    return render(request,'membership.html',{'amount':7500,'url':"gold_membership"})

def silver_membership(request):
    orderId=random.randint(0,100)
    global insta_mojo, member_email, f_name, l_name, mobile, age, Member_ship_type,response
    if (request.method == 'POST'):
        member_email = request.POST.get('email')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        Member_ship_type = "Silver"
        payload={
        "appId":API_KEY,
        "secretKey":AUTH_TOKEN,
        "orderId":orderId,
        "orderAmount":"5000",
        "orderCurrency":"INR",
        "orderNote":"silver_membership",
        "customerName":f_name,
        "customerEmail":member_email,
        "customerPhone":mobile,
        "returnUrl":"http://127.0.0.1:8000/"
    }
        res=requests.request("POST",url,data=payload)
        text=(res.text)
        response=text[30:len(text)-3]

        data = {
                'f_name': f_name,
                'l_name': l_name,
                'member_email': member_email,
                'mobile': mobile,
                'age': age,
                'Membership':Member_ship_type,

            }

        settings.fire.collection('membership').add(data)
        return redirect(response)

        #return render(request, 'membership.html', context={'url': response, 'amount': 5000})

    return render(request, 'membership.html', {'amount': 5000, 'url': "silver_membership"})

def vip_membership(request):
    orderId=random.randint(0,100)
    global insta_mojo, member_email, f_name, l_name, mobile, age, Member_ship_type,response
    if (request.method == 'POST'):
        member_email = request.POST.get('email')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        mobile = request.POST.get('mobile')
        age = request.POST.get('age')
        Member_ship_type = "VIP"
        payload={
            "appId":API_KEY,
            "secretKey":AUTH_TOKEN,
            "orderId":orderId,
            "orderAmount":"10000",
            "orderCurrency":"INR",
            "orderNote":"vip_membership",
            "customerName":f_name,
            "customerEmail":member_email,
            "customerPhone":mobile,
            "returnUrl":"http://127.0.0.1:8000/"
        }
        res=requests.request("POST",url,data=payload)
        text=(res.text)
        response=text[30:len(text)-3]

        data = {
                'f_name': f_name,
                'l_name': l_name,
                'member_email': member_email,
                'mobile': mobile,
                'age': age,
                'Membership':Member_ship_type,

            }

        ettings.fire.collection('membership').add(data)
        return redirect(response)
        #return render(request, 'membership.html', context={'url': response, 'amount': 10000})

    return render(request, 'membership.html', {'amount': 10000, 'url': "vip_membership"})

def your_tickets(request):
    global email
    my_ticket=settings.fire.collection("Tickets").get()
    ticket_email=[]
    ticket_date=[]
    ticket_phone=[]
    ticket_count=[]
    ticket_from=[]
    ticket_id=[]
    ticket_pass_name=[]
    start=[]
    end=[]
    bus=[]
    for i in my_ticket:
        dicts=i.to_dict()
        if(dicts['email']==email):
            ticket_email.append(dicts['email'])
            ticket_date.append(dicts['date'])
            ticket_phone.append(dicts['phone'])
            ticket_from.append(dicts['from'])
            ticket_id.append(dicts['ticket_id'])
            ticket_pass_name.append(dicts['name'])
            start.append(dicts['start_time'])
            end.append(dicts['end_time'])
            bus.append(dicts['busname'])
    print(ticket_email)
    print(ticket_date)
    print(ticket_from)
    return render(request,'mybookings.html',{
    'datas':zip(ticket_pass_name,ticket_from,ticket_id,start,end,bus),


    })

@csrf_exempt
def payment_success(request):
    data={
    'depature':views.depature,
    'name':views.pass_name,
    'count':views.number,
    'bus_name':views.pass_booked_bus_name,
    'arrival':views.arrive,
    'ticketId':views.ticket,
    'phone':views.pass_phone,
    'mail':views.pass_mail,
    'date':views.date,
    'amount':views.amount,

    }
    print(data)
    return render(request,'pdf.html',data)
