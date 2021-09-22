# johnny-five

### remote
https://github.com/rwaldron/johnny-five

## Commit #1 
### Hash
[47a67671f1ef93c2b3887f8dd0fd998c411e539c](https://github.com/rwaldron/johnny-five/commit/47a67671f1ef93c2b3887f8dd0fd998c411e539c)

### Message
Update readme to include note about serial line hang

### Antipattern Category
X

### Keyword
hang

### Note
Not a performance-related commit


## Commit #2
### Hash
[d3541a70d7767e52fb9aa67b32d9f32669abf45f](https://github.com/rwaldron/johnny-five/commit/d3541a70d7767e52fb9aa67b32d9f32669abf45f)

### Message
update median computation

### PR
https://github.com/rwaldron/johnny-five/pull/138

### Antipattern Category
New:unstable_and_slow_noise_handling
### Keyword
faster

### Note
__commit description:__
New median should be more stable than the last. It's also faster in
toto than sorting with the default comparator.
Update checking for threshold event changes. No need to check if median
=== last if we're later going to just check for a threshold.

__Analyzer observations:__
This project works with sensors. The data collected from these sensors can be noisy. Hence, this project contains an median computation approach to select the most accurate data from the noisy inputs.  This commit aims to imrpove this noise handling procedure with a **faster** and **more stable** technique. 


## Commit #3
### Hash
[c97bb0c818dfe18cee69ae11b090d73de416a6ba](https://github.com/rwaldron/johnny-five/commit/c97bb0c818dfe18cee69ae11b090d73de416a6ba)

### Message
Slow down on turns

### Antipattern Category
X

### Keyword
slow

### Note
Not a performance-related commit

## Commit #4
### Hash
[d2d7e8eda9eb1b0ae046f11f58417e89b06130be](https://github.com/rwaldron/johnny-five/commit/d2d7e8eda9eb1b0ae046f11f58417e89b06130be)

### Message
Refactor Led state.isOn fix to avoid getting stuck in an infinite interval

### Antipattern Category
X

### Keyword
stuck

### Note
This is a bug which is fied by this commit. It does not reflect any performance antipattern.


## Commit #5
### Hash
[d235c79da6908b8e00a892da85aaf4c0f9095685](https://github.com/rwaldron/johnny-five/commit/d235c79da6908b8e00a892da85aaf4c0f9095685)

### Message
Refactor animation for easier/faster unit testing

### PR
https://github.com/rwaldron/johnny-five/pull/508

### Antipattern Category
New:build:Slow_Simulation/Hardware_Tests

### Keyword
faster

### Note
This is a very interesting case, where unit testings of Animation classes are slow, and thereby the build process is slow.
The tesst were actually running the animation which is very time-taking in some cases. Also, developers could not mock the time-taking parts. This commit make sure that the tests can be eecuted without  actually running an animation.

## Commit #6 
### Hash
[339d8de98a6b4d8d85aa720c79e85aa05422fd00](https://github.com/rwaldron/johnny-five/pull/529/commits/339d8de98a6b4d8d85aa720c79e85aa05422fd00)

### Message
Make easing tests more tolerant

### Antipattern Category
X

### Keyword
slow

### Note
__Commit Description:__ 
We don’t have a timed test here, but sometimes Travis runs slow enough
that even simple things take a few more ms than expected. This just
relaxes the tolerance on the test to allow for that.

__Analyzer observation:__ 
This commit tackles a travis-related issue.

## Commit #7
### Hash
[99a7d3504cbe40b5622e65c69ee47bcb971d30a5](https://github.com/loadbxh/Arduino-Uno/commit/99a7d3504cbe40b5622e65c69ee47bcb971d30a5)

### Message
Removing board.breakouts and resolving IMU.Drivers at runtime

### Antipattern Category
X

### Keyword
runtime

### Note
This commit does not impact the CPS performance.

## Commit #8
### Hash
[e5b65aaed92ec924d81fc7a653a9257d70795988](https://github.com/rwaldron/johnny-five/commit/e5b65aaed92ec924d81fc7a653a9257d70795988)

### Message
Explicit 'test' task; extended slow tests

### PR
https://github.com/rwaldron/johnny-five/pull/679

### Antipattern Category
New:build:Slow_Simulation/Hardware_Tests

### Keyword
slow

### Note
This commit makes sure that by default slow tests should not get run because Some tests are failing on multiple kinds of slow hardware and also in CI/CD (flaky tests).
For more detailed discussion look at the PR.

## Commit #9
### Hash
[5d763415ec8f7dc45ed04d5931455f7bef24edd0](https://github.com/rwaldron/johnny-five/pull/965/commits/5d763415ec8f7dc45ed04d5931455f7bef24edd0)

### Message
Increase PWM frequency for PCA9685

### PR
https://github.com/rwaldron/johnny-five/pull/965

### Antipattern Category
X

### Keyword
increase

### Note
This is not a performance-related commit.

## Commit #10
### Hash
[79a715443e8a229a2ad7b71a5a352bac31f2246f](https://github.com/rwaldron/johnny-five/commit/79a715443e8a229a2ad7b71a5a352bac31f2246f)

### Message
Servo: limit history to 5 records to prevent potential memory leaks

### Antipattern Category
General:performance:using_massive_arrays_likes

### Keyword
memory

### Note
According to [this paper](https://ieeexplore.ieee.org/document/7884631), which is published in SANER 2017, one of the antipatterns in Java which leads to memory leak is over-using Java Collections because they are occupying lots of memory. This is the same thing for arrays in JavaScript. Before this commit, the project saves the history of the states of each Servo (a phsyical part in CPS). Thsi commit limits the array size to 5 to prevnt memory leakage.

## Commit #11
### Hash
[6f8def6d6a41a30e95c0c6aafdf09c31c8f748b1](https://github.com/loadbxh/Arduino-Uno/commit/6f8def6d6a41a30e95c0c6aafdf09c31c8f748b1)

### Message
Use more then 8 predefined characters

### Antipattern Category
X

### Keyword
memory

### Note
This is not performance-related commit.

## Commit #12
### Hash
[5d9a46252b52363d069d8f8eb402313044553200](https://github.com/loadbxh/Arduino-Uno/commit/5d9a46252b52363d069d8f8eb402313044553200)

### Message
LCD: add test for memory leak fix

### Antipattern Category
X

### Keyword
memory

### Note
This commit adds tests for the previous memory leak fix



## Commit #13
### Hash
[bedcbe3933bec91e793d0d1363f11b8c0a1b5432](https://github.com/loadbxh/Arduino-Uno/commit/bedcbe3933bec91e793d0d1363f11b8c0a1b5432)

### Message
LCD: Wait for fast instructions to complete

### Antipattern Category
New:Impatient_requester

### Keyword
fast

### Note
This commit fixes [Issue #1295](https://github.com/rwaldron/johnny-five/issues/1295).

The execution time for the vast majority of instructions is at least
37 microseconds. See datasheet pages 24 and 25.
https://www.sparkfun.com/datasheets/LCD/HD44780.pdf
It's important to wait 37 microseconds here to prevent fast IO plugins
like Pi-IO from executing the next instruction before the current
instruction has completed. This commit add this waiting time.



## Commit #14
### Hash
[0d5ca14723d12fce82ac417fee2e1cf08b683c94](https://github.com/eric-erki/JavaScript-Robotics-and-IoT-programming-framework/commit/0d5ca14723d12fce82ac417fee2e1cf08b683c94)

### Message
ESC: deprecate speed(percent), introduce throttle(us).

### PR
https://github.com/rwaldron/johnny-five/pull/1484

### Antipattern Category
General:performance:using_massive_arrays_likes

### Keyword
speed

### Note

Other commit: https://github.com/rwaldron/johnny-five/pull/1484/commits/12d242e126d927761faca50c3665d7834c203687

__Commit desc:__
```
- Eliminates "history" memory leak
- Deprecates speed()
- Introduces throttle(us)
```

The performance-related change here is __Eliminates "history" memory leak__.
This is a change similar to Commit #10. Instead of keeping the whole stroy of  ESC (Electronic Speed Control) speed, the new version keep the last speed, whichis the only required information.

