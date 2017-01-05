""" Unit tests for the graph file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from greengraph import Greengraph 
import os
import numpy
from mock import Mock, patch

def test_command_geolocate():                                   #Test geolocate works as expected. Need to include mocks.
    assert_equal(Greengraph('a', 'b').geolocate('Rome'), (41.9027835, 12.4963655) )
    
def test_location_sequence():
    actual_array = open(os.path.join(os.path.dirname(__file__),
                                   'Fixtures/LondonCambridge.npy'), 'rb')
    #with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
    #    mock_get.assert_equal(numpy.load('H:/Documents/bPython/Project/greengraph/tests/Fixtures/LondonCambridge.npy'))
    mock_array = Greengraph('London', 'Cambridge').location_sequence( (51.5073509, -0.1277583),(52.205337, 0.121817), 5)
    numpy.array_equal(mock_array, actual_array)   