# Pencil
https://pencil-app-noah.herokuapp.com

# Requirements

* Streamlit : to showcase the app
* OpenCV : to modify the input image in order to get a sketch of it
* Pillow : to work with .JPG file in Python
* Numpy : to turn the image into an array in order to manipulate it

# How it works

* The user is prompted to upload an image
* When the image is uploaded, it is read by the PIL library and displayed on screen
* To convert it into a sketch, we call the pencil function
* It takes the uploaded image as an argument and manipulate it to convert it into a "drawing", using Numpy and OpenCV
* The result is then showed and screen, and a download button appear
* If the user click Download, the array is converted back into a .JPG file and a download link appears
* The user can then download the result

# Result
