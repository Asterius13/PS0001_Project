# PS0001_Project
Codes for all functions related and needed for the project.

#The code here is done solely by me, the GitHub user: Asterius13 for a university module project.
#This is a simple photo editing 'app' in which I had to implement the functions given a skeleton of the file named picedit.py.
#The functions completed by me are: change_brightness, change_contrast, grayscale, blur_effect, embossed_effect, edge_detection, rectangle_select, magic_wand_select, sepia 
and lastly a menu function. The rest were implemented beforehand and I need not touch them for the project.

#change_brightness: accept a value from the user ranging from -255 to 255 to change its RGB values by.

#change_contrast: accept a value from the user ranging from -255 to 255 to change its RGB values by.

#grayscale: using a formula and the 3 RGB components of each pixel, compute a new gray value and assign it to that pixel's RGB components.

#blur_effect: use a numpy array of the image to do matrix multiplication with the gaussian matrix. pixels at the sides are untouched/unfiltered.

#embossed_effect: use a numpy array of the image to do matrix multiplication with the emboss matrix(provided in project details of the module I was taking). 
                  pixels at the sides are untouched/unfiltered.
                  
#edge_detection:  use a numpy array of the image to do matrix multiplication with the edge detection matrix(provided in project details of the module I was taking). 
                  pixels at the sides are untouched/unfiltered.                
                  
#rectangle_select: given that the user will give an input top left pixel and bottom right pixel, select this certain portion of the image in a mask such that future 
                   changes or filters applied will only apply to that portion selected by the user.
                   
#magic_wand_select: given a certain thres value by the user as well as a pixel in the image, compare colour distances of neighbouring pixels using a formula
                    (provided in project details). only select the pixel if its colour distance is within the thres value.
                    
#sepia: not compulsory; implemented for fun but it is based on a formula found on stackoverflow but the loops and rest of the code are original.

#This is my first major project that I've completed on my own hence I'm quite satisfied with how it turned out despite my lacking skills in Python.
