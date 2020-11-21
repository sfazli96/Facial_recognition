# How to run Facial Recognition in less than 6 steps!!
   To run in Windows or Linux, Follow these Steps
Steps:
1. First Open Command Line
2. Type cd filename.py wherever you save it on you computer
3. Then in filename type python filename.py 
4. Boom! There your camera should show your face that it is being recognized.
5. To exit out of the program press Escape Key
That's all!
(This can also be done on a raspberry pi as well but frame rate is slow, more information will appear in the future)

Requirements:
1. You need a PC/Desktop that runs on Linux or Windows. 
2. Download OpenCV2 from this website
https://pypi.org/project/opencv-python/
3. Get the face_cascade file from this github or create your own include it in your directory folder
https://github.com/adarsh1021/facedetection/blob/master/haarcascade_frontalface_default.xml (Can skip 4 and 5, proceed to step 6)
4. Find any image (person or anime is fine) that ends with .png, jpg, jpeg, etc. (optional part only for checking if recognition recognizes an image)
5. Include this image in the folder directory. (optional part only for checking if recognition recognizes an image)
6. Next install this dependicies: sudo apt-get install libopencv-dev python-opencv in the command line
7. Install pip in order to use openCV2 -> python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose and pip install opencv-python
8. Both commands run those in your home directory i.e Desktop, Documents, etc.
9. Upgrade pip just in case of errors -> pip install --upgrade pip
10. Or other option download anaconda https://docs.anaconda.com/anaconda/install/linux/ Follow the instructions on the website
11. Then go back to step 2 to follow rest of instructions and OpenCV2 should be install through anaconda.
12. Voila! You should be good to run and play around with the facial recognition. (If there is a step missing, then repeat process once more or do sudo apt-update and sudo apt-upgrade on command line to check your operating system. sudo apt-update && sudo apt-upgrade should make it show that you have less errors)

References: https://github.com/adarsh1021/facedetection (used simple python implementation for face detection)
                                                          https://stackoverflow.com/questions/21596281/how-does-one-convert-a-grayscale-image-to-rgb-in-opencv-python (Used for converting grayscale image to rgb)
https://pypi.org/project/opencv-python/ (Used libraries and dependencies to use opencv)
