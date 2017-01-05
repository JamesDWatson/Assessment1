""" Unit tests for the graph file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from greengraph import Greengraph 
import os
import numpy
from mock import Mock, patch
import yaml

def test_graph_init():
    assert Greengraph('a', 'b').start == 'a'
    assert Greengraph('a', 'b').end == 'b'

def test_geocoder():
    #assert str(type(Greengraph( 'a', 'b').geocoder)) == str(geopy.geocoders.googlev3.GoogleV3)
    assert str("geopy.geocoders.googlev3.GoogleV3") in str(Greengraph( 'a', 'b').geocoder)

def test_command_geolocate():                                   #Test geolocate works as expected. Need to include mocks.
    assert_equal(Greengraph('a', 'b').geolocate('Rome'), (41.9027835, 12.4963655) )
    
def test_location_sequence():
    actual_array = open(os.path.join(os.path.dirname(__file__),
                                   'Fixtures/LondonCambridge.npy'), 'rb')
    mock_array = Greengraph('London', 'Cambridge').location_sequence( (51.5073509, -0.1277583),(52.205337, 0.121817), 5)
    numpy.array_equal(mock_array, actual_array)   

def test_location_sequence_again():
    with open(os.path.join(os.path.dirname(__file__),'Fixtures','location_sequence.yaml')) as location_file:
        loc_arguments = yaml.load(location_file)
        for loc_arg in loc_arguments:
            start = loc_arg['start']
            end = loc_arg['end']
            steps = loc_arg['steps']
            test_sequence = Greengraph('a','b').location_sequence(start, end, steps)
            numpy.testing.assert_equal(test_sequence.shape,(steps,2))
            numpy.testing.assert_array_equal(test_sequence[0],start)
            numpy.testing.assert_array_equal(test_sequence[-1],end)
    
    
#def test_geolocate():
#    with open(os.getcwd()+"/greengraph/tests/Fixtures/geolocate_samples.yaml", 'r') as ymlfile:  
#        test_data = yaml.load(ymlfile)
#    g=Greengraph('','')
#    lat_long=g.geocoder.geocode(test_data['Name'], exactly_one=False)[0][1]
#    assert_almost_equal(test_data['Lat'],lat_long[0],places=2)
#    assert_almost_equal(test_data['Long'],lat_long[1],places=2)

    
    
#def test_green_between():
#    actual_array = numpy.load('Fixtures/green_between_array.npy')
#    #with patch('requests.get', return_value=Mock(content=mock_image.read()))
#    with patch('Map(*location).count_green()', return_value = 108032 )
#        mock_array = Greengraph('London', 'Cambridge').green_between(3)    