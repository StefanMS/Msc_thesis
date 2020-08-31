import numpy as np
import cv2
import cv2.aruco as aruco
 
 
cap = cv2.VideoCapture(0)
 
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #print(frame.shape) #480x640
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters =  aruco.DetectorParameters_create()
 
    #print(parameters)
 
    '''    detectMarkers(...)
        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
        mgPoints]]]]) -> corners, ids, rejectedImgPoints
        '''
        #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    print(corners)
    #x = (corners[i-1][0][0][0] + corners[i-1][0][1][0] + corners[i-1][0][2][0] + corners[i-1][0][3][0]) / 4
    #y = (corners[i-1][0][0][1] + corners[i-1][0][1][1] + corners[i-1][0][2][1] + corners[i-1][0][3][1]) / 4
    #print(x,y)

    #rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, markerLength, camera_matrix, dist_coeffs) # For a single marker
    #rotM = np.zeros(shape=(3,3))
    #cv2.Rodrigues(rvec[i-1], rotM, jacobian = 0)
    #ypr = cv2.RQDecomp3x3(rotM)
    #print(ypr)
    

    #It's working.
    # my problem was that the cellphone put black all around it. The alrogithm
    # depends very much upon finding rectangular black blobs
 
    #gray = aruco.drawDetectedMarkers(gray, corners)
    finalImage = aruco.drawDetectedMarkers(frame, corners)
    if corners != [] :
        cv2.putText(finalImage,'Marker detected', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 1)


    #print(rejectedImgPoints)
    # Display the resulting frame
    cv2.imshow('frame',finalImage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
