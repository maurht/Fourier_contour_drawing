Hi,

This is a quick project just done to demostrate something i knew was possible yet never really tried to do it.

The code works by extracting a contour out of an image using cv2. This is contained in contour.create_contour(). The setting in it work for the image i tested everything with, athough different settings might be necessary for other images in line 7.
I included a Jupyter notebook as a version to play with the setting and get the threshold just right, as the countour the cv2.findContours needs a well definied contour. Appropiate changes might be needed in the contour.py file.

For the image i used this was kinda easy but really for other images it might be a hazzle.

Once that is out of the way i found it appropiate to first calculate the fourier coefficients separetely as they are the most labor intensive part of the process and after funning that a file with the coefficients will be created. This files can of course be reused so that the calculation does not have to be done many times for one set of coefficients.
After that the main.py will create graphs where the veracity of the Fourier series is reprecented. 

The maths were really not an issue as they're pretty straight forward, yet the part were i struggled the most is the image processing as this is the first project i worked with cv2.
As the contour is just a well ordered set of points that if read from top to bottom or the other way around draw the intended image/contour, in theory, the later part of the program could take care of any curve that it may be presented with, so the part where the most improvement could go is where the contour is created.
