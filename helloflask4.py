#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
import folium
from flask import Flask
from flask import request

app = Flask(__name__)

# Accept a (GET) at this location
# /custom?lat=x.yz&lon=a.bc
@app.route("/custom", methods = ["GET"])   # other methods could be included in this list
def custom():
    if request.method == "GET":
        # if user supplied both lat and lon we can create a map
        if request.args.get("lat") and request.args.get("lon"):
            lat = request.args.get("lat")
            lon = request.args.get("lon")
        # else they didn't supply the correct arguments 
        else:
            lat = 40.284      # Hershey, PA
            lon = -76.649     # Hershey, PA
    
    # starting coordinates
    start_coords = [lat, lon]
    
    # create the map
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    
    # return the HTML code that is the map
    return folium_map._repr_html_()
    
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

