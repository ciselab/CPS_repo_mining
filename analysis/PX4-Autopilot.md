# PX4-Autopilot

### Remote
https://github.com/PX4/PX4-Autopilot

## Commit #1
### Hash
[a704acc2a20936d7e6d6828ae0ddf2cf7dc3578b](https://github.com/PX4/PX4-Autopilot/commit/a704acc2a20936d7e6d6828ae0ddf2cf7dc3578b?w=1)
### Message
Out of memory warning, flash and RAM optimizations
### Antipattern Category
?
### Keyword
memory
### Note
sleep before starting the i2c handler

## Commit #2
### Hash
[7e0f8b3edaf584a48cd3bc3351e3205fd0106cdc](https://github.com/PX4/PX4-Autopilot/commit/7e0f8b3edaf584a48cd3bc3351e3205fd0106cdc?w=1)
### Message
Formatting changes to make the Python style checker happy (copied from the bootloader project).\
Increase the erase timeout to avoid issues with large/slow flash.
### Antipattern Category
X
### Keyword
slow
### Note
-


## Commit #3
### Hash
[a4b0e3ecbe2d012eac7545cce14829866bacc813](https://github.com/PX4/PX4-Autopilot/commit/a4b0e3ecbe2d012eac7545cce14829866bacc813?w=1)
### Message
Add retry-on-error for non-protocol errors.\
Add more performance counters; run test #1 faster.
### Antipattern Category
?
### Keyword
performance
### Note
decreased sleep from 10000 -> 1000, increased number for count

## Commit #4
### Hash
[6948defdb26711fd8336b5e0173664bf98517406](https://github.com/PX4/PX4-Autopilot/commit/6948defdb26711fd8336b5e0173664bf98517406?w=1)
### Message
mavlink: HIL fixes, performance optimization
### Antipattern Category
?
### Keyword
performance
### Note
added:
```C++
_main_loop_delay(1000)
```
still here:
```C++
#define MAIN_LOOP_DELAY 10000	// 100 Hz @ 1000 bytes/s data rate
```

## Commit #5
### Hash
[e505f4fae5596b2b53c120a7cb2a03d2d974c83a](https://github.com/PX4/PX4-Autopilot/commit/e505f4fae5596b2b53c120a7cb2a03d2d974c83a?w=1)
### Message
sdlog2: use orb_check() instead of poll() to minimize polling overhead, bugs and compiler warnings fixed
### Antipattern Category
?
### Keyword
overhead
### Note
added:
```C
useconds_t sleep_delay = 10000;		// default log rate: 100 Hz
```

## Commit #6
### Hash
[1e54dc4409df700b8b4c4a4480238db27b270dfc](https://github.com/PX4/PX4-Autopilot/commit/1e54dc4409df700b8b4c4a4480238db27b270dfc?w=1)
### Message
commander: Accel calibration: Reduce memory footprint, be more responsive
### Antipattern Category

### Keyword
memory
### Note
```C++
/* allow user enough time to read the message */
sleep(3);
sleep(1);
```

```C++
/* inform user about already handled side */
if (data_collected[orient]) {
	mavlink_and_console_log_info(mavlink_fd, "%s side done, rotate to a different side", orientation_strs[orient]);
	sleep(3);
	sleep(1);
```

How long is long enough for a user?

## Commit #7
### Hash
[cced8ed69e046cacd5949757d5f33b5e885f8d10](https://github.com/PX4/PX4-Autopilot/commit/cced8ed69e046cacd5949757d5f33b5e885f8d10?w=1)
### Message
POSIX: added hrt_queue for handling fast periodic events

The workqueues measure time in ticks  which is typically 10ms.\
Some interrupt events in Nuttx occur at about 1ms so a more\
granular workqueue is needed for POSIX.\
...
### Antipattern Category
?
### Keyword
fast
### Note
```C
/* might sleep less if a signal received and new item was queued */
usleep(next);
```
```C
/* Default to sleeping for 1 sec */
next  = 1000000; 
```

## Commit #8
### Hash
[16cb971d6306884e3d238d24e32bf2ca5afcafee](https://github.com/PX4/PX4-Autopilot/commit/16cb971d6306884e3d238d24e32bf2ca5afcafee?w=1)
### Message
POSIX: Increase app start spacing
### Antipattern Category

### Keyword
increase
### Note
only change:
```C++
usleep(20000);
usleep(40000);
```

## Commit #9
### Hash
[b70c9a84c621af6d0a48c0f1ba99e9385426e4ff](https://github.com/PX4/PX4-Autopilot/commit/b70c9a84c621af6d0a48c0f1ba99e9385426e4ff?w=1)
### Message
systemlib: Add ability to dump memory usage
### Antipattern Category
X
### Keyword
memory
### Note
Print usage, not performance intersting.

## Commit #10
### Hash
[fa590bbe8038941423ddb8ecb36d94dc7298b167](https://github.com/PX4/PX4-Autopilot/commit/fa590bbe8038941423ddb8ecb36d94dc7298b167?w=1)
### Message
Correct float parsing args and increase altitude monitoring frequency
### Antipattern Category
?
### Keyword
increase
### Note
increasesd monitoring frequency, not explained why this is needed....
```python
time.sleep(1)
time.sleep(.2)
```

## Commit #11
### Hash
[94aaf0d298467596e7c6e067e3252dc0f937b429](https://github.com/PX4/PX4-Autopilot/commit/94aaf0d298467596e7c6e067e3252dc0f937b429?w=1)
### Message
increase sleep time in accel calibration routine to make accel calibration work on snapdragon
### Antipattern Category
?
### Keyword
increase
### Note
```C++
mavlink_and_console_log_info(mavlink_log_pub, CAL_QGC_ORIENTATION_DETECTED_MSG, detect_orientation_str(orient));
		// TODO FIXME: sleep here, so that QGC receives this with higher chance.
		usleep(1000);
		usleep(10000);
```
Interesting that this was needed.. doesn't feel like the correct solution.

## Commit #12
### Hash
[acc40c82173d8bae9569f7833cd0f00173ccbc63](https://github.com/PX4/PX4-Autopilot/commit/acc40c82173d8bae9569f7833cd0f00173ccbc63?w=1)
### Message
orb unittest: increase waiting time so that test does not fail on slow devices

This test failed on the pixracer because the subscriber thread was too slow\
and thus orb messages got lost. This behavior is expected, but the test\
should not fail because of that, so we increase the sleeping time.
### Antipattern Category
?
### Keyword
slow
### Note
Interesting

## Commit #13
### Hash
[d846ad5dacfa4ab89fd611116d0ea8d21b9bc181](https://github.com/PX4/PX4-Autopilot/commit/d846ad5dacfa4ab89fd611116d0ea8d21b9bc181?w=1)
### Message
sensors: move voting into sensors module

- voting is now at a central place instead of duplicated within the
  estimators
  -> this also means that estimators that did not do voting so far,
     now have voting, like ekf2
- estimators requiring more than that can still subscribe to the raw
  sensors
- allows sensors_combined to be 3 times smaller
  - reduces logger, memcpy (cache) & RAM overhead
- all modules requiring only 1 or 2 sensor values now automatically get
  the voted result
- this also adds voting to baro
### Antipattern Category
?
### Keyword
overhead
### Note
File: src/modules/ekf_att_pos_estimator/ekf_att_pos_estimator_main.cpp
Line: 610
```C++
/* system is in HIL now, wait for measurements to come in one last round */
usleep(60000);
```
removed lines (next 4):
```C++
/* HIL is slow, set permissive timeouts */
_voter_gyro.set_timeout(500000);
_voter_accel.set_timeout(500000);
_voter_mag.set_timeout(500000);

/* now read all sensor publications to ensure all real sensor data is purged */
orb_copy(ORB_ID(sensor_combined), _sensor_combined_sub, &_sensor_combined);
```
## Commit #14
### Hash
[45ffb190e32b8ae8970940c24554e99f0eb2e275](https://github.com/PX4/PX4-Autopilot/commit/45ffb190e32b8ae8970940c24554e99f0eb2e275?w=1)
### Message
logger: add -p <topic> option to poll on a topic instead of running at fixed rate

this will be needed for fast replay. In addition, this option disables\
the orb interval.\
It can be removed again once we have time simulation.
### Antipattern Category
?
### Keyword
fast
### Note
Not interesting (code wise for this analysis), though the need for a -p option to shorten the interval, in the logger, is.
  
## Commit #15
### Hash
[aa9fbbedd54a7a0e346ea03f439dcdf4f90c6113](https://github.com/PX4/PX4-Autopilot/commit/aa9fbbedd54a7a0e346ea03f439dcdf4f90c6113?w=1)
### Message
add oneshot mode capability\
change fmu to task\
increase fmu_servo task priority to max and enable true oneshot\
use lowest FMU priority which minimizes jitter\
constrain oneshot updates to control group 0 events
### Antipattern Category
?
### Keyword
increase
### Note
Interesting need for:
```C++
/* wait until the task is up and running or has failed */
while (_task > 0 && _task_should_exit) {
	usleep(100);
}
```
