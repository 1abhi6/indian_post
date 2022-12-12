from django.shortcuts import render
import requests


def home(request):
    pin_code = "401303"
    url = "https://api.postalpincode.in/pincode/{}"
    res = requests.get(url.format(pin_code)).json()
    print(type(len(res[0]['PostOffice'])))
    print(type(res[0]['PostOffice']))
    lengthOfResponse = len(res[0]['PostOffice'])
    res_data = {
        'message': res[0]['Message'],
        'name': []
    }
    result={
        'res_data':res_data
    }
    for i in range(0, lengthOfResponse):
        res_data['name'].append(res[0]['PostOffice'][i])
    print(res_data)

    return render(request, "index.html", result)
