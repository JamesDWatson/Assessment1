""" Unit tests for the command file """

from nose.tools import assert_raises, assert_almost_equal
#from model import energy
from greengraph import Greengraph 

def test_command_fails_numerical_input():
    with assert_raises(TypeError) as exception: 
        Greengraph(5, 'London')     #5 should not be an acceptable argument.
    #energy([1.0, 2, 3])