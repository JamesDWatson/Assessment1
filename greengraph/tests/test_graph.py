""" Unit tests for the graph file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
from greengraph import Greengraph 

def test_command_geolocate():                                   #Test geolocate works as expected.
    assert_equal(Greengraph('a', 'b').geolocate('Rome'), (41.9027835, 12.4963655) )