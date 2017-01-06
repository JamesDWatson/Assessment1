""" Unit tests for the graph file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from greengraph import Greengraph
import geopy
import greengraph
import os
import numpy
from mock import Mock, patch
import yaml

def test_graph_init():
    assert Greengraph('a', 'b').start == 'a'
    assert Greengraph('a', 'b').end == 'b'

def test_geocoder():
    assert str("geopy.geocoders.googlev3.GoogleV3") in str(Greengraph( 'a', 'b').geocoder)

#def test_command_geolocate():                                   #Test geolocate works as expected. Need to include mocks.
#    assert_equal(Greengraph('a', 'b').geolocate('Rome'), (41.9027835, 12.4963655) )
    
#def test_command_geolocate():
#    with patch('geopy.geocoder.geocode', return_value=Mock((41.9027835, 12.4963655))) as mock_get:
#        mock_get.assert_equal( Greengraph('a', 'b').geolocate('Rome'), (41.9027835, 12.4963655))
        
    
def test_location_sequence():
    actual_array = open(os.path.join(os.path.dirname(__file__),
                                   'Fixtures/LondonCambridge.npy'), 'rb')
    mock_array = Greengraph('London', 'Cambridge').location_sequence( (51.5073509, -0.1277583),(52.205337, 0.121817), 5)
    numpy.array_equal(mock_array, actual_array)   
    
def test_location_sequence_inputs():
    with assert_raises(ValueError) as exception: 
        Greengraph('London', 'Hawaii').location_sequence( ( 190, 0), (0,0) , 3 )
        
def test_location_sequence_again():                             #Test location_sequence arrays have correct propteries
    with open(os.path.join(os.path.dirname(__file__),'Fixtures','location_sequence.yaml')) as location_file:
        loc_arguments = yaml.load(location_file)
        for loc in loc_arguments:
            start = loc['start']
            end = loc['end']
            steps = loc['steps']
            test_sequence = Greengraph('a','b').location_sequence(start, end, steps)
            numpy.testing.assert_equal(test_sequence.shape,(steps,2))
            numpy.testing.assert_array_equal(test_sequence[0],start)
            numpy.testing.assert_array_equal(test_sequence[-1],end)

def test_green_between():
    #mock_image_end = open(os.path.join(os.path.dirname(__file__),
    #                                   'Fixtures/london2.png'), 'rb')
    actual_data = [(51.5073509, -0.1277583), (52.205337, 0.121817) ]   
    false_green = Mock(name="count_green", side_effect=[158198, 108032])
    with patch.object(greengraph.map.Map, 'count_green', false_green) as mock_count_green:
        mock_green = Greengraph('London', 'Cambridge').green_between(2)
        numpy.testing.assert_array_equal(mock_green, [158198, 108032])            
            
#def test_green_between():
#    with patch( greengraph.map.Map, return_value=Mock( name="Map", side_effect=[108032, 2, 3])) as mock_get:
#         mock_get.assert_equal(Greengraph('London', 'Cambridge').green_between([[  5.15073509e+01,  -1.27758300e-01],
#                                                [  5.18563439e+01,  -2.97065000e-03],
#                                               [  5.22053370e+01,   1.21817000e-01]]), [108032, 2, 3])      
    
#def test_green_between(): 
#    actual_array = numpy.load('Fixtures/green_between_array.npy')
#    #with patch('requests.get', return_value=Mock(content=mock_image.read()))
#    with patch('Map(*location).count_green()', return_value = 108032 )
#        mock_array = Greengraph('London', 'Cambridge').green_between(3)    