""" Unit tests for the map file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from .map import Map
from numpy import load

def test_map_green_works():
    assert_almost_equal(Map(51.5072, -0.1275).green(1.1),numpy.load('greenlondonpixels.npy')) #Convert image to green image and then to array. Then compare array with reference.