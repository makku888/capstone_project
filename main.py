import json
import csv
from gps_class import GPSVis

vis = GPSVis(data_path='random_coordinates.csv',
             map_path='test_map.png',  # Path to map downloaded from the OSM.
             points=(48.82054, -122.57669, 48.75981, -122.49704)) # Two coordinates of the map (upper left, lower right)

vis.create_image(color=(0, 0, 255), width=3)  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')



print()
