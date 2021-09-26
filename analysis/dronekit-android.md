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


## Commit #11
### Hash
[d022d2b75934df71798424e11b6db13f25ed93ee](https://github.com/dronekit/dronekit-android/commit/d022d2b75934df71798424e11b6db13f25ed93ee)

### Message
Parameters: sip - ListView / Adapter model for much faster and more resource efficient parameter list


### Antipattern Category
X

### Keyword
faster

### Note
This commit makes the UI more efficient. Thid commit does not address any CPS-related performance issue. 


## Commit #12 
### Hash
[f4698eb55964af88f8aa4e31de6646c97349527f](https://github.com/dronekit/dronekit-android/commit/f4698eb55964af88f8aa4e31de6646c97349527f)

### Message
UI update - increase the size of the drawer in flight screen

### Antipattern Category
X

### Keyword
increase

### Note
This commit is a small change to UI.


## Commit #13
### Hash
[26cc1ab9febfb0ffa1f69c5af1d2b644c6c977ec](https://github.com/dronekit/dronekit-android/commit/26cc1ab9febfb0ffa1f69c5af1d2b644c6c977ec)

### Message
Feature: Fast Increment

### Antipattern Category
X

### Keyword
increase

### Note
This commit add a new feature to UI.


## Commit #14
### Hash
[ce5fad7c8d6adef7065fede1f2bc6f2c2532f267](https://github.com/dronekit/dronekit-android/commit/ce5fad7c8d6adef7065fede1f2bc6f2c2532f267)

### Message
Fast ince: Layout test

### Antipattern Category
X

### Keyword
Fast

### Note
This commit does not address any performance issue.

## Commit #15
### Hash
[ffc8e75d7c692c5977516339bb2575c4a1266d5d](https://github.com/dronekit/dronekit-android/commit/ffc8e75d7c692c5977516339bb2575c4a1266d5d)

### Message
Removed UiLanguage as functionality can be achieved by a static method using an application context object. This avoids memory allocation for the creation of the UiLanguage object, and prevent possible leakage of Activity object, as only an application context is needed to make the config update.

### Antipattern Category
General:recreate_objects
### Keyword
memory

### Note
The commit message is representative itself. This commit replaces a class by a static method with the same functionality. This change prevent the creation (and thereby memory allocation) of `UiLanguage`.

## Commit #16
### Hash
[05fdbfeff89736a3f16ad52d04383ebc03d23bfe](https://github.com/dronekit/dronekit-android/commit/05fdbfeff89736a3f16ad52d04383ebc03d23bfe)

### Message
increase features of the map interface.

### Antipattern Category
X

### Keyword
increase

### Note
This commit add new features to a UI.

## Commit #17
### Hash
[f82ad37e86517611fd5bf5185dc6328158983791](https://github.com/dronekit/dronekit-android/commit/f82ad37e86517611fd5bf5185dc6328158983791)

### Message
Huge performance gain by using Buffered streams

### Antipattern Category
General:java:Unbuffered_Streams
### Keyword
performance

### Note
Look at [list of antipatterns for java](https://www.odi.ch/prog/design/newbies.php). As explained here, using unbuffered streams can be expensive. This commit address this antipattern. it replaces the unbuffered streams to the buffered ones


## Commit #18
### Hash
[9c057a7b3fabe4777538b9cd965513f1310a2eff](https://github.com/dronekit/dronekit-android/commit/9c057a7b3fabe4777538b9cd965513f1310a2eff)

### Message
Using ByteBuffers to read the data improves even more the performance.

### Antipattern Category
X

### Keyword
performance

### Note
This commit change the previous commit to a faster buffer (bytebuffer)


## Commit #19
### Hash
[086575e9e07baca5d0439bb49c96a97db6e29efb](https://github.com/dronekit/dronekit-android/commit/086575e9e07baca5d0439bb49c96a97db6e29efb)

### Message
Making the Srtm clas just read a single value to increase the performance, instead of an entire array
### Antipattern Category
General:performance:using_massive_arrays_likes

### Keyword
performance

### Note
This commit is a general antipattern. The commit message is self-explanatory.


## Commit #20
### Hash
[4e87f94f41a4927872c91d7c029d8a72090e8e98](https://github.com/dronekit/dronekit-android/commit/4e87f94f41a4927872c91d7c029d8a72090e8e98)

### Message
decrease size of follow type selection spinner.

### Antipattern Category
X
### Keyword
decrease

### Note
A minor change to UI.


## Commit #21
### Hash
[700aa17674e2b6c91272c39a03b5be543d301f4f](https://github.com/dronekit/dronekit-android/commit/700aa17674e2b6c91272c39a03b5be543d301f4f)

### Message
Fix possible memory leak

### Antipattern Category
?
### Keyword
memory leak

### Note
???

## Commit #22 
### Hash
[5fa1d5313ecbc6a13ce6b6f69eb057bfdf72e60c](https://github.com/dronekit/dronekit-android/commit/5fa1d5313ecbc6a13ce6b6f69eb057bfdf72e60c)

### Message
improved calibration code. runs much faster on android devices.

### Antipattern Category
X
### Keyword
faster

### Note
I could not find any CPS related antipatterns in this commit.


## Commit #23 
### Hash
[cadaf1fb46f9de615df75f17b03b951c9ee0102a](https://github.com/dronekit/dronekit-android/commit/cadaf1fb46f9de615df75f17b03b951c9ee0102a)

### Message
Dronie: Slow down the drone as it reaches the final dronie mission

### Antipattern Category
X

### Keyword
Slow

### Note
It changes the speed of drone in on of the pre-defined Dronie missions.


## Commit #24 
### Hash
[aedc7902acf37b63b052f458b034fce6fe42619f](https://github.com/dronekit/dronekit-android/commit/aedc7902acf37b63b052f458b034fce6fe42619f)

### Message
update the method signature for the 'changeVehicleMode' metho

### Antipattern Category
X

### Keyword
increase

### Note
increase the visibility of changeVehicleMode for VehicleMode class.


## Commit #25 
### Hash
[e29a5fde6f5c871ce956ffe6659e8b34f3d8a5b2](https://github.com/dronekit/dronekit-android/commit/e29a5fde6f5c871ce956ffe6659e8b34f3d8a5b2)

### Message
increase resolution of latitude, longitude and altitude.

### Antipattern Category
New:rounded_numbers

### Keyword
increase
### Note
This comment change float to double for pass a more accurate number for latitude, longitude and altitude.

## Commit #26 
### Hash
[675898195440663b00e8fef17c25f16e61601326](https://github.com/dronekit/dronekit-android/commit/675898195440663b00e8fef17c25f16e61601326)

### Message
Increase the number of threads used to retrieve drone properties.

### Antipattern Category
X

### Keyword
Increase

### Note
This commit increase the number of threads for collecting drone properties. It does not address any antipattern.

## Commit #27
### Hash
[19a5c29337da5d104733dbb1c4be6d8fb8b0c834](https://github.com/dronekit/dronekit-android/commit/19a5c29337da5d104733dbb1c4be6d8fb8b0c834)

### Message
increase altitude precision.

### Antipattern Category
New:rounded_numbers

### Keyword
increase

### Note
Same as Commit #25.


## Commit #28 
### Hash
[8d1c6819f3929093df8bf1b0388e76b047e5b068](https://github.com/dronekit/dronekit-android/commit/8d1c6819f3929093df8bf1b0388e76b047e5b068?w=1)

### Message
improved performance of the mavlink processing and dispatching of events.
### Antipattern Category
New:Impatient_requester

### Keyword
performance

### Note
Timeout issue. The timeout was hardcoded to 3 seconds. This commit change it to 15 seconds (5 times more) to increase the chance of communication success. So, it is both impatient requester and hardcoded timeout.


## Commit #29
### Hash
[304d4f13b711dade2d882a4a32183b1b909d00e5](https://github.com/dronekit/dronekit-android/commit/304d4f13b711dade2d882a4a32183b1b909d00e5)

### Message
increasing travis vm memory allocation.

### Antipattern Category
X

### Keyword
memory

### Note
This is a build related (travis) change.


## Commit #30
### Hash
[03b9f063861914c243c082e9c9c41d55cd9db2d7](https://github.com/dronekit/dronekit-android/commit/03b9f063861914c243c082e9c9c41d55cd9db2d7)

### Message
increasing gradle memory allocation.

### Antipattern Category
X

### Keyword
memory

### Note
This is a build related (gradle) change.


## Commit #31 
### Hash
[ea3ddf18d4a295e2f6afb7dad0e4994724dc8c9e](https://github.com/dronekit/dronekit-android/commit/ea3ddf18d4a295e2f6afb7dad0e4994724dc8c9e)

### Message
increasing travis vm memory allocation.

### Antipattern Category
X

### Keyword
memory

### Note
This is a build related (travis) change.


## Commit #32 
### Hash
[0cc25085be89f67bf2ef7d9ed562f6cbb84bb6bf](https://github.com/dronekit/dronekit-android/commit/0cc25085be89f67bf2ef7d9ed562f6cbb84bb6bf)

### Message
testing with larger memory increase.

### Antipattern Category
X

### Keyword
memory

### Note
This is a build related (travis) change.


## Commit #33 
### Hash
[655b400a1a1732f7d4b79d1606b47eca463f8d62](https://github.com/dronekit/dronekit-android/commit/655b400a1a1732f7d4b79d1606b47eca463f8d62)

### Message
increase logging for easy debugging.

### Antipattern Category
X

### Keyword
increase

### Note
This commit increase the logging. It does not address any performance issue.



## Commit #34 
### Hash
[4c954e7d95af483393aa8f1f1f91b35b29a4018b](https://github.com/dronekit/dronekit-android/commit/4c954e7d95af483393aa8f1f1f91b35b29a4018b)

### Message
increased the size of the memory heap.

### Antipattern Category
X

### Keyword
memory
### Note
This commit increase the size of the heap memory.


## Commit #35 
### Hash
[27b16751ffad6dccda2fb45717e61377fce28f78](https://github.com/dronekit/dronekit-android/commit/27b16751ffad6dccda2fb45717e61377fce28f78)

### Message
mavlink library update to fix spurious memory allocations.

### Antipattern Category
Network:performance:large_payload_sizes

### Keyword
memory

### Note
This commit reduces the maximum size of the payloads which are crated and sent by MAVLINK (a protocol for communicating with small unmanned vehicle). This is a performance issue but it is a networking antipattern, which can be seen in CPSs as well. The MAVLink max size was 512 bytes. However, in the new version of the MAVLink this threshold is [reduced to 256](https://mavlink.io/en/guide/serialization.html#payload_truncation). The large payloads lead to more memory and I/O consumption.



## Commit #36 
### Hash
[abef06d707e79d30fcbc0a8053df377035541162](https://github.com/dronekit/dronekit-android/commit/abef06d707e79d30fcbc0a8053df377035541162)

### Message
Version increase for the hotfix release for release 1.5.0.

### Antipattern Category
X

### Keyword
increase

### Note
Update one of the dependencies.


## Commit #37
### Hash
[8f62427612d394a633ade3bb31bc61a5f7c51a09](https://github.com/dronekit/dronekit-android/commit/8f62427612d394a633ade3bb31bc61a5f7c51a09)

### Message
Update the connection logic for the ControlTower instance. The new logic reuse any existing services runtime, otherwise it fires its local version.
### Antipattern Category
X

### Keyword
runtime

### Note
This commit does not address any CPS performance issue. It make sure that the class create a local service if it does not exist.

## Commit #38
### Hash
[8aa313d34c658040492f91d8bee8d05fe08e17af](https://github.com/dronekit/dronekit-android/commit/8aa313d34c658040492f91d8bee8d05fe08e17af)

### Message
Increase max heap size from 2g to 4g
### Antipattern Category
X

### Keyword
Increase

### Note
Increase heap memory size.

## Commit #39 
### Hash
[ba936869a5aa894892bf51bc6df581f173e22040](https://github.com/dronekit/dronekit-android/commit/ba936869a5aa894892bf51bc6df581f173e22040)

### Message
Fix infinite loop when heightStep is 0

### Antipattern Category
X

### Keyword
infinite

### Note
this is a fix for an infinite loop. This commit fixes it by adding a simple if condition before for loop.