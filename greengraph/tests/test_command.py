""" Unit tests for the command file """

from nose.tools import assert_raises, assert_almost_equal, assert_equal
#from model import energy
from greengraph import Greengraph 


def test_command_fails_numerical_input():
    with assert_raises(TypeError) as exception: 
        Greengraph(5, 'London')     #5 should not be an acceptable argument.
    #energy([1.0, 2, 3])
    
def test_command_fails_negative_input():                        #Value of steps must be a postive.
    with assert_raises(ValueError) as exception: 
        Greengraph( 'Cambridge', 'London').green_between(-1)    #-1 should not be an acceptable argument.

def test_command_fails_non_integer_input():                     #Value of steps must be an integer.
    with assert_raises(TypeError) as exception: 
        Greengraph( 'Cambridge', 'London').green_between(0.5)   #0.5 should not be an acceptable argument.
        
def test_command_geolocate():                                   #Test geolocate works as expected.
    assert_equal(Greengraph('a', 'b').geolocate('Rome'), (41.9027835, 12.4963655) )