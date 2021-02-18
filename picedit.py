import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

def change_brightness(image, value):
    # Create a copy of the image loaded by user
    img = image.copy()
    
    # Store the image dimensions in local variables row and col
    row = len(img) 
    col = len(img[0]) 

    # Loop to add the user inputted value after undergoing an  
    # error check in menu function 
    for r in range(row):
        for c in range(col):
            for clr in range(0,3):
                #Add value to RGB component of pixel
                img[r,c,clr] += value
        
                # Ensure values of each RGB component doesn't exceed 
                # range of 0 to 255
                if img[r,c,clr] > 255:
                    img[r,c,clr] = 255
                elif img[r,c,clr] < 0:
                    img[r,c,clr] = 0

    #Return new image with its changed brightness
    return img
  
def change_contrast(image, value):
    # Create a copy of the image loaded by user
    img = image.copy()
    
    # Store the image dimensions in local variables row and col
    row = len(img)
    col = len(img[0]) 

    # Loop to add the user inputted value after undergoing an  
    # error check in menu function
    for r in range(row):
        for c in range(col):
            # Defining factor F which depends on user's value
            F = (259*(value+255))/(255*(259-value))
            
            for clr in range(0,3):
                # Calculate new RGB values
                img[r,c,clr] = F * (img[r,c,clr] - 128) + 128
            
                # Ensure value of each RGB component doesn't exceed 
                # range of 0 to 255
                if img[r,c,clr] > 255:
                    img[r,c,clr] = 255
                elif img[r,c,clr] < 0:
                    img[r,c,clr] = 0

    # Return new image with its changed contrast
    return img

def grayscale(image):
    # Create a copy of the image loaded by user
    img = image.copy()
   
    # Store the image dimensions in local variables row and col
    row = len(img) 
    col = len(img[0]) 

    # Iterate through the image array 
    for r in range(row):
        for c in range(col):
            
            # Calculate gray value using formula below
            gray = (0.3*img[r,c,0] + 0.59*img[r,c,1] + 0.11*img[r,c,2]) 

            # Ensure gray value is within range
            if gray > 255:
                gray = 255
            elif gray < 0:
                gray = 0
            
            # Assign the gray value to each RGB component of each pixel
            img[r,c,0] = gray
            img[r,c,1] = gray
            img[r,c,2] = gray

    #Return new grayscale image
    return img

def blur_effect(image):
    # Create a copy of the image; altered values are placed here
    img = image.copy()
    
    # Create a copy where values will be worked on but unchanged
    img_edit = image.copy()
    
    # Store the image dimensions in local variables row and col
    row = len(img) 
    col = len(img[0]) 

    # Iterate through image array 
    for r in range(row):
        for c in range(col):
            
            # If we're looking at pixels at the first/last row
            # pass them, don't apply the blur filter on them
            if r == 0 or r == row-1:
                pass
            
            # As long as the pixels are in the first or last column, 
            # pass through them without applying the blur filter 
            elif c == 0 or c == col-1:
                pass
            
            # If all conditions above were not met, pixel is not rejected
            # and hence undergoes blur filter outlined below
            else:
                # Create a matrix to store the 9 pixels' RGB values
                
                # Matrix of red values
                M_red = np.array([ [img_edit[r-1][c-1][0]], [img_edit[r-1][c][0]], [img_edit[r-1][c+1][0]],
                                   [img_edit[r][c-1][0]], [img_edit[r][c][0]], [img_edit[r][c+1][0]],
                                   [img_edit[r+1][c-1][0]], [img_edit[r+1][c][0]], [img_edit[r+1][c+1][0]] ])
                
                # Matrix of green values
                M_green = np.array([ [img_edit[r-1][c-1][1]], [img_edit[r-1][c][1]], [img_edit[r-1][c+1][1]],
                                     [img_edit[r][c-1][1]], [img_edit[r][c][1]], [img_edit[r][c+1][1]],
                                     [img_edit[r+1][c-1][1]], [img_edit[r+1][c][1]], [img_edit[r+1][c+1][1]] ])
                
                # Matrix of blue values
                M_blue = np.array([ [img_edit[r-1][c-1][2]], [img_edit[r-1][c][2]], [img_edit[r-1][c+1][2]],
                                    [img_edit[r][c-1][2]], [img_edit[r][c][2]], [img_edit[r][c+1][2]],
                                    [img_edit[r+1][c-1][2]], [img_edit[r+1][c][2]], [img_edit[r+1][c+1][2]] ])
                
                # Gaussian matrix
                k = np.array([[0.0625], [0.125], [0.0625],
                              [0.125], [0.25], [0.125],
                              [0.0625], [0.125], [0.0625]])
                   
                # Derive new RGB components
                new_red = sum(M_red*k)
                new_green = sum(M_green*k)
                new_blue = sum(M_blue*k)
                
                # Ensure RGB values within range 0-255
                if new_red > 255:
                    new_red = 255
                elif new_red < 0:
                    new_red = 0
                    
                if new_green > 255:
                    new_green = 255
                elif new_green < 0:
                    new_green= 0    
                 
                if new_blue > 255:
                    new_blue = 255
                elif new_blue < 0:
                    new_blue = 0    
                
                # Assign the pixel new blurred RGB components
                img[r,c,0] = new_red
                img[r,c,1] = new_green
                img[r,c,2] = new_blue
    
    # Return newly blurred image
    return img

def edge_detection(image):
    # Create a copy of the image; altered values are placed here
    img = image.copy()
    
    # Create a copy where values will be worked on but unchanged
    img_edit = image.copy()

    # Store the image dimensions in local variables row and col
    row = len(img) 
    col = len(img[0]) 

    # Iterate through the image array
    for r in range(row):
        for c in range(col):
            
            # If we're looking at pixels at the first/last row
            # pass them, don't apply the filter on them
            if r == 0 or r == row-1:
                pass
            
            # As long as the pixels are in the first or last column, 
            # pass through them without applying the blur filter 
            elif c == 0 or c == col-1:
                pass
            
            # If all conditions above were not met, pixel is not rejected
            # and hence undergoes edge detection outlined below
            else:
                # Create a matrix to store the 9 pixels' RGB values
                
                # Matrix of red values
                M_red = np.array([ [img_edit[r-1][c-1][0]], [img_edit[r-1][c][0]], [img_edit[r-1][c+1][0]],
                                   [img_edit[r][c-1][0]], [img_edit[r][c][0]], [img_edit[r][c+1][0]],
                                   [img_edit[r+1][c-1][0]], [img_edit[r+1][c][0]], [img_edit[r+1][c+1][0]] ])
                
                # Matrix of green values
                M_green = np.array([ [img_edit[r-1][c-1][1]], [img_edit[r-1][c][1]], [img_edit[r-1][c+1][1]],
                                     [img_edit[r][c-1][1]], [img_edit[r][c][1]], [img_edit[r][c+1][1]],
                                     [img_edit[r+1][c-1][1]], [img_edit[r+1][c][1]], [img_edit[r+1][c+1][1]] ])
                
                # Matrix of blue values
                M_blue = np.array([ [img_edit[r-1][c-1][2]], [img_edit[r-1][c][2]], [img_edit[r-1][c+1][2]],
                                    [img_edit[r][c-1][2]], [img_edit[r][c][2]], [img_edit[r][c+1][2]],
                                    [img_edit[r+1][c-1][2]], [img_edit[r+1][c][2]], [img_edit[r+1][c+1][2]] ])
                
                # Edge detection matrix
                k = np.array([[-1], [-1], [-1],
                              [-1], [8], [-1],
                              [-1], [-1], [-1]])
                
                # Derive new RGB components
                new_red = sum(M_red*k) + 128
                new_green = sum(M_green*k) + 128
                new_blue = sum(M_blue*k) + 128
                
                # Ensure values within range 0-255
                if new_red > 255:
                    new_red = 255
                elif new_red < 0:
                    new_red = 0
                    
                if new_green > 255:
                    new_green = 255
                elif new_green < 0:
                    new_green= 0    
                 
                if new_blue > 255:
                    new_blue = 255
                elif new_blue < 0:
                    new_blue = 0    
                
                # Assign the pixel new & error-checked RGB components
                img[r,c,0] = new_red 
                img[r,c,1] = new_green
                img[r,c,2] = new_blue
                
    # Return newly edge-detected image
    return img

def embossed(image):
    # Create a copy of the image; altered values are placed here
    img = image.copy()
    
    # Create a copy where values will be worked on but unchanged
    img_edit = image.copy()
    
    # Store the image dimensions in local variables row and col
    row = len(img) 
    col = len(img[0]) 
    
    # Iterate through the image array
    for r in range(row):
        for c in range(col):
            
            # If we're looking at pixels at the first/last row
            # pass them, don't apply the filter on them
            if r == 0 or r == row-1:
                pass
            
            # As long as the pixels are in the first or last column, 
            # pass through them without applying the blur filter 
            elif c == 0 or c == col-1:
                pass
            
            # If all conditions above were not met, pixel is not rejected
            # and hence undergoes embossing process outlined below
            else:
                # Create a matrix to store the 9 pixels' RGB values
                
                # Matrix of red values
                M_red = np.array([ [img_edit[r-1][c-1][0]], [img_edit[r-1][c][0]], [img_edit[r-1][c+1][0]],
                                    [img_edit[r][c-1][0]], [img_edit[r][c][0]], [img_edit[r][c+1][0]],
                                    [img_edit[r+1][c-1][0]], [img_edit[r+1][c][0]], [img_edit[r+1][c+1][0]] ])
                
                # Matrix of green values
                M_green = np.array([ [img_edit[r-1][c-1][1]], [img_edit[r-1][c][1]], [img_edit[r-1][c+1][1]],
                                    [img_edit[r][c-1][1]], [img_edit[r][c][1]], [img_edit[r][c+1][1]],
                                    [img_edit[r+1][c-1][1]], [img_edit[r+1][c][1]], [img_edit[r+1][c+1][1]] ])
                
                # Matrix of blue values
                M_blue = np.array([ [img_edit[r-1][c-1][2]], [img_edit[r-1][c][2]], [img_edit[r-1][c+1][2]],
                                    [img_edit[r][c-1][2]], [img_edit[r][c][2]], [img_edit[r][c+1][2]],
                                    [img_edit[r+1][c-1][2]], [img_edit[r+1][c][2]], [img_edit[r+1][c+1][2]] ])
                
                # Embossed matrix
                k = np.array([[-1], [-1], [0],
                              [-1], [0], [1],
                              [0], [1], [1]])
                
                # Derive new RGB components
                new_red = sum(M_red*k) + 128
                new_green = sum(M_green*k) + 128
                new_blue = sum(M_blue*k) + 128
                
                # Ensure values within range 0-255
                if new_red > 255:
                    new_red = 255
                elif new_red < 0:
                    new_red = 0
                    
                if new_green > 255:
                    new_green = 255
                elif new_green < 0:
                    new_green= 0    
                 
                if new_blue > 255:
                    new_blue = 255
                elif new_blue < 0:
                    new_blue = 0    
                
                # Assign the pixel new & error-checked RGB components
                img[r,c,0] = new_red 
                img[r,c,1] = new_green
                img[r,c,2] = new_blue
                
    #Return new embossed image
    return img

def rectangle_select(image, x, y):
    # Create a copy of the image
    img = image.copy()            

    # Store the image dimensions in local variables row and col
    row = len(img) 
    col = len(img[0]) 
    
    # Creates mask populated with zeros
    mask = np.zeros((len(img), len(img[0])))
    
    # Iterate through the mask array
    for r in range(row):
        for c in range(col):
            # If pixel has row and column within range of the top
            # and bottom pixel (r,c) values, then select it by assigning
            # value of 1 in the mask array
            if x[0] <= r <= y[0] and x[1] <= c <= y[1]:
                mask[r,c] = 1    

    # Return new mask array
    return mask
    
def magic_wand_select(image, x, thres):
    # Create a copy of the image
    img = image.copy()            
    
    # Store dimensions of img numpy array
    row = len(img)
    col = len(img[0])
    
    # Creates mask populated with zeros
    mask = np.zeros((len(img),len(img[0])))
    
    # Create a list to store the coordinates of pixels starting with x
    # in which its neighbours have yet to be checked
    tbc = [x]
    
    # Select pixel x in the mask array 
    mask[x] = 1

    # Save the x and y - coordinates of the input x pixel
    xx = x[0]
    xy = x[1]
    
    # Keep looping if the list tbc is not empty yet
    while tbc:
        
            # Assign a variable to store row and column value of 
            # the last element in the list, then remove it
            r = tbc[-1][0]
            c = tbc[-1][1]
            tbc.pop()
            
            # Row above and below respectively
            i = r-1
            j = r+1
            
            # Column to the right and left respectively
            k = c+1
            l = c-1
            
            # If the neighbouring coordinates are not yet checked and 
            # it does not exceed size of image, proceed to calculate 
            if 0 <= i < row and mask[i,c] == 0:
                
                # Check top pixel
                red_diff = img[xx,xy,0] - img[i,c,0]
                green_diff = img[xx,xy,1] - img[i,c,1]
                blue_diff = img[xx,xy,2] - img[i,c,2]
                avg_red = (img[xx,xy,0] + img[i,c,0]) / 2
        
                # Calculate colour distance of top pixel
                dist = math.sqrt( (2+(avg_red)/256) * (red_diff**2) + (4*(green_diff**2)) + (2+(255-avg_red)/256) * (blue_diff**2) )
    
                # Select in mask array if colour distance is equal to 
                # or smaller than the thres value
                if dist <= thres:
                    mask[i,c] = 1
                    tbc.append((i,c)) 
                
                # Assign checked values that are not selected the value 2 in the mask
                else:
                    mask[i,c] = 2
                
            # If the neighbouring bottom coordinates are yet to be checked 
            # and it does not exceed size of image, proceed to calculate 
            if  0 <= j < row and mask[j,c] == 0:
                # Check bottom pixel
                red_diff = img[xx,xy,0] - img[j,c,0]
                green_diff = img[xx,xy,1] - img[j,c,1]
                blue_diff = img[xx,xy,2] - img[j,c,2]
                avg_red = (img[xx,xy,0] + img[j,c,0]) / 2
        
                # Calculate colour distance of bottom pixel
                dist = math.sqrt( (2+(avg_red)/256) * (red_diff**2) + (4*(green_diff**2)) + (2+(255-avg_red)/256) * (blue_diff**2) )
        
                # Select in mask array if colour distance is equal to 
                # or smaller than the thres value
                if dist <= thres:
                    mask[j,c] = 1
                    tbc.append((j,c))
                # Assign checked values that are not selected the value 2 in the mask
                else:
                    mask[j,c] = 2
                
            # If the neighbouring right oordinates are yet to be checked  
            # and it does not exceed size of image, proceed to calculate         
            if 0 <= k < col and mask[r,k] == 0:
                # Check right pixel
                red_diff = img[xx,xy,0] - img[r,k,0]
                green_diff = img[xx,xy,1] - img[r,k,1]
                blue_diff = img[xx,xy,2] - img[r,k,2]
                avg_red = (img[xx,xy,0] + img[r,k,0]) / 2
        
                # Calculate colour distance of right pixel
                dist = math.sqrt( (2+(avg_red)/256) * (red_diff**2) + (4*(green_diff**2)) + (2+(255-avg_red)/256) * (blue_diff**2) )
    
                if dist <= thres:
                    mask[r,k] = 1
                    tbc.append((r,k))  
                # Assign checked values that are not selected the value 2 in the mask
                else: 
                    mask[r,k] = 2
            
        # If the neighbouring left coordinates are yet to be checked 
        # and it does not exceed size of image, proceed to calculate         
            if 0 <= l < col and mask[r,l] == 0: 
                # Check left pixel
                red_diff = img[xx,xy,0] - img[r,l,0]
                green_diff = img[xx,xy,1] - img[r,l,1]
                blue_diff = img[xx,xy,2] - img[r,l,2]
                avg_red = (img[xx,xy,0] + img[r,l,0]) / 2
        
                # Calculate colour distance of left pixel
                dist = math.sqrt( (2+(avg_red)/256) * (red_diff**2) + (4*(green_diff**2)) + (2+(255-avg_red)/256) * (blue_diff**2) )
                
                # Select in mask array if colour distance is equal to 
                # or smaller than the thres value
                if dist <= thres:
                    mask[r,l] = 1
                    tbc.append((r,l))
                # Assign checked values that are not selected the value 2 in the mask
                else:
                    mask[r,l] = 2
                    
    # Iterate through mask array to assign '2' back to '0'           
    for r in range(row):
        for c in range(col):
            if mask[r,c] == 2:
                mask[r,c] = 0
                
    return mask

def compute_edge(mask):           
    rsize, csize = len(mask), len(mask[0]) 
    edge = np.zeros((rsize,csize))
    if np.all((mask == 1)): return edge        
    for r in range(rsize):
        for c in range(csize):
            if mask[r][c]!=0:
                if r==0 or c==0 or r==len(mask)-1 or c==len(mask[0])-1:
                    edge[r][c]=1
                    continue
                
                is_edge = False                
                for var in [(-1,0),(0,-1),(0,1),(1,0)]:
                    r_temp = r+var[0]
                    c_temp = c+var[1]
                    if 0<=r_temp<rsize and 0<=c_temp<csize:
                        if mask[r_temp][c_temp] == 0:
                            is_edge = True
                            break
    
                if is_edge == True:
                    edge[r][c]=1
            
    return edge

def save_image(filename, image):
    img = image.astype(np.uint8)
    mpimg.imsave(filename,img)

def load_image(filename):
    img = mpimg.imread(filename)
    if len(img[0][0])==4: # if png file
        img = np.delete(img, 3, 2)
    if type(img[0][0][0])==np.float32:  # if stored as float in [0,..,1] instead of integers in [0,..,255]
        img = img*255
        img = img.astype(np.uint8)
    mask = np.ones((len(img),len(img[0]))) # create a mask full of "1" of the same size of the laoded image
    img = img.astype(np.int32)
    return img, mask

def display_image(image, mask):
    # if using Spyder, please go to "Tools -> Preferences -> IPython console -> Graphics -> Graphics Backend" and select "inline"
    tmp_img = image.copy()
    edge = compute_edge(mask)
    for r in range(len(image)):
        for c in range(len(image[0])):
            if edge[r][c] == 1:
                tmp_img[r][c][0]=255
                tmp_img[r][c][1]=0
                tmp_img[r][c][2]=0
 
    plt.imshow(tmp_img)
    plt.axis('off')
    plt.show()
    print("Image size is",str(len(image)),"x",str(len(image[0])))

def menu():
    img = np.array([])
    
    # While image hasn't been loaded, keep prompting user for action
    while img.size == 0:
        choice = input('What do you want to do?\n' 
                       'e - exit\n'
                       'l - load a picture\n'
                       '\nYour choice:')
        # Exit
        if choice == 'e':
            break
        
        # Load a picture
        elif choice == 'l':
            while True:
                # Continuously prompt for file name until it is a valid
                # image file type
                try:
                    filename = input("Please input a .png or .jpg file:")
                    if filename[-4:] == ".jpg" or filename[-4:] == ".png":
                        # load_image() returns img and mask
                        img, mask = load_image(filename)
                        # Create copy of the image loaded by user
                        masked_img = img.copy()
                        # Create a copy of the original mask (all pixels selected)
                        orig_mask = mask.copy()
                        break
                except FileNotFoundError: 
                    print("\nFile not found")
        
        # Any other input other than 'e' and 'l', prompt for user input  
        else:
            print("\nPlease either load an image or exit the program")

    while img.size > 0:
        # Keep printing menu after each action until user inputs 'e'
        choice = input('What do you want to do?\n'
                       'e - exit\n'
                       'l - load a picture\n'
                       's - save the current picture\n'
                       '1 - adjust brightness\n'
                       '2 - adjust contrast\n'
                       '3 - apply grayscale\n'
                       '4 - apply blur\n'
                       '5 - edge detection\n'
                       '6 - embossed\n'
                       '7 - rectangle select\n'
                       '8 - magic wand select\n'
                       '9 - sepia effect'
                       '\nYour choice:')
        # Exit
        if choice == 'e':
            break
        
        # Load a picture
        elif choice == 'l':
            while True:
                # Continuously prompt for file name until it is a valid
                # image file type
                try:
                    filename = input("Please input a png or jpg file:")
                    if filename.lower()[-4:] == ".jpg" or filename.lower()[-4:] == ".png":
                      # load_image() returns img and mask
                      img, mask = load_image(filename)
                      # Create copy of the image loaded by user
                      masked_img = img.copy()
                      # Create a copy of the original mask (all pixels selected)
                      orig_mask = mask.copy()
                      break
                except FileNotFoundError: 
                        print("\nFile not found")
        
        # Save current picture
        elif choice == 's':
            # No return object
            save_image(filename, img)
            
        # Adjust brightness
        elif choice == '1':
            # Store the image dimensions in local variables row and col
            row = len(img) 
            col = len(img[0]) 
            
            # Getting error-checked user inputs
            while True:
                # Ensure value is within range and right data type
                    try:
                        value = int(input("Please input a value from -255 to 255:"))
                        # If value is within -255 and 255 then break out of the loop
                        if value >= -255 and value <= 255:
                            break
                    except ValueError or TypeError:
                        continue
                    
            # Filter whole image first       
            img = change_brightness(img, value)
            
            # As the mask can only contain 0 (not selected) or 1 (selected),
            # if the number of non-zeros = row x column of image that means the
            # whole image is selected in the mask, hence just display full image
            if np.count_nonzero(mask) == row * col:
                # Store latest copy of image in masked_img
                masked_image = img.copy()
                display_image(img,mask)
                    
            else:
                # Iterate through the masked_img array
                for r in range(row):
                    for c in range(col):
                        # If pixel is selected in mask array
                        # replace the selected with the filtered pixel from img
                        if mask[r,c] == 1:
                            masked_img[r,c] = img[r,c] 
                
                # Store latest copy of image in img
                img = masked_img.copy()    
                # Display the image with only the selected mask changed
                display_image(masked_img, orig_mask)
                            
        # Adjust contrast
        elif choice == '2':
            # Store the image dimensions in local variables row and col
            row = len(img) 
            col = len(img[0]) 
            
            # Getting error-checked user inputs
            while True:
                # Ensure value is within range and right data type
                    try:
                        value = int(input("Please input a value from -255 to 255:"))
                        # If value is within -255 and 255 then break out of the loop
                        if value >= -255 and value <= 255:
                            break
                    except ValueError or TypeError:
                        continue
                    
            # Filter whole image first       
            img = change_contrast(img, value)
            
            # As the mask can only contain 0 (not selected) or 1 (selected),
            # if the number of non-zeros = row x column of image that means the
            # whole image is selected in the mask, hence just display full image
            if np.count_nonzero(mask) == row * col:
                # Store latest copy of image in masked_img
                masked_image = img.copy()
                display_image(img,mask)
                    
            else:
                # Iterate through the masked_img array
                for r in range(row):
                    for c in range(col):
                        # If pixel is selected, replace with the filtered pixel
                        if mask[r,c] == 1:
                            masked_img[r,c] = img[r,c]
                            
                # Store latest copy of image in img            
                img = masked_img.copy()      
                # Display the image with only the selected mask changed
                display_image(masked_img,orig_mask)
            
        # Grayscale effect
        elif choice == '3':
            # Store the image dimensions in local variables row and col
            row = len(img) 
            col = len(img[0]) 
            
            # Filter whole image first
            img = grayscale(img)
            
            # As the mask can only contain 0 (not selected) or 1 (selected),
            # if the number of non-zeros = row x column of image that means the
            # whole image is selected in the mask, hence just display full image
            if np.count_nonzero(mask) == row * col:
                # Store latest copy of image in masked_img
                masked_image = img.copy()
                display_image(img,mask)
                    
            else:
                # Iterate through the masked_img array
                for r in range(row):
                    for c in range(col):
                        # If pixel is selected, replace with the filtered pixel
                        if mask[r,c] == 1:
                            masked_img[r,c] = img[r,c]
                
                # Store latest copy of image in img
                img = masked_img.copy()            
                # Display the image with only the selected mask changed
                display_image(masked_img,orig_mask)
            
        # Blur effect
        elif choice == '4':
            # Store the image dimensions in local variables row and col
            row = len(img) 
            col = len(img[0]) 
            
            img = blur_effect(img)
            
            # As the mask can only contain 0 (not selected) or 1 (selected),
            # if the number of non-zeros = row x column of image that means the
            # whole image is selected in the mask, hence just display full image
            if np.count_nonzero(mask) == row * col:
                # Store latest copy of image in masked_img
                masked_image = img.copy()
                display_image(img,mask)
                    
            else:
                # Iterate through the masked_img array
                for r in range(row):
                    for c in range(col):
                        # If pixel is selected, replace with the filtered pixel
                        if mask[r,c] == 1:
                            masked_img[r,c] = img[r,c]
                            
                # Store latest copy of image in img            
                img = masked_img.copy()
                # Display the image with only the selected mask changed
                display_image(masked_img,orig_mask)
            
        # Edge detection
        elif choice == '5':
            
            # Store the image dimensions in local variables row and col
            row = len(img) 
            col = len(img[0]) 
            
            img = edge_detection(img)
            
            # As the mask can only contain 0 (not selected) or 1 (selected),
            # if the number of non-zeros = row x column of image that means the
            # whole image is selected in the mask, hence just display full image
            if np.count_nonzero(mask) == row * col:
                # Store latest copy of image in masked_img
                masked_image = img.copy()
                display_image(img,mask)
                    
            else:
                # Iterate through the masked_img array
                for r in range(row):
                    for c in range(col):
                        # If pixel is selected, replace with the filtered pixel
                        if mask[r,c] == 1:
                            masked_img[r,c] = img[r,c]
                
                # Store latest copy of image in img
                img = masked_img.copy()
                # Display the image with only the selected mask changed
                display_image(masked_img,orig_mask)
                
        # Embossed
        elif choice == '6':
            # Store the image dimensions in local variables row and col
            row = len(img) 
            col = len(img[0]) 
            
            img = embossed(img)
            
            # As the mask can only contain 0 (not selected) or 1 (selected),
            # if the number of non-zeros = row x column of image that means the
            # whole image is selected in the mask, hence just display full image
            if np.count_nonzero(mask) == row * col:
                # Store latest copy of image in masked_img
                masked_image = img.copy()
                display_image(img,mask)
                    
            else:
                # Iterate through the masked_img array
                for r in range(row):
                    for c in range(col):
                        # If pixel is selected, replace with the filtered pixel
                        if mask[r,c] == 1:
                            masked_img[r,c] = img[r,c]
                
                # Store latest copy of image in img
                img = masked_img.copy()
                # Display the image with only the selected mask changed
                display_image(masked_img, orig_mask)
             
        # Rectangle select    
        elif choice == '7':
            # Store the image dimensions in local variables row and col
            row = len(img) - 1
            col = len(img[0])- 1
            
            while True: #outer
                    # Get row value for pixel x (top left)
                    try:
                        while True: #inner 
                            xx = int(input("Enter row value of the top left pixel:"))
                            # If exceeds img dimensions, prompt again
                            if xx < 0 or xx > row:
                                print(f"Please enter a value within 0 to {row}")
                                continue #with inner loop
                            else:
                                break #out of inner while loop
                    except (ValueError or TypeError):
                        print(f"Please enter a valid integer value within 0 to {row}")
                        continue #with outer while loop
                    break #out of outer while loop
                    
            while True: #outer
                # Get column value for pixel x (top left)
                try:
                    while True: #inner
                        xy = int(input("Enter column value of the top left pixel:"))
                        # If exceeds img dimensions, prompt again
                        if xy < 0 or xy > col:
                            print(f"Please enter a value within 0 to {col}")
                            continue #with inner while loop
                        else:
                            break #out of inner while loop
                except (ValueError or TypeError):
                    print(f"Please enter a valid integer value within 0 to {col}")
                    continue #with outer while loop
                break #out of outer while loop
              
            while True: #outer
                # Get row value for pixel y (bottom right)
                try:
                    while True: #inner
                        yx = int(input("Enter row value of the bottom right pixel:"))
                        # If exceeds img dimensions, prompt again
                        if yx < 0 or yx > row or yx < xx:
                            print(f"Please enter a value within {xx} to {row}.")
                            continue #with inner while loop
                        else:
                            break #out of inner while loop
                except (ValueError or TypeError):
                    print(f"Please enter a value within {xx} to {row}.")
                    continue #with outer while loop
                break #out of outer while loop
            
            while True: #outer
                # Get column value for pixel y (bottom right)
                try: 
                    while True: #inner
                        yy = int(input("Enter column value of the bottom right pixel:"))
                        # If exceeds img dimensions, prompt again
                        if yy < 0 or yy > col or yy < xy:
                            print(f"Please enter a value within {xy} to {col}")
                            continue #with inner while loop
                        else:
                            break #out of inner while loop
                except (ValueError or TypeError):
                    print(f"Please enter a value within {xy} to {col}.")
                    continue #with outer while loop
                break #out of outer while loop
                
            # Store the obtained ints in a tuple as coordinates for pixels x & y
            x = (xx, xy)
            y = (yx, yy)

            # Apply rectangle selection function
            mask = rectangle_select(img, x, y)
            display_image(img, mask)
                
        # Magic wand selection        
        elif choice == '8':
            # Store the image dimensions in local variables row and col
            row = len(img) - 1
            col = len(img[0]) - 1 
            
            while True:
                # Get row value for pixel x (top left)
                try:
                    while True:
                        xx = int(input("Enter the row value of the pixel:"))
                        # If exceeds img dimensions, prompt again
                        if xx < 0 or xx > row:
                            print(f"Please enter a value within 0 to {row}")
                            continue #with inner while loop
                        else: 
                            break #out of inner while loop
                except (ValueError or TypeError or UnboundLocalError):
                    print(f"Please enter a valid integer value within 0 to {row}")
                    continue #with outer while loop
                break #out of outer while loop
                
            while True:    
                # Get column value for pixel x (top left)
                try:
                    while True:
                        xy = int(input("Enter the column value of the pixel:"))
                        # If exceeds img dimensions, prompt again
                        if xy < 0 or xy > col:
                            print(f"Please enter a value within 0 to {col}")
                            continue #with inner while loop
                        else: 
                            break #out of inner while loop
                except (ValueError or TypeError or UnboundLocalError):
                    print(f"Please enter a valid integer value within 0 to {col}")
                    continue #with outer while loop
                break #out of outer while loop
                
            while True:
                try:
                    thres = float(input("Enter an appropriate threshold  value:"))
                    if thres >= 0:
                        break
                    else:
                        print("Threshold value cannot be negative, please try again!")
                except (ValueError or TypeError or UnboundLocalError):
                    print("A common value for a threshold is 300, please try again")
                    continue #with outer while loop
                
            # Store the obtained ints in a tuple as coordinates for pixel x 
            x = (xx, xy)
            # Apply magic wand selection on image
            mask = magic_wand_select(img, x, thres)     
            display_image(img, mask)
        
        elif choice == '9':
            # Store the image dimensions in local variables row and col
            row = len(img) 
            col = len(img[0]) 
            
            # Apply filter on the whole image first
            img = sepia(img)
            
            # As the mask can only contain 0 (not selected) or 1 (selected),
            # if the number of non-zeros = row x column of image that means the
            # whole image is selected in the mask, hence just display full image
            if np.count_nonzero(mask) == row * col:
                # Store latest copy of image in masked_img
                masked_image = img.copy()
                display_image(img,mask)
                    
            else:
                # Iterate through the masked_img array
                for r in range(row):
                    for c in range(col):
                        # If pixel is selected, replace with the filtered pixel
                        if mask[r,c] == 1:
                            masked_img[r,c] = img[r,c]
                
                # Store latest copy of image in img
                img = masked_img.copy()
                display_image(masked_img,orig_mask)
            
        # If none of the inputs were valid, reprompt with an error message
        else:
            print("\nPlease input a valid option as seen from the menu")
                
# extra filters for fun            
def sepia(image):
    # Create a copy of image to work on
    img = image.copy()
    
    # Store dimensions of image array in local variables
    row = len(img)
    col = len(img[0])
    
    # Iterate through the image array to generate sepia values
    for r in range(row):
        for c in range(col): 
            
                # Store original RGB values for easy access
                orig_red = img[r,c,0]
                orig_green = img[r,c,1]
                orig_blue = img[r,c,2]
                
                # Calculate new RGB values using sepia formula
                new_red = (.393 * orig_red) + (.769 * orig_green + (.189 * orig_blue) )
                new_green = (orig_red * .349) + (orig_green *.686) + (orig_blue * .168)
                new_blue = (orig_red * .272) + (orig_green *.534) + (orig_blue * .131)
                
                # Error checking all three new RGB values
                if new_red > 255:
                    new_red = 255
                elif new_red < 0:
                    new_red = 0
                
                if new_green > 255:
                    new_green = 255
                elif new_green < 0:
                    new_green = 0
                    
                if new_blue > 255:
                    new_blue = 255
                elif new_blue < 0:
                    new_blue = 0
                    
                # Assign error-checked new sepia values to pixel
                img[r,c,0] = new_red
                img[r,c,1] = new_green
                img[r,c,2] = new_blue
                
    return img

if __name__ == "__main__":
    menu()





