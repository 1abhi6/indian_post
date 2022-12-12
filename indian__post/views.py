from django.shortcuts import render
import requests


def home(request):
    pin_code = "401303"
    url = "https://api.postalpincode.in/pincode/{}"
    res = requests.get(url.format(pin_code)).json()
   
    res_data = {
        'message': res[0]['Message'],
        'name': [],
        # 'lengthData':[]
    }
    lengthOfResponse = len(res[0]['PostOffice'])

    for i in range(0, lengthOfResponse):
        res_data['name'].append(res[0]['PostOffice'][i])
        # res_data['lengthData'].append(i+1)
    



    result = {
        'res_data': res_data
    }

    return render(request, "index.html", result)
