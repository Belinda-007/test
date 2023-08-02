import cv2
import numpy as np

def draw_circle(frame, center, radius, color, thickness):
    cv2.circle(frame, center, radius, color, thickness)

def main():
    cap = cv2.VideoCapture(0)

    circle_center = (100, 100)  # Initial center of the circle
    circle_radius = 30         # Radius of the circle
    circle_color = (0, 255, 0)  # Green color (BGR format)
    circle_thickness = 2       # Thickness of the circle outline

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Update the circle center with each frame
        circle_center = (circle_center[0] + 1, circle_center[1] + 1)

        # Draw the circle on the frame
        draw_circle(frame, circle_center, circle_radius, circle_color, circle_thickness)

        cv2.imshow('Real-Time Video Drawing', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()