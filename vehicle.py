
import cv2
import numpy as np
import pywhatkit
cap = cv2.VideoCapture("video.mp4")


count_line_position = 550

# Define the code and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))


# Create background subtractor object
fgbg = cv2.createBackgroundSubtractorMOG2()

# Define kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# Initialize variables
area_threshold = 500
car_count = 0
previous_frame = None


offset = 6


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Apply morphological operations
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    # Find contours
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    cv2.line(frame,(2,count_line_position),(1200,count_line_position),(255,127,0),3)
    

    # Draw bounding boxes around the vehicles
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > area_threshold:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #cv2.putText(frame, "Vehicle:"+str(car_count), (x,y-20), cv2.FONT_HERSHEY_TRIPLEX, 1, (225, 244, 100), 2)


            # Calculate centroid of the vehicle
            centroid = (int(x + w/2), int(y + h/2))

            # Draw the centroid on the frame
            cv2.circle(frame, centroid, 3, (0, 0, 255), -1)

            # Count the vehicle if it crosses the center of the frame
            if centroid[1] < (count_line_position+offset) and centroid[1] > (count_line_position-offset) :
                car_count += 1
                6
                if car_count == 35:
                    pywhatkit.sendwhatmsg_instantly("+918851100534", "Vehicle 35 has crossed the count line!")

            previous_frame = centroid

    cv2.putText(frame, f"Car count: {car_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 250), 3)

    out.write(frame)

    cv2.imshow('frame', frame)

    
        
    if cv2.waitKey(1) == 13:
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()