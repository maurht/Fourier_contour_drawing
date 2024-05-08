import cv2 as cv
import matplotlib.pyplot as plt

def create_contour(taffy: str):
    img = cv.imread(taffy, cv.IMREAD_UNCHANGED)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(img_gray,0,255,cv.THRESH_BINARY)


    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    c_n = 0

    c_x = [contours[c_n][i][0][0] for i in range(len(contours[c_n]))]
    c_y = [contours[c_n][i][0][1] for i in range(len(contours[c_n]))]

    return c_x, c_y