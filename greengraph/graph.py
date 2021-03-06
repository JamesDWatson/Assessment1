import numpy as np
import geopy
from .map import Map

class Greengraph(object):
    def __init__(self, start, end):
        self.start=start
        self.end=end
        self.geocoder=geopy.geocoders.GoogleV3(domain="maps.google.co.uk") #Chooses domain to take maps from.
        
        #Test flags.
        #First test to see if either start or finish arguments are numbers (does not prohibit postcodes).
        def is_number(s):    #Function checks if string has a representation as a float.
            try:
                float(s)
                return True
            except ValueError:
                return False
    
        if is_number(self.start) == True or is_number(self.end) == True:
            raise TypeError("Start and finish should be a *string*, not a number.")
    
    
    
    def geolocate(self, place):
        return self.geocoder.geocode(place, exactly_one=False)[0][1]
    
    def location_sequence(self, start,end,steps):
        
        #Test flags
        if start[0] > 90 or start[0] < -90 or end[0] > 90 or end[0] < -90:
            raise ValueError("Latitudes must be between -90 and 90.")
        
        if start[1] > 180 or start[1] < -180 or end[1] > 180 or end[1] < -180:
            raise ValueError("Longitudes must be between -180 and 180.")
        
        lats = np.linspace(start[0], end[0], steps) #Generates set of equally spaced latitudes.
        longs = np.linspace(start[1],end[1], steps)
        return np.vstack([lats, longs]).transpose() #Stacks as vertical arrays
    
    
    def green_between(self, steps):
        
        #Test flags.
        if float(steps) != int(float(steps)):
            raise TypeError("Steps must be a postive *integer*.")
            
        if float(steps) <= 0:
            raise ValueError("Steps must be a *postive* integer.")
        
        return [Map(*location).count_green()
                for location in self.location_sequence(
                    self.geolocate(self.start), 
                    self.geolocate(self.end),
                    steps)]
            
        
        