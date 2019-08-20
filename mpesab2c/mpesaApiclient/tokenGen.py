import requests
from requests.auth import HTTPBasicAuth

consumer_key="cN98civcidJHVDcWTo5vbdvQxkb4Iyqc"
secret_key="AsGaz7hiN41dMBlT"
url="https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

req=requests.get(url,auth=HTTPBasicAuth(consumer_key,secret_key))

json_reponse = (req.json())
myToken = json_reponse["access_token"]