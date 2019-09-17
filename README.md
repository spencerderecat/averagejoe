# averagejoe

All of the computer vision code lives here:

EightHunnid.py:

Establishes Connection between Virtual machine and raspberry pi to send position data to rpi -> then send through UNOs

Threading2Vids.py:

Starts and runs both cameras with method declared in runcameras.py

RunCameras.py:

starts camera and derives an x position to return from 0-800 (pixel width of whole view).

Motion_detector.py:

Uses gaussian smoothing to find the target 
