# Hand Gesture Mouse Control

This program allows you to control the mouse cursor and perform left-clicks using hand gestures captured from a webcam. It utilizes the OpenCV library to capture video frames, the Mediapipe library for hand tracking, and the mouse library for controlling mouse movements and clicks.

## Dependencies

The following dependencies are required to run the program:

- OpenCV
- Mediapipe
- mouse

You can install these dependencies using pip:

```shell
pip install opencv-python mediapipe mouse
```

## Usage

1. Run the program by executing the script.
2. A window will open displaying the webcam feed with hand tracking overlays.
3. Extend your hand towards the camera and make sure your palm and fingers are visible.
4. Adjust the distance from the camera to ensure accurate hand tracking.
5. Control the mouse cursor by moving your index finger.
6. Move the index finger within a specific range to control the mouse cursor position on the screen.
7. Bring the middle finger close to the index finger to perform a left-click.
8. When the middle finger and index finger are close together, a rectangle will appear on the screen indicating a left-click action.

## License

This program is licensed under the [MIT License](LICENSE).

## Acknowledgements

The hand tracking functionality in this program is based on the HandTrackingModule, which is a custom module using the Mediapipe library for hand tracking.
