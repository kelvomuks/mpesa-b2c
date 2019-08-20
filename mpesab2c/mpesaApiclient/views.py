from django.shortcuts import render
import requests
from . import keys
from . import tokenGen
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from requests.auth import HTTPBasicAuth
import json
from django.http import JsonResponse
from .models import B2CResponse
# from . import credentialGen

consumer_key = keys.consumer_key
secret_key = keys.secret_key
# security_cred=credentialGen.cipher
# Create your views here.
@csrf_exempt
def mapi(request):

  access_token = tokenGen.myToken
  api_url = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
  requests.get(api_url,auth=HTTPBasicAuth(consumer_key,secret_key))
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
    "InitiatorName": "John Doe",
    "SecurityCredential":"32SzVdmCvjpmQfw3X2RK8UAv7xuhh304dXxFC5+3lslkk2TDJY/Lh6ESVwtqMxJzF7qA== ",
    "CommandID": "SalaryPayment",
    "Amount": 14248,
    "PartyA": 123456 ,
    "PartyB": 254722000000 ,
    "Remarks": " you salary",
    "QueueTimeOutURL": "http://c7f50b58.ngrok.io/que/",
    "ResultURL": "http://c7f50b58.ngrok.io/result/",
    "Occasion": " "
  }
  
  response = requests.post(api_url, json = request, headers=headers)
  print(response.text)
  j = json.loads(response.text)
  c = j['ConversationID']
  orig = j['OriginatorConversationID']
  typ = j['ResponseDescription']
  code = j['ResponseCode']
  B2CResponse.objects.create(Resulttype=typ,ResultCode=code,ConversationId=c,OriginatorConversationId=orig)
  return HttpResponse(response) 



@csrf_exempt
def reUrl(request):
  pass
  print("res...")
  data = json.loads(request.read())
  r  = data.get('Result')
  og=r.get('OriginatorConversationID')
  if B2CResponse.objects.get(OriginatorConversationId=og):
    h = B2CResponse.objects.get(OriginatorConversationId=og)
    print(h)
    h.Status = True
    h.save()
  

        
  #   return render(request,context)
  message = {
    "ResultCode":0,
    "ResultDesc":"The service was accepted successfuly",
    "ThirdPartyTransID": "emtech" 
  }
  return JsonResponse({'message':message})

 
@csrf_exempt
def queUrl(request):
  print("these are th results")

  pass
 # print("hello me")