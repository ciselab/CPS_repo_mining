# PX4-Autopilot

## Sleep

### Remote
https://github.com/PX4/PX4-Autopilot

## Commit #1
### Hash
[a704acc2a20936d7e6d6828ae0ddf2cf7dc3578b](https://github.com/PX4/PX4-Autopilot/commit/a704acc2a20936d7e6d6828ae0ddf2cf7dc3578b?w=1)
### Message
Out of memory warning, flash and RAM optimizations
### Antipattern Category
New:Delayed_Sync_With_Physical_Events
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
New:Delayed_Sync_With_Physical_Events
### Keyword
slow
### Note
From commit message: Increase the erase timeout to avoid issues with large/slow flash.
```Python
- # erase is very slow, give it 10s
- deadline = time.time() + 10
+ # erase is very slow, give it 20s
+ deadline = time.time() + 20
```
Manually adjusting the waiting time for erasing flash chips to work for the selection of flash chips supported.
Note: Different solution possible? Know when done with erasing flash chip?
mPossible solution: Add a configuration file with matching durations for each supporting flash chips. Default value to fall back to.


## Commit #3
### Hash
[a4b0e3ecbe2d012eac7545cce14829866bacc813](https://github.com/PX4/PX4-Autopilot/commit/a4b0e3ecbe2d012eac7545cce14829866bacc813?w=1)
### Message
Add retry-on-error for non-protocol errors.\
Add more performance counters; run test #1 faster.
### Antipattern Category
New:Hard-coded-timing
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
New:Hard-coded-timing
### Keyword
performance
### Note
Performance improvement, but the number is based on what?
```
- mavlink start -r 10000 -d /dev/ttyACM0
+ mavlink start -r 5000 -d /dev/ttyACM0
```
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
X
### Keyword
overhead
### Note
added:
```C
useconds_t sleep_delay = 10000;		// default log rate: 100 Hz
```
Notes:
```C
/* work around some stupidity in task_create's argv handling */
```
```C
/* warning! using union here to save memory, elements should be used separately! */
```

## Commit #6
### Hash
[1e54dc4409df700b8b4c4a4480238db27b270dfc](https://github.com/PX4/PX4-Autopilot/commit/1e54dc4409df700b8b4c4a4480238db27b270dfc?w=1)
### Message
commander: Accel calibration: Reduce memory footprint, be more responsive
### Antipattern Category
X
### Keyword
memory
### Note
```C++
/* allow user enough time to read the message */
- sleep(3);
+ sleep(1);
```

```C++
/* inform user about already handled side */
if (data_collected[orient]) {
	mavlink_and_console_log_info(mavlink_fd, "%s side done, rotate to a different side", orientation_strs[orient]);
- 	sleep(3);
+ 	sleep(1);
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
X
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
New:Hard-coded-timing
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
Print usage, not performance interesting.

## Commit #10
### Hash
[fa590bbe8038941423ddb8ecb36d94dc7298b167](https://github.com/PX4/PX4-Autopilot/commit/fa590bbe8038941423ddb8ecb36d94dc7298b167?w=1)
### Message
Correct float parsing args and increase altitude monitoring frequency
### Antipattern Category
Smith:Are_we_there_yet?
### Keyword
increase
### Note
increasesd monitoring frequency, not explained why this is needed....
```python
# Wait for completion of mission items
while (current_sequence < len(missionlist)-1 and elapsed_time < max_execution_time):
-    time.sleep(1)
+    time.sleep(.2)
```

## Commit #11
### Hash
[94aaf0d298467596e7c6e067e3252dc0f937b429](https://github.com/PX4/PX4-Autopilot/commit/94aaf0d298467596e7c6e067e3252dc0f937b429?w=1)
### Message
increase sleep time in accel calibration routine to make accel calibration work on snapdragon
### Antipattern Category
New:Delayed_Sync_With_Physical_Events
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
New:build:Slow_Simulation/Hardware_Tests
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
New:Hard-coded-timing
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
X
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
X
### Keyword
increase
### Note
Interesting:
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
Consistend typo:
```C++
gpio_led_state = Falied;
```
Note: where is the memory leak that was fixed?

## Commit #18
### Hash
[4e5b223a0889871f4c321bc853522371d9c7827a](https://github.com/PX4/PX4-Autopilot/commit/4e5b223a0889871f4c321bc853522371d9c7827a?w=1)
### Message
hrt test decrease time
### Antipattern Category
New:Hard-coded-timing\
New:build:Slow_Simulation/Hardware_Tests
### Keyword
decrease
### Note
Shortend timing.

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
X
### Keyword
runtime
### Note
Changed queue size from 10 to 1, for AttitudeTarget and PoseStamped.
```Python
- 'mavros/setpoint_raw/attitude', AttitudeTarget, queue_size=10)
+ 'mavros/setpoint_raw/attitude', AttitudeTarget, queue_size=1)
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
New:Hard-coded-timing
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
New:Hard-coded-timing
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
Smith:Where_am_I_?\
General:Hard-coding
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
CI/CD:Too_many_changes
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
New:Hard-coded-timing\
New:build:Slow_Simulation/Hardware_Tests
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
[190b96a46c3540ec03823ac4370e166a79e1f811](https://github.com/PX4/PX4-Autopilot/commit/190b96a46c3540ec03823ac4370e166a79e1f811?w=1)
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
New:Hard-coded-timing
General:Hard-coding
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
New:Hard-coded-timing
General:Hard-coding
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
New:Hard-coded-timing
General:Hard-coding
### Keyword
increase
### Note
Multiple increases of sleep duration.

## Non-sleep

## Commit #32
### Hash
[4ce72e03b6ddd0894b2e96c2d6791e3317820462](https://github.com/PX4/PX4-Autopilot/commit/4ce72e03b6ddd0894b2e96c2d6791e3317820462?w=1)
### Message
Increase range of pulse count in PWM driver
...
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #33
### Hash
[0362fd4c2229ac1cf9b2743d28e4389a6b8e1722](https://github.com/PX4/PX4-Autopilot/commit/0362fd4c2229ac1cf9b2743d28e4389a6b8e1722?w=1)
### Message
(1) Fix a critical memory leak in the TCP read-ahead buffering logic; Add an option to suppress SDIO multi-block transfers in order to work around a buggy SDIO driver
...
### Antipattern Category
?
### Keyword
memory
### Note
Memory leak fix; TODO: reread

## Commit #34
### Hash
[9c338d809eaf32ae4a51fc74661f7d86a81a7d74](https://github.com/PX4/PX4-Autopilot/commit/9c338d809eaf32ae4a51fc74661f7d86a81a7d74?w=1)
### Message
STM32 quad encoder: Don't calculate the timer prescaler value at runtime; pre-calculate it at compiler time
...
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #35
### Hash
[227b5d0f56b4aacb68a53b07664f41565de53879](https://github.com/PX4/PX4-Autopilot/commit/227b5d0f56b4aacb68a53b07664f41565de53879?w=1)
### Message
Fix a deadlock when using the NSH ifconfig command over Telnet
### Antipattern Category
General: Deadlock
### Keyword
deadlock
### Note
TODO: reread

## Commit #36
### Hash
[5b83507116be57e0c84daea74d30dea382f20f97](https://github.com/PX4/PX4-Autopilot/commit/5b83507116be57e0c84daea74d30dea382f20f97?w=1)
### Message
Fix infinite loop in CDC/ACM driver
...
### Antipattern Category
?
### Keyword
infinite
### Note
```
* drivers/usbdev/cdcacm.c: Fix an infinite loop that occurs when the serial device is unregisters.
```

## Commit #37
### Hash
[b66dd903b6b5d1d6a72d53be54cca36fdfb3d653](https://github.com/PX4/PX4-Autopilot/commit/b66dd903b6b5d1d6a72d53be54cca36fdfb3d653?w=1)
### Message
NxWidgets: Fix a potential deadlock that can occur waiting for toolbard geometry data
...
### Antipattern Category
General: Deadlock
### Keyword
deadlock
### Note
Deadlock fix; TODO: reread

## Commit #38
### Hash
[47125132adb0ef34b429f2563b860c713a037032](https://github.com/PX4/PX4-Autopilot/commit/47125132adb0ef34b429f2563b860c713a037032?w=1)
### Message
Calypso update from Denis Carkiki.  Adds UWire driver and support for external memory in NuttX heap
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #39
### Hash
[55c75c6ba007f72e98e6b47c63e85d6f0482d339](https://github.com/PX4/PX4-Autopilot/commit/55c75c6ba007f72e98e6b47c63e85d6f0482d339?w=1)
### Message
Update STM3240G-EVAL defconfig to support NxConsole keyboard input; increase spacing of icons on the start window
...
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #40
### Hash
[0e3afd21b0f44f81c4f2befca6da6d2914f06e80](https://github.com/PX4/PX4-Autopilot/commit/0e3afd21b0f44f81c4f2befca6da6d2914f06e80?w=1)
### Message
The SST25 driver now works with SST25 (at least using the slow write mode)
...
### Antipattern Category
New:Hard-coded-timing
### Keyword
slow
### Note
```C
#if 0 /* Makes writes too slow */
      if ((status & SST25_SR_BUSY) != 0)
        {
          sst25_unlock(priv->dev);
          usleep(1000);
          sst25_lock(priv->dev);
        }
#endif
```

## Commit #41
### Hash
[d09ff7e1f92d3842f6716c4fce1f8e98026057b9](https://github.com/PX4/PX4-Autopilot/commit/d09ff7e1f92d3842f6716c4fce1f8e98026057b9?w=1)
### Message
Add LPC32xx memory map and interrupt numbers
...
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #42
### Hash
[139cd091768c57272fe1f80d725d4a3a24d2e3d0](https://github.com/PX4/PX4-Autopilot/commit/139cd091768c57272fe1f80d725d4a3a24d2e3d0?w=1)
### Message
Faster sensor bus resets on timeouts, massively reworked fixed wing app, tested
### Antipattern Category
CI/CD:Large_change
New:Hard-coded-timing
### Keyword
faster
### Note
From GitHub:
```
Large diffs are not rendered by default
```
Removed:
```C
- // 10 Hz loop
- usleep(100000);
```
Still here:
```C
/* 20Hz loop*/
usleep(50000);
```
TODO: reread

## Commit #43
### Hash
[6c4aadedf42de266e592f84cda27d8af1bbe56b5](https://github.com/PX4/PX4-Autopilot/commit/6c4aadedf42de266e592f84cda27d8af1bbe56b5?w=1)
### Message
Switch back from max performance to size as the default optimization level.  Individual modules can still override this if they need to.
### Antipattern Category
X
### Keyword
performance
### Note
Only change:
```
- MAXOPTIMIZATION		 = -O3
+ MAXOPTIMIZATION		 = -Os
```

## Commit #44
### Hash
[0472eeae0533c06d42d82d12176c575f0cdeddf0](https://github.com/PX4/PX4-Autopilot/commit/0472eeae0533c06d42d82d12176c575f0cdeddf0?w=1)
### Message
Add EEPROM read/write performance counters.
### Antipattern Category
?
### Keyword
performance
### Note
Infinite while loop, like ```while(1)```, but a compiler might generate a warning with ```while(1)``` and not with ```for (;;)``` (TODO: verify this).
Line 271:
```C
for (;;)
	{

	  perf_begin(priv->perf_reads);
	  ret = I2C_TRANSFER(priv->dev, &msgv[0], 2);
	  perf_end(priv->perf_reads);
	  if (ret >= 0)
		break;

	  /* XXX probably want a bus reset in here and an eventual timeout */
	  fvdbg("read stall");
	  usleep(1000);
	}
```

## Commit #45
### Hash
[0dc0a0539dafdf1727763cc145f02faa8a8e7d22](https://github.com/PX4/PX4-Autopilot/commit/0dc0a0539dafdf1727763cc145f02faa8a8e7d22?w=1)
### Message
Increase the retry count while probing for I2C sensors.  This will also unwedge stuck sensors.
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #46
### Hash
[704679d7b1a8338d656f3ce6565390568ef876b4](https://github.com/PX4/PX4-Autopilot/commit/704679d7b1a8338d656f3ce6565390568ef876b4?w=1)
### Message
Removed delay after receiving in recvfrom().  This was killing network performance
...
### Antipattern Category
?
### Keyword
performance
### Note
```C
- /* No timeout */
+ /* No timeout -- hang forever waiting for data. */
```
TODO: reread

## Commit #47
### Hash
[648420e67a546b33400fd2fe5b6a50410276ae3d](https://github.com/PX4/PX4-Autopilot/commit/648420e67a546b33400fd2fe5b6a50410276ae3d?w=1)
### Message
Add support for DMA memory allocator to FAT file system
...
### Antipattern Category
X
### Keyword
memory
### Note
Added support.

## Commit #48
### Hash
[491a83acb40aa1fa87c1c6894c3ecbe957c19e54](https://github.com/PX4/PX4-Autopilot/commit/491a83acb40aa1fa87c1c6894c3ecbe957c19e54?w=1)
### Message
Fix for recvfrom() hang when the new CONFIG_NET_TCP_RECVDELAY is set to zero (from Max Holtzberg)
### Antipattern Category
X
### Keyword
hang
### Note
-

## Commit #49
### Hash
[d7fb2175eb73fc7ec1616c3ad78fffd1bc1590ab](https://github.com/PX4/PX4-Autopilot/commit/d7fb2175eb73fc7ec1616c3ad78fffd1bc1590ab?w=1)
### Message
A simple file write performance test
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #50
### Hash
[731b466aca72e22039f46678e890a50dd59b59b4](https://github.com/PX4/PX4-Autopilot/commit/731b466aca72e22039f46678e890a50dd59b59b4?w=1)
### Message
If server fails to create a thread because of lack-of-resources (EAGAIN), don't terminate.  Keep serving... Memory may become available again later.
...
### Antipattern Category
?
### Keyword
memory
### Note
Naming
```C
if (ret == EAGAIN)
{
  /* Lacked resources to create a new thread. This is a temporary
   * condition, so we close this peer, but keep serving for
   * other connections.
   */

  continue;
}

/* Something is very wrong... Break out and stop serving */

break;
```
TODO: reread

## Commit #51
### Hash
[8de1d1d182bed68c075f279541c32a7493aef0bc](https://github.com/PX4/PX4-Autopilot/commit/8de1d1d182bed68c075f279541c32a7493aef0bc?w=1)
### Message
Update Olimex-LPC1766STK setenv.sh to make it faster to use CodeSourcery.
...
### Antipattern Category
General:Code_Duplication
### Keyword
faster
### Note
-

## Commit #52
### Hash
[642f3426a7aadd9fd345590a4c0881d7e64014a7](https://github.com/PX4/PX4-Autopilot/commit/642f3426a7aadd9fd345590a4c0881d7e64014a7?w=1)
### Message
Added mag calibration routine, fixed minor typos without runtime effects
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #53
### Hash
[f9a8818d1e040bdf1a4bb62041a469ceee67dbf4](https://github.com/PX4/PX4-Autopilot/commit/f9a8818d1e040bdf1a4bb62041a469ceee67dbf4?w=1)
### Message
Switch from -Os to -O3.  This generates *much* faster code, although at a ~50% size penalty.  We can afford the space.
### Antipattern Category
X
### Keyword
faster
### Note
Performance improvement, no anti-pattern.

## Commit #54
### Hash
[c522b5446dd4e692d15b37de8ad199765259e35b](https://github.com/PX4/PX4-Autopilot/commit/c522b5446dd4e692d15b37de8ad199765259e35b?w=1)
### Message
Work in progress on to/from memory BSON coding.
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #55
### Hash
[edd2715f84532f6c4c748cc97f0fe8a2982aa885](https://github.com/PX4/PX4-Autopilot/commit/edd2715f84532f6c4c748cc97f0fe8a2982aa885?w=1)
### Message
reverted memory change, sdlog app needs more than 2K
### Antipattern Category
?
### Keyword
memory
### Note
Increased memory size, which was previously decreased (hash: b82d303d296aec26f2cd78e3b2f1ab56399b2626a3e83027381c00c5ad9bd0be, message: Reducing stack sizes to free some RAM ).

## Commit #56
### Hash
[7961d6ce58b0567f4c24cb0b242e2cd875a70c5b](https://github.com/PX4/PX4-Autopilot/commit/7961d6ce58b0567f4c24cb0b242e2cd875a70c5b?w=1)
### Message
Make ostest RR scheduler test use less memory from Freddie Chopin; Plus build fix from...
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #57
### Hash
[dca3bce1ca89595f5df3788da34afe3b30bfb35a](https://github.com/PX4/PX4-Autopilot/commit/dca3bce1ca89595f5df3788da34afe3b30bfb35a?w=1)
### Message
Add a new performance counter for measuring periodic/interval events.
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #58
### Hash
[14d874f4a15653fce2902f016b1e75373afadd51](https://github.com/PX4/PX4-Autopilot/commit/14d874f4a15653fce2902f016b1e75373afadd51?w=1)
### Message
Fix some memory corruption bugs.
### Antipattern Category
New:Rounded_numbers
General:Hard-coding
### Keyword
memory
### Note
```C
- int send_data(int uart, char *buffer, int size)
+ int send_data(int uart, uint8_t *buffer, int size)
```
Hard-coded:
```C
/* The buffer size used to store messages. This must be at least as big as the number of
 * fields in the largest message struct. 
 */
#define MESSAGE_BUFFER_SIZE 50
```

## Commit #59
### Hash
[92e1d5eb78d9d04a89b0413718c8bab6e9af7f63](https://github.com/PX4/PX4-Autopilot/commit/92e1d5eb78d9d04a89b0413718c8bab6e9af7f63?w=1)
### Message
Possible fix for #78 - increase the wait timeout for discard when flashing PX4IO. It's not clear this solves the issue, but I can't reproduce it with this added.
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
Change:
```C++
- ret = recv(c, 10);
+ ret = recv(c, 250);
+ if (ret == OK) {
+ 	//log("discard 0x%02x", c);
}
```

## Commit #60
### Hash
[35c82ff2fc63ab823770f9776e6b6a0f81cd4452](https://github.com/PX4/PX4-Autopilot/commit/35c82ff2fc63ab823770f9776e6b6a0f81cd4452?w=1)
### Message
Make mixer ioctls load from a memory buffer rather than a file. This is prep for uploading the memory buffer to IO to be processed there.
### Antipattern Category
?
### Keyword
memory
### Note
TODO: reread

## Commit #61
### Hash
[375d3c14d742248b434c080527886a95ea1d563f](https://github.com/PX4/PX4-Autopilot/commit/375d3c14d742248b434c080527886a95ea1d563f?w=1)
### Message
increase the UART buffer sizes to 256

The most critical one is the GPS serial port receive buffer size,
which needs to be at least 128 to support the UBLOX protocol, but it
seems a good idea for people running a FMU without a IO board to
increase the UART buffer sizes generally
### Antipattern Category
?
### Keyword
increase
### Note
Hardware requirements.

## Commit #62
### Hash
[ca690f60272b5330f632cd18b58ee9af89fbc9ae](https://github.com/PX4/PX4-Autopilot/commit/ca690f60272b5330f632cd18b58ee9af89fbc9ae?w=1)
### Message
Fixed #153 - when no microSD card is present, test used to hang, now aborts with error.
### Antipattern Category
X
### Keyword
hang
### Note
Change now checks if the microSD card is mounted.

## Commit #63
### Hash
[070651221f4f60c2074e7641affa10e2b8714f07](https://github.com/PX4/PX4-Autopilot/commit/070651221f4f60c2074e7641affa10e2b8714f07?w=1)
### Message
Add split package logic to improve TCP send performance with delayed ACKs
...
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #64
### Hash
[1094575ce544860bc66b7c88d6b5eaf419d5ed7d](https://github.com/PX4/PX4-Autopilot/commit/1094575ce544860bc66b7c88d6b5eaf419d5ed7d?w=1)
### Message
Fix a bug where recv[from]() would hang when remote host gracefully closed connection
...
### Antipattern Category
?
### Keyword
hang
### Note
Interesting note:
```
* net/recvfrom():  Fix a bug.  When the host closes a connection
(gracefully).  recv[from]() returned success and the closure
was never detected.  Hmmm.. I don't know why the network monitor
did not catch this event.  This is an important bug fix.
```

## Commit #65
### Hash
[3bec164b3ae1cd7f9b5dcec532e7d073be96d45d](https://github.com/PX4/PX4-Autopilot/commit/3bec164b3ae1cd7f9b5dcec532e7d073be96d45d?w=1)
### Message
Fix a recently introduced memory leak
...
### Antipattern Category
X
### Keyword
memory
### Note
-
## Commit #66
### Hash
[e0f83af96fdab2cd5b239dec3a842c4a2a92ad85](https://github.com/PX4/PX4-Autopilot/commit/e0f83af96fdab2cd5b239dec3a842c4a2a92ad85?w=1)
### Message
Reset the collection state machine on all I2C errors, increase the retry count.
### Antipattern Category
?
### Keyword
increase
### Note
Why the need to increase the retry rate?

## Commit #67
### Hash
[621063ac084954bba11189c8566776aff25bfaeb](https://github.com/PX4/PX4-Autopilot/commit/621063ac084954bba11189c8566776aff25bfaeb?w=1)
### Message
Increase the number of I2C retries.
### Antipattern Category
?
### Keyword
increase
### Note
See Commit #66.

## Commit #68
### Hash
[b620136af4f8de913fd12872a91a80f62861dc4c](https://github.com/PX4/PX4-Autopilot/commit/b620136af4f8de913fd12872a91a80f62861dc4c?w=1)
### Message
Added support for MTK revision 19, working condition but configuration of MTK is very slow and needs improvement
### Antipattern Category
X
### Keyword
slow
### Note
-

## Commit #69
### Hash
[e896944adcce3d0d5e333186a76b35850e5f9bc9](https://github.com/PX4/PX4-Autopilot/commit/e896944adcce3d0d5e333186a76b35850e5f9bc9?w=1)
### Message
ms5611: try to measure the performance cost of I2C timeouts
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #70
### Hash
[8c7e2546ed5222145a6d1745e77d01f7c21c24fc](https://github.com/PX4/PX4-Autopilot/commit/8c7e2546ed5222145a6d1745e77d01f7c21c24fc?w=1)
### Message
Simplify the PX4IO main loop to cut down on memory consumption.
### Antipattern Category
New:Hard-coded-timing
### Keyword
memory
### Note
Removed:
```C
for (;;) {
	/* run this loop at ~100Hz */
	int result = poll(fds, 2, 10);
```
Interesting improvements:
```C
- // we use usleep() instead of poll() as poll() is not
- // interrupted by signals in nuttx, whereas usleep() is
- usleep(20000);
+ /* track the rate at which the loop is running */
+ perf_count(loop_perf);
```
Antipattern category on old (removed) code changes.

## Commit #71
### Hash
[5b93ab0372dd1208112156850908b87143a0c0dd](https://github.com/PX4/PX4-Autopilot/commit/5b93ab0372dd1208112156850908b87143a0c0dd?w=1)
### Message
Clean up and compact the output to fit inside a 80 column display.

Bug fix:
- running/sleeping count

Plus:
- added task state
- show the idle task (to make the number of tasks match the reported number)
- convert some calc to floating point where it doesn't hurt performance (for clarity)
- accept 'q' (standard) and escape to exit the program
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #72
### Hash
[52bb5e561c2407937d80545c127e37da6d2c3a04](https://github.com/PX4/PX4-Autopilot/commit/52bb5e561c2407937d80545c127e37da6d2c3a04?w=1)
### Message
Fix memory sizing so that we get the extra 64K we promised.
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #73
### Hash
[7e8d8f9e7226bcc04a5f8dd4b01c9a6a4f1f9910](https://github.com/PX4/PX4-Autopilot/commit/7e8d8f9e7226bcc04a5f8dd4b01c9a6a4f1f9910?w=1)
### Message
Call sub-makes with -r to make them start faster (mostly on Windows, where this inhibits an enormous amount of silly scanning for things).\
Force non-parallel builds for the NuttX archives.
### Antipattern Category
X
### Keyword
faster
### Note
-

## Commit #74
### Hash
[8fcbb4f669d8c9003f778f35a94278383e0360ac](https://github.com/PX4/PX4-Autopilot/commit/8fcbb4f669d8c9003f778f35a94278383e0360ac?w=1)
### Message
Merge SDIO changes and hack config to make it work.\
We need to resolve the DMA-safe memory allocation story, but until then let's disable the CCM. We still have as much RAM as the v1.x boards in this mode.
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #75
### Hash
[af27101ffecf2ad4642b1ced23640ff133c7246f](https://github.com/PX4/PX4-Autopilot/commit/af27101ffecf2ad4642b1ced23640ff133c7246f?w=1)
### Message
px4io: changed adc_measure() to return 0xffff on error, and lower timeout\
the timeout of 1ms was far too long, and could impact flight
performance\
Returning 0xffff on error matches the FMU code, and allows bad values
to be discarded
### Antipattern Category
New:Hard-coded-timing
### Keyword
performance
### Note

## Commit #76
### Hash
[dca844a808643131ee299a46a7cb82aea933822f](https://github.com/PX4/PX4-Autopilot/commit/dca844a808643131ee299a46a7cb82aea933822f?w=1)
### Message
Based on comments in:\
http://answers.px4.ethz.ch/question/1337/px4io-receiver-connection-problem/?answer=1346#post-id-1346

increase the longest PPM pulse we recognize out to 550µs.
### Antipattern Category
General:Lack_of_documentation
### Keyword
increase
### Note
Problem loading page (link in commit message). Anti-pattern regarding documentation of issue/commit?

## Commit #77
### Hash
[eab01a2efd0c1f1fc9cf32181c63a7e5494f0004](https://github.com/PX4/PX4-Autopilot/commit/eab01a2efd0c1f1fc9cf32181c63a7e5494f0004?w=1)
### Message
Hotfix: Generate map files for modules as well for more in-depth memory-use debugging.
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #78
### Hash
[1bf8f7b47ec8dd8f2f494fe40f193b3d1712e025](https://github.com/PX4/PX4-Autopilot/commit/1bf8f7b47ec8dd8f2f494fe40f193b3d1712e025?w=1)
### Message
sdlog2 performance increased, fixes and cleanup
### Antipattern Category
CI/CD:Large_change
### Keyword
performance
### Note
-

## Commit #79
### Hash
[4253c16b3f3eeb9ed05d2b80c8ce9531a11ffad3](https://github.com/PX4/PX4-Autopilot/commit/4253c16b3f3eeb9ed05d2b80c8ce9531a11ffad3?w=1)
### Message
Increase array size.
### Antipattern Category
General:Lack_of_documentation
### Keyword
increase
### Note
Why was this needed?

## Commit #80
### Hash
[b5f4f1ee808c176c5dc0705b76584b438f151650](https://github.com/PX4/PX4-Autopilot/commit/b5f4f1ee808c176c5dc0705b76584b438f151650?w=1)
### Message
Adressed performance concern and fixed a copy paste bug
### Antipattern Category
General:Hard-coding
### Keyword
performance
### Note
-

## Commit #81
### Hash
[5cb1f4662fb28f68e539f2c8930c0f48ccea3521](https://github.com/PX4/PX4-Autopilot/commit/5cb1f4662fb28f68e539f2c8930c0f48ccea3521?w=1)
### Message
multirotor_attitude_control performance improved, tested in flight. PID library new functionality and bugfixes.
### Antipattern Category
New:Rounded_numbers
### Keyword
performance
### Note
-

## Commit #82
### Hash
[87c3d1a8c14e9d97bb98d8255c1ba35e875b6c81](https://github.com/PX4/PX4-Autopilot/commit/87c3d1a8c14e9d97bb98d8255c1ba35e875b6c81?w=1)
### Message
More link performance counters.
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #83
### Hash
[40c56ab61e04fe73aff3a84d20ffc81e102373f3](https://github.com/PX4/PX4-Autopilot/commit/40c56ab61e04fe73aff3a84d20ffc81e102373f3?w=1)
### Message
Corrected bug in px4io driver that lead to hang of FMU-IO communication
### Antipattern Category
?
### Keyword
hang
### Note
Fixed bug by removing:
```C++
orb_copy(ORB_ID(safety), _to_safety, &safety);
```

## Commit #84
### Hash
[53d69f9e919445d13fe1c98a0164d238b7ff4af6](https://github.com/PX4/PX4-Autopilot/commit/53d69f9e919445d13fe1c98a0164d238b7ff4af6?w=1)
### Message
Added highlighting of current line to make editing and double-clicking warnings/errors faster
### Antipattern Category
X
### Keyword
faster
### Note
-

## Commit #85
### Hash
[70f272bd22e9ccdb9dbc1c15dd76fce4449ea0ab](https://github.com/PX4/PX4-Autopilot/commit/70f272bd22e9ccdb9dbc1c15dd76fce4449ea0ab?w=1)
### Message
Disabled SDIO DMA, enabled CCM memory
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #86
### Hash
[e88d63ef272124e8c0ee9574506d14866feadb8b](https://github.com/PX4/PX4-Autopilot/commit/e88d63ef272124e8c0ee9574506d14866feadb8b?w=1)
### Message
Increased USB buffer size to cope with fast transfers
### Antipattern Category
X
### Keyword
fast
### Note
-

## Commit #87
### Hash
[3f4315b4767ff221936e135b3252794a952f2b95](https://github.com/PX4/PX4-Autopilot/commit/3f4315b4767ff221936e135b3252794a952f2b95?w=1)
### Message
Hotfix: Increase stack size for low prio commander task
### Antipattern Category
?
### Keyword
increase
### Note
Why this number?
```C++
- pthread_attr_setstacksize(&commander_low_prio_attr, 2048);
+ pthread_attr_setstacksize(&commander_low_prio_attr, 2992);
```

## Commit #88
### Hash
[0810b264e5679795f100df3a7363ba3ad9d7765e](https://github.com/PX4/PX4-Autopilot/commit/0810b264e5679795f100df3a7363ba3ad9d7765e?w=1)
### Message
Hotfix: Increase work stack sizes
### Antipattern Category
?
### Keyword
increase
### Note
Same question as in Commit #87.

## Commit #89
### Hash
[3851bf5c10181fe0f56af40fc7e35a3b72bbb845](https://github.com/PX4/PX4-Autopilot/commit/3851bf5c10181fe0f56af40fc7e35a3b72bbb845?w=1)
### Message
Hotfix: Improve UART1 receive performance
### Antipattern Category
?
### Keyword
performance
### Note
Forgotten setting to turn on. Antipattern?

## Commit #90
### Hash
[81a4df0953e738041d9fdc2b2eb353a635f3003b](https://github.com/PX4/PX4-Autopilot/commit/81a4df0953e738041d9fdc2b2eb353a635f3003b?w=1)
### Message
sensors: slow down updates rate to 200Hz to free some CPU time
### Antipattern Category
New:Delayed_Sync_With_Physical_Events
?
### Keyword
slow
### Note
Maybe a different antipattern.

## Commit #91
### Hash
[537484f60d37f7f04d2ecaeb4139e2c316565eb2](https://github.com/PX4/PX4-Autopilot/commit/537484f60d37f7f04d2ecaeb4139e2c316565eb2?w=1)
### Message
Revert "sensors: slow down updates rate to 200Hz to free some CPU time"\
This reverts commit 81a4df0953e738041d9fdc2b2eb353a635f3003b.
### Antipattern Category
?
### Keyword
slow
### Note
Revent of changes in Commit #90.

## Commit #92
### Hash
[c0c366d6ee076ca812fa9672709c1e66fafdb32b](https://github.com/PX4/PX4-Autopilot/commit/c0c366d6ee076ca812fa9672709c1e66fafdb32b?w=1)
### Message
position_estimator_inav: estimate distance to bottom rate, increase time of position estimation on only accelerometer, reduce weight for GPS if flow available
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
-

## Commit #93
### Hash
[937b502d4c3fd582f7be736240f5971e8c0f7c2b](https://github.com/PX4/PX4-Autopilot/commit/937b502d4c3fd582f7be736240f5971e8c0f7c2b?w=1)
### Message
increase landing speed to v_min * 1.3 for more safety
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
-

## Commit #94
### Hash
[881c89dd1b55f5e2dbb355562665a94dcc618217](https://github.com/PX4/PX4-Autopilot/commit/881c89dd1b55f5e2dbb355562665a94dcc618217?w=1)
### Message
increase safety margin for takeoff speed
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
Similar to Commit #93.

## Commit #95
### Hash
[3ad9dd030c01e233a78aebfd2e20e67168962255](https://github.com/PX4/PX4-Autopilot/commit/3ad9dd030c01e233a78aebfd2e20e67168962255?w=1)
### Message
Added performance counter for write IOCTL
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #96
### Hash
[5b302fef59354f536e83a0b14572d2f954a6e682](https://github.com/PX4/PX4-Autopilot/commit/5b302fef59354f536e83a0b14572d2f954a6e682?w=1)
### Message
HOTFIX: Increased attitude control updates to 50 Hz - was less than 10 Hz and unintended slow
### Antipattern Category
New:Hard-coded-timing
### Keyword
slow
### Note
-

## Commit #97
### Hash
[70d4ef480ac5461ef54ac72a54bd335007e233cc](https://github.com/PX4/PX4-Autopilot/commit/70d4ef480ac5461ef54ac72a54bd335007e233cc?w=1)
### Message
geofence: do not keep fence in memory
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #98
### Hash
[c4fc730acad12b74f51d9ba7d3ff267e3e1a1ab3](https://github.com/PX4/PX4-Autopilot/commit/c4fc730acad12b74f51d9ba7d3ff267e3e1a1ab3?w=1)
### Message
FMUv2: make all UARTs use 512 byte buffer, 2048 for CDCACM output\
this is important when using UARTs for things like secondary GPS
modules, which may produce large enough transfers that 128 bytes is
not enough.\
The 2048 buffer for CDCACM transmit makes mavlink log and parameter
transfer faster
### Antipattern Category
X
### Keyword
faster
### Note
-

## Commit #99
### Hash
[3be1a5182db7bd3802b77e7c03fc14f00ca218c3](https://github.com/PX4/PX4-Autopilot/commit/3be1a5182db7bd3802b77e7c03fc14f00ca218c3?w=1)
### Message
FMUv1: use larger CDCACM buffer size for faster log transfer on FMUv1
### Antipattern Category
X
### Keyword
faster
### Note
-

## Commit #100
### Hash
[480d31f7548d2a4dc7ad55dc2de1f9733045bbd3](https://github.com/PX4/PX4-Autopilot/commit/480d31f7548d2a4dc7ad55dc2de1f9733045bbd3?w=1)
### Message
fw: increase invalid airspeed threshold
### Antipattern Category
New:Hard-coded-timing
General:Hard-coding
### Keyword
increase
### Note
-

## Commit #101
### Hash
[8c8e9a4ff9584de9d48c1773ead49054ae538b06](https://github.com/PX4/PX4-Autopilot/commit/8c8e9a4ff9584de9d48c1773ead49054ae538b06?w=1)
### Message
Enable the PX4IO self check and debug interfaces. No reason to disable them, since they are runtime-configured (and needed, for the case of memory)
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #102
### Hash
[c3e4e4ee68f1f31d3ae281b0afb281fc7c58bc27](https://github.com/PX4/PX4-Autopilot/commit/c3e4e4ee68f1f31d3ae281b0afb281fc7c58bc27?w=1)
### Message
Build fix, replaced usleep with up_udelay in memory lockdown state
### Antipattern Category
?
### Keyword
memory
### Note
Renaming issue?
```C
- usleep(300000);
+ up_udelay(300000);
```

## Commit #103
### Hash
[2aa76f1a3c4eb99074b38d287e0f18a98973671d](https://github.com/PX4/PX4-Autopilot/commit/2aa76f1a3c4eb99074b38d287e0f18a98973671d?w=1)
### Message
Fixes to memory check handling, split out switch handling to allow separate initialization
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #104
### Hash
[dda50c62bfd26463718f50d2f9c1cdbecc7de4ac](https://github.com/PX4/PX4-Autopilot/commit/dda50c62bfd26463718f50d2f9c1cdbecc7de4ac?w=1)
### Message
hmc5883: much faster calibration code with bug fixes\
this fixes two bugs in "hmc5883 calibrate" and also makes it much
faster, so it can be run on every boot. It now uses the correct 2.5Ga
range when calibrating, and fixes the expected values for X/Y/Z axes\
The basic calibration approach is similar to the APM2 driver, waiting
for 10 good samples after discarding some initial samples. That allows
the calibration to run fast enough that it can be done on every boot
without causing too much boot delay.
### Antipattern Category
X
### Keyword
fast
### Note
```C++
/* expected axis scaling. The datasheet says that 766 will
* be places in the X and Y axes and 713 in the Z
* axis. Experiments show that in fact 766 is placed in X,
* and 713 in Y and Z. This is relative to a base of 660
* LSM/Ga, giving 1.16 and 1.08 */
 ```
Left commented out print:
```C++
//print_info();
```
```C++
// ::printf("set_excitement enable=%d regA=0x%x\n", (int)enable, (unsigned)conf_reg);
```

## Commit #105
### Hash
[08a6057ef8c4aa796751c5ac07ab8efa7529b150](https://github.com/PX4/PX4-Autopilot/commit/08a6057ef8c4aa796751c5ac07ab8efa7529b150?w=1)
### Message
Increase SPI GPIO speed for FMUv1 analog to v2
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #106
### Hash
[44cd82e2fef20a3fc5aa61711b4cc06012a1e21d](https://github.com/PX4/PX4-Autopilot/commit/44cd82e2fef20a3fc5aa61711b4cc06012a1e21d?w=1)
### Message
Set default autoland wait time to -1 (infinite wait)
### Antipattern Category
X
### Keyword
infinite
### Note
-

## Commit #107
### Hash
[3d21a73ddf18b89552aa9bd65965ff6b311487b8](https://github.com/PX4/PX4-Autopilot/commit/3d21a73ddf18b89552aa9bd65965ff6b311487b8?w=1)
### Message
navigator: fixed infinite RTL->LOITER->RTL... loop on failsafe
### Antipattern Category
X
### Keyword
infinite
### Note
-

## Commit #108
### Hash
[f6694c2cef62ee3284598ed1b4d8c6954effab4e](https://github.com/PX4/PX4-Autopilot/commit/f6694c2cef62ee3284598ed1b4d8c6954effab4e?w=1)
### Message
rc.fw_defaults: increase acceptance radius which is used by navigator to generate virtual waypoints (RTL etc.)
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #109
### Hash
[ccfe476326d8b01e33a3a7ea115054a31fa7a2b9](https://github.com/PX4/PX4-Autopilot/commit/ccfe476326d8b01e33a3a7ea115054a31fa7a2b9?w=1)
### Message
decrease MC_PITCHRATE_P for TBS Discovery
### Antipattern Category
X
### Keyword
decrease
### Note
Manual tweaking?

## Commit #110
### Hash
[8425b9bef21e310d1cbd29aad65d34e9dd974d55](https://github.com/PX4/PX4-Autopilot/commit/8425b9bef21e310d1cbd29aad65d34e9dd974d55?w=1)
### Message
Increase NFILE_DESCRIPTORS to 36
### Antipattern Category
General:Lack_of_documentation
### Keyword
increase
### Note
-

## Commit #111
### Hash
[9e41f6af18d3d84413501ce37737d574fd20816d](https://github.com/PX4/PX4-Autopilot/commit/9e41f6af18d3d84413501ce37737d574fd20816d?w=1)
### Message
mavlink: memory leaks on exit fixed, minor fixes
### Antipattern Category
?
### Keyword
memory
### Note
TODO: reread

## Commit #112
### Hash
[4cee3614c7bc2e960ac52e59014bc4d08b8da11e](https://github.com/PX4/PX4-Autopilot/commit/4cee3614c7bc2e960ac52e59014bc4d08b8da11e?w=1)
### Message
rc.usb: increase data rate to 10000bytes/s for USB
### Antipattern Category
General:Lack_of_documentation
### Keyword
increase
### Note
Why the change right now?

## Commit #103
### Hash
[183a0cdb22fd824d87912ea3d2c2470f0d28ed39](https://github.com/PX4/PX4-Autopilot/commit/183a0cdb22fd824d87912ea3d2c2470f0d28ed39?w=1)
### Message
MC: default MC_YAWRATE_I changed for all setups, navigator: increase yaw acceptance to 0.2rad ~ 11deg
### Antipattern Category
General:Code_Duplication
### Keyword
increase
### Note
Antipattern General:Code_Duplication might not be avoidable?

## Commit #104
### Hash
[e075d05f579091fb9c605c856650cbfd1587a044](https://github.com/PX4/PX4-Autopilot/commit/e075d05f579091fb9c605c856650cbfd1587a044?w=1)
### Message
Move Pauls EKF into a class and instantiate only when / if needed. Checking for low memory conditions as we should.
### Antipattern Category
New:Hard-coded-timing
### Keyword
memory
### Note
Line 1180/1192 (fw_att_pos_estimator_main.cpp ):
```C
warnx("tripping covariance #3 with NaN values");
P[3][3] = nan_val; // covariance matrix
_ekf->P[3][3] = nan_val; // covariance matrix
usleep(100000);

warnx("tripping Kalman gains with NaN values");
Kfusion[0] = nan_val; // Kalman gains
_ekf->Kfusion[0] = nan_val; // Kalman gains
usleep(100000);

warnx("tripping stored states[0] with NaN values");
storedStates[0][0] = nan_val;
_ekf->storedStates[0][0] = nan_val;
usleep(100000);
```

## Commit #105
### Hash
[7b95d36405cb63b53fd1fea2c25e29aedca5a3a2](https://github.com/PX4/PX4-Autopilot/commit/7b95d36405cb63b53fd1fea2c25e29aedca5a3a2?w=1)
### Message
navigator hotfix: Increase acceptance range for yaw setpoints.
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #106
### Hash
[b770c9fc1edc570fc216bdf849f84519e4e3513f](https://github.com/PX4/PX4-Autopilot/commit/b770c9fc1edc570fc216bdf849f84519e4e3513f?w=1)
### Message
position_estimator_inav: increase acceptable EPH/EPV, in commander use EPH/EPV to decide if global position valid
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #107
### Hash
[595eb679b30442b52ccc7a2c2ce7ade7b5e5c6c9](https://github.com/PX4/PX4-Autopilot/commit/595eb679b30442b52ccc7a2c2ce7ade7b5e5c6c9?w=1)
### Message
ekf_att_pos_estimator: Fixed mag initialization, now starts with initial measurement instead of defaults for faster convergence
### Antipattern Category
X
### Keyword
faster
### Note
-

## Commit #108
### Hash
[d1bd4b0a45ec0f6f081560fbadf675e21ce53d83](https://github.com/PX4/PX4-Autopilot/commit/d1bd4b0a45ec0f6f081560fbadf675e21ce53d83?w=1)
### Message
qu4d increase pwm max
### Antipattern Category
General:Lack_of_documentation
### Keyword
increase
### Note
-

## Commit #109
### Hash
[8d3fed09443faa6a3c79b68b7800ed3472877a1c](https://github.com/PX4/PX4-Autopilot/commit/8d3fed09443faa6a3c79b68b7800ed3472877a1c?w=1)
### Message
Reduce potential dataman memory fragmentation\
The data manager dynamically allocates relatively small work item blocks
on an as needed basis. It never frees these, instead maintaining then in
a list of available block for reuse when needed. Even if these blocks
are small, the are required at non-deterministic times and can end up
scattered in memory thus causing memory fragmentation. In order to
mitigate this problems work item blocks are allocated in groups of 8 in
contiguous memory to reduce the number of scattered memory allocations.
In reality, based on current usage, rarely will more than one group of 8
be allocated.
### Antipattern Category
?
### Keyword
memory
### Note
Fix: see commit message.

## Commit #110
### Hash
[18ed3cbbb8ba4eabd32db3d07c7480c1af22ebc0](https://github.com/PX4/PX4-Autopilot/commit/18ed3cbbb8ba4eabd32db3d07c7480c1af22ebc0?w=1)
### Message
Increase servo out rate via USB
### Antipattern Category
General:Lack_of_documentation
### Keyword
increase
### Note
-
