# dronekit-android

### remote
https://github.com/dronekit/dronekit-android

## Commit #1 
### Hash
[b1d67d71e7b1d637b314d00d8602cdc8cd674fd9](https://github.com/dronekit/dronekit-android/commit/b1d67d71e7b1d637b314d00d8602cdc8cd674fd9)

### Message
Shrink joystick handle a little to increase move resolution

### Antipattern Category
X

### Keyword
increase

### Note
This commit is a small change to UI.


## Commit #2
### Hash
[faf8f09a5a9eeaeca02ce59f9ecb842e7c2f0794](https://github.com/dronekit/dronekit-android/commit/faf8f09a5a9eeaeca02ce59f9ecb842e7c2f0794)

### Message
Removing the need to clear the map in PlanningActivity.

### Antipattern Category
Smith:General:Unnecessary_Processing 

### Keyword
performance

### Note
This commit improves the performance since the method mapClear() is very heavy. It removes the unnecessary process of map reset in the PlanningActivity class.


## Commit #3
### Hash
[e41fec48360cc4720eb08f827c9a25740dc603b5](https://github.com/dronekit/dronekit-android/commit/e41fec48360cc4720eb08f827c9a25740dc603b5)

### Message
Changing the way to start a path, now you do it with a fast click.

### Antipattern Category
X

### Keyword
fast

### Note
This commit is a small change to UI to improve the user experience.



## Commit #4
### Hash
[f1ef0aea6f46b65661a4d824560cd567c6be5d2d](https://github.com/dronekit/dronekit-android/commit/f1ef0aea6f46b65661a4d824560cd567c6be5d2d)

### Message
Fix the problem where you always added two waypoints when doing a fast click.


### Antipattern Category
X

### Keyword
fast

### Note
This commit is a small change to UI to improve the user experience. In general "fast click" is a user gesture. 


## Commit #5
### Hash
[1f605c0e51de179f564b8478f68027f10be102ea](https://github.com/dronekit/dronekit-android/commit/1f605c0e51de179f564b8478f68027f10be102ea)

### Message
Changing layout to increase the map size

### Antipattern Category
X

### Keyword
increase

### Note
This commit is a small change to UI.


## Commit #6
### Hash
[eea6fbc8c065daef7394158504f7608f7f2440aa](https://github.com/dronekit/dronekit-android/commit/eea6fbc8c065daef7394158504f7608f7f2440aa)

### Message
Increase mission row height, so they are easier to handle

### Antipattern Category
X

### Keyword
Increase

### Note
This commit is a small change to UI.


## Commit #7
### Hash
[ecf355c7f58be415934fdf05da87762c66991857](https://github.com/dronekit/dronekit-android/commit/ecf355c7f58be415934fdf05da87762c66991857)

### Message
Zoom: Increase padding around bounded coords to prevent markers being positioned off-screen

### Antipattern Category
X

### Keyword
Increase

### Note
Fix a bug in UI.


## Commit #8
### Hash
[6bb4e0460ece576a7ac8a652a3e5bab33de91557](https://github.com/dronekit/dronekit-android/commit/6bb4e0460ece576a7ac8a652a3e5bab33de91557)

### Message
better text layout in the telemetry. Getting the hang of it.

### Antipattern Category
X

### Keyword
hang

### Note
This commit improve the UI to be more user friendly.


## Commit #9
### Hash
[8f8084d3ca4f7bc6a9d584a483a60e14c8163bbb](https://github.com/dronekit/dronekit-android/commit/8f8084d3ca4f7bc6a9d584a483a60e14c8163bbb)

### Message
better text layout in the telemetry. Getting the hang of it.

### Antipattern Category
X

### Keyword
hang

### Note
This commit improve the UI to be more user friendly.


## Commit #10
### Hash
[2c9d9bc08147b0952eba4b6ef28701641a99bb21](https://github.com/dronekit/dronekit-android/commit/2c9d9bc08147b0952eba4b6ef28701641a99bb21)

### Message
TUNING: Adding code to setup the streaming rate when in the Tuning screen

### Antipattern Category
New:Fixed_Communication_Rate
### Keyword
increases

### Note
__Commit desc:__ This increases the rate when entering the screen, and reset's to default values after that. This gives a much faster update of the chart.


This commit makes the streaming rate dynamic according to the user activity. Before this commit, the stream rate was hard-coded and fixed. To improve the performance of the system, this commit make sure that the stream rate increases between the controller and drone when a specifig app fragment (TUNING fragment) is opened by the user.

-----
## Commit #1 
### Hash
[]()

### Message

### Antipattern Category

### Keyword

### Note