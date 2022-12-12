from django.shortcuts import render
import requests


def home(request):
    result = {}

    # Working for search by pin code
    res_data = {}
    if request.method == 'POST':
        try:

            pin_code = int(request.POST.get('pinInput'))
            url = "https://api.postalpincode.in/pincode/{}"
            res = requests.get(url.format(pin_code)).json()

            res_data = {
                'message': res[0]['Message'],
                'name': [],
                'status': True,
                'pin_code': pin_code
                # 'lengthData':[]
            }
            lengthOfResponse = len(res[0]['PostOffice'])

            for i in range(0, lengthOfResponse):
                res_data['name'].append(res[0]['PostOffice'][i])
                # res_data['lengthData'].append(i+1)
            print(res_data)

        except:
            # res_data = {
            #     'message': "Pin code do not exist. Please check your PIN Code and try again"
            # }
            pass
        result = {
            'res_data': res_data,
        }

        print(result)
    return render(request, "index.html", result)

# Working for search by Post Office
# def post(request):
#     res_data_name = {}
#     if request.method == 'POST':
#         post_office = request.POST.get('nameInputOffice')
#         url = "https://api.postalpincode.in/postoffice/{}"
#         res = requests.get(url.format(post_office)).json()
#         # print(post_office)
#         res_data_name = {
#             'message': res[0]['Message'],
#             'name': [],
#             'status': True,
#             'post_office': post_office
#         }
#         # print(res_data_name)
#         lengthOfResponseName = len(res[0]['PostOffice'])
#         for i in range(0, lengthOfResponseName):
#             res_data_name['name'].append(res[0]['PostOffice'][i])

#     result = {
#         'res_data_name': res_data_name
#     }

#     return redirect(request, "index.html", result)
