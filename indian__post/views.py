from django.shortcuts import render
import requests


def home(request):
    result = {}
    res_data = {}
    if request.method == 'POST':
        try:

            pin_code = int(request.POST.get('pinInput'))
            url = "https://api.postalpincode.in/pincode/{}"
            res = requests.get(url.format(pin_code)).json()

            res_data = {
                'message': res[0]['Message'],
                'name': [],
                'status':True,
                'pin_code':pin_code
                # 'lengthData':[]
            }
            lengthOfResponse = len(res[0]['PostOffice'])

            for i in range(0, lengthOfResponse):
                res_data['name'].append(res[0]['PostOffice'][i])
                # res_data['lengthData'].append(i+1)
        
        except:
            res_data={
                'message': "Pin code do not exist. Please check your PIN Code and try again"
            }

    result = {
        'res_data': res_data,
        
    }

    return render(request, "index.html", result)
