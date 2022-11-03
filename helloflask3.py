from flask import Flask

import folium

app = Flask(__name__)

# HTTP GET /
# create a map that returns hershey 
@app.route('/')
def index():
    start_coords = (40.284, -76.649)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

# HTTP GET /kansascity
# create a map that returns a display of kansas city
@app.route('/kansascity')
def kansascity():
    start_coords = (39.099, -94.578)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224, debug=True)

