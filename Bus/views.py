from django.shortcuts import render
from .bus_data import Data_set
import time
from datetime import date as dates
import random
from journey_begins import settings
from instamojo_wrapper import Instamojo
from django.shortcuts import redirect
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

url="https://test.cashfree.com/api/v1/order/create"
API_KEY="258402db0c10ba8cb3e7ad13a2204852"
AUTH_TOKEN="47a0337a632177ce686619461542259f9a16796d"



bus_list=Data_set().data
curr_time=time.gmtime()
#firestore

ticket_key=['a','b','c','d','e','f','g','A','B','H','J','I','i','k','r','t','u','q','w']

#bus_data
pass_name=""
name=[]
fare=[]
s_point=[]
e_point=[]
bus_type=[]
bus=""
start=[]
end=[]
offers=[]
seats=[]
depature=""
arrive=""
date=""
pass_booked_bus_name=""
pass_booked_fees=0
amount=0
index=0
ticket=""
number=0
pass_phone=""
flag=False
pass_mail=""
counter=[]
def search_bus(request):

    global name
    global fare
    global s_point
    global e_point
    global bus_type
    global bus
    global start
    global end
    global offers
    global seats
    global depature
    global arrive
    global date

    if(request.method=="POST"):
        depature=request.POST.get('depature').strip().title()
        arrive=request.POST.get('arrive').strip().title()
        date=request.POST.get('date')

        input_date=date.split("-")
        a=str(dates.today())
        curr_date=a.split("-")

        if(input_date[0]<curr_date[0]):
            return render(request,'404.html')

        elif(input_date[1]<curr_date[1]):
            return render(request, '404.html')
        elif(input_date[2]<curr_date[2] and input_date[1]==curr_date[1]):
            return render(request, '404.html')


        try:
            curr_hour=curr_time.tm_hour
            if(bus_list[depature][arrive]):

                bus=(bus_list[depature][arrive])

                name = (bus_list[depature][arrive]['name'])
                fare = (bus_list[depature][arrive]['fare'])
                s_point = (bus_list[depature][arrive]['s_point'])
                e_point = (bus_list[depature][arrive]['e_point'])
                bus_type = (bus_list[depature][arrive]['bus_type'])

            for i in range(len(name)):
                start_time=curr_hour+random.randint(1,5)
                if(start_time>24):
                    start_time=abs(start_time-24)
                start.append((start_time))

            for j in start:
                end_time=j+random.randint(1,5)
                if(end_time>24):
                    end_time=abs(end_time-24)
                end.append(end_time)

            for k in fare:
                t=random.choice([10,20,12,15,5,7,19])
                offers.append(k-t)

            for m in range(len(name)):
                seats.append(random.choice([20,30,40,50,45,35]))

            return render(request,'searchbus.html',{
                'depature':depature,
                'arrive':arrive,
                'date':date,
                'length':len(name),
                'datas':zip(name,fare,s_point,e_point,start,end,bus_type,offers,seats)
                })
        except:
            return render(request,'404.html')
    else:
        return render(request,'404.html')



def bus_filter_Ac(request):
    global name
    global fare
    global s_point
    global e_point
    global bus_type
    global bus
    global start
    global end
    global offers
    global seats
    global depature
    global arrive
    global date

    Ac_name=[]
    Ac_fare=[]
    Ac_s_point=[]
    Ac_e_point=[]
    Ac_bus_type=[]
    Ac_end=[]
    Ac_start=[]
    Ac_offers=[]
    Ac_seats=[]
    count=0

    for i in bus['bus_type']:
        if(i=='Ac'):
            Ac_name.append(bus['name'][count])
            Ac_fare.append(bus['fare'][count])
            Ac_s_point.append(bus['s_point'][count])
            Ac_e_point.append(bus['e_point'][count])
            Ac_bus_type.append(i)
            Ac_start.append(start[count])
            Ac_end.append(end[count])
            Ac_offers.append(offers[count])
            Ac_seats.append(offers[count])
            count+=1
        else:
            count+=1


    return render(request,'searchbus.html',{
     'depature':depature,
     'arrive':arrive,
     'date':date,
     'length':len(name),
     'datas':zip(Ac_name,Ac_fare,Ac_s_point,Ac_e_point,Ac_start,Ac_end,Ac_bus_type,Ac_offers,Ac_seats)
     })

def bus_filter_Nc(request):
    global name
    global fare
    global s_point
    global e_point
    global bus_type
    global bus
    global start
    global end
    global offers
    global seats
    global depature
    global arrive
    global date

    Ac_name=[]
    Ac_fare=[]
    Ac_s_point=[]
    Ac_e_point=[]
    Ac_bus_type=[]
    Ac_end=[]
    Ac_start=[]
    Ac_offers=[]
    Ac_seats=[]
    count=0

    for i in bus['bus_type']:
        if(i=='Nc'):
            Ac_name.append(bus['name'][count])
            Ac_fare.append(bus['fare'][count])
            Ac_s_point.append(bus['s_point'][count])
            Ac_e_point.append(bus['e_point'][count])
            Ac_bus_type.append(i)
            Ac_start.append(start[count])
            Ac_end.append(end[count])
            Ac_offers.append(offers[count])
            Ac_seats.append(offers[count])
            count+=1
        else:
            count+=1


    return render(request,'searchbus.html',{
     'depature':depature,
     'arrive':arrive,
     'date':date,
     'length':len(name),
     'datas':zip(Ac_name,Ac_fare,Ac_s_point,Ac_e_point,Ac_start,Ac_end,Ac_bus_type,Ac_offers,Ac_seats)
     })

#waste
def multipass(request):
    global name, pass_booked_bus_name, pass_booked_fees, offers,amount,ticket_key,index,depature,arrive,date,ticket,number,flag,pass_name,pass_phone
    global pass_mail
    if(request.method=='POST'):
        pass_name=request.POST.get('name')
        pass_mail=request.POST.get('mail')
        pass_phone=request.POST.get('phone')
        data={
            'name':pass_name,
            'email':pass_mail,
            'phone':pass_phone,
            'ticket_id':ticket,
            'ticket_count':number,
            'from':depature,
            'to':arrive,
            'date':date
        }
        return render(request,'passenger.html')


def bookseats(request,starting=""):
    global name, pass_booked_bus_name, pass_booked_fees, offers,amount,ticket_key,index,depature,arrive,date,ticket,number,flag,pass_name,pass_phone
    global pass_mail,counter,start,end
    if(starting=="passenger"):
        number=request.POST.get('count')
        amount=int(number)*pass_booked_fees
        for i in range(2):
            ticket += random.choice(ticket_key) * 2
            ticket += random.choice(ticket_key) * 1
        for i in range(1,int(number)+1):
            counter.append((i))

        return render(request,'passenger.html',{'price':amount,'count':counter})
    elif(starting=='multipass'):
        if(request.method=='POST'):

            pass_name=request.POST.get('name')
            pass_mail=request.POST.get('mail')
            pass_phone=request.POST.get('phone')

            membership_option=request.POST.get('membership_option')
            membership_firestore=settings.fire.collection('membership').get()
            if(membership_option=='yes'):
                for i in membership_firestore:
                    dicts=i.to_dict()
                    try:
                        if(dicts['mobile']==pass_phone):

                            data={
                                'name':pass_name,
                                'email':pass_mail,
                                'phone':pass_phone,
                                'ticket_id':ticket,
                                'ticket_count':number,
                                'from':depature,
                                'to':arrive,
                                'date':date,
                                'start_time':start[index],
                                'end_time':end[index],
                                'busname':pass_booked_bus_name,
                                }


                            amount-=offers[index]
                            settings.fire.collection('Tickets').add(data)
                        else:
                            return HttpResponse("you are not in membership")

                    except:
                        return HttpResponse("Somethin went wrong.....")


                return render(request,'passenger.html',{'price':amount,'count':counter})
            elif(membership_option=='no'):
                data={
                    'name':pass_name,
                    'email':pass_mail,
                    'phone':pass_phone,
                    'ticket_id':ticket,
                    'ticket_count':number,
                    'from':depature,
                    'to':arrive,
                    'date':date,
                    'start_time':start[index],
                    'end_time':end[index],
                    'busname':pass_booked_bus_name,
                    }
                settings.fire.collection('Tickets').add(data)


            else:
                return HttpResponse("you are not in membership")
            return render(request,'passenger.html',{'price':amount,'count':counter})

    elif(starting=='payment'):
        payload={
                "appId":API_KEY,
                "secretKey":AUTH_TOKEN,
                "orderId":ticket,
                "orderAmount":amount,
                "orderCurrency":"INR",
                "orderNote":"Tickets",
                "customerName":pass_name,
                "customerEmail":pass_mail,
                "customerPhone":pass_phone,
                "returnUrl":"http://127.0.0.1:8000/payment_success"
            }
        res=requests.request("POST",url,data=payload)
        text=(res.text)
        response=text[30:len(text)-3]
        return redirect(response)
        """
        if(request.method=='POST'):
            #pass_name=request.POST.get('name')
            #pass_mail=request.POST.get('mail')
            #pass_phone=request.POST.get('phone')
            #membership_option=request.POST.get('membership_option')



            payload={
                    "appId":API_KEY,
                    "secretKey":AUTH_TOKEN,
                    "orderId":ticket,
                    "orderAmount":amount,
                    "orderCurrency":"INR",
                    "orderNote":"Tickets",
                    "customerName":pass_name,
                    "customerEmail":pass_mail,
                    "customerPhone":pass_phone,
                    "returnUrl":"http://127.0.0.1:8000/payment_success"
                }
            res=requests.request("POST",url,data=payload)
            text=(res.text)
            response=text[30:len(text)-3]
            return redirect(response)
        else:
            return HttpResponse(1)


                data={
                    'name':pass_name,
                    'email':pass_mail,
                    'phone':pass_phone,
                    'ticket_id':ticket,
                    'ticket_count':number,
                    'from':depature,
                    'to':arrive,
                    'date':date
                }
                settings.fire.collection('Tickets').add(data)



            elif(membership_option=="yes"):
                membership_firestore=settings.fire.collection('membership').get()
                for i in membership_firestore:
                    dicts=i.to_dict()
                    try:
                        if(dicts['mobile']==pass_phone):
                            data = {
                                'name': pass_name,
                                'email': pass_mail,
                                'phone': pass_phone,
                                'ticket_id': ticket,
                                'ticket_count': number,
                                'from': depature,
                                'to': arrive,
                                'date': date
                            }
                            settings.fire.collection('Tickets').add(data)
                            return redirect("/payment_success")

                    except:
                        pass
                    #print(dicts)
            return HttpResponse("You are not in membership")
        return HttpResponse("hii")
        """
    if(starting!='payment'):
        index=((name.index(starting)))
        pass_booked_bus_name=name[index]
        pass_booked_fees=offers[index]
        return render(request,'bookseats.html',{'price':pass_booked_fees,'name':pass_booked_bus_name})
