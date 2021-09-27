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
X
### Keyword
memory
### Note
Sleep 0.3 seconds after the memory shortage lockdown. We dont see any antipattern but even the full file changed in this commit has lots of code smells. For instance, there is no evidence why they waited for 0.3 seconds and assure that the memory will be free after this time.

## Commit #2
### Hash
[7e0f8b3edaf584a48cd3bc3351e3205fd0106cdc](https://github.com/PX4/PX4-Autopilot/commit/7e0f8b3edaf584a48cd3bc3351e3205fd0106cdc?w=1)
### Message
Formatting changes to make the Python style checker happy (copied from the bootloader project).\
Increase the erase timeout to avoid issues with large/slow flash.
### Antipattern Category
New:Hard-coded-timing

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
X
### Keyword
increase
### Note
increasesd monitoring frequency.
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
New:Hard-coded-timing
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
X
### Keyword
memory
### Note
Consistend typo:
```C++
gpio_led_state = Falied;
```
Memory leak is fixed by adding the the following statement:
```C++
free (gpio_led_data);
```
The CPS developers did not free up the memory before this commit, but now they fixed it. There is no perfromance antipatterns.

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
New:Hard-coded-timing
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
X
### Keyword
memory
### Note
Memory leak fixed by defining a customized buffering logic.

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
New:Delayed_Sync_With_Physical_Events
### Keyword
infinite
### Note
```
* drivers/usbdev/cdcacm.c: Fix an infinite loop that occurs when the serial device is unregisters.
```

 As mentioned in the documentation, "The driver needs to reset the software (in order to flush the requests) and to disable the software connection when the device is unregistered".
 Also, it mentioned that "All requests must be canceled while the class driver is still bound".

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
X
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
There is no CPS-related performance antipatterns.

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
X
### Keyword
performance
### Note
```C
- /* No timeout */
+ /* No timeout -- hang forever waiting for data. */
```
This commit fixes a bug in network connection.

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
X
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
This is not an performance antipattern. This commit make sure that the connection waits for resources to be available.

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
New:Hard-coded-fine-tuning
### Keyword
memory
### Note
Increased memory size in the drone, which was previously decreased (hash: [ab63a77edf78a198117757a1d5e2dbe34cde1263](https://github.com/PX4/PX4-Autopilot/commit/ab63a77edf78a198117757a1d5e2dbe34cde1263), message: Reducing stack sizes to free some RAM ).

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
General:Performance:Unbuffered_Streams
### Keyword
memory

### Note
This commit change the file reading to using buffered stream to save IO resources.

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
X
### Keyword
increase
### Note
Before this commit, the CPS developers did not follow the documentation regarding the Hardware requirements for the buffer size. This commit fixes this issue.

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
X
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

This commit fixes a bug. There is not performance antipattern exposed here.

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
X
### Keyword
increase
### Note
There is no antipattern detected here.

## Commit #67
### Hash
[621063ac084954bba11189c8566776aff25bfaeb](https://github.com/PX4/PX4-Autopilot/commit/621063ac084954bba11189c8566776aff25bfaeb?w=1)
### Message
Increase the number of I2C retries.
### Antipattern Category
X
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
X
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
General:Lack_of_documentation
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
General:Lack_of_documentation
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
X
### Keyword
performance
### Note
Forgotten setting to turn on.

## Commit #90
### Hash
[81a4df0953e738041d9fdc2b2eb353a635f3003b](https://github.com/PX4/PX4-Autopilot/commit/81a4df0953e738041d9fdc2b2eb353a635f3003b?w=1)
### Message
sensors: slow down updates rate to 200Hz to free some CPU time
### Antipattern Category
New:Fixed_Communication_Rate

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
New:Hard-coded-fine-tuning

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
X
### Keyword
memory
### Note
This commit changes usleep to up_udelay to make sure that the system works even in memory lockdown state. However, according to our research, up_udelay is only a loop and should not be considered as an alternative for usleep. It is not an antipattern, but it can be considered as an smell.
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
X
### Keyword
memory
### Note
This commit fixes a bug in the communication.

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

## Commit #113
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

## Commit #114
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

## Commit #115
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

## Commit #116
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

## Commit #117
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

## Commit #118
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

## Commit #119
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
X
### Keyword
memory
### Note
Fix: see commit message.
This commit fixes a potential memory fragmentation. this is fixed by grouping the blocks. This is not an antipattern.

## Commit #120
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

## Commit #121
### Hash
[0655aeb7ecb73eeaedfbd41171f07f9a247b32db](https://github.com/PX4/PX4-Autopilot/commit/0655aeb7ecb73eeaedfbd41171f07f9a247b32db?w=1)
### Message
startup: NuttX seems to free memory only AFTER the next command is issued, requiring us to give it some time to do memory management so it does not keep starting tasks on top of each other. May need some consideration on main startup script as well.
### Antipattern Category
New:Hard-coded-timing
### Keyword
memory
### Note
```
# Enable a number of interesting streams we want via USB
mavlink stream -d /dev/ttyACM0 -s NAMED_VALUE_FLOAT -r 10
+ usleep 1000
mavlink stream -d /dev/ttyACM0 -s OPTICAL_FLOW -r 10
+ usleep 1000
mavlink stream -d /dev/ttyACM0 -s VFR_HUD -r 20
+ usleep 1000
mavlink stream -d /dev/ttyACM0 -s ATTITUDE -r 20
+ usleep 1000
mavlink stream -d /dev/ttyACM0 -s ATTITUDE_CONTROLS -r 30
+ usleep 1000
mavlink stream -d /dev/ttyACM0 -s SERVO_OUTPUT_RAW_0 -r 20
+ usleep 1000
```

## Commit #122
### Hash
[b43f2e8be95417cdb58b670e549cffc6445b8f81](https://github.com/PX4/PX4-Autopilot/commit/b43f2e8be95417cdb58b670e549cffc6445b8f81?w=1)
### Message
USB startup: Give NuttX enough time to tear down an app and free memory before starting the next
### Antipattern Category
New:Hard-coded-timing
### Keyword
memory
### Note
Connected to Commit #111.
```
mavlink stream -d /dev/ttyACM0 -s NAMED_VALUE_FLOAT -r 10
- usleep 1000
+ usleep 100000
mavlink stream -d /dev/ttyACM0 -s OPTICAL_FLOW -r 10
- usleep 1000
+ usleep 100000
mavlink stream -d /dev/ttyACM0 -s VFR_HUD -r 20
- usleep 1000
+ usleep 100000
mavlink stream -d /dev/ttyACM0 -s ATTITUDE -r 20
- usleep 1000
+ usleep 100000
mavlink stream -d /dev/ttyACM0 -s ATTITUDE_CONTROLS -r 30
- usleep 1000
+ usleep 100000
mavlink stream -d /dev/ttyACM0 -s SERVO_OUTPUT_RAW_0 -r 20
- usleep 1000
+ usleep 100000
```

## Commit #123
### Hash
[aa312f96f8d682c85b422ef8c5fbc89b9391712e](https://github.com/PX4/PX4-Autopilot/commit/aa312f96f8d682c85b422ef8c5fbc89b9391712e?w=1)
### Message
drivers: Fix compile warnings and non-standard performance counter names
### Antipattern Category
New:Rounded_numbers
### Keyword
performance
### Note
-

## Commit #124
### Hash
[b9b81beb17eb449921f11f46bc419056dce03852](https://github.com/PX4/PX4-Autopilot/commit/b9b81beb17eb449921f11f46bc419056dce03852?w=1)
### Message
fw att: add performance counter
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #125
### Hash
[b3d6dcb2e5a1f66c42d575f13cbc5a7eef16db27](https://github.com/PX4/PX4-Autopilot/commit/b3d6dcb2e5a1f66c42d575f13cbc5a7eef16db27?w=1)
### Message
Pre-emptively increase the log buffer - after the last cleanup we got again plenty of RAM
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note

## Commit #126
### Hash
[fe28069effe77dcac143c0194b982028438068f3](https://github.com/PX4/PX4-Autopilot/commit/fe28069effe77dcac143c0194b982028438068f3?w=1)
### Message
Increase UART1 & UART5 RX&Tx buffer sizes\
To fix MAVLink message garbling problems.
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note
Check the comments on the commit.
TODO: reread, maybe a new antipattern?

## Commit #127
### Hash
[d0f4232ac6e2ff9d796df9d995e749734edc32ee](https://github.com/PX4/PX4-Autopilot/commit/d0f4232ac6e2ff9d796df9d995e749734edc32ee?w=1)
### Message
Build and runtime fixes for matlab csv serial bridge
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #128
### Hash
[72afa2ca2bb7ce85262dd201b7620e310484f6c5](https://github.com/PX4/PX4-Autopilot/commit/72afa2ca2bb7ce85262dd201b7620e310484f6c5?w=1)
### Message
Capture TX issues in performance counter instead of spamming console in mavlink app
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #129
### Hash
[092ede366a531ad68f7ccc2f372f83b8d2993242](https://github.com/PX4/PX4-Autopilot/commit/092ede366a531ad68f7ccc2f372f83b8d2993242?w=1)
### Message
Estimator: Clean up delta quat calculations, put them in a sweet spot between accuracy and runtime.
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #130
### Hash
[fea4845ed97ca5219ceb8af0b0fb6d68603eea17](https://github.com/PX4/PX4-Autopilot/commit/fea4845ed97ca5219ceb8af0b0fb6d68603eea17?w=1)
### Message
SPI: make _bus protected\
this allows runtime use of internal/external bus to determine if DRDY
should be used on the L3GD20
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #131
### Hash
[d6632ee2dda39de78be1bbfa6754af8b59c58655](https://github.com/PX4/PX4-Autopilot/commit/d6632ee2dda39de78be1bbfa6754af8b59c58655?w=1)
### Message
ardrone: Optimize for size, since performance is good at any rate
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #132
### Hash
[2de38d0628f3146caea28cd42b30840241269f41](https://github.com/PX4/PX4-Autopilot/commit/2de38d0628f3146caea28cd42b30840241269f41?w=1)
### Message
Improve update performance and clean up compiler warnings in px4io driver\
- Fix compiler warnings in px4io_serial.cpp
- Fix compiler warnings in px4io_uploader.cpp
- Rename confusing overloaded send method with nearly identical
parameters in px4io_uploader.cpp
- Improve update performance by using maximum size programming buffer
since we are no longer limited by stack size.
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #133
### Hash
[8e12d79ef4b32da98dfb13af1321a6855ecbdc3d](https://github.com/PX4/PX4-Autopilot/commit/8e12d79ef4b32da98dfb13af1321a6855ecbdc3d?w=1)
### Message
Increase GPS position timeout to real-life timeouts. More work needed.
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
Manually adjusted timeout.
```C++
- #define POSITION_TIMEOUT		(600 * 1000)		/**< consider the local or global position estimate invalid after 600ms */
+ #define POSITION_TIMEOUT		(2 * 1000 * 1000)	/**< consider the local or global position estimate invalid after 600ms */
```

## Commit #134
### Hash
[3b3e6f5aaafd1247447cad7070e3488e5798ce3c](https://github.com/PX4/PX4-Autopilot/commit/3b3e6f5aaafd1247447cad7070e3488e5798ce3c?w=1)
### Message
Increase filter pass-band
### Antipattern Category
X
### Keyword
increase
### Note
-

## Commit #135
### Hash
[c9eea8fbfaad7bfb3eee36a49588c9ac3a42ddc6](https://github.com/PX4/PX4-Autopilot/commit/c9eea8fbfaad7bfb3eee36a49588c9ac3a42ddc6?w=1)
### Message
nshterm: increase stack size to fix crash on 'ls -l'
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
```
- MODULE_STACKSIZE = 1200
+ MODULE_STACKSIZE = 1400
```

## Commit #136
### Hash
[1dc23d0c49d99fa93284a277a6bc4970ac0e7b3b](https://github.com/PX4/PX4-Autopilot/commit/1dc23d0c49d99fa93284a277a6bc4970ac0e7b3b?w=1)
### Message
Disable mTECS until runtime error is better understood
### Antipattern Category
X
### Keyword
runtime
### Note
Commenting bits of code, untill a better solution is found.

## Commit #137
### Hash
[7f293be7d77603768899aedb438821dd19b8b4d7](https://github.com/PX4/PX4-Autopilot/commit/7f293be7d77603768899aedb438821dd19b8b4d7?w=1)
### Message
mavlink, rc.usb: increase HIL_CONTROLS rate and datarate on USB to allow HIL simulation @ 200Hz
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
```C++
- #define MAX_DATA_RATE	10000	// max data rate in bytes/s
+ #define MAX_DATA_RATE	20000	// max data rate in bytes/s
```

## Commit #138
### Hash
[3f4aef60c88b1e570dd30bc47a13d5340073e9a9](https://github.com/PX4/PX4-Autopilot/commit/3f4aef60c88b1e570dd30bc47a13d5340073e9a9?w=1)
### Message
Increase timeout in an attempt to prevent timout python failure
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
```Python                
- self.port = serial.Serial(portname, baudrate, timeout=0.5)
+ self.port = serial.Serial(portname, baudrate, timeout=2.0)
```

## Commit #139
### Hash
[54fc6aa6788a125b387926a45023844daa42ec48](https://github.com/PX4/PX4-Autopilot/commit/54fc6aa6788a125b387926a45023844daa42ec48?w=1)
### Message
Hotfix: Optimize shell commands for size - we do not need massive performance there
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #140
### Hash
[a54ef70a207cd892a9ef406df6f1aa0732035537](https://github.com/PX4/PX4-Autopilot/commit/a54ef70a207cd892a9ef406df6f1aa0732035537?w=1)
### Message
Decrease I2C timeout in config so it matches the previous 500 us timeout as close as possible. This is necessary after fixing the NuttX I2C timeout logic
### Antipattern Category
New:Hard-coded-timing
### Keyword
decrease
### Note
-

## Commit #141
### Hash
[6791ab72a910b00818026ac60d95d8df20bfa0d3](https://github.com/PX4/PX4-Autopilot/commit/6791ab72a910b00818026ac60d95d8df20bfa0d3?w=1)
### Message
Run faster for better accuracy.
### Antipattern Category
New:Hard-coded-timing
### Keyword
faster
### Note
-

## Commit #142
### Hash
[bc23b6239c50527aa550eed3bc6f17dec15c5c97](https://github.com/PX4/PX4-Autopilot/commit/bc23b6239c50527aa550eed3bc6f17dec15c5c97?w=1)
### Message
increase ram
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
They just increased the RAM size without mentioning any reason.

## Commit #143
### Hash
[0553771f4fd6fbdba43669a8f17185ed61f96a51](https://github.com/PX4/PX4-Autopilot/commit/0553771f4fd6fbdba43669a8f17185ed61f96a51?w=1)
### Message
Adapted for sharded library use with ROS. Problems to solve: error library from PX4 does not work yet. math functions such as isfinite need to be shared as well. performance library needs to be shared as well (commented for now)
### Antipattern Category
X
### Keyword
performance
### Note
Commenting bits of code, to temporarily fix issue.

## Commit #144
### Hash
[cfe14d78c5a9d2f80ebc0282e4bc400dcba6a795](https://github.com/PX4/PX4-Autopilot/commit/cfe14d78c5a9d2f80ebc0282e4bc400dcba6a795?w=1)
### Message
Adapted for sharded library use with ROS. Problems to solve: error library from PX4 does not work yet. math functions such as isfinite need to be shared as well. performance library needs to be shared as well (commented for now)
### Antipattern Category
X
### Keyword
performance
### Note
See commit #133.

## Commit #145
### Hash
[77c823d3cd0f49014a33632ec9ef3efdd7d3dfa5](https://github.com/PX4/PX4-Autopilot/commit/77c823d3cd0f49014a33632ec9ef3efdd7d3dfa5?w=1)
### Message
Adapted for sharded library use with ROS. Problems to solve: error library from PX4 does not work yet. math functions such as isfinite need to be shared as well. performance library needs to be shared as well (commented for now)
### Antipattern Category
X
### Keyword
performance
### Note
See commit #134 & #133.

## Commit #146
### Hash
[2b8a9b632555708731d93f4aa7945d19e83d3134](https://github.com/PX4/PX4-Autopilot/commit/2b8a9b632555708731d93f4aa7945d19e83d3134?w=1)
### Message
Restored performance counter functionality, ROS package used own source file for function definitions but per_counter.h stays the same
### Antipattern Category
X
### Keyword
performance
### Note
See commit #135 & #134 & #133.

## Commit #147
### Hash
[038e1cac03198259d6f7630c6bb7c65c35f44fae](https://github.com/PX4/PX4-Autopilot/commit/038e1cac03198259d6f7630c6bb7c65c35f44fae?w=1)
### Message
increase default engine failure threshold
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
```C
- PARAM_DEFINE_FLOAT(COM_EF_TIME, 5.0f);
+ PARAM_DEFINE_FLOAT(COM_EF_TIME, 10.0f);
```

## Commit #148
### Hash
[ba2f55c3d7f5872aaf07e20b58b15df85417d43a](https://github.com/PX4/PX4-Autopilot/commit/ba2f55c3d7f5872aaf07e20b58b15df85417d43a?w=1)
### Message
Revert "increase ram"\
This reverts commit bc23b6239c50527aa550eed3bc6f17dec15c5c97.
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
See commit #132.

## Commit #149
### Hash
[5bc2b34e482fe8c4b0cab8f9748bd97dc3e17291](https://github.com/PX4/PX4-Autopilot/commit/5bc2b34e482fe8c4b0cab8f9748bd97dc3e17291?w=1)
### Message
Reset performance counters on arming to allow better resolution during flight
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #150
### Hash
[acb739655d5c2ebf50449842ae2b7b9b7c76dbd1](https://github.com/PX4/PX4-Autopilot/commit/acb739655d5c2ebf50449842ae2b7b9b7c76dbd1?w=1)
### Message
Remove huge memory overhead in RC channels topic, was completely unnecessary
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #151
### Hash
[2f271888d2ed934c271637c22554b503ce68e535](https://github.com/PX4/PX4-Autopilot/commit/2f271888d2ed934c271637c22554b503ce68e535?w=1)
### Message
Added performance counter for SD log performance of write() call
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #152
### Hash
[08d6cbe6bf0b5b04f63e42c6c60f5b1fe6167547](https://github.com/PX4/PX4-Autopilot/commit/08d6cbe6bf0b5b04f63e42c6c60f5b1fe6167547?w=1)
### Message
commander: Decrease RC-signal-regained message length to stay within 50 character length limit at all times
### Antipattern Category
X
### Keyword
decrease
### Note
-

## Commit #153
### Hash
[c906c2123822ef127026eeaf272b3aceed9f8995](https://github.com/PX4/PX4-Autopilot/commit/c906c2123822ef127026eeaf272b3aceed9f8995?w=1)
### Message
px4io: prevent use of uninitialised memory in io_set_arming_state()\
the vehicle may not have setup a control_mode. We need to check the
return of orb_copy() to ensure we are getting initialised values
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #154
### Hash
[5bb03f1c2db3eb5620caf806b053f8194490969a](https://github.com/PX4/PX4-Autopilot/commit/5bb03f1c2db3eb5620caf806b053f8194490969a?w=1)
### Message
subscriber example increase stack size
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note
```
- MODULE_STACKSIZE = 1200
+ MODULE_STACKSIZE = 2400
```

## Commit #155
### Hash
[71f6a34367794a887704e2898f8a10101bacfb12](https://github.com/PX4/PX4-Autopilot/commit/71f6a34367794a887704e2898f8a10101bacfb12?w=1)
### Message
mc att: increase stack size
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note
-

## Commit #156
### Hash
[262b9fc7545805c7b93a15cbb80a2f67db5ecdf0](https://github.com/PX4/PX4-Autopilot/commit/262b9fc7545805c7b93a15cbb80a2f67db5ecdf0?w=1)
### Message
fw pos ctl: make loop performance counter more meaningful
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #157
### Hash
[c9ca61ef5b23a370fcaf3e2a0546ab5452b65733](https://github.com/PX4/PX4-Autopilot/commit/c9ca61ef5b23a370fcaf3e2a0546ab5452b65733?w=1)
### Message
mavlink: don't slow mission updates down like this, otherwise we might miss mission results
### Antipattern Category
New:Hard-coded-timing
### Keyword
slow
### Note
Removed antipattern.

## Commit #158
### Hash
[9292c8f405b0ed208443df0b1f9ebd497bb518ab](https://github.com/PX4/PX4-Autopilot/commit/9292c8f405b0ed208443df0b1f9ebd497bb518ab?w=1)
### Message
add interrupt latency printout command and mean/variance to interval performance counter
### Antipattern Category
New:Hard-coded-timing
### Keyword
performance
### Note
-

## Commit #159
### Hash
[c583f1fe8b9e66b42dd4697a5908541dfdd57f69](https://github.com/PX4/PX4-Autopilot/commit/c583f1fe8b9e66b42dd4697a5908541dfdd57f69?w=1)
### Message
increase commander framesize
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note
```
- EXTRACXXFLAGS = -Wframe-larger-than=1900
+ EXTRACXXFLAGS = -Wframe-larger-than=2000
```

## Commit #160
### Hash
[ee7e008008caa04f905654cb18e6d68fd980f8cd](https://github.com/PX4/PX4-Autopilot/commit/ee7e008008caa04f905654cb18e6d68fd980f8cd?w=1)
### Message
increase commander framesize
### Antipattern Category
X
### Keyword
increase
### Note
Same as Commit #149.

## Commit #161
### Hash
[59e0b67c8eaa4295c23f53500ff5c8e3b34ff5a8](https://github.com/PX4/PX4-Autopilot/commit/59e0b67c8eaa4295c23f53500ff5c8e3b34ff5a8?w=1)
### Message
NuttxConfig: increase I2C timeout to 10ms
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
-

## Commit #162
### Hash
[ca47952281cfe66732b08d3878eb6c8b1613abeb](https://github.com/PX4/PX4-Autopilot/commit/ca47952281cfe66732b08d3878eb6c8b1613abeb?w=1)
### Message
l3gd20: added register checking\
this checks at runtime that key registers have correct values
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #163
### Hash
[04c273bca6c99f31fd04741234d9c8efa849b553](https://github.com/PX4/PX4-Autopilot/commit/04c273bca6c99f31fd04741234d9c8efa849b553?w=1)
### Message
sdlog2: slow down the free space check a bit more
### Antipattern Category
New:Hard-coded-timing
### Keyword
slow
### Note
-

## Commit #164
### Hash
[e8eff3061f5e9c451c94d081932cac0e62e1a9b9](https://github.com/PX4/PX4-Autopilot/commit/e8eff3061f5e9c451c94d081932cac0e62e1a9b9?w=1)
### Message
Revert "sdlog2: slow down the free space check a bit more"\
This reverts commit 04c273bca6c99f31fd04741234d9c8efa849b553.
### Antipattern Category
New:Hard-coded-timing
### Keyword
slow
### Note
See Commit #153.

## Commit #165
### Hash
[a3bce71b97b6e958737d11414cce2609e5d4848d](https://github.com/PX4/PX4-Autopilot/commit/a3bce71b97b6e958737d11414cce2609e5d4848d?w=1)
### Message
Performance counters: Estimate RMS for elapsed counters. Allow to use a perf counter across processes, deal with overruns and other resulting inconsistencies from cross-process use.
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #166
### Hash
[2bff39d562f1d7c0ffa5e8875d355eb3271c70fe](https://github.com/PX4/PX4-Autopilot/commit/2bff39d562f1d7c0ffa5e8875d355eb3271c70fe?w=1)
### Message
MPU6K driver: Start performance counters for system latency, as its commonly the main sensor
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #167
### Hash
[172dbf37070e2dccadc8779d6e0926d3f8d60706](https://github.com/PX4/PX4-Autopilot/commit/172dbf37070e2dccadc8779d6e0926d3f8d60706?w=1)
### Message
Performance counters: Add option to set otherwise estimated time interval
### Antipattern Category
X
### Keyword
performance
### Note
It add a non performance-related option.

## Commit #168
### Hash
[05367f8a006ae6e36fec0911c97490c31033551b](https://github.com/PX4/PX4-Autopilot/commit/05367f8a006ae6e36fec0911c97490c31033551b?w=1)
### Message
Handle slight increase of frame size in example
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note
```
- EXTRACFLAGS = -Wframe-larger-than=1200
+ EXTRACFLAGS = -Wframe-larger-than=1300
```

## Commit #169
### Hash
[ae6198b0bad801535c879d3269920e12781cea92](https://github.com/PX4/PX4-Autopilot/commit/ae6198b0bad801535c879d3269920e12781cea92?w=1)
### Message
sdlog2: Made sdlog writer performance available in log fiiles, reduced telemetry messages
### Antipattern Category
X
### Keyword
performance
### Note
-

## Commit #170
### Hash
[1cff86b0b562301020973f354043f27272d29f5b](https://github.com/PX4/PX4-Autopilot/commit/1cff86b0b562301020973f354043f27272d29f5b?w=1)
### Message
ros mixer: increase number of controls to default to fix undefined behaviour
### Antipattern Category
X
### Keyword
increase
### Note
This commit changes size of an array to consider two more behaviors. It is not related to performance of the CPS.

## Commit #171
### Hash
[f23e603d02ba416ae250770cdaad6a859d6bae69](https://github.com/PX4/PX4-Autopilot/commit/f23e603d02ba416ae250770cdaad6a859d6bae69?w=1)
### Message
mc attctl multiplatform: increase stack size
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note
-

## Commit #172
### Hash
[9c627255ccc980270fe56b6c4ddeb494e1ce0f50](https://github.com/PX4/PX4-Autopilot/commit/9c627255ccc980270fe56b6c4ddeb494e1ce0f50?w=1)
### Message
MPU6000: Increase gyro offset tolerance to 7 dps
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
This increase the maximm acceptable Gyro offset's dynamic range to 7dps (degress per second).

## Commit #173
### Hash
[3b07890361d56ce80d881e3969ff097b5cd96af4](https://github.com/PX4/PX4-Autopilot/commit/3b07890361d56ce80d881e3969ff097b5cd96af4?w=1)
### Message
update sitl default params, make posctrl very slow for now
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
slow
### Note
This commit reverts back to use the default paramaters for the drone. 

## Commit #174
### Hash
[28e943ca28f10cc1ea205a0e18cf814c8a2afa52](https://github.com/PX4/PX4-Autopilot/commit/28e943ca28f10cc1ea205a0e18cf814c8a2afa52?w=1)
### Message
setting parameters at runtime to get rid of the designated union initializer
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #175
### Hash
[c7d0cb6bd72deef810cfe1a16ac7b78810f8036b](https://github.com/PX4/PX4-Autopilot/commit/c7d0cb6bd72deef810cfe1a16ac7b78810f8036b?w=1)
### Message
lsm303d: Fix memory initialization and error_count not set
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #176
### Hash
[74177a2688f1163ec9659f3847d7cd17d0eb325f](https://github.com/PX4/PX4-Autopilot/commit/74177a2688f1163ec9659f3847d7cd17d0eb325f?w=1)
### Message
px4_uploader: Push program bytes faster by using bigger blocks
### Antipattern Category
General:Hard-coding
General:Lack_of_documentation
### Keyword
faster
### Note
-

## Commit #177
### Hash
[81648f84cd97ec865ba7f20cebeb6285f7ef6d18](https://github.com/PX4/PX4-Autopilot/commit/81648f84cd97ec865ba7f20cebeb6285f7ef6d18?w=1)
### Message
increase RTL descend altitude
### Antipattern Category
New:Hard-coded-fine-tuning
General:Lack_of_documentation
### Keyword
increase
### Note
-

## Commit #178
### Hash
[48bf84ff3754109fe6cf8e0e161eb70ae0987bfe](https://github.com/PX4/PX4-Autopilot/commit/48bf84ff3754109fe6cf8e0e161eb70ae0987bfe?w=1)
### Message
oreoled: support send_bytes ioctl\
Also increase maximum command length to 24 bytes
### Antipattern Category
General:Hard-coding
General:Lack_of_documentation
### Keyword
increase
### Note
-

## Commit #179
### Hash
[3e5b8ded8cdd650e961008ce65c93dd64a326554](https://github.com/PX4/PX4-Autopilot/commit/3e5b8ded8cdd650e961008ce65c93dd64a326554?w=1)
### Message
Increase rate of MAVLink output on companion link
### Antipattern Category
General:Hard-coding
General:Lack_of_documentation
### Keyword
increase
### Note
-

## Commit #180
### Hash
[5c3f4d21944fb779feade46e1aba81ca5705462f](https://github.com/PX4/PX4-Autopilot/commit/5c3f4d21944fb779feade46e1aba81ca5705462f?w=1)
### Message
GPIO led: Do not allocate memory statically, but only when module loads
### Antipattern Category
X
### Keyword
memory
### Note
This is an issue in handling memory in C. It is not considered as an antipattern.

## Commit #181
### Hash
[61437a5587b20e7e3c79fd1ab91e945dc0c316fb](https://github.com/PX4/PX4-Autopilot/commit/61437a5587b20e7e3c79fd1ab91e945dc0c316fb?w=1)
### Message
MAVLink app: Do no allocate memory statically, but only on execution on stack.
### Antipattern Category
X
### Keyword
memory
### Note
Memory usage improvement. Related to Commit #170.

## Commit #182
### Hash
[2883edaecd442e3049ad3224989cb384096e637a](https://github.com/PX4/PX4-Autopilot/commit/2883edaecd442e3049ad3224989cb384096e637a?w=1)
### Message
ros sitl: increase Z gains for ardrone and iris
### Antipattern Category
General:Hard-coding
General:Lack_of_documentation
### Keyword
increase
### Note
Hardware support.

## Commit #183
### Hash
[9db48df3d63836c5cca4480d847777c166bb31e8](https://github.com/PX4/PX4-Autopilot/commit/9db48df3d63836c5cca4480d847777c166bb31e8?w=1)
### Message
Slightly increase commander stack size to accomodate any additional printf calls
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
-

## Commit #184
### Hash
[37de377dcffb07ef49bacc0ec6ff722dadba1154](https://github.com/PX4/PX4-Autopilot/commit/37de377dcffb07ef49bacc0ec6ff722dadba1154?w=1)
### Message
commander: Increase stack size for low prio task to accomodate accel cal.
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
See commit #173.

## Commit #185
### Hash
[ad54ff616dc83a703fe51c2a80a0662618116782](https://github.com/PX4/PX4-Autopilot/commit/ad54ff616dc83a703fe51c2a80a0662618116782?w=1)
### Message
commander: Increase frame size limit
### Antipattern Category
X
### Keyword
increase
### Note
This is a change in config file.

## Commit #186
### Hash
[78741c87e5415c9e894f619e28b145e127576a56](https://github.com/PX4/PX4-Autopilot/commit/78741c87e5415c9e894f619e28b145e127576a56?w=1)
### Message
MAVLink app: 1) only transmit active params, 2) send params faster, 3) ensure no overflow occurs on buffer when sending at higher rate.
### Antipattern Category
New:Fixed_Communication_Rate
### Keyword
faster
### Note
-

## Commit #187
### Hash
[9a9efdaaa5a1a67be9a0939495503f222a1f3987](https://github.com/PX4/PX4-Autopilot/commit/9a9efdaaa5a1a67be9a0939495503f222a1f3987?w=1)
### Message
commander: Increase timeout on airspeed sensor for the prearm_check
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
-

## Commit #188
### Hash
[f1b2efeeaf1ca41fa20263af37b94485dcb9cee6](https://github.com/PX4/PX4-Autopilot/commit/f1b2efeeaf1ca41fa20263af37b94485dcb9cee6?w=1)
### Message
increase default roll/pitch rate limits to 360dps
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
-

## Commit #189
### Hash
[f23bc38d3ec45c2b3d2d72b06e2426d40cefd10c](https://github.com/PX4/PX4-Autopilot/commit/f23bc38d3ec45c2b3d2d72b06e2426d40cefd10c?w=1)
### Message
increase default roll/pitch rate limits to 360dps
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
See Commit #178.

## Commit #190
### Hash
[6e060c01a76401172e452e562993f79acfef9d1a](https://github.com/PX4/PX4-Autopilot/commit/6e060c01a76401172e452e562993f79acfef9d1a?w=1)
### Message
SDLOG2: Optimize runtime efficiency
### Antipattern Category
X
### Keyword
runtime
### Note
This commit improves the efficiency of the project by improving the memory allocation. However, this change is dedicated only to C. So, it is not a performance antipattern specifically for CPSs.

## Commit #191
### Hash
[5299f767069be3bd8014a86a11a1748371e952a3](https://github.com/PX4/PX4-Autopilot/commit/5299f767069be3bd8014a86a11a1748371e952a3?w=1)
### Message
POSIX: initialize before running script\
The initialization functions were called after the script
commands were run causing a deadlock waiting for an
uninitialized semaphore.
...
### Antipattern Category
X
### Keyword
deadlock
### Note
-

## Commit #192
### Hash
[6db77dc8bbae32ee15a17e7a5caa90f7e6191b2c](https://github.com/PX4/PX4-Autopilot/commit/6db77dc8bbae32ee15a17e7a5caa90f7e6191b2c?w=1)
### Message
Experimental virtual file support\
QuRT does not have a filesystem, so creating a virtual filesystem
that could be implemented as an in-memory file or a remote file
over fastRPC.
...
### Antipattern Category
X
### Keyword
memory
### Note
QuRT is an os for Qualcomm Technologies processors. It does not have filesystem so this commit makes a virtual FS for it. 

```C++
#define PX4_MAX_DEV 100
#define PX4_MAX_DEV 30
```
Why have ```int i=0;``` out the for-loop?
```C++
int i=0;
printf("Files:\n");
for (; i<PX4_MAX_DEV; ++i) {
```

## Commit #193
### Hash
[3ac95fb5816dcbdce4a269767c3f6019c434811f](https://github.com/PX4/PX4-Autopilot/commit/3ac95fb5816dcbdce4a269767c3f6019c434811f?w=1)
### Message
lsm303d: run sampling 200usec faster to avoid aliasing\
this runs the sampling of the accelerometer 200usec faster than
requested and then throw away duplicates using the accelerometer
status register data ready bit. This avoids aliasing due to drift in
the stm32 clock compared to the lsm303d clock
### Antipattern Category
X
### Keyword
faster
### Note
They increase the polling frequency for the reason that they mentioned in the commit message ("This avoids aliasing due to drift in the stm32 clock compared to the lsm303d clock")


## Commit #194
### Hash
[a710159263ea5f561d352073504958a9a9f85c81](https://github.com/PX4/PX4-Autopilot/commit/a710159263ea5f561d352073504958a9a9f85c81?w=1)
### Message
mpu6000: sample at 200usec faster rate to avoid aliasing

this runs the mpu6000 200usec faster than requested then detects and
disccards duplicates by comparing accel values. This avoids a nasty
aliasing issue due to clock drift between the stm32 and mpu6000
### Antipattern Category
New:Hard-coded-timing
### Keyword
faster
### Note
They increase the polling frequency for the reason that they mentioned in the commit message ("This avoids aliasing due to drift in the stm32 clock compared to the lsm303d clock")
```C++
/*
  we set the timer interrupt to run a bit faster than the desired
  sample rate and then throw away duplicates by comparing
  accelerometer values. This time reduction is enough to cope with
  worst case timing jitter due to other timers
 */
 ```
 
## Commit #195
### Hash
[dc4d5619eae2bb6eebfe2f11ee97f5734a35d731](https://github.com/PX4/PX4-Autopilot/commit/dc4d5619eae2bb6eebfe2f11ee97f5734a35d731?w=1)
### Message
Reduced the amount of memory used by params to only that that is needed

Conflicts:
	src/modules/systemlib/param/param.c
### Antipattern Category
X
### Keyword
memory
### Note
-

## Commit #196
### Hash
[f154f6e5e7598b02c2a5c5bb87e646a3425421a8](https://github.com/PX4/PX4-Autopilot/commit/f154f6e5e7598b02c2a5c5bb87e646a3425421a8?w=1)
### Message
MAVLink transmission: Allow faster overall transmissions.
### Antipattern Category
New:Hard-coded-timing
### Keyword
faster
### Note
-

## Commit #197
### Hash
[5c53d38652dc6c97e216ea6b70215a95890df572](https://github.com/PX4/PX4-Autopilot/commit/5c53d38652dc6c97e216ea6b70215a95890df572?w=1)
### Message
FMUv2 config: Increase USB TX buf size further to speed up MAVLink FTP transfers
### Antipattern Category
New:Fixed_Communication_Rate
### Keyword
increase
### Note
-

## Commit #198
### Hash
[03ef6a30ec5fa7c09b0de3ba00d577ccca5d39e6](https://github.com/PX4/PX4-Autopilot/commit/03ef6a30ec5fa7c09b0de3ba00d577ccca5d39e6?w=1)
### Message
Speed up param transmit now that we are faster on USB
### Antipattern Category
New:Fixed_Communication_Rate
### Keyword
faster
### Note
The change in USB makes it possible to have a faster communication.

## Commit #199
### Hash
[38004cdd955dad01801b750e18e45ac5dd3000e4](https://github.com/PX4/PX4-Autopilot/commit/38004cdd955dad01801b750e18e45ac5dd3000e4?w=1)
### Message
PreflightCheck: Increase GPS timeout to 4 sec
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
-

## Commit #200
### Hash
[a90caf7b7b3e70fb61b57c6dce6710d78debbfcd](https://github.com/PX4/PX4-Autopilot/commit/a90caf7b7b3e70fb61b57c6dce6710d78debbfcd?w=1)
### Message
l3gd20: faster gyro interrupts
### Antipattern Category
New:Hard-coded-timing
### Keyword
faster
### Note
-

## Commit #201
### Hash
[bc75814d500c673fa8699f8d242c88e610ecded2](https://github.com/PX4/PX4-Autopilot/commit/bc75814d500c673fa8699f8d242c88e610ecded2?w=1)
### Message
Increase buffer sizes on companion link
### Antipattern Category
X
### Keyword
increase
### Note
it is a change in a config file 

## Commit #202
### Hash
[d43b0513cec925125e0cef00b9df8ffbe1801f72](https://github.com/PX4/PX4-Autopilot/commit/d43b0513cec925125e0cef00b9df8ffbe1801f72?w=1)
### Message
Increase buffer sizes on companion link
### Antipattern Category
X
### Keyword
increase
### Note
it is a change in a config file 

## Commit #203
### Hash
[a734fc96d117a732e5584e758ccff52fe041e828](https://github.com/PX4/PX4-Autopilot/commit/a734fc96d117a732e5584e758ccff52fe041e828?w=1)
### Message
extensive orb_advert_t fixes\
The calls to orb_advertise were being mishandled throughout the code.
There were ::close() calls on memory pointers, there were checks
against < 0 when it is a pointer to a object and values larger than
0x7ffffffff are valid. Some places orb_advert_t variables were
being initialized as 0 other places as -1.\
The orb_advert_t type was changed to uintptr_t so the pointer value
would not be wrapped as a negative number. This was causing a failure
on ARM.\
Tests for < 0 were changed to == 0 since a null pointer is the valid
representation for error, or uninitialized.
...
### Antipattern Category
CI/CD:Too_many_changes
### Keyword
memory
### Note
Many changes, but needed due to the type of change.

## Commit #204
### Hash
[b7986e6fdd103064128d0933f7cb32ab4252159b](https://github.com/PX4/PX4-Autopilot/commit/b7986e6fdd103064128d0933f7cb32ab4252159b?w=1)
### Message
land detector: Improve performance for fixed wing setups
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
performance
### Note
-

## Commit #205
### Hash
[acfd1ea51976300b5b89a7dc0f8c5158b3150604](https://github.com/PX4/PX4-Autopilot/commit/acfd1ea51976300b5b89a7dc0f8c5158b3150604?w=1)
### Message
POSIX: added hrt_queue for handling fast periodic events\
The workqueues measure time in ticks  which is typically 10ms.
Some interrupt events in Nuttx occur at about 1ms so a more
granular workqueue is needed for POSIX.
...
### Antipattern Category
General:bottleneck
### Keyword
fast
### Note
This process makes abottleneck since it is slower than the periodic event occurance.

## Commit #206
### Hash
[fb778af8b3274be5ae5963382af0161ac6c7848e](https://github.com/PX4/PX4-Autopilot/commit/fb778af8b3274be5ae5963382af0161ac6c7848e?w=1)
### Message
increase max file descriptors to 100
### Antipattern Category
General:Hard-coding 
### Keyword
increase
### Note
 it is changig the number of file description (OS config). Not related to CPS.

## Commit #207
### Hash
[4aa4038e270c33e36ba2f8db866db3c6abec6222](https://github.com/PX4/PX4-Autopilot/commit/4aa4038e270c33e36ba2f8db866db3c6abec6222?w=1)
### Message
increase number of arguments passable to apps
### Antipattern Category
X
### Keyword
increase
### Note
Not a performance-related change.

## Commit #208
### Hash
[9155e8a7fe2a7611c6b1ed136b5691475546a65c](https://github.com/PX4/PX4-Autopilot/commit/9155e8a7fe2a7611c6b1ed136b5691475546a65c?w=1)
### Message
FX79: Increase travel
### Antipattern Category
General:Lack_of_documentation
?
### Keyword
increase
### Note
TODO: reread

## Commit #209
### Hash
[8838b18da75d6f4354f73b38152c2ca98f9197aa](https://github.com/PX4/PX4-Autopilot/commit/8838b18da75d6f4354f73b38152c2ca98f9197aa?w=1)
### Message
FW attitude control: Run attitude controller as fast as we can to minimize latency
### Antipattern Category
New:Fixed_Communication_Rate
New:Hard-coded-timing
### Keyword
fast
### Note
-

## Commit #210
### Hash
[55ed9e96126cab150dbad1d9bd9db392b75781d9](https://github.com/PX4/PX4-Autopilot/commit/55ed9e96126cab150dbad1d9bd9db392b75781d9?w=1)
### Message
ECL: Run TECS filter faster, adjust gains accordingly
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
faster
### Note
-

## Commit #211
### Hash
[9ecf4345a5cacc05f3c434d3c7516ade700d000f](https://github.com/PX4/PX4-Autopilot/commit/9ecf4345a5cacc05f3c434d3c7516ade700d000f?w=1)
### Message
ORBMap: bugfix, got rid of infinite Looping Louie
### Antipattern Category
X
### Keyword
infinite
### Note
-

## Commit #212
### Hash
[3d92364d9eb391d3f0d615df7092d96194e2d5b0](https://github.com/PX4/PX4-Autopilot/commit/3d92364d9eb391d3f0d615df7092d96194e2d5b0?w=1)
### Message
camera trigger : increase free cycling time when we are not enabled
### Antipattern Category
-
### Keyword
increase
### Note
-

## Commit #213
### Hash
[1a8703ec1c0aee86aa2440fc8b7cd627f65854a9](https://github.com/PX4/PX4-Autopilot/commit/1a8703ec1c0aee86aa2440fc8b7cd627f65854a9?w=1)
### Message
Improved logging with both compile and runtime level filtering\
The device level debug will have to be removed and the debugging
can be based on this new logging structure which can tell where
an error (or debug output) occured whch the current implmentation
cannot.\
The one limitation is the new macros cannot take a char* for the
format parameter. It must be an actual string literal because it
is concatenated with other strings.
...
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #214
### Hash
[552c9800a9a394e5ad351309d62278aecd44073f](https://github.com/PX4/PX4-Autopilot/commit/552c9800a9a394e5ad351309d62278aecd44073f?w=1)
### Message
px4_log: Fixed compiler warning when using PX4_LOG\
If __px4_log_level_current is unsigned then the runtime filter
comparison warns because an unsigned value can't be less than zero.\
Changed typed to signed so compiler will not issue a warning.
...
### Antipattern Category
X
### Keyword
runtime
### Note
-

## Commit #215
### Hash
[52b0f17ff31213e1c073cf53c069e8883a3ca0e9](https://github.com/PX4/PX4-Autopilot/commit/52b0f17ff31213e1c073cf53c069e8883a3ca0e9?w=1)
### Message
increase highest pwm to 2150
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
This commit increases the maximum speed of the motor.

## Commit #216
### Hash
[5cf20c8dcfeba450bcc926f4a73b81c382a9ad43](https://github.com/PX4/PX4-Autopilot/commit/5cf20c8dcfeba450bcc926f4a73b81c382a9ad43?w=1)
### Message
increase fw idle for ATTCTL and POSCTL to 0.2
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
-

## Commit #217
### Hash
[7043869237b5294233ca8dfaa613ceaaaf3d95bd](https://github.com/PX4/PX4-Autopilot/commit/7043869237b5294233ca8dfaa613ceaaaf3d95bd?w=1)
### Message
VDev:
- increase max number of devices to 200
- increase max number of file descriptors to 200
- add warning if number of file descriptor exceeds max value
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note
Same as Commit #196

## Commit #218
### Hash
[640024357f3b3a261031b750cf7a7b5a82e53a78](https://github.com/PX4/PX4-Autopilot/commit/640024357f3b3a261031b750cf7a7b5a82e53a78?w=1)
### Message
Land detector: increase ground speed threshold
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
-

## Commit #219
### Hash
[cae604ac1f8177775048dacdc899d4372efaf0ec](https://github.com/PX4/PX4-Autopilot/commit/cae604ac1f8177775048dacdc899d4372efaf0ec?w=1)
### Message
HMC5883: Increase the number of calibration cycles to ensure a stable result
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
The calibration cycle checks the results if we have enough good results it stops the calibration. This value is hard-coded and is changed by this commit because it was not the best number of cycles and good results for calibration of a hardware.

## Commit #220
### Hash
[5bec38b37dbdf87720b98021850141e817de4191](https://github.com/PX4/PX4-Autopilot/commit/5bec38b37dbdf87720b98021850141e817de4191?w=1)
### Message
MC land detector: Slightly decrease allowed vertical motion during landed state. This is important so that fast descends do not result in a false positive landed state
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
fast
### Note
The commit message is quite clear and self explanatory.

## Commit #221
### Hash
[b1b555ceb6f8121cfa87e6dbed1274a232a45006](https://github.com/PX4/PX4-Autopilot/commit/b1b555ceb6f8121cfa87e6dbed1274a232a45006?w=1)
### Message
MAVLink app: Increase max data rate
### Antipattern Category
New:Fixed_Communication_Rate
### Keyword
increase
### Note
This commit changes the communication rate in MAVLink (a protocol for communicating with small unmanned vehicle).

## Commit #222
### Hash
[ec21a71b369ff609fa74ccb5b71a4d275e9e5068](https://github.com/PX4/PX4-Autopilot/commit/ec21a71b369ff609fa74ccb5b71a4d275e9e5068?w=1)
### Message
Commander: increase mag cal timeout
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
-

## Commit #223
### Hash
[06c45aadfbca55d88ff643a1ca526065a1d357e7](https://github.com/PX4/PX4-Autopilot/commit/06c45aadfbca55d88ff643a1ca526065a1d357e7?w=1)
### Message
FW attitude control: Increase default integrator gains to compensate common airframe trim issues
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
-

## Commit #224
### Hash
[0321f416a0f31e75234b32d86094b6898d77439c](https://github.com/PX4/PX4-Autopilot/commit/0321f416a0f31e75234b32d86094b6898d77439c?w=1)
### Message
Increase allowance for vertical velocity in landed mode
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
-

## Commit #225
### Hash
[e443a3f3be42ed9ebfcf0ca588d7b0a4d359f582](https://github.com/PX4/PX4-Autopilot/commit/e443a3f3be42ed9ebfcf0ca588d7b0a4d359f582?w=1)
### Message
Harmonize FW default gains, increase TECS height rate default gain considerably
### Antipattern Category
New:General:Hard-coded-fine-tuning
### Keyword
increase
### Note
-

## Commit #226
### Hash
[e09771be17d8965f8928b6d577e4222c01e67fa6](https://github.com/PX4/PX4-Autopilot/commit/e09771be17d8965f8928b6d577e4222c01e67fa6?w=1)
### Message
NSH terminal: Increase hold-off time to ensure USB is up and running
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
-

## Commit #227
### Hash
[a589d15c5212c3249599932080f656ce2b7a0044](https://github.com/PX4/PX4-Autopilot/commit/a589d15c5212c3249599932080f656ce2b7a0044?w=1)
### Message
Refactored debug() and log() in CDev\
These functions used vprintf which is not available on all platforms.
They also do not enable line and file debug output.\
Changed to macros that preserve the output format.  Uses new macro that
can be used to implement per object, runtime selectable logging
...
### Antipattern Category
?
CI/CD:Too_many_changes
### Keyword
runtime
### Note
Due to platform, specific changes. The CI/CD:Too_many_changes was needed due to the type of change.

## Commit #228
### Hash
[1ef7d1348794d0d55d1799b6a7ae29a2c0debfc5](https://github.com/PX4/PX4-Autopilot/commit/1ef7d1348794d0d55d1799b6a7ae29a2c0debfc5?w=1)
### Message
Increase NSH back-off time
### Antipattern Category
New:Hard-coded-timing
### Keyword
increase
### Note
-

## Commit #229
### Hash
[c5ec4de6eab8aa7639f263aa42c88f0d76061820](https://github.com/PX4/PX4-Autopilot/commit/c5ec4de6eab8aa7639f263aa42c88f0d76061820?w=1)
### Message
Increase NSH back-off time
### Antipattern Category
X
### Keyword
increase
### Note
Same as Commit #218.

## Commit #230
### Hash
[eea2f61f02bb7ea092770a956f64443f1f190496](https://github.com/PX4/PX4-Autopilot/commit/eea2f61f02bb7ea092770a956f64443f1f190496?w=1)
### Message
Retire attitude-only EKF due to performance and memory consumption considerations
### Antipattern Category
X
### Keyword
performance
### Note
-
