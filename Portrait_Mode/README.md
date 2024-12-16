# Portrait Mode App

## Description
An Android App that segments the foreground from the background. The app has 2 modes:
- Green screen: Background objects are replaced by a green screen of the users choice.
- Portrait mode: Background objects are blurred.

Algorithm developed in Python and then ported to Java.

This project was in collaboration with Jason Vasko for ECE 420: Embedded Signal Processing, at University of Illinois.

## Features

- **Real-Time Image Processing:**
  - Processes live camera feeds with real-time foreground and background segmentation.
  - Applies effects like green screen replacement or blurred background.

- **Signal Processing Techniques:**
  - Clustering-based pixel classification for intensity grouping.
  - Morphological operations (erosion and dilation) for segmentation refinement.
  - 2D convolution filters (e.g., box blur) for background processing.

- **Optimized Hardware Utilization:**
  - Efficiently uses Android's Camera API for capturing and processing live video feeds.
  - Custom configurations for camera parameters, including auto-exposure adjustments and orientation handling.

## Technologies Used

- **Programming Language:** Java
- **Platform:** Android
- **Libraries/Frameworks:** Android SDK
- **Domains:**
  - Real-Time Image Processing
  - Computer Vision
  - Embedded Systems

## How It Works

1. **Camera Feed Initialization:**
   - Uses Android's `Camera` API to capture video frames.
   - Processes frames in real-time using custom algorithms for image enhancement and segmentation.

2. **Foreground-Background Segmentation:**
   - Detects and separates foreground from the background using clustering techniques.
   - Applies either a green screen effect or background blurring.

3. **Image Rendering:**
   - Processes each frame using a pipeline of convolution, clustering, and morphological operations.
   - Displays the final processed image using `Canvas` and `Bitmap` on Android's `SurfaceView`.

## Examples
[Beach Background Video](www.youtube.com/shorts/4OCvr5BBibo)

[Forest Background Video](https://www.youtube.com/shorts/xNL-d1uN93I)

[Portrait Mode Video](https://www.youtube.com/shorts/smbveQzrgtQ)

## Applications

- Green screen or chroma-key video effects.
- Real-time video processing for augmented reality applications.
- Mobile-based computer vision demonstrations.


