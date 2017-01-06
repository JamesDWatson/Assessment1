
==========
Greengraph
==========

This program is designed to take two place names (e.g. 'London' and 'Cambridge') and then plot the amount of 'greenery' between
these two locations. 

In more detail the program works as follows:
- Takes the two place names (e.g. 'London' and 'Cambridge').
- Uses Google to find the longitude and latitudes of these two places.
- Takes these longitudes and latitudes and then finds equally spaced points between these two longitudes and latitudes.
- At each of these coordinates, it takes a satelite image from Google Maps, converts it into a n x n x 3 array in where each
pixel in a picture of size nxn is described by 3 values (it's greeness, blueness and redness).
- It takes each of the pixels and compares the values for the redness, greenness and blueness to decide if the pixel is 'mostly' 
 green.
- It then takes all the mostly green pixels and creates and array. If the pixel is mostly green it's give the value true, and
  otherwise is false.
- The program then sums all the green pixels in the program returns the sum.
- It then at each of the latitudes and longitudes (including the intial, final and intermediate values) it plots this sum of 
  the green pixels.                                                       

------------                                                         
Installation
------------                                                         
Manual install: To install this program manually, go into greengraph folder (which should contain setup.py) and then run 'python setup.py install'
from the command line.  
                                                         
pip install: Can be installed from https://github.com/JamesDWatson/Assessment1      
                                                         
------
Usage 
------
 To run from the command line after installation, use the command                                                        
                                                         
greengraph –-start place1 –-finish place2 –-steps noofsteps –out imagename.png
                                                         
where place1 and place2 are your place names. noofsteps is the number of steps you wish the program to output in your graph.
imagename.png is the name of the image you wish to save to.
                                                         
-------
Authors
-------
This program was writen by James Watson. Questions should be directed to 05watson.j@gmail.com
                                                         
A signficant portion of the code was taken from James Herthington's Research Software Engineering With Python
MPHYG001 course at http://development.rc.ucl.ac.uk/training/engineering                                                          