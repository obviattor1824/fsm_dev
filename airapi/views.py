from django.http import HttpResponse
from airtable import Airtable


def air_api(request):
    airtable = Airtable('appf5QcGhI1kMEZq7', 'Clients')
    all_contacts = airtable.get_all()
    return HttpResponse(all_contacts)
