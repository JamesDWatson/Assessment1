""" Unit tests for the map file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
import greengraph
from numpy import load
from mock import Mock, patch
import os

#def test_map_green_works():
#    assert_almost_equal(Map(51.5072, -0.1275).green(1.1),numpy.load('greenlondonpixels.npy')) #Convert image to green image and then to array. Then compare array with reference.

latitude = 51.5073509
longitude = -0.1277583  #Latitude and longitude of London.


#with patch.object(requests,'get') as mock_get:
#    london_map=map_at(51.5073509, -0.1277583)


def test_build_map():
    mock_image = open(os.path.join(os.path.dirname(__file__),
                                   'Fixtures/london.png'), 'rb')
    with patch('requests.get', return_value=Mock(content=mock_image.read())) as mock_get:
        test_map = greengraph.map.Map(latitude, longitude)
        mock_get.assert_called_with(
            'http://maps.googleapis.com/maps/api/staticmap?',
            params={'center': '51.5073509,-0.1277583', 'zoom': 10, 'maptype': 'satellite', 'sensor': 'false', 'size': '400x400', 'style': 'feature:all|element:labels|visibility:off'}
        )

        #params={'size': '400x400', 'sensor': 'false', 'center': '51.5073509,-0.1277583', 'zoom': 10, 'style': 'feature:all|element:labels|visibility:off'}
