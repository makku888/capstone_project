import json
import csv
from gps_class import GPSVis


"""
Creating an object "vis" with the GPSVis class so it will have the coordinates,
map image, and top left & bottom right coordinates associated with it.
"""
vis = GPSVis(data_path='test_coordinates.csv',
             map_path='test_map.png',  # Path to map downloaded from the OSM.
             points=(48.82054, -122.57669, 48.75981, -122.49704)) # Two coordinates of the map (upper left, lower right)

vis.create_image(color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks in RGB values 0 - 255
vis.plot_map(output='save')  # Save the new map with plotted points as a png file

print()

"""
Writing aircraft GPS locations from the json file into the csv file in the format: lat, lon

lastPosition:    if 'lat' and 'lon' are not updated within 60 seconds they are no longer valid.
However, if the aircraft is still being received, 'lastPosition' will be the GPS coordinates the plane was last seen at.
"""
with open('test_info.json', 'r') as jsonfile:   # 'r' for "read this file"
    data = json.load(jsonfile)

rows = []  # This array object will hold the lat, lon pair and then written into the csv file

for aircraft in data['aircraft']:
    lat = None
    lon = None

    if 'lat' in aircraft and 'lon' in aircraft:
        lat = aircraft['lat']
        lon = aircraft['lon']
    
    elif 'lastPosition' in aircraft:    # if 'lat' and 'lon' are not updated in 60 seconds they are no longer valid. If the aircraft is still being received, 'lastPosition' will be the GPS coordinates the plane was last seen at.
        lat = aircraft['lastPosition'].get('lat')
        lon = aircraft['lastPosition'].get('lon')

    if lat is not None and lon is not None:
        rows.append([lat,lon])

    with open('test_coordinates.csv', 'w', newline='') as csvfile:  #'w' for "write to this file"
        writer = csv.writer(csvfile)
        writer.writerows(rows)