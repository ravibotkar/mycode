import json

import requests

url = (
        "http://api.open-notify.org"
)
iss1 = json.loads(requests.get(f"{url}/iss-now.json").text)
print(iss1)
print(type(iss1))

folium.Marker(
    location=[47.3489, -124.708],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(vis1, width=450, height=250)
    ),
).add_to(my_map)

my_map
