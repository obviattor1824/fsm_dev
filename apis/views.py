from django.http import HttpResponse
from django.shortcuts import render
from xero import Xero
from xero.auth import PrivateCredentials
from airtable import Airtable
import json


def index(request):
    return render(request, "base.html")

def xero_api(request):
    # Connect to Xero
    with open('privatekey.pem') as keyfile:
        rsa_key = keyfile.read()
    credentials = PrivateCredentials('MQNHWHQUGCSSIW1DBOJ7460LUCIR2O',rsa_key)
    xero = Xero(credentials)

    # Get all Yachts from Xero
    tracking_categories=xero.trackingcategories.filter(Name='Yacht')
    yachts = tracking_categories[0]['Options']

    # Create list of all yachts from Xero
    xero_yachts = []
    for yacht in yachts:
        xero_yachts.append(yacht['Name'])
    print (xero_yachts)
    # print (json.dumps(yachts, indent=1))

    # Connect to airtable
    airtable = Airtable('appf5QcGhI1kMEZq7', 'Boats')

    # Get all boat names from airtable
    boat_names = airtable.get_all(fields=['Boat Name'])

    # Create list of all yachts from airtable
    air_yachts = []
    for boat in boat_names:
        air_yachts.append(boat['fields']['Boat Name'])
    print (air_yachts)
    # print (json.dumps(boats, indent=1))

    # Compare boat names and create list of boats to add to xero
    add_to_xero = []

    for air_yacht in air_yachts:
        if air_yacht in xero_yachts:
            pass
        else:
            add_to_xero.append(air_yacht)
    # print('add to xero:', add_to_xero)

    xero_test = "New yacht"
    print (xero_test)

    xero.trackingcategories.put({'Name': 'Yacht', 'Options': {'Name': 'new_yachts', 'Status': 'ACTIVE'}})
    # xero.contacts.put({'Name': 'New Xero Contact by Dave'}) THIS WORKED!

    '''for yacht_to_add in add_to_xero:
        xero.trackingcategories.put([{"TrackingCategoryID": "f645671f-db5b-4399-8501-f86a734f2eb5",'Name':yacht_to_add}])
        '''

    # Check projects functionality - SPOLIER: AttributeError: 'Xero' object has no attribute 'projects'
    projects = xero.projects.all()
    print (projects)
    return render(request, "xero_api.html")
