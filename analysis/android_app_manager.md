# Android app manager

remote: https://github.com/ros-android/android_app_manager

## Commit #1 
[980febbe5e1af05a21c9f08a8133e8b2804f2265](https://github.com/ros-android/android_app_manager/commit/980febbe5e1af05a21c9f08a8133e8b2804f2265)

__message:__ Increase wifi timeout.

__Antipattern Category:__ Smith:Where_Was_I

__keyword:__ increase

This commit increases the timeout for waiting for a wifi from 30 seconds to 90 seconds.
 
 According to Smith's study, Smith:Where_Was_I antipattern happens when the following scenario occurs:
 
 "an IOT application first tries   to   connect to the all of its last known devices, but there has been a change to the environment and all devices are not available to re-connect. Its timeout interval is much too long (**over 1 minute**) so the  user  experiences  a  frustrating  delay  before  she/he  is  able  to  interact with the app and reach the desired state." 


## Commit #2 
[feaf968ca40f8869989d7fa899a3dca678fb741c](https://github.com/ros-android/android_app_manager/commit/feaf968ca40f8869989d7fa899a3dca678fb741c)

__message:__ Fix a variety of potential hang-ups with the starting application dialog

__Antipattern Category:__ X

__keyword:__ hang

This commit is not performance-related. Also, I could not find any sign of antipatterns here.

