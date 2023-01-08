from django.shortcuts import render
import requests
from geopy.geocoders import ArcGIS
import folium


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
            }

            lengthOfResponse = len(res[0]['PostOffice'])

            for i in range(0, lengthOfResponse):
                res_data['name'].append(res[0]['PostOffice'][i])

            locToBeSearched = []
            states=[]
            for i in range(0, len(res_data["name"])):
                # states.append(res_data["name"][i]["Name"])
                # states.append(res_data["name"][i]["State"])
                # # print(states)
                # locToBeSearched.append(states[i])
                locToBeSearched.append(res_data["name"][i]["Name"])
                locToBeSearched.append(res_data["name"][i]["State"])
            print(locToBeSearched)

            # View on map
            locToBeSearchedWithLatLong = []
            locObj = ArcGIS()

            for item in locToBeSearched:
                s = locObj.geocode(item)
                locToBeSearchedWithLatLong.append(s.latitude)
                locToBeSearchedWithLatLong.append(s.longitude)
            print(locToBeSearchedWithLatLong)

            map = folium.Map(
                location=[locToBeSearchedWithLatLong[0], locToBeSearchedWithLatLong[1]])
            fg = folium.FeatureGroup(name="postOffliceLocation")

            for i in range(0, len(locToBeSearched)):
                fg.add_child(folium.Marker(location=[locToBeSearchedWithLatLong[i], locToBeSearchedWithLatLong[i+1]],
                             popup=locToBeSearched[i].capitalize(), icon=folium.Icon(color="blue")))

            map.add_child(fg)
            map.save("templates/map.html")

        except:
            pass
        result = {
            'res_data': res_data,
        }

    return render(request, "index.html", result)


def map(request):
    return render(request, "map.html")
