import numpy as np

import cv2 as cv
'''
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(101 ,169 ,108 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(83 ,182 ,200 ), thickness=-1)
cv.imwrite(r'b_g_y.png',square)
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(83 ,182 ,200 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(101 ,169 ,108 ), thickness=-1)
cv.imwrite(r'b_y_g.png',square)
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(101 ,169 ,108 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(101 ,169 ,108 ), thickness=-1)
cv.imwrite(r'b_g_g.png',square)
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(83 ,182 ,200 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(83 ,182 ,200 ), thickness=-1)
cv.imwrite(r'b_y_y.png',square)
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(127 ,120 ,124 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(127 ,120 ,124 ), thickness=-1)
cv.imwrite(r'b_gr_gr.png',square)
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(101 ,169 ,108 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(127 ,120 ,124 ), thickness=-1)
cv.imwrite(r'b_g_gr.png',square)
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(127 ,120 ,124 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(101 ,169 ,108 ), thickness=-1)
cv.imwrite(r'b_gr_g.png',square)
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(127 ,120 ,124 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(83 ,182 ,200 ), thickness=-1)
cv.imwrite(r'b_gr_y.png',square)
'''
square = np.zeros((64, 64, 3))
cv.rectangle(square,(0,0),(32,64),(83 ,200 ,182 ), thickness=-1)  
cv.rectangle(square,(32,0),(64,64),(127 ,120 ,124 ), thickness=-1)
cv.imwrite(r'b_y_gr.png',square)

#print(square.view())
#square_img = Image.fromarray(square)
#(gr,gr) (y,y) (g,g) (gr,y) (y,gr) (gr,g) (g,gr) (g,y) (y,g)
#square_img.show()



# yellow ---> 83 ,200 ,182 
# green ---> 101 ,108 ,169 
# grey ---> 127 ,120 ,124 