from django.http import HttpResponse
from xero import Xero
from xero.auth import PrivateCredentials


def index(request):
    return HttpResponse("Hiya")

def xero_api(request):
    with open('privatekey.pem') as keyfile:
        rsa_key = keyfile.read()
    credentials = PrivateCredentials('MQNHWHQUGCSSIW1DBOJ7460LUCIR2O',rsa_key)
    xero = Xero(credentials)
    all_contacts=xero.contacts.all()
    return HttpResponse(all_contacts)