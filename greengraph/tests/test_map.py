""" Unit tests for the map file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
import greengraph
from numpy import load
from mock import Mock, patch
import os
import numpy
import yaml

latitude = 51.5073509
longitude = -0.1277583  #Latitude and longitude of London.

def test_map_url_output():                                   #Checks the map function gives the right URL output.
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'Fixtures/london.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = greengraph.map.Map(latitude, longitude)
        mock_get.assert_called_with(
            'http://maps.googleapis.com/maps/api/staticmap?',
            params={'center': '51.5073509,-0.1277583', 'zoom': 10, 'maptype': 'satellite', 'sensor': 'false', 'size': '400x400', 'style': 'feature:all|element:labels|visibility:off'}
        )

def test_green_function():                                  #Compares output with array stored in memory.
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'Fixtures/london2.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        assert numpy.array_equal(greengraph.map.Map(latitude, longitude).green(1.1), numpy.load('H:/Documents/bPython/Project/greengraph/tests/Fixtures/greenlondonarray.npy')) #Convert image to green image and then to array. Then compare array with reference.
        

def test_count_green_function():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'Fixtures/london2.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
            assert_equal(greengraph.map.Map(latitude, longitude).count_green(1.1), 108032)
        
    