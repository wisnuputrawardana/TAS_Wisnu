from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np

# Window
window_threshold_color = 'Threshold Color'
window_threshold_circle = 'Threshold Circle'

# Value of HSV Circle           
low_H = 0
low_S = 76
low_V = 156
high_H = 12  # max_value_H
high_S = 255
high_V = 255

low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'

# Value of Hough
min_circ = 1
max_circ = 250
parame1 = 100
parame2 = 9
minDistance = 100
dp = 1
dp_name = "Dp"
minDist_name = "MinDist"
min_circ_name = 'Min r'
max_circ_name = 'Max r'
parame1_name = 'param1'
parame2_name = 'param2'

# mopohology
erotion_name = 'erotion'
dilation_name = 'dilasi'
erotion = 0
dilation = 0

# =============================Value Circle================================

def on_low_H_thresh_trackbar(val):
    global low_H
    low_H = val
    cv.setTrackbarPos(low_H_name, window_threshold_color, low_H)

def on_high_H_thresh_trackbar(val):
    global high_H
    high_H = val
    cv.setTrackbarPos(high_H_name, window_threshold_color, high_H)


def on_low_S_thresh_trackbar(val):
    global low_S
    low_S = val
    cv.setTrackbarPos(low_S_name, window_threshold_color, low_S)


def on_high_S_thresh_trackbar(val):
    global high_S
    high_S = val
    cv.setTrackbarPos(high_S_name, window_threshold_color, high_S)


def on_low_V_thresh_trackbar(val):
    global low_V
    low_V = val
    cv.setTrackbarPos(low_V_name, window_threshold_color, low_V)


def on_high_V_thresh_trackbar(val):
    global high_V
    high_V = val
    cv.setTrackbarPos(high_V_name, window_threshold_color, high_V)

def on_Dp_thresh_trackbar(val):
    global dp
    dp = val
    if(dp == 0):
        dp = 1
    else:
        dp = dp
    cv.setTrackbarPos(dp_name, window_threshold_circle, dp)

def on_minDist_thresh_trackbar(val):
    global minDistance
    minDistance = val
    if(minDistance == 0):
        minDistance = 1
    else:
        minDistance = minDistance
    cv.setTrackbarPos(minDist_name, window_threshold_circle, minDistance)

def on_min_circ_thresh_trackbar(val):
    global min_circ
    global max_circ
    min_circ = val
    if(min_circ >= max_circ):
        min_circ = max_circ
    else:
        min_circ = min_circ
    cv.setTrackbarPos(min_circ_name, window_threshold_circle, min_circ)


def on_max_circ_thresh_trackbar(val):
    global min_circ
    global max_circ
    max_circ = val
    if(max_circ <= min_circ):
        max_circ = min_circ
    else:
        max_circ = max_circ
    cv.setTrackbarPos(max_circ_name, window_threshold_circle, max_circ)


def on_param1_thresh_trackbar(val):
    global parame1
    parame1 = val
    if(parame1 <= 10):
        parame1 = 10
    else:
        parame1 = parame1
    cv.setTrackbarPos(parame1_name, window_threshold_circle, parame1)


def on_param2_thresh_trackbar(val):
    global parame2
    parame2 = val
    if(parame2 <= 10):
        parame2 = 10
    else:
        parame2 = parame2
    cv.setTrackbarPos(parame2_name, window_threshold_circle, parame2)


def on_erotion_thresh_trackbar(val):
    global erotion
    erotion = val
    cv.setTrackbarPos(erotion_name, window_threshold_circle, erotion)


def on_dilation_thresh_trackbar(val):
    global dilation
    dilation = val
    cv.setTrackbarPos(dilation_name, window_threshold_circle, dilation)


cap = cv.VideoCapture(0)
cv.namedWindow(window_threshold_color, cv.WINDOW_NORMAL)
cv.namedWindow(window_threshold_circle, cv.WINDOW_NORMAL)
cv.resizeWindow(window_threshold_color, 300, 200)
cv.resizeWindow(window_threshold_circle, 300, 200)

# =============================Value Circle================================
cv.createTrackbar(low_H_name, window_threshold_color, low_H, 179, on_low_H_thresh_trackbar)
cv.createTrackbar(high_H_name, window_threshold_color, high_H, 179, on_high_H_thresh_trackbar)
cv.createTrackbar(low_S_name, window_threshold_color, low_S, 255, on_low_S_thresh_trackbar)
cv.createTrackbar(high_S_name, window_threshold_color, low_H, 255, on_high_S_thresh_trackbar)
cv.createTrackbar(low_V_name, window_threshold_color, low_V, 255, on_low_V_thresh_trackbar)
cv.createTrackbar(high_V_name, window_threshold_color, high_V, 255, on_high_V_thresh_trackbar)
cv.createTrackbar(dp_name, window_threshold_circle, dp, 2, on_Dp_thresh_trackbar)
cv.createTrackbar(minDist_name, window_threshold_circle, minDistance, 500, on_minDist_thresh_trackbar)
cv.createTrackbar(min_circ_name, window_threshold_circle, min_circ, 500, on_min_circ_thresh_trackbar)
cv.createTrackbar(max_circ_name, window_threshold_circle, max_circ, 500, on_max_circ_thresh_trackbar)
cv.createTrackbar(parame1_name, window_threshold_circle, parame1, 100, on_param1_thresh_trackbar)
cv.createTrackbar(parame2_name, window_threshold_circle, parame2, 100, on_param2_thresh_trackbar)
cv.createTrackbar(erotion_name, window_threshold_circle, erotion, 50, on_erotion_thresh_trackbar)
cv.createTrackbar(dilation_name, window_threshold_circle, dilation, 50, on_dilation_thresh_trackbar)


while True:

    ret, frame = cap.read()
    if frame is None:
        break
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # ===============================Detection Circle=============================
    frame_threshold_circle = cv.inRange(
        frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    frame_threshold_circle = cv.medianBlur(frame_threshold_circle, 5)

    # --------------------------------Morphology---------------------------------
    element_erotion = cv.getStructuringElement(
        cv.MORPH_ELLIPSE, (2*erotion+1, 2 * erotion+1))
    res_erotion = cv.morphologyEx(frame_threshold_circle, 2, element_erotion)

    element_dilation = cv.getStructuringElement(
        cv.MORPH_ELLIPSE, (2*dilation+1, 2*dilation+1))
    res_dilation = cv.morphologyEx(res_erotion, 3, element_dilation)

    # -------------------------------HoughCircles-----------------------------------
    circles = cv.HoughCircles(
        res_dilation, cv.HOUGH_GRADIENT, dp = dp, minDist = minDistance, param1=parame1, param2=parame2, minRadius=min_circ, maxRadius=max_circ)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            print("Objek x:", x, "  Objek y:", y, "  radius:", r)
            # draw the circle in the output image, then draw a rectangle
            cv.circle(frame, (x, y), r, (0, 255, 0), 2)
            cv.circle(frame, (x, y), 1, (0, 255, 0), 1)

    cv.imshow(window_threshold_color, res_dilation)
    cv.imshow(window_threshold_circle, frame)

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        cv.destroyAllWindows
        break