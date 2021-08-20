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

## Commit #16
### Hash
[1c0dd8ba497d109fb9cd3a82f4526b9e466d6c2b](https://github.com/PX4/PX4-Autopilot/commit/1c0dd8ba497d109fb9cd3a82f4526b9e466d6c2b?w=1)
### Message
Simulator: Add scaling API to adjust for slow simulators

The simulation engine had the ability to pause already and properly handled load spikes, however, it was not hardened against constant drift. This addition enables it to run at a constant slower-than-realtime rate successfully.
### Antipattern Category
X
### Keyword
slow
### Note
Needed for use with the simulator.

## Commit #17
### Hash
[1e0489f48b4a4dd1c953ec4f514d01114eb4d7da](https://github.com/PX4/PX4-Autopilot/commit/1e0489f48b4a4dd1c953ec4f514d01114eb4d7da?w=1)
### Message
PX4 System gpio_led:Code cleanup

Use PX4 log and module documantation\
Fixed memory leaks
### Antipattern Category
?
### Keyword
memory
### Note
```C++
gpio_led_state = Falied;
```

## Commit #18
### Hash
[4e5b223a0889871f4c321bc853522371d9c7827a](https://github.com/PX4/PX4-Autopilot/commit/4e5b223a0889871f4c321bc853522371d9c7827a?w=1)
### Message
hrt test decrease time
### Antipattern Category
X
### Keyword
decrease
### Note
Branch number changed.

## Commit #19
### Hash
[d375880c4bee5b4f7c287bfd2921f3a1e9d648a7](https://github.com/PX4/PX4-Autopilot/commit/d375880c4bee5b4f7c287bfd2921f3a1e9d648a7?w=1)
### Message
improve mavros SITL tests (#8652)
-created a test base class to centralize redundant methods among the different tests
-added mission waypoint list topic listener (this also helps make sure the simulation is ready)
-check number of mission waypoints in FCU against mission
-increase time for mavros topics to be ready from 30 to 60 seconds
-reduce position check loop rates
-clean up logging
-support QGC plan for mission file format, see #8619
-vehicle is an arg for mission test launch file, working toward other airframes
-Jenkins: fix vtol vehicle arg value
-get MAV_TYPE param and use FW radius for pure fixed-wing mission position check
-remove unused vehicle arg from test in multiple tests launch, clearing runtime warning
### Antipattern Category
?
### Keyword
runtime
### Note
Changed queue size from 10 to 1, for AttitudeTarget and PoseStamped.
```Python
'mavros/setpoint_raw/attitude', AttitudeTarget, queue_size=10) # removed line
'mavros/setpoint_raw/attitude', AttitudeTarget, queue_size=1) # added line
```
```Python
# ROS services
service_timeout = 30
```

## Commit #20
### Hash
[cbf3cee0961fbe8c17fb0aa9468f25564f286c08](https://github.com/PX4/PX4-Autopilot/commit/cbf3cee0961fbe8c17fb0aa9468f25564f286c08?w=1)
### Message
ll40ls: increase the number of samples used to find a correlation peak for LitarLite\
...
### Antipattern Category
?
### Keyword
increase
### Note
After:
```C++
// wait for sensor reset to complete
usleep(1000);
```
Added (after writing to reg.):
```C++
// wait for register write to complete
usleep(1000);
```

## Commit #21
### Hash
[56150c28ddbf941ec28254cd679a46da9ff8e16e](https://github.com/PX4/PX4-Autopilot/commit/56150c28ddbf941ec28254cd679a46da9ff8e16e?w=1)
### Message
ll40ls: increase the sleep time after resetting registers\
...
### Antipattern Category
?
### Keyword
increase
### Note
Similar to Commit [#20](https://github.com/ciselab/CPS_repo_mining/blob/imara_analysis/analysis/PX4-Autopilot.md#commit-20).\
Increased sleep duration, from 1000 to 50000:
```C++
// wait for sensor reset to complete
usleep(1000);
usleep(50000);
```

## Commit #22
### Hash
[8b629454de069c835ad086b78e498f955c5193fd](https://github.com/PX4/PX4-Autopilot/commit/8b629454de069c835ad086b78e498f955c5193fd?w=1)
### Message
esc_calibration: increase safety and initialise all data
- do not do calibration if not very sure that battery is not connected
- initialise all structs and variables\
...
### Antipattern Category
?
### Keyword
increase
### Note
Replaced:
```C++
hrt_abstime battery_connect_wait_timeout = 30000000;
hrt_abstime pwm_high_timeout = 3000000;
hrt_abstime timeout_start;
```
By:	
```C++
hrt_abstime battery_connect_wait_timeout = 30*1000*1000;
hrt_abstime pwm_high_timeout = 3*1000*1000;
hrt_abstime timeout_start = 0;
```
Same with sleep:
```C++
usleep(50000);
usleep(50*1000);
```

## Commit #23
### Hash
[0c5c741b1a63ff90b9137d6327ccdd10fab6c084](https://github.com/PX4/PX4-Autopilot/commit/0c5c741b1a63ff90b9137d6327ccdd10fab6c084?w=1)
### Message
add posix shell\
squashed & rebased version, not including:
- listener changes
- src/firmware renaming

Commits:\
tag_to_version.py: fix Python3 error\
subprocess.communicate returns bytes instead of a str which is not the
same for Python3. Therefore, we need to decode the bytes.\
cmake: remove folder src/firmware\
The folder src/firmware was not intuitive. Why would the binaries for
SITL be inside a src and why even inside a src/firmware folder. Also,
the rootfs was put there which made it even more confusing.\
The CMakeLists.txt files are moved into cmake/ and get now called from
the main CMakeLists.txt.

qshell: support for return value

Instead of just sending commands, qshell will now also wait until
the command has finished on QURT and sent back a return value. This will
allow all modules on the DSP side to be spawned from the Linux side
meaning that we only need one config/startup file instead of two.

adb_upload: create folders before pushing

Previously the script failed if the folder on the destination was not
already existing. This therefore makes pushing easier.

posix: spawn PX4 modules in bash

This adds the possibility to spawn PX4 modules out of bash. Basically,
the main executable can now be started as a server/daemon or as a
client.
The server replaces the existing functionality of the main exe with
the pxh shell, however, it also opens a pipe that clients can talk to.

Clients can run or spawn PX4 modules or commands by connecting to the
server over the pipe. They clients will get the stdout and return value
of their commands via a client specific pipe back.

This work will allow to start all modules using a bash script similar to
the way it is done in NuttX where the NuttShell scripts the startup
scripts and starts the modules.

SITL: use new client shell in SITL

This is a first step to use the new shell capabilities for SITL.
The new startup bash script rcS merges (and therefore replaces) the two
existing scripts rcS_gazebo_iris and rcS_jmavsim_iris.

More cleanup will be necessary for the rest of the SITL startup scripts.

Snapdragon: use new shell to start all modules

Instead of different mainapp.config and px4.config files, we can now use
a unified rcS bash script which starts all the modules based on
parameters, mainly the SYS_AUTOSTART param.

Snapdragon: fix the airframe description

pxh: argv needs to end with a nullptr

The comment was wrong that argv needs an additional 0 termination.
Instead it needs a nullptr at the end.

px4_posix_tasks: variable cleanup

The px4_task_spawn_cmd function got a cleanup while debugging, however,
no functional changes.

Snapdragon: move some drivers to 4100 config

These drivers are supported by the community, so they go into the 4100
config.

Snapdragon: update 210qc platform

px4_daemon: use doxygen comments

apps.h_in: fix string printf: use .c_str()

px4_daemon: \b -> \n in printf

px4_daemon: handle error in generate_uuid (close the file on error)

posix main: some clarifications in comment (it's the symlinks not the script aliases)

cmake: remove new install command again

This one was probably wrong and untested. Installing needs revisiting.

POSIX: remove argument USES_TERMINAL

POSIX: copy init and mixer files for SITL

Instead of using non-working install commands, the mixer and startup
files are now copied as part of the build in cmake.

adb_upload.sh: remove leftover commented printf

POSIX main: just the pointer instead of memmove

POSIX main: remove chroot

chroot is removed because it hasn't been used anywhere and seems
untested.

px4_daemon: remove client pipe when cleaning up

px4_daemon: fail if the client pipe already exists

The client pipe is supposed to be specific (by UUID), so the path
shouldn't exist already.

history: limit the number of history entries

This is a protection to avoid filling the memory if we are entering a
lot of commands (e.g. auto-generated).

px4_daemon: add a threadsafe map and use it

px4_daemon: whitespace

px4_daemon: fix client parsing

Sometimes the client ends up reading more than one packet in one read.
The parsing is not made for this and would require a (ring)buffer for
it.

The solution of this commit just reads as much as needed from the pipe
which avoids having to do buffering and parsing.

posix: changes sitl_run.sh and main.cpp cleanup

This changes the paths in sitl_run.sh quite a bit to allow the px4
binary to run in the rootfs directory which should make it convenient
and very close to the NuttX variant.

Also main.cpp got a big cleanup after the big rebase with some
conflicts. Quite some functionality was removed but it has yet to be
seen if it needs to be re-added.

px4_log: cleanup log levels, now they make sense

Before DEBUG and INFO log levels where inverted which didn't make much
sense in my eyes.

dataman: fix path for bash shell

logger: fix paths for bash shell

mavlink: fix paths for bash shell

param: fix path for bash shell

inav: fix paths for bash shell

sdlog2: fix paths for bash shell

ROMFS: add forgotten mixer to list

SITL init: more models, more options

- Support for different models using the unified startup
script rcS.
- Support to choose the estimator by setting the environment variable
  PX4_ESTIMATOR.
- Support to choose the logger by setting the environment variable
  PX4_LOGGER.

rcS: fix string comparison

listener: use template file

Instead of having all of the C++ code inside the Python file it is
nicer to have a separate template file with the C++ headers, etc.

px4_log: add PX4_INFO_RAW for raw printfs

This allows to do custom formatting but is still transported over
sockets to clients.

topic_listener: use PX4_INFO_RAW instead of printf

commander: use PX4_INFO_RAW for status

listener: rewrite to classes and factory

posix: fix some argument warnings

generate_listener.py: by accident changed shebang

listener: big refactor of the generator

Hopefully this makes it easier to read and change in the future.

rcS: manually take over rebase changes

listener: remove leftover try

listener: properly clean up topic instance

rcS: take over some vehicle specific changes

posix-configs: vehicle specifics to separate files

posix-configs: remove leftover lines

uORBDevices: new PX4_INFO_RAW instead of printf

px4_log: just use printf on NuttX

listener: use less binary space, strip on NuttX

generate_listener.py: remove commented code

cmake: fix syntax error from merge

px4_daemon: fixes after rebase of apps.h/cpp fix

px4_daemon: namespace missing

posix: only create stub for fsync on QURT

unitests: reduce dependencies of param test

This makes the unit test compile and link again after the bash changes.

QURT: some compile fixes after a rebase

SITL: arg change for sitl_run.sh to use rcS_test

This allows to use a custom startup file for testing.

SITL: add the folder test_data

SITL: implement shutdown command as systemcmd

The shutdown command needs to be a proper systemcmd, otherwise the alias
and symlink generation doesn't work and we end up calling shutdown of
the host computer which is to be avoided.

px4fmu_test: same IO_pass mixer as px4fmu_default

px4fmu_test: use normal quad x mixer

There is no good reason to use a specific test mixer, except more cmake
code around it. Therefore just use the same mixer as default, and at
some point px4fmu_test and px4fmu_default can get merged

POSIX: cleanup, dir and symlink fixes

This cleans up the logic behind the symlinking and creating directories.

POSIX: correct arg order in usage info

tests: fix paths for SITL tests

POSIX: printf fix

sitl_run.sh: try to make this run on Mac as well

cmake: try to make jenkins happier

Path cleanup, the bin is no longer in src/firmware

POSIX: fix symlink logic

SITL: prefix all exported env variables

cmake: fix path for ROS tests

integrationtests: fix log path

launch: try to make tets with ROS working again

px4_defines: fix after wrong merge deconflicting

px4_defines: get paths for POSIX correct

cmake: fix cmake arguments

This was fine with cmake 3.6 but did not work with cmake 3.2.2

cmake: use cp instead of cmake -E copy

cmake -E copy does not support copying multiple files with versions <
3.5. Therefore, just use cp for now.

ROMFS: fix build error after rebase

cmake: fix paths in configs

launch: use `spawn_model` again

cmake: various fixes after big rebase

param: path fixes after rebase

posix platform: fixes after rebase

test_mixer: fix screwed up rebase
### Antipattern Category
?
### Keyword
memory
### Note
Very long commit message. Lots of small changes, many files have been adjusted, also some very large changes.\
Number of files adjusted: 62.
```C++
} else if (pret == 0) {
	// Timing out is fine.
} else {
	// Something is wrong.
	usleep(10000);
}
```
Have been removed, but check returns on lines 135 and 137.
```C++
135	-	return 0;
136		appState.setRunning(false);
137	-	return rc;
141	+	return 0;
```

## Commit #24
### Hash
[828e31d3a914166c8bb3897c6191f4203f151b7a](https://github.com/PX4/PX4-Autopilot/commit/828e31d3a914166c8bb3897c6191f4203f151b7a?w=1)
### Message
lockstep_scheduler: optimize performance
- use a linked-list instead of std::vector. Insertion and removal are now
  O(1)
- avoid malloc and use a thread_local instance of TimedWait.
  It gets destroyed when the thread exits, so we have to add protection
  in case a thread exits too quickly. This in turn requires a fix to the
  unit-tests.
### Antipattern Category
?
### Keyword
performance
### Note
```C++
#ifndef UNIT_TESTS // unit tests don't define system_usleep and execute faster w/o sleeping here
	system_sleep(5000);
#endif
```

## Commit #25
### Hash
[721f9f901f7e2725318b30fc64d5448070fa09af](https://github.com/PX4/PX4-Autopilot/commit/721f9f901f7e2725318b30fc64d5448070fa09af?w=1)
### Message
log_writer_file: fix race condition for fast consecutive stop & start calls
### Antipattern Category
X
### Keyword
fast
### Note
```C++
// At this point we don't expect the file to be open, but it can happen for very fast consecutive stop & start
// calls. In that case we wait for the thread to close the file first.
``` 

## Commit #26
### Hash
[1d932f6ec9d4a59ba4c68a59fc134bcd925328af](https://github.com/PX4/PX4-Autopilot/commit/1d932f6ec9d4a59ba4c68a59fc134bcd925328af?w=1)
### Message
IMU drivers using FIFOs increase max length to 16 and sync similar implementations
 - this provides some extra space when the FIFO transfers don't align perfectly
 - I've also made an effort to keep the different drivers (icm20602, icm20608g, ism330ldc) in sync so we can factor out the common portions later once we've confident in the pattern.
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #27
### Hash
[7e39ef8b8fc871abbd4f5f7ab5a450580d893345](https://github.com/PX4/PX4-Autopilot/commit/7e39ef8b8fc871abbd4f5f7ab5a450580d893345?w=1)
### Message
MAVLink sim: Start faster\
This reduces test times across the board.
### Antipattern Category
X
### Keyword
faster
### Note
```C++
- system_sleep(1);
+ system_usleep(100);
```

## Commit #28
### Hash
[8](https://github.com/PX4/PX4-Autopilot/commit/8?w=1)
### Message
SMbus battery driver - a lot of updates and optimizations

- added support for BQ40Z80 based battery
- added performance counter for interface errors
- added SMART_BATTERY_INFO mavlink message
- general code cleanups and optimization
- fixed: void flooding the log in case of interface error
- fixed: using _batt_startup_capacity instead of _batt_capacity for discharged_mah
- update: read manufacture_date
- update: get _cell_count from parameter and not const 4
- update: avoid re-reading data that has already been read and stored on class already
- currently the battery type defined by BAT_SMBUS_MODEL parameter and not by auto detection
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #29
### Hash
[2956aa340e480396fd5a37d558477f6e7ce9878b](https://github.com/PX4/PX4-Autopilot/commit/2956aa340e480396fd5a37d558477f6e7ce9878b?w=1)
### Message
module: increase max timeout for stopping modules from 2s to 5s\
The gps module might take up to 4s to stop (if stopped during module
configuration).
### Antipattern Category
?
### Keyword
increase
### Note
Adjustments needed for gps module.

## Commit #30
### Hash
[3924792c2025316a55ffa01a7f4fd15e3ee071d9](https://github.com/PX4/PX4-Autopilot/commit/3924792c2025316a55ffa01a7f4fd15e3ee071d9?w=1)
### Message
Jenkins: HIL improve run_tests.py and run_nsh_cmd.py helper
 - switch to python3
 - run_nsh_cmd.py return error if command fails
 - decrease timeout in checking for output
 - Jenkins hardware tests tolerate certain command failures that aren't available on all boards (flash constrained, etc)
### Antipattern Category
?
### Keyword
decrease
### Note
Encoding/decoding usage of utf-8 enforced. Multiple timeouts hardcoded.

## Commit #31
### Hash
[a34e57a4cc8817186327436edc1aa14d2174be67](https://github.com/PX4/PX4-Autopilot/commit/a34e57a4cc8817186327436edc1aa14d2174be67?w=1)
### Message
Simulator: Increase stack, publication affinity
This commit increases the send thread stack size and changes the thread affinity of the lockstep clocking topic. It also improves verbosity in case error states occur.
### Antipattern Category
?
### Keyword
increase
### Note
Multiple increases of sleep duration.
