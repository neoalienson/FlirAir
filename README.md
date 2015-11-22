for details about this App and Hardware setup, please visit http://devpost.com/software/flirair
* Folder Structure and files

  * Assets, Images for use in App and presentations

  * controller/start_capture.sh, script for run raspberrypi_capture every seconds, and write the captured
    FLIR image to output.pgm

  * controller/raspberrypi_capture, Lepton capture for raspberry pi

  * controller/seek.py, Run contiously to read output.pbm from captured FLIR
    image, and action.txt from httpd.py. Using the information the script
    adjust Fan tilt, rotation and fan speed 

  * controller/httpd.py, HTTP server that receives request from iOS App and
    save the GET parameters to action.txt

  * FlirAir, iOS App with XCode project

  * server/, Server-side code for saving request to action.txt from iOS App

