# Etch3D
This is the project for Meng Project

Get started

1. install virtual environment for this web application.
We use Flask in Python as a web framework. 
a. install Python
b. install Flask
see the details in the section "Installing Flask" in the following page:
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

2.Clone or download this project

3.run demo.py to start the server.


How to use it

--- 11/16/2015 ---

index page: http://127.0.0.1:5000/

Upload vtk file through this page and see the result in the marching-cube page	

2d mask editor page: http://127.0.0.1:5000/editor

Create the 2D mask using this online editor.
Click "Send the SVG" on the right, the mask will be saved as .svg file and it will sent to a simulator in the back-end.

3d model display page: http://127.0.0.1:5000/marchingCube

A 3d model of that 2d mask will be shown using marching-cube algorithm. More details about this algorithm could be found in the following webpage:
http://paulbourke.net/geometry/polygonise/

A slider bar on the top right corner is used to adjust the value of isolevel, which will give you a different output. 


