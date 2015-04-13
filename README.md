# gesture_recognition
A homebrew hand motion gesture recognition suite.

I started this project so I could eventually implement it on a beaglebone to
control a [pandora](http://www.pandora.com/) client through
[pianobar](http://6xq.net/projects/pianobar/) using motion gestures. However,
this one will be significantly more complex than the eventual beaglebone
version.

# Demo

[![demo](http://img.youtube.com/vi/ofHGYk0FUa4/0.jpg)](http://www.youtube.com/watch?v=ofHGYk0FUa4)

<iframe width="420" height="315" src="https://www.youtube.com/embed/ofHGYk0FUa4" frameborder="0" allowfullscreen></iframe>


## Overview
I've split the project up as follows

* Acception/Rejection of hand detections and hand tracking
  * Tracks the segmented hand centroid
* Motion detection/segmentation
  * Detects motion to help with hand detection and tracking
* Skin segmentation
  * Segments skin color pixels for hand segmentation
* Gesture classifier
  * Matches recorded hand gestures with best match from a stored database of
    gestures


## To do
* Create custom gesture template dataset
* Choose a method for skin segmentation that is adaptive to illumination changes
* Make the tracking more robust to false detects and outlier movements
* Improve the precision of centroid of hand tracking


## Hand candidate acception/rejection and tracking
After candidate hand movement is detected using motion detection and skin
segmentation the candidate's bounding box is estimated which initializes mean
shift tracking on the skin segmented CrCb candidate hand region. Hand candidates
are rejected or accepted based on:

1. Portion of skin pixels within the hand bounding box is above a predetermined
   threshold
2. Ratio of the area of hand's bounding box to image size lies within a range
   (not too big, not too small)
3. Aspect ratio of hand region bounding box lies within a range (not too 'fat'
   or 'skinny')

These being based on the assumptions:

1. Hand in image is (near) upright
2. Skin pixel thresholding result on hand is dense enough to cover most of the
   hand or is at least roughly uniformly distributed over the hand

Additionally, handling multiple moving objects is not currently
supported. Currently all motion detection is clumped into one region.


## Motion detection
Uses ideas from
[A System for Video Surveillance and Monitoring](https://www.ri.cmu.edu/pub_files/pub2/collins_robert_2000_1/collins_robert_2000_1.pdf)
to detect and segment transient moving objects in scene.


## Skin segmentation
Uses static CrCb thresholding based on statistics collected from datasets of
skin pixels. For robustness I'm considering using a short training phase to
learn skin color statistics from the user camera.


## Gesture classifier
A slight modification of the
[$1 classifier](http://depts.washington.edu/aimgroup/proj/dollar/) by Wobbrock
et al. - a geometric template matcher originally used for recognizing gestures
generated by a stylus or touchpad.

Based on the current sampling rate of the hand tracking, 32 points seems to work
well for representing gestures.


## Dependencies
* python 2.7
* matplotlib
* opencv
* h5py
