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
Interesting, increased sleep duration to not have the tests fail. Why it was increased by set amount is not explained.

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
No (CPS performance) antipattern was found reviewing this commit.

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
A lot of changes in this commit (335 additions with 192 deletions over 7 files).
Added support; not interesting for CSP-PA.

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
No (CPS performance) antipattern was found reviewing this commit.

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
Moved calculation to at coompiler time, no (CPS performance) antipattern was found in this commit.

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
Added support and changes made to make use of added implementation.
No (CPS performance) antipattern was found reviewing this commit.

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
Visualization changes, no (CPS performance) antipattern was found reviewing this commit.

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
Added memory map, see commit message.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
These files all contain the same code additions and changes:
> nuttx/configs/olimex-lpc1766stk/ftpc/setenv.sh
> nuttx/configs/olimex-lpc1766stk/hidkbd/setenv.sh
> nuttx/configs/olimex-lpc1766stk/nettest/setenv.sh
> nuttx/configs/olimex-lpc1766stk/nsh/setenv.sh
> nuttx/configs/olimex-lpc1766stk/nx/setenv.sh
> nuttx/configs/olimex-lpc1766stk/ostest/setenv.sh
> nuttx/configs/olimex-lpc1766stk/slip-httpd/setenv.sh
> nuttx/configs/olimex-lpc1766stk/thttpd/setenv.sh
> nuttx/configs/olimex-lpc1766stk/usbserial/setenv.sh
> nuttx/configs/olimex-lpc1766stk/usbstorage/setenv.sh
> nuttx/configs/olimex-lpc1766stk/wlan/setenv.sh 


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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.
Though the change:
```C
- while (true)
+ for (;;) {
```
was found here as well.
Probably related to compiler causing issues for an infite while(true) loop, but not with for(;;). While doing the same thing.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
Decreased timeout, not explained in a lot of details how the performance degredation was detected and why this will (still) work.
```C
- if (hrt_elapsed_time(&now) > 1000) {
+ if (hrt_elapsed_time(&now) > 100) {
```

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
No (CPS performance) antipattern was found reviewing this commit.

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
4 Files changed with 351 additions and 176 deletions -> large change for one commit.

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
Copy paste bug probably due to reusing of code, where some minor changes were needed.

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
Increase accuracy:
```C
- pid->count = 0;
- pid->saturated = 0;
- pid->last_output = 0;
+ pid->dt_min = dt_min;
+ pid->count = 0.0f;
+ pid->saturated = 0.0f;
```

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
Timing flow is hardcoded:
```C
  static const hrt_abstime gps_topic_timeout = 1000000;		// GPS topic timeout = 1s
  static const hrt_abstime flow_topic_timeout = 1000000;	// optical flow topic timeout = 1s
  static const hrt_abstime sonar_timeout = 150000;		// sonar timeout = 150ms
- static const hrt_abstime sonar_valid_timeout = 1000000;	// assume that altitude == distance to surface during this time
- static const hrt_abstime flow_valid_timeout = 1000000;	// assume that altitude == distance to surface during this time
+ static const hrt_abstime sonar_valid_timeout = 1000000;	// estimate sonar distance during this time after sonar loss
+ static const hrt_abstime xy_src_timeout = 2000000;		// estimate position during this time after position sources loss
  static const uint32_t updates_counter_len = 1000000;
  static const uint32_t pub_interval = 10000;			// limit publish rate to 100 Hz
```

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
ToDo: reread

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
No (CPS performance) antipattern was found reviewing this commit.

## Commit #96
### Hash
[5b302fef59354f536e83a0b14572d2f954a6e682](https://github.com/PX4/PX4-Autopilot/commit/5b302fef59354f536e83a0b14572d2f954a6e682?w=1)
### Message
HOTFIX: Increased attitude control updates to 50 Hz - was less than 10 Hz and unintended slow
### Antipattern Category
New:Hard-coded-timing
New:Fixed_Communication_Rate
### Keyword
slow
### Note
Manually adjusted fequency, initeresting for Antipattern: Fixed Communication Rate.
```C++
- orb_set_interval(_att_sub, 100);
+ /* rate limit attitude control to 50 Hz (with some margin, so 17 ms) */
+ orb_set_interval(_att_sub, 17);
```

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
Manually adjusted threshold from 0.1 to 0.5.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
Manual tweaking? ToDo: reread.

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
No explanation why the NFILE_DESCRIPTORS were changed from 32 to 36.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No (CPS performance) antipattern was found reviewing this commit.

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
No explanation why the pwm was changed:
```
- set PWM_MAX 1900
+ set PWM_MAX 2100
```

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
No explanation why the servo out rate was increased.

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


## Commit #231
### Hash
[fc3acdb2c1b6c656c6a815f04e036b1159a1dfc5](https://github.com/PX4/PX4-Autopilot/commit/fc3acdb2c1b6c656c6a815f04e036b1159a1dfc5)
### Message
cmake: param refactoring

Use a struct to contain all the parameters so the ordering in
memory is not machine dependent.
### Antipattern Category
X
### Keyword
memory
### Note
This is a change to refactor the params for cmake (a build automation framework)


## Commit #232
### Hash
[0490046af45e8e4f8ae94961000211236ba25501](https://github.com/PX4/PX4-Autopilot/commit/0490046af45e8e4f8ae94961000211236ba25501)
### Message
MS5611: Increase the requirements about the PROM contents and CRC.
### Antipattern Category
X
### Keyword
Increase
### Note
This commit add more requirements for initializing a hardware. This commit fixes a funtionality issue.


## Commit #233
### Hash
[cdb2a5432b79a8c882d6c192c3fff615afbe683d](https://github.com/PX4/PX4-Autopilot/commit/cdb2a5432b79a8c882d6c192c3fff615afbe683d)
### Message
FMUv1: Do not support CAN build, since its out of reach memory wise anyway
### Antipattern Category
X
### Keyword
memory
### Note
This commit remove CAN module build from FMUv1 (the earlier and archived version of PX4's Flight Management System) build process in cmake.




## Commit #234
### Hash
[ae65269de9f0ea1e63ba5addce1e1788c62c93ee](https://github.com/PX4/PX4-Autopilot/commit/ae65269de9f0ea1e63ba5addce1e1788c62c93ee)
### Message
UAVCAN: Increase stack since its hitting almost the limit
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
Increase

### Note
This commit increases the stack size in UAVCAN node.  UAVCAN is a protocol designed for reliable intra-vehicle communications. the fixed stack size for this communication was almost full during the production. Hence, this commit increases the limit of this stack.


## Commit #235
### Hash
[407191d4ab1a90bb413c3db1241cbba8adb95172](https://github.com/PX4/PX4-Autopilot/commit/407191d4ab1a90bb413c3db1241cbba8adb95172)

### Message
UAVCAN driver transformed to use global memory pool
### Antipattern Category
X
### Keyword
memory

### Note
With this commit UAVCAN has access to the global memory pool. Not a performance issue.


## Commit #236
### Hash
[a570d1de7d20f6d0817fd6210473a58db9c3aa13](https://github.com/PX4/PX4-Autopilot/commit/a570d1de7d20f6d0817fd6210473a58db9c3aa13)

### Message
UAVCAN memory usage status and shrink
### Antipattern Category
General:performance:using_massive_arrays_likes
### Keyword
memory
### Note
This commit makes sure that the memory pool gets shrinked during the process.

## Commit #237
### Hash
[1ace017cb88319829c80e9571d71c903a4bc78a4](https://github.com/PX4/PX4-Autopilot/commit/1ace017cb88319829c80e9571d71c903a4bc78a4)

### Message
Deallocating memory used by UAVCAN virtual iface on destruction
### Antipattern Category
General:C:not_deallocating
### Keyword
memory
### Note
This commit pop all of the franmes that are already stored in the queue before node destruction. This manual deallocation is only needed in C and C++.


## Commit #238
### Hash
[ca4e55fec301bb80af20a94fdfcdbf8d9551a83d](https://github.com/PX4/PX4-Autopilot/commit/ca4e55fec301bb80af20a94fdfcdbf8d9551a83d)

### Message
UAVCAN allocator as a dedicated type; reporting a warning if memory leak is deetcted upon destruction
### Antipattern Category
General:C:not_deallocating
### Keyword
memory
### Note
Same as previous Commit, this one also check if the blocks are deallocated duting the destruction.

## Commit #239
### Hash
[109bee855b3d734b63fe88bd3eec5fdc8d443b58](https://github.com/PX4/PX4-Autopilot/commit/109bee855b3d734b63fe88bd3eec5fdc8d443b58)

### Message
Node on leaked memory in UAVCAN driver
### Antipattern Category
General:C:not_deallocating
### Keyword
memory
### Note
Same as previous Commit, this memory leak comes from memory allocation and dellocation in C.

## Commit #240
### Hash
[6c4f09c0e4fe3a243bb68c9bcac03110b1c2a4d1](https://github.com/PX4/PX4-Autopilot/commit/6c4f09c0e4fe3a243bb68c9bcac03110b1c2a4d1)

### Message
Fixed memory leak in UAVCAN baro driver
### Antipattern Category
General:C:not_deallocating
### Keyword
memory
### Note
Same as previous Commit, this memory leak comes from memory allocation and dellocation in C.

## Commit #241
### Hash
[9d86dbb6a1c3625f912ffc9470c0184c274d0da2](https://github.com/PX4/PX4-Autopilot/commit/9d86dbb6a1c3625f912ffc9470c0184c274d0da2)

### Message
Fixed memory leaks in the primary UAVCAN thread
### Antipattern Category
General:C:not_deallocating
### Keyword
memory
### Note
Same as previous Commit, this memory leak comes from memory allocation and dellocation in C.

## Commit #242
### Hash
[1aa9304b638eacff7f491836d44db16612807ddd](https://github.com/PX4/PX4-Autopilot/commit/1aa9304b638eacff7f491836d44db16612807ddd)

### Message
Logging rate was limited to 1 Hz

I set the maximum to 100 Hz, since most SD cards are not fast enough for more. (but more is still possible with forcing)
### Antipattern Category
New:Fixed_Communication_Rate
### Keyword
fast
### Note
This commit set the max logging rate to 100HZ since the previous value (1HZ) was too slow. This limitation should reflect the minimum speed of the SD card used in this system

## Commit #243
### Hash
[8b70bd248742e2ca291c17c98150d34980957ddb](https://github.com/PX4/PX4-Autopilot/commit/8b70bd248742e2ca291c17c98150d34980957ddb)

### Message
Commander: Increase stack for commandline calibration
### Antipattern Category
X
### Keyword
increase
### Note
Changes a variable in build framework (cmake)

## Commit #244
### Hash
[bd4497f8837c6a68d162ab09de633353e54dfd89](https://github.com/PX4/PX4-Autopilot/commit/bd4497f8837c6a68d162ab09de633353e54dfd89)

### Message
Simulator: Add performance counters for delay
### Antipattern Category
X
### Keyword
performance
### Note
This commit adds performance counters for logging purposes and monitoring the reason behind a delay.

## Commit #245
### Hash
[17caae00aac16338af46c8481c5f3fd9257aa0b0](https://github.com/PX4/PX4-Autopilot/commit/17caae00aac16338af46c8481c5f3fd9257aa0b0)

### Message
Attitude estimator Q: Add performance counters for delay
### Antipattern Category
X
### Keyword
performance
### Note
This commit adds performance counters for logging purposes and monitoring the reason behind a delay.


## Commit #246
### Hash
[d07c69d3298206b10836a4e57d5155858875f13b](https://github.com/PX4/PX4-Autopilot/commit/d07c69d3298206b10836a4e57d5155858875f13b)

### Message
MAVLink: Output RC inputs faster
### Antipattern Category
New:Fixed_Communication_Rate
### Keyword
faster
### Note
RC input is a key part of any autopilot, giving the pilot control of the airframe, allowing them to change modes and also giving them control of auxiliary equipment such as camera mounts. This commit increase the speed of tese inputs.


## Commit #247
### Hash
[fa197ee490297b39c6ccff47233ffa515306785d](https://github.com/PX4/PX4-Autopilot/commit/fa197ee490297b39c6ccff47233ffa515306785d)

### Message
FMU driver: Run slightly faster to accomodate S.BUS
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
faster
### Note
This commit make the system compatible with  S.BUS. This commit reduce the intervals in FMU driver from 2K to 1500. Net commit will change it again.

## Commit #248
### Hash
[a4aa844151b07c993d814ab9024ffabe40a7a52f](https://github.com/PX4/PX4-Autopilot/commit/a4aa844151b07c993d814ab9024ffabe40a7a52f)

### Message
FMU driver: Slightly increase run interval to save load
### Antipattern Category
New:Hard-coded-fine-tuning
New:Hard-coded-timing

### Keyword
increase
### Note
This commit changes the same value as the previous commit. it changes it from 1500 to 1800.


## Commit #249
### Hash
[f99e14144e1abae33650817fbc84c702520a56bf](https://github.com/PX4/PX4-Autopilot/commit/f99e14144e1abae33650817fbc84c702520a56bf)

### Message
Q estimator: Increase stack size as needed
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
stack size is an input parameter for task_create method.
task_create is a method from Apache NuttX (a real-time embedded operating system (RTOS)). NuttX is the primary RTOS for running PX4 on a flight-control board.
 This method creates and activates a new task with a specified priority and returns its system-assigned ID.
 Stack size is the size (in bytes) of the stack needed for the task. the amount of stack required is dependent on many parameters such as function call nesting depth.
 This commit change the stack size for Q estimator task.

## Commit #250
### Hash
[3515e6ae918d1e29a656ead9e99ba79f9704957d](https://github.com/PX4/PX4-Autopilot/commit/3515e6ae918d1e29a656ead9e99ba79f9704957d)

### Message
INAV: Increase stack size as needed
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Look at commit 249.  This commit change the stack size for INAV task.

## Commit #251
### Hash
[66e9abc7741c567766a3ffd3719f3709fd699b20](https://github.com/PX4/PX4-Autopilot/commit/66e9abc7741c567766a3ffd3719f3709fd699b20)

### Message
SDLOG2: increase stack size as needed
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Look at commit 249.  This commit change the stack size for SDLOG2 task.


## Commit #252
### Hash
[3c26ca99a07eb6957d894295133dc9cb0f4999a5](https://github.com/PX4/PX4-Autopilot/commit/3c26ca99a07eb6957d894295133dc9cb0f4999a5)

### Message
Q estimator: Increase phase margin
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
the phase margin is the difference between the phase lag φ and -180°, for an amplifier's output signal at zero dB gain.
This commit changes this value.

## Commit #253
### Hash
[65002d279f4f672a19885bbad08db23e00f245f6](https://github.com/PX4/PX4-Autopilot/commit/65002d279f4f672a19885bbad08db23e00f245f6)

### Message
Commander: Allow setting home position faster
### Antipattern Category
New:Hard-coded-timing
### Keyword
faster
### Note
The commander node should  update home position on arming if at least an X amount of time spent from commander initialization. This timing is to avoid setting home on in-air restart
This value changed from various values to 500ms.

## Commit #254
### Hash
[1fc774bbf881c49138500073c28197dedb036b08](https://github.com/PX4/PX4-Autopilot/commit/1fc774bbf881c49138500073c28197dedb036b08)

### Message
Q estimator: Increase phase margin
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Same as commit 252.

## Commit #255
### Hash
[bff0f225b19058efb4fde675a5d1cf3354280585](https://github.com/PX4/PX4-Autopilot/commit/bff0f225b19058efb4fde675a5d1cf3354280585)

### Message
FMU driver: Update faster
### Antipattern Category
New:Hard-coded-fine-tuning
New:Hard-coded-timing

### Keyword
faster
### Note
Same as Commit 248

## Commit #256
### Hash
[05a73d2821246557e6ae44639210fbd93a73f4b8](https://github.com/PX4/PX4-Autopilot/commit/05a73d2821246557e6ae44639210fbd93a73f4b8)

### Message
added takeoff logic for position controller to get the uav off the ground fast and transition smoothly to poctl after takeoff, added landing logic to reduce thrust to zero once on the ground
### Antipattern Category
X
### Keyword
fast
### Note
This commit adds functionality for fast takeoff.

## Commit #257
### Hash
[62763904f24db62ca8aafaac16495ebc48ac0cb3](https://github.com/PX4/PX4-Autopilot/commit/62763904f24db62ca8aafaac16495ebc48ac0cb3)

### Message
Simulator: Add performance counter for incoming packet interval
### Antipattern Category
X
### Keyword
performance
### Note
Adds profiling of the interval at which packets are received.

## Commit #258
### Hash
[5bc2019fd583d61cd6cc329da771079f887ab58a](https://github.com/PX4/PX4-Autopilot/commit/5bc2019fd583d61cd6cc329da771079f887ab58a)

### Message
Fixes for qurt build

Added missing functions that were added for other targets but not for qurt.

Added workaround for missing sem_timedwait(). This may have a performance
impact until a sem_timedwait is supported.

std::to_string is not supported by the hexagon compiler

Signed-off-by: Mark Charlebois <charlebm@gmail.com>
### Antipattern Category
X
### Keyword
performance
### Note
Implements a custom `sem_timedwait` function for the qurt target. The implementation makes use of a work queue to to unlock the current thread after the timeout.

## Commit #259
### Hash
[21b99b408cec117c994b7af017c41614aa92a1dd](https://github.com/PX4/PX4-Autopilot/commit/21b99b408cec117c994b7af017c41614aa92a1dd)

### Message
Yaw fix: increase threshold
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
A threshold was changed to stop yaw from moving, but there is no justification of the value.

## Commit #260
### Hash
[be1db2ced51d837dc062aa9d509955c0aa41bfab](https://github.com/PX4/PX4-Autopilot/commit/be1db2ced51d837dc062aa9d509955c0aa41bfab)

### Message
quick fix:
Remove throttle non-increase condition for landing since this has lead to
quads falling out of the sky.
### Antipattern Category
X
### Keyword
increase
### Note
Not a performance anti-pattern.

## Commit #261
### Hash
[ab65a55fbf374a881318921e982e1df158853dc7](https://github.com/PX4/PX4-Autopilot/commit/ab65a55fbf374a881318921e982e1df158853dc7)

### Message
Change arming transfer to only set the register if the local configuration changed. Move its write operation to the fast rate so that arming / disarming is instantaneous
### Antipattern Category
Known:Is-everything-ok
New:Fixed-communication-rate
### Keyword
fast
### Note
This increases the frequency at which the arming state is checked and published. But it makes sure to never write the same state twice.

## Commit #262
### Hash
[08ef2e8a1c08c6189de3f2912944c5ce495d50cc](https://github.com/PX4/PX4-Autopilot/commit/08ef2e8a1c08c6189de3f2912944c5ce495d50cc)

### Message
Param command: Increase stack as needed
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
The affected code makes use of the `px4_add_module` cmake function to declare a module with a certain stack size. In this commit the stack size is increased.

On the current master branch this hard-coded value is gone.

## Commit #263
### Hash
[f460e955549d3fb4425d42f23f9e51cd98978132](https://github.com/PX4/PX4-Autopilot/commit/f460e955549d3fb4425d42f23f9e51cd98978132)

### Message
Param: Increase robustness of default save command
### Antipattern Category
General:Hard-coding
### Keyword
increase
### Note
This commit changes a save function to retry 5 times before giving up.

## Commit #264
### Hash
[99068aebac4d16f2b84eec739c8678bdabc8e661](https://github.com/PX4/PX4-Autopilot/commit/99068aebac4d16f2b84eec739c8678bdabc8e661)

### Message
FMUv4: Run FRAM bus faster
### Antipattern Category
New:Fixed-communication-rate
### Keyword
faster
### Note
The frequency of something was increased. It seems that the value might be taken from the hardware specification.

From the source:
> Default SPI2 to 12MHz and de-assert the known chip selects.
>
>	MS5611 has max SPI clock speed of 20MHz

## Commit #265
### Hash
[b37082e3904d6a0adeab59e76c903f819abfa7ee](https://github.com/PX4/PX4-Autopilot/commit/b37082e3904d6a0adeab59e76c903f819abfa7ee)

### Message
MS5611: Run SPI bus faster
### Antipattern Category
New:Fixed-communication-rate
### Keyword
faster
### Note
Same as #264.

## Commit #266
### Hash
[ff690dda8072bb8068772cebfe4cd7979d491151](https://github.com/PX4/PX4-Autopilot/commit/ff690dda8072bb8068772cebfe4cd7979d491151)

### Message
increase priority of sPort_telemetry to 200
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
increase priority of sPort_telemetry to 200 from 2000

## Commit #267
### Hash
[17c3aa3bac9b6b817259b1e4b37f159e47df9cfb](https://github.com/PX4/PX4-Autopilot/commit/17c3aa3bac9b6b817259b1e4b37f159e47df9cfb)

### Message
MC att control: Slightly increase max yaw rate
### Antipattern Category
New:Hard-coded-fine-tuning

### Keyword
increase
### Note
  commit: min-max : 0.0-360.0
  main: min:max changed to 0.0-1800.0
In commit value is changed from 30 to 45, doc not changed (old value of 30 remained), in master the value is 200 . Not a performance issue.

## Commit #268
### Hash
[1454e2acbae79d7982e5b9de07f882a2a5f3a901](https://github.com/PX4/PX4-Autopilot/commit/1454e2acbae79d7982e5b9de07f882a2a5f3a901)

### Message
Libuavcan update: Reduces STM32 CAN IRQ overhead with new error handling logic
### Antipattern Category
Smith:General:Unnecessary_Processing

### Keyword
overhead
### Note
new module, assertions and simpler returns for errors.

## Commit #269
### Hash
[39ee36a8ea38805cb01450ff9fe5a6f5d8c5c136](https://github.com/PX4/PX4-Autopilot/commit/39ee36a8ea38805cb01450ff9fe5a6f5d8c5c136)

### Message
Pre-empt HRT execution in SITL if simulator is slow
### Antipattern Category
X

### Keyword
slow
### Note
Issue: Simulation lockstep #3675
PR message: This PR implements the Simulator -> SITL direction and blocks the execution of SITL if the simulator is lagging. It also does time bookkeeping and ensures the blocked execution does not lead to jumping timestamps. "Flight tested" in Sim, leads to a lot more stability.

The new function uses the old one if there is not a delay time.

## Commit #270
### Hash
[65081ca6819d6b01d2612a70ec48e1f577d4b02f](https://github.com/PX4/PX4-Autopilot/commit/65081ca6819d6b01d2612a70ec48e1f577d4b02f)

### Message
FMUv2: Increase USB buffer to speed up log transfers
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
USB buffer is increased from 4000 to 8000

## Commit #271
### Hash
[45ea58d451983ae50889a1547dbdcf01d0e491de](https://github.com/PX4/PX4-Autopilot/commit/45ea58d451983ae50889a1547dbdcf01d0e491de)

### Message
FMUv4: Increase USB and UART buffers to speed up log transfers
### Antipattern Category
New:Hard-coded-fine-tuning

### Keyword
increase
### Note
USB buffer is increased from 4000 to 8000, UART from 2000 to 4000.

## Commit #272
### Hash
[9583ff1b8bd13f5669bb9265721f595d4e196fac](https://github.com/PX4/PX4-Autopilot/commit/9583ff1b8bd13f5669bb9265721f595d4e196fac)

### Message
Add memory debugging switch support
### Antipattern Category
X

### Keyword
memory
### Note
optimization flags for debug

## Commit #273
### Hash
[de8c4c9901391c28ee4d86c5cf026db74b6042ac](https://github.com/PX4/PX4-Autopilot/commit/de8c4c9901391c28ee4d86c5cf026db74b6042ac)

### Message
Pixracer: Increase streams and data rate via Wifi
### Antipattern Category
New:Fixed-communication-rate

### Keyword
increase
### Note
Start mavlink maximum sending rate decreased from 800000 to 20000.

## Commit #274
### Hash
[12437f1fc6ab604b43287ed960806a5d455f66db](https://github.com/PX4/PX4-Autopilot/commit/12437f1fc6ab604b43287ed960806a5d455f66db)

### Message
increase stack size for frsky telemetry daemon
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Issue: increase stack size for frsky telemetry daemon #3780
Seems the product was failing after a feature was added, where the stack size
wasn't checked. Value changed from 2000 to 2200.

## Commit #275
### Hash
[9516e2559aaf29f1657e8690027cec0fec38fbd9](https://github.com/PX4/PX4-Autopilot/commit/9516e2559aaf29f1657e8690027cec0fec38fbd9)

### Message
Changes to improve performance

The work queue processing was causing too much overhead so a more
efficient check was implemented.

Signed-off-by: Mark Charlebois <charlebm@gmail.com>
### Antipattern Category
General:performance:using_massive_arrays_likes

### Keyword
performance
### Note
Better management of the queue elements.

## Commit #276
### Hash
[f5211030dcba9806c6969b6fd105980ef350204a](https://github.com/PX4/PX4-Autopilot/commit/f5211030dcba9806c6969b6fd105980ef350204a)

### Message
Changes to improve performance

The work queue processing was causing too much overhead so a more
efficient check was implemented.

Signed-off-by: Mark Charlebois <charlebm@gmail.com>
### Antipattern Category

### Keyword
performance
### Note


## Commit #277
### Hash
[a1a615b9079b029a451ee2cd326607635006f7e0](https://github.com/PX4/PX4-Autopilot/commit/a1a615b9079b029a451ee2cd326607635006f7e0)

### Message
Added param shared memory support

Signed-off-by: Mark Charlebois <charlebm@gmail.com>
### Antipattern Category

### Keyword
memory
### Note


## Commit #278
### Hash
[dbd89fe584d478af71cbf6a2cf8c5731b5976158](https://github.com/PX4/PX4-Autopilot/commit/dbd89fe584d478af71cbf6a2cf8c5731b5976158)

### Message
px4_qurt_tasks: fix hang because of absolute time

The timeout was triggered using absolute time instead of a delay in
usec. This lead to the system hanging. With the fix it continues after
the timeout, however, the rates still don't seem right.
### Antipattern Category

### Keyword
hang
### Note


## Commit #279
### Hash
[3cda3610d0d90fc6abd50d82633cecd139788116](https://github.com/PX4/PX4-Autopilot/commit/3cda3610d0d90fc6abd50d82633cecd139788116)

### Message
param: workaround for QURT

There is no such thing as set_param_no_autosave on QURT, therefore just
save it anyway. On the Snapdragon the overhead should not be a problem.
### Antipattern Category

### Keyword
overhead
### Note


## Commit #280
### Hash
[4adfea7fa9bc7ab7a0b251280f62ecd7d14f2a38](https://github.com/PX4/PX4-Autopilot/commit/4adfea7fa9bc7ab7a0b251280f62ecd7d14f2a38)

### Message
Resolved shared memory parameter problems and removed additional debug code.
### Antipattern Category

### Keyword
memory
### Note


## Commit #281
### Hash
[75fad09263c27af36d5233396fc0d35f4cacdb52](https://github.com/PX4/PX4-Autopilot/commit/75fad09263c27af36d5233396fc0d35f4cacdb52)

### Message
Fixed problem causing a failure to obtain the shared memory lock on the AppsProc.
### Antipattern Category

### Keyword
memory
### Note


## Commit #282
### Hash
[d2575c25563d5731f6db0a1607d096198d32cabe](https://github.com/PX4/PX4-Autopilot/commit/d2575c25563d5731f6db0a1607d096198d32cabe)

### Message
ESC cal: Increase timeouts
### Antipattern Category

### Keyword
increase
### Note


## Commit #283
### Hash
[b98602df8b3317fbe2bb055e728777d3bdb5dee4](https://github.com/PX4/PX4-Autopilot/commit/b98602df8b3317fbe2bb055e728777d3bdb5dee4)

### Message
sdlog2:
increase stack size and fix indentation
### Antipattern Category

### Keyword
increase
### Note


## Commit #284
### Hash
[3ab6fe7edd2cadc83749a9e4186a5248368dff93](https://github.com/PX4/PX4-Autopilot/commit/3ab6fe7edd2cadc83749a9e4186a5248368dff93)

### Message
do not allocate unnecessary memory in logging app
### Antipattern Category

### Keyword
memory
### Note


## Commit #285
### Hash
[0960e1a8207a9abfa91b9df99d3632eff117a97a](https://github.com/PX4/PX4-Autopilot/commit/0960e1a8207a9abfa91b9df99d3632eff117a97a)

### Message
make structs static and decrease stack size, run astyle
### Antipattern Category

### Keyword
decrease
### Note


## Commit #286
### Hash
[607053cfbc9b0ae79e64348b22ce98e40227c822](https://github.com/PX4/PX4-Autopilot/commit/607053cfbc9b0ae79e64348b22ce98e40227c822)

### Message
decrease stack allocation to 1100
### Antipattern Category

### Keyword
decrease
### Note


## Commit #287
### Hash
[613ec40d864e557fa76de658ee08b38401acc92c](https://github.com/PX4/PX4-Autopilot/commit/613ec40d864e557fa76de658ee08b38401acc92c)

### Message
LPE: comment out gps delay handling, too much memory required.
### Antipattern Category

### Keyword
memory
### Note


## Commit #288
### Hash
[213cdf1a9139488f156721a72feded53d839d964](https://github.com/PX4/PX4-Autopilot/commit/213cdf1a9139488f156721a72feded53d839d964)

### Message
mavlink: send out parameters faster over UDP
### Antipattern Category

### Keyword
faster
### Note


## Commit #289
### Hash
[a446a337e99b57f6936896944f5ed2809e36267f](https://github.com/PX4/PX4-Autopilot/commit/a446a337e99b57f6936896944f5ed2809e36267f)

### Message
Revert "mavlink: send out parameters faster over UDP"

This reverts commit 213cdf1a9139488f156721a72feded53d839d964.

Raising the stream rate of param values had the nice effect that
receiving the params became really quick. However, on the downside it
set all other streams pretty slow. This needs to be fixed differently.
### Antipattern Category

### Keyword
slow
### Note


## Commit #290
### Hash
[ec930d2372da90aedaed157a9610f4a8c860fbab](https://github.com/PX4/PX4-Autopilot/commit/ec930d2372da90aedaed157a9610f4a8c860fbab)

### Message
Increase stack size by 100 bytes. From @tridge
### Antipattern Category

### Keyword
increase
### Note


## Commit #291
### Hash
[e69799882815b53654aa39eee6b34983161d44db](https://github.com/PX4/PX4-Autopilot/commit/e69799882815b53654aa39eee6b34983161d44db)

### Message
fix sdlog2 self deadlock bug
### Antipattern Category

### Keyword
deadlock
### Note


## Commit #292
### Hash
[f3e147f57bf699b1ea349c76c095f1a40bf36709](https://github.com/PX4/PX4-Autopilot/commit/f3e147f57bf699b1ea349c76c095f1a40bf36709)

### Message
make replay faster
### Antipattern Category

### Keyword
faster
### Note


## Commit #293
### Hash
[47d3e093a4abb2bd4e34cc5c2c02813b19424f8b](https://github.com/PX4/PX4-Autopilot/commit/47d3e093a4abb2bd4e34cc5c2c02813b19424f8b)

### Message
Increase Wifi data rate
### Antipattern Category

### Keyword
increase
### Note


## Commit #294
### Hash
[832dde7531e7ed20fe177f9f9138aeb8445eb8bb](https://github.com/PX4/PX4-Autopilot/commit/832dde7531e7ed20fe177f9f9138aeb8445eb8bb)

### Message
Update rcS to run Wifi faster
### Antipattern Category

### Keyword
faster
### Note


## Commit #295
### Hash
[21f403e12b1c800c3e4bd901c363a886736f6466](https://github.com/PX4/PX4-Autopilot/commit/21f403e12b1c800c3e4bd901c363a886736f6466)

### Message
gps: make sure the gps module compiles for POSIX & add it to the posix_sitl_default cmake

- Note that the simulator still uses gpssim by default
- now the gps module can be used in the SITL. this makes it possible to test
  the real gps HW under POSIX
  additional steps needed to use it:
  - in the rcS_jmavsim_iris, make sure to start the gps instead of gpssim:
    gps start -d /dev/ttyACM0 -s
  - disable the mavlink serial connection in simulator_mavlink.cpp,
    openUart(PIXHAWK_DEVICE, 115200);
- this also fixes a memory leak in the gps module
### Antipattern Category

### Keyword
memory
### Note


## Commit #296
### Hash
[80e05dd3a329e7c8b4ba45f14aaa25befa53cf65](https://github.com/PX4/PX4-Autopilot/commit/80e05dd3a329e7c8b4ba45f14aaa25befa53cf65)

### Message
orb: fix memory leaks, forgotten unlock & wrong exit condition in advertisement

How can someone just add a FIXME for such a simple case?!
### Antipattern Category

### Keyword
memory
### Note


## Commit #297
### Hash
[a8a57ca20cec3d66d6ba5fd65ce5a99b25f8b678](https://github.com/PX4/PX4-Autopilot/commit/a8a57ca20cec3d66d6ba5fd65ce5a99b25f8b678)

### Message
make iris move a bit faster in gazebo and removed broken assertion from posctl test
### Antipattern Category

### Keyword
faster
### Note


## Commit #298
### Hash
[fff535857de0a883901b08c59fd10b5781f7da44](https://github.com/PX4/PX4-Autopilot/commit/fff535857de0a883901b08c59fd10b5781f7da44)

### Message
drivers/gps: fix segfault when parsing arguments

running gps command without parameters results in segfault
due to illegal access to unallocated memory

Signed-off-by: Nicolae Rosia <nicolae.rosia@gmail.com>
### Antipattern Category

### Keyword
memory
### Note


## Commit #299
### Hash
[b781006e208b56bd23502b2bb49bdfa240317052](https://github.com/PX4/PX4-Autopilot/commit/b781006e208b56bd23502b2bb49bdfa240317052)

### Message
Increase sending of navstate and gpsfix to 2 Hz
### Antipattern Category

### Keyword
increase
### Note


## Commit #300
### Hash
[29c5c25f4712a85cad9d9eecb880ac0708f20d61](https://github.com/PX4/PX4-Autopilot/commit/29c5c25f4712a85cad9d9eecb880ac0708f20d61)

### Message
fix bug in the logging app:
- either sensor combined or the replay topic where copied into
the union buffer but at times the memory was overwritten by other
topics which updated below
- this change makes sure that the two topics are copied into the union
buffer at the correct location in the code
### Antipattern Category

### Keyword
memory
### Note


## Commit #301
### Hash
[9f5e9594f5af5b6424911f20cae20907b48ec261](https://github.com/PX4/PX4-Autopilot/commit/9f5e9594f5af5b6424911f20cae20907b48ec261)

### Message
implement ekf instance and block parameter instance as class members
in order to avoid memory management
### Antipattern Category

### Keyword
memory
### Note


## Commit #302
### Hash
[99a682e7a72f43af20003b50f2593d2d26ef1ee2](https://github.com/PX4/PX4-Autopilot/commit/99a682e7a72f43af20003b50f2593d2d26ef1ee2)

### Message
fix px4_task_spawn_cmd: memory leak, if one of the pthread_* calls fails
### Antipattern Category

### Keyword
memory
### Note


## Commit #303
### Hash
[27d821ac9ff2f14573f5e5d4e2a2932e21e4b442](https://github.com/PX4/PX4-Autopilot/commit/27d821ac9ff2f14573f5e5d4e2a2932e21e4b442)

### Message
fix position_estimator_inav_main: put terrain_estimator on the stack

This fixes a memory leak
### Antipattern Category

### Keyword
memory
### Note


## Commit #304
### Hash
[32cd154d7c479f821400a54bd2cc249934319113](https://github.com/PX4/PX4-Autopilot/commit/32cd154d7c479f821400a54bd2cc249934319113)

### Message
Revert "ESC cal: Increase timeouts"

This reverts commit d2575c25563d5731f6db0a1607d096198d32cabe.
### Antipattern Category

### Keyword
increase
### Note


## Commit #305
### Hash
[b9333d95f4a090ada153a485558162c43c0286de](https://github.com/PX4/PX4-Autopilot/commit/b9333d95f4a090ada153a485558162c43c0286de)

### Message
Navigator: Run faster
### Antipattern Category

### Keyword
faster
### Note


## Commit #306
### Hash
[ffb0d37c8a56c88e83e257b770053fe24946fc48](https://github.com/PX4/PX4-Autopilot/commit/ffb0d37c8a56c88e83e257b770053fe24946fc48)

### Message
Commander: Fix reposition handling,  run faster to allow catching of consecutive commands
### Antipattern Category

### Keyword
faster
### Note


## Commit #307
### Hash
[d3068b4337d05e2c4e7fa932ec794a5fbae271a4](https://github.com/PX4/PX4-Autopilot/commit/d3068b4337d05e2c4e7fa932ec794a5fbae271a4)

### Message
px4_task_spawn_cmd: fix memory leak on posix
### Antipattern Category

### Keyword
memory
### Note


## Commit #308
### Hash
[871c112699660a1d96f4caff42fd5e6197a20835](https://github.com/PX4/PX4-Autopilot/commit/871c112699660a1d96f4caff42fd5e6197a20835)

### Message
sdlog2: log normal data and replay on Snapdragon

In SITL and on Snapdragon, the logging performance is high enough, so we
can log both: the usual topics, as well as the ekf2 replay fields.

Note that the ekf2 replay still needs to be enabled via param.
### Antipattern Category

### Keyword
performance
### Note


## Commit #309
### Hash
[26596dbe157bf71e380b3c57f5371c5483902a2f](https://github.com/PX4/PX4-Autopilot/commit/26596dbe157bf71e380b3c57f5371c5483902a2f)

### Message
fix infinite loop when not logging
### Antipattern Category

### Keyword
infinite
### Note


## Commit #310
### Hash
[4ce658ab99992c3988422f04a1c7c56f0ea84e0a](https://github.com/PX4/PX4-Autopilot/commit/4ce658ab99992c3988422f04a1c7c56f0ea84e0a)

### Message
logger: move _writer.lock() call after write_changed_parameters()

write_changed_parameters() also takes the lock and thus would deadlock
otherwise.
### Antipattern Category

### Keyword
deadlock
### Note


## Commit #311
### Hash
[cf667dedb8b6f4f314860523627bbc5c796387ef](https://github.com/PX4/PX4-Autopilot/commit/cf667dedb8b6f4f314860523627bbc5c796387ef)

### Message
tests: increase stack size from 8000 to 9000

clang failed with:
../src/systemcmds/tests/test_mathlib.cpp:56:5: fatal error: stack frame
size of 7400 bytes in function 'test_mathlib' [-Wframe-larger-than=]
int test_mathlib(int argc, char *argv[])
### Antipattern Category

### Keyword
increase
### Note


## Commit #312
### Hash
[7a44ee7429161eb1cf5aeb2af0cf919efb55ccac](https://github.com/PX4/PX4-Autopilot/commit/7a44ee7429161eb1cf5aeb2af0cf919efb55ccac)

### Message
Added support for external shared libraries

The FC_ADDON drivers are shared libraries that have PX4 wrappers.
The wrappers are built as modules which are static libraries and
cannot have shared library dependencies.

The shared libraries are required to resolve the symbols at runtime
and need to be linked with the libmainapp shared library.

Signed-off-by: Mark Charlebois <charlebm@gmail.com>
### Antipattern Category

### Keyword
runtime
### Note


## Commit #313
### Hash
[5b1273e3348ef705abe1c56bd7c7dc035f338f60](https://github.com/PX4/PX4-Autopilot/commit/5b1273e3348ef705abe1c56bd7c7dc035f338f60)

### Message
orb: add optional queuing of messages

This adds two uORB API calls:
- orb_advertise_queue
- orb_advertise_multi_queue

Both add a queue_size parameter to define a maximum number of buffered
item. The existing orb calls use all a queue size of one and thus their
behavior is unchanged. If a writer publishes too fast, the oldest elements
from the queue are silently dropped.
The returned timestamp is always the one from the latest message in the
queue.

Queue size can be set via ioctl during advertisement phase. After that it
cannot be changed anymore.
### Antipattern Category

### Keyword
fast
### Note


## Commit #314
### Hash
[d35814ed992a0e7182a4abb71b4927391cf402e9](https://github.com/PX4/PX4-Autopilot/commit/d35814ed992a0e7182a4abb71b4927391cf402e9)

### Message
nuttx px4fmu-v4 config: increase CONFIG_NFILE_DESCRIPTORS to 52

necessary for mavlink receiver. It had the following output:
 mavlink_rcv_if0: node_open as advertiser failed.
### Antipattern Category

### Keyword
increase
### Note


## Commit #315
### Hash
[febe75bb12d8c4fc768b48847916bbf395af553b](https://github.com/PX4/PX4-Autopilot/commit/febe75bb12d8c4fc768b48847916bbf395af553b)

### Message
logger: don't use uint8_t buffer[msg_size]; (it's C99 not C++)

Also, it's not clear where the allocation was. It looks like it was on
the heap, but the compiler could decide to put it on the stack. This is
very bad for us because we use fixed size stacks with tights bounds. So if
a user specifies a large topic to log, it could have crashed.

Now the allocation is on the heap and the user can specify any size of
topic to log (as long as there is enough memory).
### Antipattern Category

### Keyword
memory
### Note


## Commit #316
### Hash
[0fb0f17ccbe44ba480000cdaff99d5d3e42053ec](https://github.com/PX4/PX4-Autopilot/commit/0fb0f17ccbe44ba480000cdaff99d5d3e42053ec)

### Message
logger: reduce memory usage, by limiting the nr of added topics to 64 (was 128)
### Antipattern Category

### Keyword
memory
### Note


## Commit #317
### Hash
[605f731ac428efcef5c5d8b7261badeb78f626e0](https://github.com/PX4/PX4-Autopilot/commit/605f731ac428efcef5c5d8b7261badeb78f626e0)

### Message
logger: reduce maximum logged string length to 128 (use less memory)
### Antipattern Category

### Keyword
memory
### Note


## Commit #318
### Hash
[f68a6eb42cde25a9c41592f5ea4975cca7464930](https://github.com/PX4/PX4-Autopilot/commit/f68a6eb42cde25a9c41592f5ea4975cca7464930)

### Message
err/px4_log: switch everything to static function

Instead of having separate log functions for NuttX and POSIX, this now
switches everything to px4_log.h and PX4_INFO/WARN/ERR/DEBUG.

Also, the call mostly used is now a static inline function instead of a
macro which lead to a big increase in flash size for STM32.
### Antipattern Category

### Keyword
increase
### Note


## Commit #319
### Hash
[f4f0892b25447d3e7a20312ebee429b4f8d06fe1](https://github.com/PX4/PX4-Autopilot/commit/f4f0892b25447d3e7a20312ebee429b4f8d06fe1)

### Message
sdlog2: no new sessXXX folder on every arm (#4775)

Previously, if no time was set, sdlog2 created a folder like sess001,

sess002 for every logfile. The logfiles would then always be named

log001.px4log and their numbering would not actually increase.



This is now fixed and a new folder is only created per boot.
### Antipattern Category

### Keyword
increase
### Note


## Commit #320
### Hash
[4ef4be2d7012231a070a65d6783949a339d8e3f7](https://github.com/PX4/PX4-Autopilot/commit/4ef4be2d7012231a070a65d6783949a339d8e3f7)

### Message
MavlinkReceiver::handle_message_request_data_stream walks into deleted memory when you send the "stop" bit on a stream.  It also fails to restart the stream because it deletes the stream when you send the stop command, so restart needs to use stream_list to find the stream again.
### Antipattern Category

### Keyword
memory
### Note


## Commit #321
### Hash
[a73ac821ab4ce909f409c99b6b6ab5e80737eb07](https://github.com/PX4/PX4-Autopilot/commit/a73ac821ab4ce909f409c99b6b6ab5e80737eb07)

### Message
Fixes shared memory locking bug and eliminates the need for an AppsProm driver to reserve a shared memory region.
### Antipattern Category

### Keyword
memory
### Note


## Commit #322
### Hash
[e7f31393bcf1bc7a96cda34cc2f31d38160b7987](https://github.com/PX4/PX4-Autopilot/commit/e7f31393bcf1bc7a96cda34cc2f31d38160b7987)

### Message
orb: reduce size of SubscriberData struct (#4771)

- priority field uses only the lower 8 bits, so we can merge with the

  update_reported flag

- orb_set_interval is not used often, so make the necessary data an

  optional pointer and alloc only when needed.



Memory savings:

- pixracer (w. ekf2): 7.3kB

- pixhawk: 5.3kB
### Antipattern Category

### Keyword
memory
### Note


## Commit #323
### Hash
[a9a3050682b55c0ab1997caa8884dcb1a369bc11](https://github.com/PX4/PX4-Autopilot/commit/a9a3050682b55c0ab1997caa8884dcb1a369bc11)

### Message
EKF2 HIL gps decrease s_variance_m_s 5.0 -> 1.0 (#4973)
### Antipattern Category

### Keyword
decrease
### Note


## Commit #324
### Hash
[5f18f9bbba75025eaff128e7f8778e2b896061dd](https://github.com/PX4/PX4-Autopilot/commit/5f18f9bbba75025eaff128e7f8778e2b896061dd)

### Message
sdlog2: select MIN < MAX bytes to write

Previously, the MAX and MIN were both 512 meaning that usually it would
start writing at > 512 bytes but only write 512 bytes which results in
a 512 bytes write shortly followed by a e.g. 30 bytes write.

Also, performance (measured in missed poll updates) seems slightly
better on Snapdragon with bigger chunks.
### Antipattern Category

### Keyword
performance
### Note


## Commit #325
### Hash
[fe91527604ef9cbe473076d50004c7991bedb96e](https://github.com/PX4/PX4-Autopilot/commit/fe91527604ef9cbe473076d50004c7991bedb96e)

### Message
sdlog2: poll for sensor and replay on Snappy

This brings better performance, so less missed updates on Snappy, as
well as a bit of a cleanup of the poll and orb_copy logic.
### Antipattern Category

### Keyword
performance
### Note


## Commit #326
### Hash
[544ea72d4c789eac77198b7d54b35db88ff54eeb](https://github.com/PX4/PX4-Autopilot/commit/544ea72d4c789eac77198b7d54b35db88ff54eeb)

### Message
Snapdragon: set CPUs scaling to performance mode

Sdlog2 misses least updates when the CPU scaling governor is set at
maximum performance. This is not optimal to save power but the best
effort until there is a RT patched kernel on Snapdragon.
### Antipattern Category

### Keyword
performance
### Note


## Commit #327
### Hash
[fa614a3cc1534c9c5f46de9d2f118ea9b4f4e8e4](https://github.com/PX4/PX4-Autopilot/commit/fa614a3cc1534c9c5f46de9d2f118ea9b4f4e8e4)

### Message
RPi: just use RPI instead of RPI2.

The reason for this change is that RPi2 and RPi3 are compatible, and
hopefully all differences coming up can be resolved without ifdefs but
at runtime.
### Antipattern Category

### Keyword
runtime
### Note


## Commit #328
### Hash
[302719527a4213893f094e66be2f7c650eaa3e6e](https://github.com/PX4/PX4-Autopilot/commit/302719527a4213893f094e66be2f7c650eaa3e6e)

### Message
nuttx defconfig: increase nr of file descriptors, due to mavlink shell
### Antipattern Category

### Keyword
increase
### Note


## Commit #329
### Hash
[e287b05d678589650f7e6423dae351f72f006290](https://github.com/PX4/PX4-Autopilot/commit/e287b05d678589650f7e6423dae351f72f006290)

### Message
NuttX: Add file change which allows really fast log download
### Antipattern Category

### Keyword
fast
### Note


## Commit #330
### Hash
[d748f6ca710139fde08107da96c7a24df3c2d165](https://github.com/PX4/PX4-Autopilot/commit/d748f6ca710139fde08107da96c7a24df3c2d165)

### Message
attitude_estimator_q: filter accel and gyro data

Since accel and gyro are not filtered in the drivers anymore, we need to
filter them in this estimator in order to achieve a similar performance.
### Antipattern Category

### Keyword
performance
### Note


## Commit #331
### Hash
[ea9c8b968a45734e418dbade866dfe6221718b06](https://github.com/PX4/PX4-Autopilot/commit/ea9c8b968a45734e418dbade866dfe6221718b06)

### Message
attitude_estimator_q: don't spam console

We should not spam the console just because the input data is
degenerate, it would only make things worse because everything would
slow down due to the printfs.
### Antipattern Category

### Keyword
slow
### Note


## Commit #332
### Hash
[db174cf8b1b108b864724a8448dba80f2440f357](https://github.com/PX4/PX4-Autopilot/commit/db174cf8b1b108b864724a8448dba80f2440f357)

### Message
Disable EKF2 3D fusion temporarily in SITL, fix missing fast-init params for some configs
### Antipattern Category

### Keyword
fast
### Note


## Commit #333
### Hash
[17561daefb4295ec8bf90355ed806c382fd9bede](https://github.com/PX4/PX4-Autopilot/commit/17561daefb4295ec8bf90355ed806c382fd9bede)

### Message
TAP power: Shut down faster
### Antipattern Category

### Keyword
faster
### Note


## Commit #334
### Hash
[eceb7e21b2cad7bc892c7b594103bcddf1c96350](https://github.com/PX4/PX4-Autopilot/commit/eceb7e21b2cad7bc892c7b594103bcddf1c96350)

### Message
Include memory in CPU load message
### Antipattern Category

### Keyword
memory
### Note


## Commit #335
### Hash
[8934aaa9124f9384be918f0d6b9fc66e7b688666](https://github.com/PX4/PX4-Autopilot/commit/8934aaa9124f9384be918f0d6b9fc66e7b688666)

### Message
Load mon: populate memory usage i field for NuttX
### Antipattern Category

### Keyword
memory
### Note


## Commit #336
### Hash
[1a9688c42f096d4e029390b20c94beaea4c6e6a5](https://github.com/PX4/PX4-Autopilot/commit/1a9688c42f096d4e029390b20c94beaea4c6e6a5)

### Message
Commander: signal high memory usage
### Antipattern Category

### Keyword
memory
### Note


## Commit #337
### Hash
[5786b737720581c1a20616ed252b26f038b9b762](https://github.com/PX4/PX4-Autopilot/commit/5786b737720581c1a20616ed252b26f038b9b762)

### Message
Tweak startup order for memory
### Antipattern Category

### Keyword
memory
### Note


## Commit #338
### Hash
[7cc0b32e74e5b45f50cd8b276769889015773bdb](https://github.com/PX4/PX4-Autopilot/commit/7cc0b32e74e5b45f50cd8b276769889015773bdb)

### Message
Make altitude more efficient and estimator status safe in terms of memory overflow
### Antipattern Category

### Keyword
memory
### Note


## Commit #339
### Hash
[a7ad722b980165e16020798a7e1a0faea9cfbae6](https://github.com/PX4/PX4-Autopilot/commit/a7ad722b980165e16020798a7e1a0faea9cfbae6)

### Message
Use less memory for ESC driver
### Antipattern Category

### Keyword
memory
### Note


## Commit #340
### Hash
[d810726c6ea53a85dfae9740f6d56b13d7bf5937](https://github.com/PX4/PX4-Autopilot/commit/d810726c6ea53a85dfae9740f6d56b13d7bf5937)

### Message
EKF2: Only use the memory it needs
### Antipattern Category

### Keyword
memory
### Note


## Commit #341
### Hash
[39ce001c41249f5b8725686fff707df22e75f0ce](https://github.com/PX4/PX4-Autopilot/commit/39ce001c41249f5b8725686fff707df22e75f0ce)

### Message
MAVLink: use only the memory it needs
### Antipattern Category

### Keyword
memory
### Note


## Commit #342
### Hash
[6b4c24fb125f6842b169cb7f108451e0a3e5a166](https://github.com/PX4/PX4-Autopilot/commit/6b4c24fb125f6842b169cb7f108451e0a3e5a166)

### Message
px4_log: remove __px4_log_level_current

- there is no way to change it at runtime
- it was implemented wrong (<= comparison disabled the PANIC log level)
### Antipattern Category

### Keyword
runtime
### Note


## Commit #343
### Hash
[5a734de3196bc773c92b26b9f660a838cab8f1a2](https://github.com/PX4/PX4-Autopilot/commit/5a734de3196bc773c92b26b9f660a838cab8f1a2)

### Message
Commander: Increase stack space
### Antipattern Category

### Keyword
increase
### Note


## Commit #344
### Hash
[cc69dd566546a16ca4c3fe48bfcbf7541d721d42](https://github.com/PX4/PX4-Autopilot/commit/cc69dd566546a16ca4c3fe48bfcbf7541d721d42)

### Message
printf format fixes. (#5444)

After I got a compiler warning for a printf format in this file

(which I cannot reproduce anymore; for some reason g++ is usually

quite happy with all the errors in this file), I fixed all 'printf'

formats to match the type of their arguments as follows:



uint8_t         : %hhu

uint16_t        : %hu (or %hx)

uint32_t        : %u (or %x)

int16_t         : %hd

int and int32_t : %d

long int        : %ld



Since this file is C++, what we REALLY should be using is

ostream operator<<'s of course (type safe by design and faster

(compile time type matching, no need for format decoding)).
### Antipattern Category

### Keyword
faster
### Note


## Commit #345
### Hash
[4a5eae23a29d452596ee0c8d0961f661ae635214](https://github.com/PX4/PX4-Autopilot/commit/4a5eae23a29d452596ee0c8d0961f661ae635214)

### Message
Increase stack space on posix 64bit architectures. (#5447)

When running a simulation with, for example,

make posix jmavsim

px4 crashed almost 100% reproducable near start up.



This turned out to be a stack overflow. On gitter

it was suggested that the main reason for this could

be stack sizes, as currently used, assume a 32bit pointer

size and that doubling the stack size for everything

but NuttX would be the Right Thing.



This is the solution that I came up with (it makes

my core dumps disappear).
### Antipattern Category

### Keyword
increase
### Note


## Commit #346
### Hash
[3f07b03911fa197e2dc996a5270b8b823c60a528](https://github.com/PX4/PX4-Autopilot/commit/3f07b03911fa197e2dc996a5270b8b823c60a528)

### Message
SITL: Tune standard VTOL to have better position control performance & update gazebo
### Antipattern Category

### Keyword
performance
### Note


## Commit #347
### Hash
[cbbf5e2e7c550f3c18c1e794d549bd5a9b0410cc](https://github.com/PX4/PX4-Autopilot/commit/cbbf5e2e7c550f3c18c1e794d549bd5a9b0410cc)

### Message
filtering files for code check seperately to enable fast use of git pre-commit hook to check code style
ask user to install pre-commit hook when code style is checked
### Antipattern Category

### Keyword
fast
### Note


## Commit #348
### Hash
[937f3477d3c384e62a499150338dcfba0e46556a](https://github.com/PX4/PX4-Autopilot/commit/937f3477d3c384e62a499150338dcfba0e46556a)

### Message
Syslink memory/deck interface
### Antipattern Category

### Keyword
memory
### Note


## Commit #349
### Hash
[69f6708f37107575f66fe43a2e7261348395ed5e](https://github.com/PX4/PX4-Autopilot/commit/69f6708f37107575f66fe43a2e7261348395ed5e)

### Message
Increase sensors stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #350
### Hash
[f25947b964f31eb55e8f836077bad59973486eef](https://github.com/PX4/PX4-Autopilot/commit/f25947b964f31eb55e8f836077bad59973486eef)

### Message
hrt_work_queue posix: only send a wake-up signal if not called from own thread

The simulated timer interrupt always adds a new scheduled work task, which
is called from the work queue thread. Sending the signal creates measurable
overhead (~5% of the px4 CPU runtime) and is unnecessary, since the thread
is not sleeping anyway.
### Antipattern Category

### Keyword
runtime
### Note


## Commit #351
### Hash
[b864983c5e558eab04aaa519025e0e8c1ddacb1c](https://github.com/PX4/PX4-Autopilot/commit/b864983c5e558eab04aaa519025e0e8c1ddacb1c)

### Message
navio_sysfs_rc_in: avoid dynamic memory allocation for path
### Antipattern Category
General:Hard-coding
### Keyword
memory
### Note
Path array size changed from dynamic allocation to the fixed value of 64.

## Commit #352
### Hash
[bad107a374d297b1c76f23cd6b99c4a8ac2fcb19](https://github.com/PX4/PX4-Autopilot/commit/bad107a374d297b1c76f23cd6b99c4a8ac2fcb19)

### Message
navio_sysfs_pwm_out: avoid dynamic memory allocation & fix a memory leak

memory leak was in send_outputs_pwm()
### Antipattern Category
General:Hard-coding, General:C:not_deallocating
### Keyword
memory
### Note
Arrays size changed from dynamic allocation to fixed values, 1 array was never deallocated.
Issue: Navio drivers: avoid dynamic allocations #5606


## Commit #353
### Hash
[605cffc230c944a215ba70fc0252cff44135ab29](https://github.com/PX4/PX4-Autopilot/commit/605cffc230c944a215ba70fc0252cff44135ab29)

### Message
Fix sensor rail reset on Pixracer. Increase the reset duration to 50 ms to ensure the sensor power has bled off.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Sensor reset time increased.

## Commit #354
### Hash
[ed6295747441fa63ce3e72d590ed408d295fe5c7](https://github.com/PX4/PX4-Autopilot/commit/ed6295747441fa63ce3e72d590ed408d295fe5c7)

### Message
Increase RC buffer size
### Antipattern Category
New:Fixed-communication-rate
### Keyword
increase
### Note
Buffer size for RC doubled in the Flight Management Unit.

## Commit #355
### Hash
[0f763768b137922b4664fdcb37f6716407c118af](https://github.com/PX4/PX4-Autopilot/commit/0f763768b137922b4664fdcb37f6716407c118af)

### Message
commander: don't auto-disarm as fast if not flown

It was found inconvenient that auto-disarm triggers too quickly right
after arming when the vehicle has not actually taken off yet.

Therefore, the auto-disarm takes now by a factor of 5 longer if the
vehicle has not taken off yet.
### Antipattern Category
New:Hard-coded-timing
### Keyword
fast
### Note
Auto-disarm timeout time is increased by a factor of 5.

## Commit #356
### Hash
[e73218c112e1bb1be84f9ca47a4001a584fef1d8](https://github.com/PX4/PX4-Autopilot/commit/e73218c112e1bb1be84f9ca47a4001a584fef1d8)

### Message
Increase min agl for flow from 5 to 30 cm to prevent drift on ground.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Flow agl changed from 5 to 30.
minumum above ground level (AGL) has been changed in PX4FLOW sensor.

## Commit #357
### Hash
[44b5b52bcbf01c548a30c8dddd5c477c9ce86cb7](https://github.com/PX4/PX4-Autopilot/commit/44b5b52bcbf01c548a30c8dddd5c477c9ce86cb7)

### Message
Add suport for Memory Constrained systems
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
memory
### Note
Constraints applied for systems with limited memory.

## Commit #358
### Hash
[b1e94b98b3154a5a37f92b8cdd585b9209fc7919](https://github.com/PX4/PX4-Autopilot/commit/b1e94b98b3154a5a37f92b8cdd585b9209fc7919)

### Message
Define tap as a Memory Constrained system
### Antipattern Category
X
### Keyword
memory
### Note
Commit sets a new variable within cmake file.

## Commit #359
### Hash
[ffaed18e679e7eb780518d4c2ec42d1f1747d451](https://github.com/PX4/PX4-Autopilot/commit/ffaed18e679e7eb780518d4c2ec42d1f1747d451)

### Message
Reduce the binary size Bebop

The firmware binary is to large to fit into the onboard memory of the Parrot
Bebop. It could be uploaded to the emmc, but for ease of use it would be nice
to have it in /usr/bin. To strip the binary seems to be the best option right now.
### Antipattern Category
X
### Keyword
memory
### Note
Not an anti-pattern.

## Commit #360
### Hash
[8e0d548f51d433a472dfc4ba1f655df3e766c302](https://github.com/PX4/PX4-Autopilot/commit/8e0d548f51d433a472dfc4ba1f655df3e766c302)

### Message
logger: increase default queue size for mavlink logging to 14

tested on Pixracer: 14 still produces some dropouts once in a while, but I
think it's a fair tradefoff between RAM usage & dropouts. The queue needs
about 3.5KB of RAM.

When topic sizes/logging rates change, this will have to be reevaluated.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Size of queue for mavlink polling increased.

## Commit #361
### Hash
[326800e5a8b3e2057590946f29c7a809d4feef59](https://github.com/PX4/PX4-Autopilot/commit/326800e5a8b3e2057590946f29c7a809d4feef59)

### Message
logger: increase stack size

evaluated with: logger start -e -t -m all
and then make sure to get an error printf in the mavlink writer backend,
eg. for an ack timeout.
### Antipattern Category
New:Hard-coded-fine-tuning

### Keyword
increase
### Note
Stack size increased from 3200 to 3800.

## Commit #362
### Hash
[bdfb2bbb8d3655c84dc95702a4948a25e63bc750](https://github.com/PX4/PX4-Autopilot/commit/bdfb2bbb8d3655c84dc95702a4948a25e63bc750)

### Message
Fixed hardfault on fast proc

_baro_topic can be null in init sequence
   init call collect before the topic is inited.

I think this pattern is repeated in other drivers. I would suggest
allowing null in orb_publish to just return.
### Antipattern Category
X
### Keyword
fast
### Note
Null check for baro_topic at init.

## Commit #363
### Hash
[3a332bb11a3f0e367a261a0f9a19a33520f93cce](https://github.com/PX4/PX4-Autopilot/commit/3a332bb11a3f0e367a261a0f9a19a33520f93cce)

### Message
Printing all online nodes within UAVCAN status output. This feature increased memory footprint by about 150 bytes.
### Antipattern Category
X
### Keyword
memory
### Note
The original code does not show any performance antipattern. 

## Commit #364
### Hash
[5899ce715dcfd946fed62e654a472ca72b40d64c](https://github.com/PX4/PX4-Autopilot/commit/5899ce715dcfd946fed62e654a472ca72b40d64c)

### Message
Navigator: Leverage overlapping fields in logic to save RAM by makeing them overlap in memory as well
### Antipattern Category
X
### Keyword
memory
### Note
The original code does not show any performance antipattern. 


## Commit #365
### Hash
[d0dace7c23b862f6a28e966b5d0dc522bbd777b0](https://github.com/PX4/PX4-Autopilot/commit/d0dace7c23b862f6a28e966b5d0dc522bbd777b0)

### Message
uavcan: use math::min instead of std::min

Avoid including <memory> which can cause problems on NuttX
### Antipattern Category
X
### Keyword
memory
### Note
The original code does not show any performance antipattern. 

## Commit #366
### Hash
[25be7aa7cf30b633afd1abeb30f15547719f1471](https://github.com/PX4/PX4-Autopilot/commit/25be7aa7cf30b633afd1abeb30f15547719f1471)

### Message
incorporate Bill Premerlani's fast rotation handling from MatrixPilot
### Antipattern Category
X
### Keyword
fast
### Note
Logic changed, not an anti-pattern.

## Commit #367
### Hash
[ab43baa02d8e6f0f0b2cc6ae65647ecc2c6bfb1a](https://github.com/PX4/PX4-Autopilot/commit/ab43baa02d8e6f0f0b2cc6ae65647ecc2c6bfb1a)

### Message
Clean up Crazyflie
   1) Remove uneeded spi and reset code
   2) Use the Board commin for providing the BOARD_NAME
   3) Add PX4_PWM_ALTERNATE_RANGES in suport of a board agnostic
      way to override the PWM_.*_{MIN|MAX} values
   4) Remove #ifdefs from the IO timers*. Drive the config deltas
      from the crazyflie_timer_config.c and one board agnostic
      ifdef PX4_IO_TIMER_ALTERNATE_RATE that is non board specific

      *I would like to eliminate PX4_IO_TIMER_ALTERNATE_RATE
      as well, but I need HW to validate that the startup
      script can just set the rate on the PWM to 3921 fast
      enough to not effect the motors.
### Antipattern Category
X
### Keyword
fast
### Note
The original code does not show any performance antipattern. 

## Commit #368
### Hash
[2d451991af7b3a0b1f3b2e683bfd53d1c94e1ceb](https://github.com/PX4/PX4-Autopilot/commit/2d451991af7b3a0b1f3b2e683bfd53d1c94e1ceb)

### Message
PX4 System change to Remove #ifdefs from the IO timers

   Update the comment, to explain how to achive a different perescale
   value.

   Added PX4_IO_TIMER_ALTERNATE_RATE one board agnostic ifdef
   PX4_IO_TIMER_ALTERNATE_RATE that is non board specific.

   N.B.  I would like to eliminate PX4_IO_TIMER_ALTERNATE_RATE
   as well, but I need crazyflie HW to validate that the startup
   script can just set the rate on the PWM to 3921 fast enough to
   not effect the motors.
### Antipattern Category
X
### Keyword
fast
### Note
The original code does not show any performance antipattern. 

## Commit #369
### Hash
[ef7ed97cbd1b91ed88c2792984d72f0fa08035fc](https://github.com/PX4/PX4-Autopilot/commit/ef7ed97cbd1b91ed88c2792984d72f0fa08035fc)

### Message
ekf2: Don't send un-usable mag and baro data to the EKF

Fixes:

1) Invalid data with a zero time stamp could be the EKF ends up in the data buffers and result in loss of 'good' data from the buffers

2) Magnetometer data was arriving at a rate faster than the data buffers could handle resulting in loss of data.
### Antipattern Category
New:Fixed-communication-rate
### Keyword
faster
### Note
Magnetometer data is accumulated and the average is pushed if it arrives in an interval <50 ms.

## Commit #370
### Hash
[14fd1b869380f6bf0420e8e3db7cf1aad8f7107a](https://github.com/PX4/PX4-Autopilot/commit/14fd1b869380f6bf0420e8e3db7cf1aad8f7107a)

### Message
ulog_stream_ack.msg: lower timeout & increase max retries

We expect a short round-trip time, so lowering the retry timeout will
increase throughput on links with high drop rate.
### Antipattern Category
New:Fixed-communication-rate, New:Hard-coded-fine-tuning
### Keyword
increase
### Note
ACK_TIMEOUT is the waiting time for an ack until we retry to send the message [ms]
ACK_MAX_TRIES maximum amount of tries to (re-)send a message, each time waiting ACK_TIMEOUT ms
ACK_TIMEOUT lowered and ACK_MAX_TRIES increased. Still on main version.

## Commit #371
### Hash
[0eadf26d341e6d62bab4790c1cc24e09d869133a](https://github.com/PX4/PX4-Autopilot/commit/0eadf26d341e6d62bab4790c1cc24e09d869133a)

### Message
Log download: fix memory leak in generating the list
### Antipattern Category
General:C:not_deallocating
### Keyword
memory
### Note
File not deallocated fix.

## Commit #372
### Hash
[92a5db92a2ece6a1317fa4b1ca347d1b1e08e967](https://github.com/PX4/PX4-Autopilot/commit/92a5db92a2ece6a1317fa4b1ca347d1b1e08e967)

### Message
vtol_att_control: initialise pointers and free memory

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category
General:C:not_deallocating
### Keyword
memory
### Note
Variable not deallocated fix. Issue: Pr vtol params #5892, aimed to fix a memory leak and constant updates of variables that drastically increased CPU usage.

## Commit #373
### Hash
[b020be13f67838047d1c2532cf66a99ceb28cddf](https://github.com/PX4/PX4-Autopilot/commit/b020be13f67838047d1c2532cf66a99ceb28cddf)

### Message
flashparams: fix memory leak when saving parameters

A large buffer on the heap was not deallocated when parameters were saved,
but there were no changes to the parameters. In that case
parameter_flashfs_write() was not called, which was previously responsible
for freeing the buffer.

This patch moves the responsibility of freeing the buffer to the calling
side, which already explicitly allocates the buffer.
### Antipattern Category
General:C:not_deallocating
### Keyword
memory
### Note
Issue: flashparams: fix memory leak when saving parameters #5923.

## Commit #374
### Hash
[e3537ca6c25ba50b8c0665138a1d833861b1b5f7](https://github.com/PX4/PX4-Autopilot/commit/e3537ca6c25ba50b8c0665138a1d833861b1b5f7)

### Message
px4fmu rcS: increase mavlink rate to 100000 for SYS_COMPANION 1500000

Needed for log streaming
### Antipattern Category
New:Hard-coded-fine-tuning, New:Fixed-communication-rate
### Keyword
increase
### Note
Issue: Intel aero: config updates #5977
Commit reverted 2 weeks later.

## Commit #375
### Hash
[b0ee5256d5ea0f40fe4e3dded9be27bbc3ffa871](https://github.com/PX4/PX4-Autopilot/commit/b0ee5256d5ea0f40fe4e3dded9be27bbc3ffa871)

### Message
Disable LPE in px4fmu-v2_default

With GCC 4.9 the binary is to large for the flash memory.
This is why we disabled LPE on that platform.
### Antipattern Category
X
### Keyword
memory
### Note
The original code does not show any performance antipattern. 

## Commit #376
### Hash
[dda0de09dd2be851bc2b70c0b897a801d55b8863](https://github.com/PX4/PX4-Autopilot/commit/dda0de09dd2be851bc2b70c0b897a801d55b8863)

### Message
Load monitor: optimize performance of stack checking
### Antipattern Category
Smith:General:Unnecessary_Processing
### Keyword
performance
### Note
Issue: Log tasks low on stack #5891.


## Commit #377
### Hash
[a0cf938ced797e4ce12afe68666316acb3a4add7](https://github.com/PX4/PX4-Autopilot/commit/a0cf938ced797e4ce12afe68666316acb3a4add7)

### Message
Load monitor: lock scheduler for stack check and added performance counter for stack checking
### Antipattern Category
Unnecessary_processing
### Keyword
performance
### Note
Issue: Log tasks low on stack #5891.


## Commit #378
### Hash
[6a6e9d02a312bad94cd164ff7928336472576fec](https://github.com/PX4/PX4-Autopilot/commit/6a6e9d02a312bad94cd164ff7928336472576fec)

### Message
navigator: increase stack

The stack size was generally ok but seemed to get exhausted in the case
of a waypoint which is too far away and therefore exercises some more
code in the mission feasability checker.

Generally, we should have more margin in the navigator stack size
because there are a bunch of different code paths that can happen.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Commit was reverted later.

## Commit #379
### Hash
[a096b974558347c31692a605e14344ad624332b8](https://github.com/PX4/PX4-Autopilot/commit/a096b974558347c31692a605e14344ad624332b8)

### Message
Revert "navigator: increase stack"

This reverts commit 6a6e9d02a312bad94cd164ff7928336472576fec.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Issue: Fix matrix submodule #6063. Revert of commit #379.

## Commit #380
### Hash
[3ac056924ce508288fc34050ee44fc27a6ed7ae8](https://github.com/PX4/PX4-Autopilot/commit/3ac056924ce508288fc34050ee44fc27a6ed7ae8)

### Message
navigator: increase stack
The stack size was generally ok but seemed to get exhausted in the case
of a waypoint which is too far away and therefore exercises some more
code in the mission feasability checker.

Generally, we should have more margin in the navigator stack size
because there are a bunch of different code paths that can happen.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note

Issue: Fix matrix submodule #6063. Commit #378.

## Commit #381
### Hash
[daa88f69dbcdd8629044b4b318929cd4b408ca18](https://github.com/PX4/PX4-Autopilot/commit/daa88f69dbcdd8629044b4b318929cd4b408ca18)

### Message
bebop2 config: updated some positon control params for decent performance

- this is not the final tune!!!

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category

### Keyword
performance
### Note


## Commit #382
### Hash
[d0d9ee373b9eee712a631a1f1e5bb923bdc30e44](https://github.com/PX4/PX4-Autopilot/commit/d0d9ee373b9eee712a631a1f1e5bb923bdc30e44)

### Message
bebop config: increase logger buffer from 20kB to 200kB

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #383
### Hash
[df613361b93f9e17465383fde3b0aba4df47cf0d](https://github.com/PX4/PX4-Autopilot/commit/df613361b93f9e17465383fde3b0aba4df47cf0d)

### Message
LPE: Increase stack to allow enough safe margin
### Antipattern Category

### Keyword
increase
### Note


## Commit #384
### Hash
[cc7db94edc8bde68251e9fb2e1a8f9d865b23e5a](https://github.com/PX4/PX4-Autopilot/commit/cc7db94edc8bde68251e9fb2e1a8f9d865b23e5a)

### Message
Sensors app mag voter: Increase stale value detection threshold to accomodate low-noise mag setups
### Antipattern Category

### Keyword
increase
### Note


## Commit #385
### Hash
[5759fd5726fc40cc4bb49d06f266d428fdacd6f7](https://github.com/PX4/PX4-Autopilot/commit/5759fd5726fc40cc4bb49d06f266d428fdacd6f7)

### Message
GPS app: Increase stack to ensure 300 bytes headroom
### Antipattern Category

### Keyword
increase
### Note


## Commit #386
### Hash
[292599d3c9098b56e4a46433325d870af4b9ed45](https://github.com/PX4/PX4-Autopilot/commit/292599d3c9098b56e4a46433325d870af4b9ed45)

### Message
Revert "px4fmu rcS: increase mavlink rate to 100000 for SYS_COMPANION 1500000"

This reverts commit e3537ca6c25ba50b8c0665138a1d833861b1b5f7.

It needs changes on the Linux side, so reverting for now.
### Antipattern Category

### Keyword
increase
### Note


## Commit #387
### Hash
[c38e378f59a2f0589f17ab2d83c02bf34ef55c7c](https://github.com/PX4/PX4-Autopilot/commit/c38e378f59a2f0589f17ab2d83c02bf34ef55c7c)

### Message
bebop config: updated some gains for decent performance

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category

### Keyword
performance
### Note


## Commit #388
### Hash
[e15b67ff7035666049831e83c39b445f086e3d16](https://github.com/PX4/PX4-Autopilot/commit/e15b67ff7035666049831e83c39b445f086e3d16)

### Message
HOTFIX:For Data loss on Nuttx serial w/ DMA &  GPIO Flow Control

   This hot fix essentialy revert commit 265af481209d60033f7cd4c4216048b1ce3eb435
   in NuttX/nuttx. The commit STM32 serial: Make input hardware flow-control work with RX DMA.
   From Jussi Kivilinna has broken the DMA on an STM32F4 in a yet TBD way.
   The symptoms are lost data on RX, the DMA count decrements but
   the data ia not written to memory. This looks to be introduced but the
   non circular DMA settings.
### Antipattern Category

### Keyword
memory
### Note


## Commit #389
### Hash
[737e18dccb8d065c536e4384ee967ad90c422330](https://github.com/PX4/PX4-Autopilot/commit/737e18dccb8d065c536e4384ee967ad90c422330)

### Message
MAVLink app: Fix VTOL reporting and prevent mission reached spam

The VTOL status reporting and the mission status reporting were both suboptimal. VTOL was too slow, mission reporting too fast
### Antipattern Category

### Keyword
slow
### Note


## Commit #390
### Hash
[1141079a3b50f18d30e80716fa8e1be26184fb9b](https://github.com/PX4/PX4-Autopilot/commit/1141079a3b50f18d30e80716fa8e1be26184fb9b)

### Message
Fix Simulator: Set correct rotor count for standard VTOL

The rotor count was incorrect which meant that control surfaces like elevons were scaled incorrectly. This was the main reason for really bad SITL performance
### Antipattern Category

### Keyword
performance
### Note


## Commit #391
### Hash
[d5082251d95fc1aa3499135d836bab255fb6d9e9](https://github.com/PX4/PX4-Autopilot/commit/d5082251d95fc1aa3499135d836bab255fb6d9e9)

### Message
controllib decrease blockNameLengthMax to 40
### Antipattern Category

### Keyword
decrease
### Note


## Commit #392
### Hash
[eac6dfed3cbc4228501a681697aa2ecf74217ebd](https://github.com/PX4/PX4-Autopilot/commit/eac6dfed3cbc4228501a681697aa2ecf74217ebd)

### Message
mc_att_control: Sync attitude loops to gyro data

Sync the attitude controller to the raw gyro data to remove the latency in the rate loops caused by the sensor and estimator modules.
Attitude data latency will increase as it will be from the previous EKF update, however attitude loops are less latency sensitive.
Thermal compensation and bias data will be from the previous frame.
### Antipattern Category

### Keyword
increase
### Note


## Commit #393
### Hash
[f6f145cbe8adddc26d259f0a7373066e7a4cd817](https://github.com/PX4/PX4-Autopilot/commit/f6f145cbe8adddc26d259f0a7373066e7a4cd817)

### Message
sensors & mc_att_control: increase stack sizes due to recent changes
### Antipattern Category

### Keyword
increase
### Note


## Commit #394
### Hash
[1beb2911e242d02097cf55cadb95a259112aaf7f](https://github.com/PX4/PX4-Autopilot/commit/1beb2911e242d02097cf55cadb95a259112aaf7f)

### Message
init shmem early to avoid random crash in fastrpc (#6407)

* init shmem early to avoid possible crash



* fix_code_style



* Keep the initialziation to NULL, remove the duplicate memory allocation
### Antipattern Category

### Keyword
memory
### Note


## Commit #395
### Hash
[72ea5c53dbcbfd6c1492c15c7b57d633cac0e4bc](https://github.com/PX4/PX4-Autopilot/commit/72ea5c53dbcbfd6c1492c15c7b57d633cac0e4bc)

### Message
qurt px4_layer initialize shared memory (#6453)
### Antipattern Category

### Keyword
memory
### Note


## Commit #396
### Hash
[7e5f09f40871b8b2bfc02a2849a201fa2e690d8b](https://github.com/PX4/PX4-Autopilot/commit/7e5f09f40871b8b2bfc02a2849a201fa2e690d8b)

### Message
clang-tidy performance-unnecessary-value-param
### Antipattern Category

### Keyword
performance
### Note


## Commit #397
### Hash
[6f05fec335e810884097912afc28a79f248e2a47](https://github.com/PX4/PX4-Autopilot/commit/6f05fec335e810884097912afc28a79f248e2a47)

### Message
clang-tidy performance-unnecessary-copy-initialization
### Antipattern Category

### Keyword
performance
### Note


## Commit #398
### Hash
[c559f195eca9a0fd565825172bfd6e54586befea](https://github.com/PX4/PX4-Autopilot/commit/c559f195eca9a0fd565825172bfd6e54586befea)

### Message
land_detector: Hotfix to prevent ground contact detection when descending velocity is very slow with manual stick all the way down
Now the stick down check is only done in manual control and the thrust low is again mandatory to detect ground in any case.
### Antipattern Category

### Keyword
slow
### Note


## Commit #399
### Hash
[48e7b941620efdac1f73fa7bcdcdd3e136a47cba](https://github.com/PX4/PX4-Autopilot/commit/48e7b941620efdac1f73fa7bcdcdd3e136a47cba)

### Message
mavlink : track time offset faster
### Antipattern Category

### Keyword
faster
### Note


## Commit #400
### Hash
[df8f0da70c85039b0e0986e023c9e7753472645d](https://github.com/PX4/PX4-Autopilot/commit/df8f0da70c85039b0e0986e023c9e7753472645d)

### Message
param & param_shmem: enable locking

We need to protect access to the param_values array. This is dynamically
allocated and resized (utarray_reserve() calls realloc). If some thread
was iterating the array while another was resizing the array, the first one
would iterate on a freed array, thus accessing invalid memory.

On NuttX this could lead to hardfaults in rare conditions.

Unfortunately we need to initialize the semaphore on startup, by calling
sem_init(). This adds a param_init() method called by every board/config
that uses the params (at least I think I've found all of them)
### Antipattern Category

### Keyword
memory
### Note


## Commit #401
### Hash
[7659402fdb974b8a5b9acc2b9f8a3fcc8d69b370](https://github.com/PX4/PX4-Autopilot/commit/7659402fdb974b8a5b9acc2b9f8a3fcc8d69b370)

### Message
WIP: valgrind runtime analysis and fixes (#6521)

* Fix several valgrind identified mem leaks



* Added callgrind target.



* px4_posix_tasks use nullptr
### Antipattern Category

### Keyword
runtime
### Note


## Commit #402
### Hash
[51c8e905085cab9fe73f204b0fcdd0c43130c7a2](https://github.com/PX4/PX4-Autopilot/commit/51c8e905085cab9fe73f204b0fcdd0c43130c7a2)

### Message
FW att control: Increase stack size to ensure limits
### Antipattern Category

### Keyword
increase
### Note


## Commit #403
### Hash
[2f3b1edbd4ff1ef678028da8c04f20d858db363c](https://github.com/PX4/PX4-Autopilot/commit/2f3b1edbd4ff1ef678028da8c04f20d858db363c)

### Message
Convergence: increase yaw output in mixer
### Antipattern Category

### Keyword
increase
### Note


## Commit #404
### Hash
[4ddc7e22fb11bbf041b07f13adce89dcad2a5617](https://github.com/PX4/PX4-Autopilot/commit/4ddc7e22fb11bbf041b07f13adce89dcad2a5617)

### Message
MC pos ctrl: Force slow landing speed below min loiter altitude
### Antipattern Category

### Keyword
slow
### Note


## Commit #405
### Hash
[b1c11b14a86a1200aeb1f058b0eb9eaa7bc87bfb](https://github.com/PX4/PX4-Autopilot/commit/b1c11b14a86a1200aeb1f058b0eb9eaa7bc87bfb)

### Message
ROMFS: common: AeroFC: Do not start MAVLink over USB

STM32 pins are not exposed in AeroFC, so lets save some memory here.
### Antipattern Category

### Keyword
memory
### Note


## Commit #406
### Hash
[ef228b82aaca18d280d4a6fafd8a6f7747631dd0](https://github.com/PX4/PX4-Autopilot/commit/ef228b82aaca18d280d4a6fafd8a6f7747631dd0)

### Message
boards: AeroFC: Make it a memory constrained system

The maximum number of missions was increased in almost 8 times in
recent commit: 9369262e63 navigator: allow more mission items.

As this board loads missions in RAM, now it don't have enough memory
to allocate causing dataman start to fail, so mark it as a memory
constrained system and reduce the number of maximum missions
supported.
### Antipattern Category

### Keyword
memory
### Note


## Commit #407
### Hash
[cfa84954ea64995e1beaf3630041f77a569892d3](https://github.com/PX4/PX4-Autopilot/commit/cfa84954ea64995e1beaf3630041f77a569892d3)

### Message
param_get: add null-pointer check

If param_find() returned PARAM_INVALID, and this was directly passed to
param_get(), param_get_value_ptr() returned null and we read garbage data
(or segfaulted on systems with virtual memory).
On px4fmu-v2, this happened for the param ATT_VIBE_THRESH in sensors.
Because of the recently added parameter scoping, this param got pruned, as
it's defined in attitude_estimator_q.

credits for finding this go to Jeyong Shin (jeyong).
### Antipattern Category

### Keyword
memory
### Note


## Commit #408
### Hash
[54c8e3b26b50d66a5adc95a4f7295e7c2f19d2f9](https://github.com/PX4/PX4-Autopilot/commit/54c8e3b26b50d66a5adc95a4f7295e7c2f19d2f9)

### Message
commander: fix excessive orb_advertise calls for vehicle_status_flags

vehicle_status_flags_pub passed to publish_status_flags() was always null,
thus orb_advertise() was called each time.

Note that it did not produce a memory leak.
### Antipattern Category

### Keyword
memory
### Note


## Commit #409
### Hash
[2220c3a60d622fbd3c48b47cfc4f92f95638e92c](https://github.com/PX4/PX4-Autopilot/commit/2220c3a60d622fbd3c48b47cfc4f92f95638e92c)

### Message
ekf2: use sensors timestamp for published topics when in replay mode

when doing fast replay, hrt_absolute_time() will not match the replayed time
thus we just use the same timestamp as the input sensors.
### Antipattern Category

### Keyword
fast
### Note


## Commit #410
### Hash
[1d93b1bce300e5d3b180380d4ca8fa7883fe66f8](https://github.com/PX4/PX4-Autopilot/commit/1d93b1bce300e5d3b180380d4ca8fa7883fe66f8)

### Message
nuttx configs: increase CONFIG_NFILE_DESCRIPTORS from 51 to 53

this is needed due to the additional topics logged with the logger
### Antipattern Category

### Keyword
increase
### Note


## Commit #411
### Hash
[bc91005e7aef64ca5e89f72baceee7128678f1d3](https://github.com/PX4/PX4-Autopilot/commit/bc91005e7aef64ca5e89f72baceee7128678f1d3)

### Message
voted_sensors_update: increase accel & gyro timeout in HIL mode
### Antipattern Category

### Keyword
increase
### Note


## Commit #412
### Hash
[b1e27f43953d0578a246e3f5c19420ac663f0192](https://github.com/PX4/PX4-Autopilot/commit/b1e27f43953d0578a246e3f5c19420ac663f0192)

### Message
simulator: handle ctrl-c during startup correctly

This makes sure the px4 process does not hang when Ctrl-C is pressed
during startup.
### Antipattern Category

### Keyword
hang
### Note


## Commit #413
### Hash
[cfcc75d444f3df23166f4777819ed26261efb85d](https://github.com/PX4/PX4-Autopilot/commit/cfcc75d444f3df23166f4777819ed26261efb85d)

### Message
mavlink shell: check if there's enough free buffer to send the mavlink message

if there is not, the process on the other end of the pipe will just block.
This improves reliability over slow links.
### Antipattern Category

### Keyword
slow
### Note


## Commit #414
### Hash
[66d9d56525acda594029bc4447b8342f212f2101](https://github.com/PX4/PX4-Autopilot/commit/66d9d56525acda594029bc4447b8342f212f2101)

### Message
modules: dataman: Share memory between backends

Also having just a boolean to track if backend is running.
### Antipattern Category

### Keyword
memory
### Note


## Commit #415
### Hash
[e2aae04c95af32680dfd9dc097671f9942445ca6](https://github.com/PX4/PX4-Autopilot/commit/e2aae04c95af32680dfd9dc097671f9942445ca6)

### Message
modules: dataman: Add a ram_flash backend

This backend will keep all updated data in RAM and
persist the data between reboots using flash memory.

Using only flash memory would result in a slow backend that
would decrease the lifetime of the flash memory, using both
we can reduce the several cycles of erase & write into flash
and keep the performance of the backend almost as fast
as the RAM only backend.

Note: Do not use this backend on a sector from the same flash memory
bank as the memory bank that STM32 read instructions or it can block
the CPU from fetching instructions from flash during the erase and
write operations and cause your drone crash.
### Antipattern Category

### Keyword
performance
### Note


## Commit #416
### Hash
[f61b830ae9bcf9ecf78357e163578e6b675e2879](https://github.com/PX4/PX4-Autopilot/commit/f61b830ae9bcf9ecf78357e163578e6b675e2879)

### Message
nuttx-configs: aerofc: Enable CONFIG_STM32_FLASH_WORKAROUND_DATA_CACHE_CORRUPTION_ON_RWW

Now AeroFC is making use of both flash memory banks so it need this
workaround.
### Antipattern Category

### Keyword
memory
### Note


## Commit #417
### Hash
[5a66539b361fa584cfe15596d0c39c4d8505b5a8](https://github.com/PX4/PX4-Autopilot/commit/5a66539b361fa584cfe15596d0c39c4d8505b5a8)

### Message
HOTFIX:Backport Memory corruption due to stack coloring overreach

   Backport of upstream NuttX PR 264

   As discovered by dcabecinhas. This fix assume the 8 byte
   alignment options for size stack size or this will overwrite
   the first word after TOS
   See https://github.com/PX4/Firmware/issues/6613#issuecomment-285869778
### Antipattern Category

### Keyword
memory
### Note


## Commit #418
### Hash
[404719953c58523a311e5cf78e4caa7ff5c7807d](https://github.com/PX4/PX4-Autopilot/commit/404719953c58523a311e5cf78e4caa7ff5c7807d)

### Message
commander: fix abs bug / trigger POSCTL both ways

The check if stick were touched was only working in one direction (per
axis) because fabsf was used incorrectly.

However, this check is still only a differential check triggered by
fast movement and does not trigger if someone slowly moves a stick to
the side. Also, the sensitivity depends on the rate of the commander
loop and/or the RC update loop. The correct solution would be a proper
filtering and trigger for movement.
### Antipattern Category

### Keyword
fast
### Note


## Commit #419
### Hash
[2873d973de0e47d007018603f9fe06261b6f7e3a](https://github.com/PX4/PX4-Autopilot/commit/2873d973de0e47d007018603f9fe06261b6f7e3a)

### Message
mavlink: increase parameter rate from 120 to 300Hz

This speeds up parameter loading. Slow links like telemetry are unaffected,
since the mavlink loop runs only with ~100Hz.

Tested on various links, like:
- telemetry link
- pixracer WiFi
- pixracer USB
- SITL
### Antipattern Category

### Keyword
slow
### Note


## Commit #420
### Hash
[b4290b6b52708c631673cc03af9adee8333062ec](https://github.com/PX4/PX4-Autopilot/commit/b4290b6b52708c631673cc03af9adee8333062ec)

### Message
params: make param_t uint16_t on NuttX

param_t is only used as an offset and we have <1000 params, so an uint16_t
is enough.
This saves roughly 1KB of RAM. We only do that on NuttX because normal
integers have better performance in general.
Previously on amd64, this was even 64bits because it was an uintptr_t.
### Antipattern Category

### Keyword
performance
### Note


## Commit #421
### Hash
[0e650638e40ce62ab11a4977729695a90096e29c](https://github.com/PX4/PX4-Autopilot/commit/0e650638e40ce62ab11a4977729695a90096e29c)

### Message
param: implement RW locking

This allows concurrent read access, which are much more common; reducing
potential lock contention and increasing concurrency.

Taking a lock is expensive, and the reader lock is now even more expensive.
An RCU synchronization scheme would reduce the overhead of the readers to
increasing/decreasing an atomic counter.
Thus this should only be an intermediate step until we move towards RCU.

Tested on SITL & Pixracer.
### Antipattern Category

### Keyword
overhead
### Note


## Commit #422
### Hash
[21e04c9f7afd56adf21d02b76c89ae06fe1fc5a7](https://github.com/PX4/PX4-Autopilot/commit/21e04c9f7afd56adf21d02b76c89ae06fe1fc5a7)

### Message
UAVCAN performance audit (#6829)

* UAVCAN ESC output: removing ESC output channels from published message that are always zero. This allows the UAVCAN stack to always transfer only the minimum number of output values, avoiding redundant zeroes and the associated increase in bus load and CPU time



* Added a separate mixer file for CAN quadrotor



* Sampling profiler improvements



* PMSP: Output more endpoints



* Matrix update



* libc usage workaround



* Removed UAVCAN perfcounters
### Antipattern Category

### Keyword
performance
### Note


## Commit #423
### Hash
[c20b85e6adc2ff212bfdc83810283fae1964d510](https://github.com/PX4/PX4-Autopilot/commit/c20b85e6adc2ff212bfdc83810283fae1964d510)

### Message
Revert "UAVCAN performance audit (#6829)" (#6846)

This reverts commit 21e04c9f7afd56adf21d02b76c89ae06fe1fc5a7.
### Antipattern Category

### Keyword
performance
### Note


## Commit #424
### Hash
[2b2c307eac8af452f8b770996ff5648225000dcd](https://github.com/PX4/PX4-Autopilot/commit/2b2c307eac8af452f8b770996ff5648225000dcd)

### Message
Performance audit (intentionally duplicates #6829) (#6847)

* UAVCAN ESC output: removing ESC output channels from published message that are always zero. This allows the UAVCAN stack to always transfer only the minimum number of output values, avoiding redundant zeroes and the associated increase in bus load and CPU time



* Added a separate mixer file for CAN quadrotor



* Sampling profiler improvements



* PMSP: Output more endpoints



* Matrix update



* libc usage workaround



* Removed UAVCAN perfcounters



* Matrix submodule update
### Antipattern Category

### Keyword
performance
### Note


## Commit #425
### Hash
[7d62aa6a6d9b64977319bbfe66aab23e67884072](https://github.com/PX4/PX4-Autopilot/commit/7d62aa6a6d9b64977319bbfe66aab23e67884072)

### Message
HOTFIX:Backport Memory corruption due to stack coloring overreach complete (#6848)

Backport of upstream NuttX



       86400a252dcbe6e4aef3ecca000b469a0fe96b67

       08e92abb0ba744927ed0b32294859b0f47726f82

       4b65817e99cbdf04fefad883eca0e7c8a9add63c



       Improper rounding in redundant stack coloring

       routines could overwriting the TOS+1 and BOS-1

       depending on the value of CONFIG_ARCH_INTERRUPTSTACK



       This applies the compelet upstream set of fixes from

       David Cabecinhas <david.cab+bitbucket@gmail.com>



       Improper rouding in redundant stack coloring

       routines was overwriting the TOS+1 and BOS-1



       The legacy OABI 4 byte stack alingment was removed

       Only the EABI 8 byte alinement is supported

       The redundant interrupt stack coloring. up_initalize

       had the correct implemantation (last verson of patch)

       and the redundant version in the

       arch/arm/src/stmxxx/stmxx_irq.c was calculating the size

       wrong.



       This is fixed by rounding up CONFIG_ARCH_INTERRUPTSTACK

       by 4 bytes when allocated and alining on a 8 byte boundry
### Antipattern Category

### Keyword
memory
### Note


## Commit #426
### Hash
[a6dcbc3a222c22006b4c26e8d2280072b5c399d5](https://github.com/PX4/PX4-Autopilot/commit/a6dcbc3a222c22006b4c26e8d2280072b5c399d5)

### Message
HOTFIX:Fixes improper restoration of base_priority

   Backport of upstream:

   7601a27cee348f70bebcac95e8e8372fe0651bbf David Sidrane Thu Mar 16 14:16:18 2017 -1000  sem_holder:The logic for the list version is unchanged
   3cc2a4f7c9bb495da6c59f373f8d0e7672e4ee13 David Sidrane Wed Mar 15 14:02:55 2017 -1000  sem_holder: Fixes improper restoration of base_priority
   caf8bac7fb9452f25a3297147e7b414d46e74c6f David Sidrane Mon Mar 13 22:54:13 2017 +0000  missing semi
   d66fd9f965f27eb0446d6aed24b8758674f98b53 David Sidrane Mon Mar 13 12:34:39 2017 -1000  semaphore:sem_boostholderprio prevent overrun of pend_reprios
   3c00651cfef3a0d90bb9e6522463965ad8989e6c David Sidrane Mon Mar 13 11:56:31 2017 -1000  semaphore:sem_holder sem_findholder missing inintalization of pholder
   4d760c5ea44c5f8d30a1a595800e9fbf4874e705 David Sidrane Mon Mar 13 10:46:26 2017 -1000  semaphore:sem_holder add DEBUGASSERTs
   modified 399f3067441941072664bdbfa1bfec8ff35aa449 Gregory Nutt  Sat Mar 11 08:57:34 2017 -0600  A few cosmetic changes (removed file that had nothing to do with semaphore commit by OA)
   60d8606b19a7e7c1285a0ef5e8addaaedf26b95f David Sidrane Fri Mar 10 06:38:17 2017 -1000  Priority Inversion fixes:Initalization
   6cc8f9100b3c8026e73ca738aaa5120bd78dae74 David Sidrane Fri Mar 10 06:37:46 2017 -1000  Priority Inversion fixes:typo
   360539afacc83132acdb83da8f20c468dbe4c63d Gregory Nutt  Fri Mar 10 09:30:15 2017 -0600  Priority inheritance:  When CONFIG_SEM_PREALLOCHOLDERS==0, there is only a single, hard-allocated holder structure.
                                                                                          This is problem because in sem_wait() the holder is released, but needs to remain in the holder container
   a93e46d00c1bc3447fb290b866ed21d8f9c8e146 Gregory Nutt  Fri Mar 10 08:54:50 2017 -0600  Cosmetic (missleading OA commit message) Using !pholder is now  pholder == NULL

   sem_holder: Fixes improper restoration of base_priority
   in the case of CONFIG_SEM_PREALLOCHOLDERS=0

   Original code did not take into accout that 2 holder are needed
   and failed silently when a slot could not be allocated

   The call to sem_restorebaseprio_task context switches in the
   sem_foreachholder(sem, sem_restoreholderprioB, stcb); call
   prior to releasing the holder. So the running task is left
   as a holder as is the started task. Leaving both slots filled
   Thus failing to perforem the boost/or restoration on the
   correct tcb.

   This PR fixes this by releasing the running task slot prior
   to reprioritization that can lead to the context switch.
   To faclitate this, the interface to sem_restorebaseprio
   needed to take the tcb from the holder prior to the
   holder being freed. In the failure case where sched_verifytcb
   fails it added the overhead of looking up the holder.

   There is also the additional thunking on the foreach to
   get from holer to holder->tcb.
### Antipattern Category

### Keyword
overhead
### Note


## Commit #427
### Hash
[0d6f9941456d405fcdec7068719e80f3d02f188e](https://github.com/PX4/PX4-Autopilot/commit/0d6f9941456d405fcdec7068719e80f3d02f188e)

### Message
mc_pos_control: slow down in auto when close to target

mc_pos_control: move limit vel xy after velocity controller
### Antipattern Category

### Keyword
slow
### Note


## Commit #428
### Hash
[72fb7a5062989dcebc7607ebab0e870b72584106](https://github.com/PX4/PX4-Autopilot/commit/72fb7a5062989dcebc7607ebab0e870b72584106)

### Message
mc_pos_control: added gradual landing speed logic
depending on two altitudes that can get set as parameter
the logic linearly slows down from higher land altitude 1 to slower land altitude 2
### Antipattern Category

### Keyword
slower
### Note


## Commit #429
### Hash
[eac72051b8572fe6c7ed40e3ef22f6598fe6c51a](https://github.com/PX4/PX4-Autopilot/commit/eac72051b8572fe6c7ed40e3ef22f6598fe6c51a)

### Message
Backport of stm32f7 add DTCM to heap and use it on F7 (#6865)

* Backport:stm32f7: stm32_allocateheap: allow use DTCM memory for heap



   Back port of upstrem contrib by Jussi Kivilinna <jussi.kivilinna@haltian.com>



   stm32f7: stm32_allocateheap: allow use DTCM memory for heap



   STM32F7 has up to 128KiB of DTCM memory that is currently left unused.



   This patch adds DTCM to main heap if CONFIG_STM32F7_DTCMEXCLUDE is not enabled.



* px4fmu-v5_default:Enable inclusion of the DTCM in the heap



  CONFIG_MM_REGIONS=3 adds the DTCM region to the heap.
### Antipattern Category

### Keyword
memory
### Note


## Commit #430
### Hash
[5c6264ae3554e34c5ee1add2e9c1ee155fa7231e](https://github.com/PX4/PX4-Autopilot/commit/5c6264ae3554e34c5ee1add2e9c1ee155fa7231e)

### Message
Backport:stm32_flash changes from upsteam

  PX4 contrib from <jose.souza@intel.com>

  1) stm32: Fix erase sector number for microcontrolers with
     more than 11 sectors

     Erase a sector from the second bank cause the bit 4 of SNB being set
     but never unsed, so trying to erase a sector from the first bank
     was acually eraseing a sector from the second bank.
  2) stm32: Make up_progmem thread safe

   Writing to a flash sector while starting the erase of other sector
   have a undefined behavior so lets add a [staticaly initalized]
   semaphore and syncronize access to Flash registers.

  3) Add workaround for flash data cache corruption on
     read-while-write

    This is a know hardware issue on some STM32 see the errata
    of your model and if you make use of both memory banks you
    should enable it.

  4) Greg's cleanup

  5) PX4 clean up

    stm32_flash:Need conditional on non F4 targets
### Antipattern Category
X
### Keyword
memory
### Note
Not an anti-pattern, workaround for a known issue of the STM32 hardware and a section of the code was made thread safe.
Issues: stm32 flash fixes #6885
        Critical: Fixes Snapdragon Flight problem caused when the generated parameters.xml differs for the ARM and DSP builds #6883

## Commit #431
### Hash
[d72133a380e64b92820ebf8052497406003da4ec](https://github.com/PX4/PX4-Autopilot/commit/d72133a380e64b92820ebf8052497406003da4ec)

### Message
rcS: increase log buffer by 4kB

To reduce dropouts, and because we have enough RAM :)
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Value changed from 12 to 16, current value is 8.
Issue: Call clearenv() on NuttX #6925

## Commit #432
### Hash
[358bcb6ae04d7d04a614d2166af7cd8282bb1048](https://github.com/PX4/PX4-Autopilot/commit/358bcb6ae04d7d04a614d2166af7cd8282bb1048)

### Message
visibility.h: add #pragma GCC poison getenv setenv putenv

Just to make sure that it will never be used on NuttX. This is not an
architectural limitation, just a memory optimization, since we call
clearenv() on NuttX.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features, small memory optimization, env variables are not desired on NuttX as they use aprox. 6kB of RAM.
Issue: Call clearenv() on NuttX #6925

## Commit #433
### Hash
[412f956636f9f98a3b681e76c5a123e7f609c988](https://github.com/PX4/PX4-Autopilot/commit/412f956636f9f98a3b681e76c5a123e7f609c988)

### Message
clang-tidy enable performance-type-promotion-in-math-fn
### Antipattern Category
X
### Keyword
performance
### Note
This commit does not change any performance-related features, this commit forces the build to fail if there are float to double coversions.
Issue: WIP: clang-tidy enable performance-type-promotion-in-math-fn #6841

## Commit #434
### Hash
[c46274043f4a1514668ec745246a198d80e5b83b](https://github.com/PX4/PX4-Autopilot/commit/c46274043f4a1514668ec745246a198d80e5b83b)

### Message
printload: use sched_lock to protect access to tcb

what could have gone wrong before? A scheduling switch during the printload
could have led to a task exit, rendering the tcb invalid. After switching
back, printload would access invalid memory.

This keeps the sched_lock() section as small as possible, just grabbing the
tcb variables we need.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features, error in scheduling switch during printload.
Issue: Add preflight & postflight perf counters & process usage to ULog #6832

## Commit #435
### Hash
[23d03559795975ee74b4b990a1c7a01aa4dcc167](https://github.com/PX4/PX4-Autopilot/commit/23d03559795975ee74b4b990a1c7a01aa4dcc167)

### Message
printload: reduce memory usage of print_load_s

assuming CONFIG_MAX_TASKS = 32, this saves 256B of RAM
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features, local variable used instead of pointer in a struct.
Issue: Add preflight & postflight perf counters & process usage to ULog #6832

## Commit #436
### Hash
[4b01e5b6b62959ad97ad5691602ea6fa885009b8](https://github.com/PX4/PX4-Autopilot/commit/4b01e5b6b62959ad97ad5691602ea6fa885009b8)

### Message
printload: add print_load_buffer() method

Instead of printing to an fd, this prints to a buffer and calls a callback
for each line. To avoid code duplication, the print_load has been refactored
to print to a buffer first, then print to an fd. The overhead is not
noticable, and the behavior of print_load is unchanged.
### Antipattern Category
X
### Keyword
overhead
### Note
This commit does not change any performance-related features.
Issue: Add preflight & postflight perf counters & process usage to ULog #6832

## Commit #437
### Hash
[446c734edc92c57be6a4b60320f02cd8e4025ce5](https://github.com/PX4/PX4-Autopilot/commit/446c734edc92c57be6a4b60320f02cd8e4025ce5)

### Message
perf_counter: use a mutex to protect concurrent access to the perf_counters linked list

perf_counters is read from and written to by different threads and thus
requires synchronization. Without it we risk accessing invalid memory.

There are still remaining issues (see comment in code), they will not lead
to a crash however.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features
Issue: Add preflight & postflight perf counters & process usage to ULog #6832

## Commit #438
### Hash
[0158f1d506c145444cd5004a9ac9d6aec7da9b98](https://github.com/PX4/PX4-Autopilot/commit/0158f1d506c145444cd5004a9ac9d6aec7da9b98)

### Message
VTOL Standard transition improvements (#6904)



 * FW actuators fully on the entirety of front and back transition

 * back transition ramp up to full MC weight half way through back transition

 * increase maximum front and back transition times

 *  navigator don't reset transition altitude
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Front and Back transition times increased.
Issue: Vtol transition improvements #6904


## Commit #439
### Hash
[12182ec1fc5355d75e12672cc5a7b155fe99f4a1](https://github.com/PX4/PX4-Autopilot/commit/12182ec1fc5355d75e12672cc5a7b155fe99f4a1)

### Message
Increase max yawrate default parameters for standard delta VTOL

MC_YAWRATE_MAX 20  => 50

Signed-off-by: bresch <brescianimathieu@gmail.com>
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Yawn rate value increased from 20 to 50.
Issue: Increase max yawrate default parameters for standard delta VTOL #6981


## Commit #440
### Hash
[6ef2ae29993c02f926c8719d29d84202b1fe3142](https://github.com/PX4/PX4-Autopilot/commit/6ef2ae29993c02f926c8719d29d84202b1fe3142)

### Message
Reduce USART1 tx buffer by 8 bytes to fix aligment issue

   The recent changes to the timers increased memory by 8 bytes.
   and should have ONLY added 8 bytes
   was  20000dc0	40	20000E00
   is:  20000dc8	40	20000E08
   s/b  20000E08       1f3      next symbol

   But for some unknown reason the linker skipped to the next alignment
   of 256 and wasted 246 bytes.

   20000F00     1f3     next symbol

   Even with .align 8 in the .S file and . = ALIGN(4); in the linker
   script I could not move the allocation back only up to the next
   512 alighment.

   So this is a hack to shift things back 8 bytes.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
memory
### Note
Value reduced from 64 to 56.
Issue: Reduce USART1 tx buffer by 8 bytes to fix aligment issue #6993


## Commit #441
### Hash
[61cd89efc1827a21debd43a1dd8f46acf3456040](https://github.com/PX4/PX4-Autopilot/commit/61cd89efc1827a21debd43a1dd8f46acf3456040)

### Message
Land detector: Since multicopters take off and land slower than 0.7 m/s, setting the default detection threshold to 0.5 m/s is a much safer default
### Antipattern Category
X
### Keyword
slower
### Note
This commit does not change any performance-related features.

## Commit #442
### Hash
[3b743fbbe97bdc264455944fb16e6cee7e7c9db8](https://github.com/PX4/PX4-Autopilot/commit/3b743fbbe97bdc264455944fb16e6cee7e7c9db8)

### Message
MC position control: Smoother takeoff

This patch ramps up the throttle to hover throttle instead of a fixed value and limits the vertical takeoff speed to the value set in the parameter. This should ensure smoother, slower takeoffs, in particular in autonomous flight modes.
### Antipattern Category
General:Hard-coding
### Keyword
slower
### Note
Hard-coded values changed to dynamic ones.

## Commit #443
### Hash
[7f0db95f870fb9ce4602d6b9ed66422a3cb6e7e6](https://github.com/PX4/PX4-Autopilot/commit/7f0db95f870fb9ce4602d6b9ed66422a3cb6e7e6)

### Message
logger: reduce CPU load by ~1.5%

Reduces CPU load from ~6.9% to 5.3% (tested on Pixracer & Pixhawk). The
method is only used once, so it does not increase flash usage.
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features. This performance issue is applicable only in C++.
Issue: Logger: add logrotate & reduce CPU load #6997

## Commit #444
### Hash
[9eb0e62787d4bc6e9334f20d14aa83960c8d68ff](https://github.com/PX4/PX4-Autopilot/commit/9eb0e62787d4bc6e9334f20d14aa83960c8d68ff)

### Message
Support calibration of fast+slow gyros #6998
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features.
Issue: Support calibration of fast+slow gyros #7043

## Commit #445
### Hash
[56f4f2b41f2a20e26936d09023a3a0e383cc7893](https://github.com/PX4/PX4-Autopilot/commit/56f4f2b41f2a20e26936d09023a3a0e383cc7893)

### Message
Fix top output, indentation for #7020

Previously load stats were stored outside of the printloop, but
with the refactoring to save memory state was reset and used in
the first loop before the actual load calculations were valid.

Fixed by moving the summary info to the bottom of the top printout
after everything is computed. Also restructured the callback to
not depend on a line counter and fixed astyle glitches.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features.
Issue: Fix top output, indentation for #7020 #7074


## Commit #446
### Hash
[57fa031e2b52cd9f0cd3429bdd368fed7ea13486](https://github.com/PX4/PX4-Autopilot/commit/57fa031e2b52cd9f0cd3429bdd368fed7ea13486)

### Message
Fixes problem preventing params on snapdragon platforms from being saved to flash memory.
### Antipattern Category
General:Hard-coding
### Keyword
memory
### Note
Hard-coded variables deleted.

## Commit #447
### Hash
[2a34bde0e9fd941551cab31d8f6e1c757611e538](https://github.com/PX4/PX4-Autopilot/commit/2a34bde0e9fd941551cab31d8f6e1c757611e538)

### Message
Tools/ecl_ekf: Update EKF log analysis

Add assessment of IMU bias and mag field estimation
Reduce warning false positives by adjusting thresholds and eliminating use of peak value plots for output observer monitoring
Clear each figure after saving to reduce memory usage
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Change in log messages.
Issue: EKF2 Updates (#7087)

## Commit #448
### Hash
[5012dffeaede4228d2109358b1d08adfafdd4d19](https://github.com/PX4/PX4-Autopilot/commit/5012dffeaede4228d2109358b1d08adfafdd4d19)

### Message
Potentially infinite and deleted loops found by PVS-Studio (#7100)

 - Fixed V712

 - The compiler can optimize this code by creating an infinite loop, or simply deleting it.

 - There is need to add a volatile qualifier to the '_ExitFlag' and 'sim_delay' variables.
### Antipattern Category
X
### Keyword
infinite
### Note
This commit does not change any performance-related features.

## Commit #449
### Hash
[60fe87aac252f5b20922be07ff5f76f8106d3cb5](https://github.com/PX4/PX4-Autopilot/commit/60fe87aac252f5b20922be07ff5f76f8106d3cb5)

### Message
commander : preflight checks increase max_mags to 4
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Value changed from 3 to 4.
Issue: Pixhawk 2 mag fix (#7080)

## Commit #450
### Hash
[f04f1d6b03146c5db6bdfaed773b864a2f39848a](https://github.com/PX4/PX4-Autopilot/commit/f04f1d6b03146c5db6bdfaed773b864a2f39848a)

### Message
sensors HIL increase gyro and accel timeout

 - fixes #7050
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Same values present in the current version.
Issue: sensors HIL increase gyro and accel timeout (#7129)

## Commit #451
### Hash
[9a162a24bb31c8d7f5e89507a2099f984a68f6a4](https://github.com/PX4/PX4-Autopilot/commit/9a162a24bb31c8d7f5e89507a2099f984a68f6a4)

### Message
mc_pos_control: improved smooth takeoff and used it for manual takeoff as well
adresses:
there were setpoint twitches at the beginning and end of my smooth takeoff routine
it was to slow and not configurable
it was only available for automatic takeoff
### Antipattern Category
General:Hard-coding
### Keyword
slow
### Note
Hard coded values.
Issue: Smooth takeoff for altitude controlled flights (including auto takeoff) (#7138)

## Commit #452
### Hash
[d1dd6a16f20e4fb28ff096ab882c9a11c362e57d](https://github.com/PX4/PX4-Autopilot/commit/d1dd6a16f20e4fb28ff096ab882c9a11c362e57d)

### Message
IO v2: disable interrupt stack

This avoids burning significant memory in a configuration that is not actually using parallel tasks
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
memory
### Note
Value changed from 500 to 0.
Issue: Free RAM on IO - Take 2 #7167


## Commit #453
### Hash
[dbf754eab1833a5f83bc3d99f9644bbe49d77667](https://github.com/PX4/PX4-Autopilot/commit/dbf754eab1833a5f83bc3d99f9644bbe49d77667)

### Message
ROMFS: If UAVCAN is enabled, reduce log buffer size

This is necessary to make the space for UAVCAN in memory and doing it this way avoids negatively impacting users who do not use UAVCAN.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
memory
### Note
Log buffer values reduced if UAVCAN activated.
Issue: UAVCAN Memory optimizations #7166



## Commit #454
### Hash
[33f2897f00130daa9c4a8615a1f2313d11f34444](https://github.com/PX4/PX4-Autopilot/commit/33f2897f00130daa9c4a8615a1f2313d11f34444)

### Message
px4fmu-v4:Configure timer IO pins with pull downs

  When the CCER is cleared the IO pin tends to float. The FMUV4
  HW has no TXS0108 and if cut off while high will decay.

  By adding the pull down the pins will seek the low state faster.
  13.8 us from off to decabe below threshold.
### Antipattern Category
X
### Keyword
faster
### Note
This commit does not change any performance-related features. Pin setup for timer IO.
Issue: Force PWM off on reboot on fmuv4 (#7151)

## Commit #455
### Hash
[8ea0b2d3c51a48a7f45440583301f04e52665b02](https://github.com/PX4/PX4-Autopilot/commit/8ea0b2d3c51a48a7f45440583301f04e52665b02)

### Message
commander: rework posvel validity checks

Move into functions.
Reset probation time and recalculate checks if a mode change is demanded to give the operator ability to regain control as soon as possible after nav performance is regained. (+11 squashed commits)
Squashed commits:
[a4bb800] commander: enable pilot to quickly recover from loss of position accuracy
[19e16a0] commander: rework postal probation time
[f96284e] commander: rework bad pos and vel test probation time
[00d5f0c] commander: Allow EKF preflight checks to pass with moving vehicle

Separates the 'is using GPS' and the GPS quality checks.
Uses a reasonable subset of the GPS quality checks which allows checks to pass if the vehicle is moving.
[4cdfb5c] commander: remove unused variable
[349385a] commander: add EKF GPS quality checks to pre-arm checking

Only perform check if GPs checking is activated by parameter setting.
Display fault messages that makes it clear if EKF quality checks are failing or the EKF is not using GPS for another reason. We do not want to confuse this with GPS lock.
[340ae29] commander: make position invalid fail-safe more sticky

Require check to pass for 7 seconds before exiting failsafe. This is required because if GPs is failing innovation tests for a prolonged period, the EKF will periodically reset to the GPS and report good accuracy at the time of reset.
Adding this delay gives time for an underlying error condition (eg bad IMU or compass) to be re-detected.
[b04ac95] commander: Increase RAM allocation to eliminate low stack warnings
[9dca12f] commander: add missing position invalid fail-safe responses
[69f264d] commander: Update position invalid fail-safe responses

Replace separate logic for each case with a generic function
Add velocity checks.
[8e8cef1] commander: rework position validity checks

Consolidate existing checks for global and local position validity and add checking of velocity accuracy.
Enable checks to be bypassed using the CBRK_VELPOSERR parameter.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
performance
### Note
Stack size of a task slightly increased, some function signatures changed.
Issue: EKF2: Enable in-flight learned mag bias to be saved to non-volatile memory (#7095)

## Commit #456
### Hash
[0d7f475bd01111c5866e8ccb556ea3d5012f5307](https://github.com/PX4/PX4-Autopilot/commit/0d7f475bd01111c5866e8ccb556ea3d5012f5307)

### Message
ecl: minor updates

Initialisation changes to address valgrind errors
Change to default GPS and Airspeed time delay (these are overwritten by ekf2_main parameter settings)
Increase sensitivity of bad accelerometer checks
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features.

## Commit #457
### Hash
[65baf9983232a5697b7748c8df52e4abb6e7f067](https://github.com/PX4/PX4-Autopilot/commit/65baf9983232a5697b7748c8df52e4abb6e7f067)

### Message
Logger hotfix: Allocate buffer on logging

This enables to use the RAM normally consumed by the log buffer to be used for calibration and other memory-intense tasks.
These run typically only disarmed when logging is not enabled.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Log writer buffer is allocated when needed instead of init.

## Commit #458
### Hash
[1bb56e775e0b8feb4c0e6e37107b2d6d5cad195f](https://github.com/PX4/PX4-Autopilot/commit/1bb56e775e0b8feb4c0e6e37107b2d6d5cad195f)

### Message
IO: Fix access to free memory

The free memory was accessed from interrupt context where it should not be accessed from. We build the statistic now at a fixed rate while not armed.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Memory access from restricted context.

## Commit #459
### Hash
[981dac8e955b3a4194421605dda7a09b7c16bbc5](https://github.com/PX4/PX4-Autopilot/commit/981dac8e955b3a4194421605dda7a09b7c16bbc5)

### Message
Navigator: Increase RAM size
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
RAM size incresed.
Issue: fix qgc flow takeoff -> use min takeoff alt if no home position (#7209)


## Commit #460
### Hash
[68e76d8ed3a1974aa3365d0eb4b2314e9cc09067](https://github.com/PX4/PX4-Autopilot/commit/68e76d8ed3a1974aa3365d0eb4b2314e9cc09067)

### Message
FMUv5: Increase logging throughput considerably.

This will help to understand the sensor selection on FMUv5 in different airframes. We do have the RAM and CPU to do this on this platform.
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features. Adjusts settings for FMUv5 in a configure file.

## Commit #461
### Hash
[3c62f7a3eb1e3427e194a85a32c3ceb69cc7494d](https://github.com/PX4/PX4-Autopilot/commit/3c62f7a3eb1e3427e194a85a32c3ceb69cc7494d)

### Message
stm32:drv_input_capture bug fixes.

   Filter for channel 4 was modifying channel 1
   capture and overflow reads were using wrong paramaters
   in macros and addressing junk in memory.
   up_input_capture_get_filter was shifing results the wrong way.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Code adjustments.

## Commit #462
### Hash
[cfa61c58411f2257b9b5e09a7e4fb16b8bcdbb2d](https://github.com/PX4/PX4-Autopilot/commit/cfa61c58411f2257b9b5e09a7e4fb16b8bcdbb2d)

### Message
MavlinkReceiver: add mission manager, param manager, ftp and log handler

This makes also a slight stack size increase necessary (was 284 bytes left)
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Stack size slighty increased from 2100 to 2140 due to the addition of MAVLink mission manager.
Issue: Mavlink threadding fixes (#7226)

## Commit #463
### Hash
[2a79ddd621355690e174f134e3421e7bf67bddb1](https://github.com/PX4/PX4-Autopilot/commit/2a79ddd621355690e174f134e3421e7bf67bddb1)

### Message
MavlinkLogHandler: increase MAX_BYTES_SEND to 256kb

It increases the throughput on UDP (from around 2Mb to 2.5Mb), while the
rate via USB & telemetry stay the same.
### Antipattern Category
New:Hard-coded-fine-tuning, New:Fixed_Communication_Rate
### Keyword
increase
### Note
Max bytes sent increased from 64 * 1024 to 256 * 1024, increasing UDP throughput.
Issue: Mavlink threadding fixes (#7226)

## Commit #464
### Hash
[5a96490c689d36d319248468799644cc53b9c22a](https://github.com/PX4/PX4-Autopilot/commit/5a96490c689d36d319248468799644cc53b9c22a)

### Message
sensors : fix race condition triggered by slow-to-boot external sensors
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features. Function call added to get offsets and scaling loaded.

## Commit #465
### Hash
[32068dcd171ac6a372860ce5aaaeaa261b346e23](https://github.com/PX4/PX4-Autopilot/commit/32068dcd171ac6a372860ce5aaaeaa261b346e23)

### Message
px4io increase stack
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Stack size increase from 1400 to 1500.
Issue: MS5525 differential pressure driver (#7283)

## Commit #466
### Hash
[63cbce6bd383c431251179adb9a0764e6da9560e](https://github.com/PX4/PX4-Autopilot/commit/63cbce6bd383c431251179adb9a0764e6da9560e)

### Message
ekf2: Increase RAM to remove stack space warnings
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
RAM size increased from 5800 to 5900.
Issue: EKF: pull in miscellaneous bug fixes (#7521)

## Commit #467
### Hash
[c8b9f8afa8836ce921d92b3aba198f04bbab673c](https://github.com/PX4/PX4-Autopilot/commit/c8b9f8afa8836ce921d92b3aba198f04bbab673c)

### Message
F7 nuttx configs: increase CONFIG_STM32F7_BBSRAM_FILES to 5
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features.

## Commit #468
### Hash
[6eff7deb7edc5419bdeef3ddf2ce26fdc02a6960](https://github.com/PX4/PX4-Autopilot/commit/6eff7deb7edc5419bdeef3ddf2ce26fdc02a6960)

### Message
Extend the delay ensure post reset pulse delayed.

Given the original poster's comment that "It happens very consistently for us." I suspect the motor spin observed in https://github.com/PX4/Firmware/issues/7457 is not caused by the original issue of slow decay on the PWM pins at reset, but the post reset pulse of 3.1 Ms arriving in a window that the ESC considers it valid.



The results from testing, indicated that the if the PWM pins were clamped low for > 300 Ms, prior to reset the motors did not spin. This would delay the the post reset pulse of 3.1 Ms out by > 300 Ms. 



This change delays the reset and therefore the pulse by at least 400 Ms.
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
slow
### Note
Delay increased from 6 to 400.
Issue: px4fmu-v4:Insure the discharge of the pins PWM pins on rest. (#7459)

## Commit #469
### Hash
[f45b9048aa8662865ef95703e51fcdc70544254b](https://github.com/PX4/PX4-Autopilot/commit/f45b9048aa8662865ef95703e51fcdc70544254b)

### Message
GPS driver increase stack (244 bytes left)
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Stack increased from 1550 to 1610.
Issue: GPS driver increase stack (244 bytes left) (#7562).

## Commit #470
### Hash
[75faf5c7bd1e154fa7487cba09afcad668e704a6](https://github.com/PX4/PX4-Autopilot/commit/75faf5c7bd1e154fa7487cba09afcad668e704a6)

### Message
Preflight checks: Increase accel warn limit range
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Test limit adjusted by a factor of 0.8 instead of 0.5.

## Commit #471
### Hash
[585984fa0c846d1a1c4e63e9e9501cfff9d87cda](https://github.com/PX4/PX4-Autopilot/commit/585984fa0c846d1a1c4e63e9e9501cfff9d87cda)

### Message
fmuservo increase stack
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Task stack size slightly increased.
Issue: fmuservo increase stack (#7568)


## Commit #472
### Hash
[10f54e718eed24cd225231d653d1b1b9a07e3fd9](https://github.com/PX4/PX4-Autopilot/commit/10f54e718eed24cd225231d653d1b1b9a07e3fd9)

### Message
modules: dataman: Optimize memory usage

Use the size of each item type instead of the biggest one.

In AeroFC that runs is constrained mode it was using 7860 bytes
and now it uses 6930 bytes almost 1KB less.
### Antipattern Category
General:Hard-coding
### Keyword
memory
### Note
Size of each item used instead of the size of the biggest one.

## Commit #473
### Hash
[71136dcedf9c4006f036022652a698db9b38f092](https://github.com/PX4/PX4-Autopilot/commit/71136dcedf9c4006f036022652a698db9b38f092)

### Message
Log_writer_file: Increase stack size

Test flights reported the warning `[load_mon] log_writer_file low on stack! (292 bytes left)`

Increase stack size from 1060  to 1072 (=8 + 1060 rounded to next multiple of 8).
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
increase
### Note
Thread stack size increased from 1060 to 1072.
Issue: Fix compilation errors with arm-none-eabi-gcc 7 (#7502)

## Commit #474
### Hash
[a6c682ce504a33f64a3bde83e5f9004c252a476a](https://github.com/PX4/PX4-Autopilot/commit/a6c682ce504a33f64a3bde83e5f9004c252a476a)

### Message
mavlink_ftp: fix stack overflow & add root dir prefix

- change memory allocation from stack to a malloc'd buffer. This avoids
  increasing the stack size. And since FTP is rarely used, the buffers
  are only allocated upon use and freed after a time of 2s inactivity.
- adds PX4_ROOTFSDIR as root directory prefix. This does not change
  anything on NuttX, but in SITL it will avoid enumerating the whole
  disk tree when using QGC (which enumerates all files recursively).
### Antipattern Category
X
### Keyword
memory
### Note
Buffers used instead of changing root_dir or other local variables.

## Commit #475
### Hash
[f746f9a9b3ab349659a4efd26cba8a9d87a19964](https://github.com/PX4/PX4-Autopilot/commit/f746f9a9b3ab349659a4efd26cba8a9d87a19964)

### Message
UAVCAN: Reduce memory footprint
### Antipattern Category
General:performance:Hard-coding
### Keyword
memory
### Note
Value reduced from 7 to 6.

## Commit #476
### Hash
[2815c62acff650a0299e8f08f1faf3eec66d45b9](https://github.com/PX4/PX4-Autopilot/commit/2815c62acff650a0299e8f08f1faf3eec66d45b9)

### Message
fix power button shutdown: use an orb topic instead of a work queue call

px4_shutdown_request() was called from the power button IRQ callback, which
invoked a work queue callback. But on NuttX, the work queue uses a
semaphore, and thus it cannot be called from IRQ context.
This patch switches to publishing an uORB msg instead, which is handled in
the commander main thread.

To increase failure resistance, we could subscribe to the same topic in
another module for redundancy, in case commander runs wild.
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features.

## Commit #477
### Hash
[dcb5f80180aa89533db89c96a02d6395d1641d75](https://github.com/PX4/PX4-Autopilot/commit/dcb5f80180aa89533db89c96a02d6395d1641d75)

### Message
shutdown: increase the max timeout to 5s

To make sure slow param writes will finish before we hit the timeout. I've
seen param write durations of around 2s.
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
slow
### Note
Timeout increased from 300 ms to 5 s.


## Commit #478
### Hash
[529def11e8959373e4a644d1ded7be5ff242b0e0](https://github.com/PX4/PX4-Autopilot/commit/529def11e8959373e4a644d1ded7be5ff242b0e0)

### Message
CMake / Clang: Increase warning level
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features.

## Commit #479
### Hash
[03d86054a48d3ebf1d4a8f21ce5e4d3d4efb4f08](https://github.com/PX4/PX4-Autopilot/commit/03d86054a48d3ebf1d4a8f21ce5e4d3d4efb4f08)

### Message
landdetector: decrease land detection to 0.3
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
decrease
### Note
Time land detection trigger variable decreased from 0.5 to 0.3.
Issue: Landdetector additional state (#7314)
       land detector revert FW hysteresis constants and cleanup initialization (#7796)

## Commit #480
### Hash
[52ca49c6826c243136a09d5105156430a4570f97](https://github.com/PX4/PX4-Autopilot/commit/52ca49c6826c243136a09d5105156430a4570f97)

### Message
geofence: remove fence & fence_vertex messages

- this was never read
- it was implemented wrong, leading to memory access violations in
  publishFence (an integer was passed instead of the fence_s struct)
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features.

## Commit #481
### Hash
[1a3315e397d7a8104eef6a68b42f2b419bc6a3a8](https://github.com/PX4/PX4-Autopilot/commit/1a3315e397d7a8104eef6a68b42f2b419bc6a3a8)

### Message
msg: Fix build in python3

We can afford a slower performance in this parsers with python2 to
keep compability with python3.
http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#xrange
### Antipattern Category
X
### Keyword
performance
### Note


## Commit #482
### Hash
[afb01d015e246a93b7ebccc2d45bccd4a9920d51](https://github.com/PX4/PX4-Autopilot/commit/afb01d015e246a93b7ebccc2d45bccd4a9920d51)

### Message
px4fmu-v2:Use simple HW versioning API to differentiate V2 variant at runtime.

   There are several boards that share the px4fmu-v2 build as px4fmu-v3 build.

   It was initially envisioned, that the build would be binary compatable and
   the RC script would probe different sensors and determine at runtime the
   HW type. Unfortunately, a failed sensor, can result in mis-detection
   of the HW and result in an improper start up and not detect the HW
   failure.

   All these boards's bootloader report board type as px4fmu-v2.
   This precludes and automated selection of the correct fw if it
   had been built, by a different build i.e. px4fmu-cube etc.

   We need a way to deal with the slight differences in HW that effect
   the operations of drivers and board level functions that are different
   from the FMUv2 pinout and bus utilization.

   1) FMUv3 AKA Cube 2.0 and Cube 2.1 Bothe I2C busses are external.
      This effected the mag on GPS2 not reporting Internal and
      having the wrong rotation applied.

   2) FMUv3 does not performa a SPI buss reset correctly.
      FMUv2 provides a SPI1 buss reset. But FMUv3 is on
      SPI4. To complicate matters the CS cross bus
      boundries.

   3) PixhawkMini reused a signal that was associated with SPI4
      as a SPI1 ready signal.

   Based on hardware differnce in the use of PB4 and PB12 this code
   detects: FMUv2,  the Cube, and PixhawkMini and provides the
   simple common API for retriving the type, version and revision.

   On FmuV5 this same API will be used.
### Antipattern Category

### Keyword
runtime
### Note


## Commit #483
### Hash
[490f40bee161112c55c09c865ce9be9e96ea65d6](https://github.com/PX4/PX4-Autopilot/commit/490f40bee161112c55c09c865ce9be9e96ea65d6)

### Message
Sensors: Use temperature for airspeed validation to avoid false positives for high-performance airspeed sensors

This is required to enable new high-performance sensors which otherwise would provide incorrect readings.
### Antipattern Category

### Keyword
performance
### Note


## Commit #484
### Hash
[cc1b76682443f6de28cd07180a39ba8a6d0edb5d](https://github.com/PX4/PX4-Autopilot/commit/cc1b76682443f6de28cd07180a39ba8a6d0edb5d)

### Message
Fix memory leaks identified by cppcheck

* Add `free` / `delete`
* Add comment explaining the (presumed) motivation for the use of new instead of
  allocating on the stack
### Antipattern Category

### Keyword
memory
### Note


## Commit #485
### Hash
[9dea515eaaf758abcc0131c0c368078358972f69](https://github.com/PX4/PX4-Autopilot/commit/9dea515eaaf758abcc0131c0c368078358972f69)

### Message
frsky_telemetry S.Port: refactor to use less memory & allocations
### Antipattern Category

### Keyword
memory
### Note


## Commit #486
### Hash
[a2bfcb94ef1c03b586c55d91fffec36b8d504b8b](https://github.com/PX4/PX4-Autopilot/commit/a2bfcb94ef1c03b586c55d91fffec36b8d504b8b)

### Message
frsky_telemetry D protocol: refactor to use less memory & allocations

Also add the vehicle_gps_position & flight mode information
### Antipattern Category

### Keyword
memory
### Note


## Commit #487
### Hash
[98396a0bc57ebfdc85ff6ff54c097968387fe620](https://github.com/PX4/PX4-Autopilot/commit/98396a0bc57ebfdc85ff6ff54c097968387fe620)

### Message
frsky_telemetry: cleanup static vars, use less memory & fix process priority
### Antipattern Category

### Keyword
memory
### Note


## Commit #488
### Hash
[9644f855e3dc7be4ffdb561218338a30ab774746](https://github.com/PX4/PX4-Autopilot/commit/9644f855e3dc7be4ffdb561218338a30ab774746)

### Message
common:Define default BOARD_NUMBER_I2C_BUSES and BOARD_I2C_BUS_CLOCK_INIT

   Define the default I2C buss frequncies that are backward compatible
   with the existing code. While allowing it the defaults to be overridden
   by a board config.

   Based on the legacy STM32 code, the I2C buss numbering starts at 1.
   The bus frequency is stored in a 0 based array. If px4_i2cbus_initialize
   returns a valid device, then the _bus-1 will act as the index to the
   busses frequency.

   A board may define BOARD_NUMBER_I2C_BUSES - the number of I2C busses
   it supports* and BOARD_I2C_BUS_CLOCK_INIT to initalize the bus
   clocks for a given busses.

   BOARD_NUMBER_I2C_BUSES - the number of busses including the *highest
                            number bus. If the board has 2 I2C
                            busses I2C1 and I2C3 BOARD_NUMBER_I2C_BUSES
                            would be set to 3

   BOARD_I2C_BUS_CLOCK_INIT - Initalization for the bus frequencies
                              by bus. A call init, with a frequency
                              less then the value used for the
                              Initalization will result in the device
                              not starting becuase the buss runs too
                              fast for it.
### Antipattern Category

### Keyword
fast
### Note


## Commit #489
### Hash
[281ee5e5afcbde6dbad46068cfae975cc216aa3e](https://github.com/PX4/PX4-Autopilot/commit/281ee5e5afcbde6dbad46068cfae975cc216aa3e)

### Message
vmount: increase stack size
### Antipattern Category

### Keyword
increase
### Note


## Commit #490
### Hash
[55a2930cdb1e3162751d78193400a0983131238c](https://github.com/PX4/PX4-Autopilot/commit/55a2930cdb1e3162751d78193400a0983131238c)

### Message
vmount: reduce stack size to 1900 as recommended by @bkueng (maximum used memory observed: 1552)
### Antipattern Category

### Keyword
memory
### Note


## Commit #491
### Hash
[83643a719ab472f1ddac0943c868c0f33399adfc](https://github.com/PX4/PX4-Autopilot/commit/83643a719ab472f1ddac0943c868c0f33399adfc)

### Message
nuttx config: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

This is needed when logger is logging to file and ulog streaming gets
activated.
### Antipattern Category

### Keyword
increase
### Note


## Commit #492
### Hash
[79f49fd851bf14d65c4b3b50bc37eca349883bef](https://github.com/PX4/PX4-Autopilot/commit/79f49fd851bf14d65c4b3b50bc37eca349883bef)

### Message
bugfix:px4fmu-v5 (STM32F7) random sd write failures

   This is a back port of upstream NuttX PX4 contrib of

   ef42c25 stm32f7:SDMMC add dcache alignment check in dma{recv|send}setup
                   In the where CONFIG_SDIO_PREFLIGHT is not used and dcache
                   write-buffed mode is used (not write-through) buffer alignment
                   is required for DMA transfers because a) arch_invalidate_dcache
                   could lose buffered writes data and b) arch_flush_dcache could
                   corrupt adjacent memory if the buffer and the bufflen, are not on
                   ARMV7M_DCACHE_LINESIZE boundaries.

   1e7ddfe  stm32f7:SDMMC remove widebus limitation on DMA
                    There is no documantation for the STM32F7 that limits DMA on
                    1 bit vrs 4 bit mode.

   dffab2f  stm32f7:DMA add dcache alignment check in stm32_dmacapable
                    In the case dcache write-buffed mode is used (not write-through)
                    buffer alignment is required for DMA transfers because
                    a) arch_invalidate_dcache could lose buffered writes data and
                    b) arch_flush_dcache could corrupt adjacent memory if the
                    maddr and the mend+1, the next next address are not on
                    ARMV7M_DCACHE_LINESIZE boundaries.

   38cbf1f  stm32f7:DMA correct comments and document stm32_dmacapable
            Updated comment to proper refernce manual for STM32F7 not STM32F4.
            Added stm32_dmacapable input paramaters documentation.
### Antipattern Category

### Keyword
memory
### Note


## Commit #493
### Hash
[a9b12cc8b40ba4b3c253d7922fb8377fdacf165a](https://github.com/PX4/PX4-Autopilot/commit/a9b12cc8b40ba4b3c253d7922fb8377fdacf165a)

### Message
Changed the default behavior for the client launching as a infinite loop
### Antipattern Category

### Keyword
infinite
### Note


## Commit #494
### Hash
[fb7b33e75510a81620fc9b4189d1d0315ea1f1e1](https://github.com/PX4/PX4-Autopilot/commit/fb7b33e75510a81620fc9b4189d1d0315ea1f1e1)

### Message
Use updated micro-CDR with memory leak fix (#7838)

* Fixed memory leak (indicated by cppcheck) upstream
### Antipattern Category

### Keyword
memory
### Note


## Commit #495
### Hash
[5f5dca480430bb9af3056768ae05b17e80af5f5d](https://github.com/PX4/PX4-Autopilot/commit/5f5dca480430bb9af3056768ae05b17e80af5f5d)

### Message
vdev: replace static list with an std::map

VDev::getDev() is used in px4_access, which is used in orb_exists. And if
the topic does not exist, it iterates over all 500 indexes, which is slow.
It was slow even if the topic existed, the map reduces runtime from linear
to logarithmic (there are around 80 items in the container).
This is only used on posix.
### Antipattern Category

### Keyword
runtime
### Note


## Commit #496
### Hash
[2b714e079b97976da1b6f633699f7b79f1c01389](https://github.com/PX4/PX4-Autopilot/commit/2b714e079b97976da1b6f633699f7b79f1c01389)

### Message
driver: vdev_posix, increase PX4_MAX_FD (#7905)

 - avoid "exceeded maximum number of file descriptors" when "make posix gazebo_typhoon_h480"

 - closes #7892
### Antipattern Category

### Keyword
increase
### Note


## Commit #497
### Hash
[9dc505150485fd6fe9fbdb70ac1643269b90f3c0](https://github.com/PX4/PX4-Autopilot/commit/9dc505150485fd6fe9fbdb70ac1643269b90f3c0)

### Message
mc_pos_control auto: use current velocity if smaller than velocity setpoint when slowing down
### Antipattern Category

### Keyword
slowing
### Note


## Commit #498
### Hash
[540c0bdafb181b790136737041b7c443545665ab](https://github.com/PX4/PX4-Autopilot/commit/540c0bdafb181b790136737041b7c443545665ab)

### Message
mc_pos_control: accelerate faster
### Antipattern Category

### Keyword
faster
### Note


## Commit #499
### Hash
[3f73a56f5a0af0810c86c9ccb4b4647c6001b00c](https://github.com/PX4/PX4-Autopilot/commit/3f73a56f5a0af0810c86c9ccb4b4647c6001b00c)

### Message
mc_pos_control: accelerate faster in auto and increase speed at 90degrees angle
### Antipattern Category

### Keyword
faster
### Note


## Commit #500
### Hash
[807d45c99c3c224df4e3660494ecf7a4069ad0f5](https://github.com/PX4/PX4-Autopilot/commit/807d45c99c3c224df4e3660494ecf7a4069ad0f5)

### Message
mc_pos_control slowing down close to target take over previous setpoint if low
### Antipattern Category

### Keyword
slowing
### Note


## Commit #501
### Hash
[19e7ba63eee330da07da68e4da650cb273534d98](https://github.com/PX4/PX4-Autopilot/commit/19e7ba63eee330da07da68e4da650cb273534d98)

### Message
param: use separate param save lock

param save is an expensive operation that can take several 100ms. And
previously it was possible that a param_get() caller was blocked on a
save operation. If this happened due to a param change notification,
important modules, such as sensors, could have been blocked for a longer
period (and affecting the flight performance).
With this patch, this situation is not possible anymore, because a param
save now uses the reader lock and a separate file lock.

However it is still possible that a param_set() needs to wait for a save
operation, thus blocking for a longer time. param_set() thus needs to be
avoided in important modules when the system is armed.
In the case of mavlink it works, since it does not affect the flight if
the mavlink receiver is blocked over a longer time. It is only problematic
if a joystick is used as input or in offboard control.
### Antipattern Category

### Keyword
performance
### Note


## Commit #502
### Hash
[d6df692b7a69460642f1efaad967538f8b6ef1c2](https://github.com/PX4/PX4-Autopilot/commit/d6df692b7a69460642f1efaad967538f8b6ef1c2)

### Message
param MPC_MAN_TILT_MAX: decrease maximum from 90 to 85 degrees

At 90 degrees the yaw is extremely unstable (tested with HIL), it
overshoots and only very slowly converges to the correct value.
This behavior is also noticable with lower angles, but not so extreme.
It definitely needs to be looked into further, but for now this makes it
safer.
### Antipattern Category

### Keyword
decrease
### Note


## Commit #503
### Hash
[ea0dd5827bc69ef588654308f030881b9978c51c](https://github.com/PX4/PX4-Autopilot/commit/ea0dd5827bc69ef588654308f030881b9978c51c)

### Message
esc35-v1 nsh: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

   Updated to match master
   This is needed when logger is logging to file and ulog streaming gets
   activated
### Antipattern Category

### Keyword
increase
### Note


## Commit #504
### Hash
[c2394053835fa8e5a56fae8debfbd4311555818c](https://github.com/PX4/PX4-Autopilot/commit/c2394053835fa8e5a56fae8debfbd4311555818c)

### Message
nxphlite-v3 nsh: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

   Updated to match master
   This is needed when logger is logging to file and ulog streaming gets
   activated
### Antipattern Category

### Keyword
increase
### Note


## Commit #505
### Hash
[054d489b96948b05371d49e1885cb359d10bc432](https://github.com/PX4/PX4-Autopilot/commit/054d489b96948b05371d49e1885cb359d10bc432)

### Message
px4-stm32f4discovery nsh: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

   Updated to match master
   This is needed when logger is logging to file and ulog streaming gets
   activated
### Antipattern Category

### Keyword
increase
### Note


## Commit #506
### Hash
[0f5c75b4c6d8dedce159cd1e14c27558f123ddd0](https://github.com/PX4/PX4-Autopilot/commit/0f5c75b4c6d8dedce159cd1e14c27558f123ddd0)

### Message
px4esc-v1 nsh: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

   Updated to match master
   This is needed when logger is logging to file and ulog streaming gets
   activated
### Antipattern Category

### Keyword
increase
### Note


## Commit #507
### Hash
[4e86bc7620bb7aaf655cd84587ca855028ac8ad0](https://github.com/PX4/PX4-Autopilot/commit/4e86bc7620bb7aaf655cd84587ca855028ac8ad0)

### Message
px4nucleoF767ZI-v1 nsh: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

   Updated to match master
   This is needed when logger is logging to file and ulog streaming gets
   activated
### Antipattern Category

### Keyword
increase
### Note


## Commit #508
### Hash
[72cdf1de12c5ef71bb650bf7ceb84cf2463bce01](https://github.com/PX4/PX4-Autopilot/commit/72cdf1de12c5ef71bb650bf7ceb84cf2463bce01)

### Message
sim nsh: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

   Updated to match master
   This is needed when logger is logging to file and ulog streaming gets
   activated
### Antipattern Category

### Keyword
increase
### Note


## Commit #509
### Hash
[edd741ea76c802563bbdf1d23dcb50b056209baf](https://github.com/PX4/PX4-Autopilot/commit/edd741ea76c802563bbdf1d23dcb50b056209baf)

### Message
tap-v1 nsh: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

   Updated to match master
   This is needed when logger is logging to file and ulog streaming gets
   activated
### Antipattern Category

### Keyword
increase
### Note


## Commit #510
### Hash
[4fdce9bf2172c5e35e46079ea0de5d7209d956b4](https://github.com/PX4/PX4-Autopilot/commit/4fdce9bf2172c5e35e46079ea0de5d7209d956b4)

### Message
px4-same70xplained-v1 nsh: increase CONFIG_NFILE_DESCRIPTORS from 53 to 54

   Updated to match master
   This is needed when logger is logging to file and ulog streaming gets
   activated
### Antipattern Category

### Keyword
increase
### Note


## Commit #511
### Hash
[f83df2a9a6a27b4566ed6ddd8ee433529df673a3](https://github.com/PX4/PX4-Autopilot/commit/f83df2a9a6a27b4566ed6ddd8ee433529df673a3)

### Message
Updated nuttx submodule 7.22+

  Updated to latest upstream with PX4 contrib for STM32 I2C that
  fixes an hang in driver.
### Antipattern Category

### Keyword
hang
### Note


## Commit #512
### Hash
[bb71e47ddf5106587df83273364fbf451153ae05](https://github.com/PX4/PX4-Autopilot/commit/bb71e47ddf5106587df83273364fbf451153ae05)

### Message
Updated nuttx submoulde 7.22+ w/i2c fix ==px4_firmware_nuttx-master

   Latest nuttx 7.22+ with PX4 contrib for stm32 f4 I2C hang.
### Antipattern Category

### Keyword
hang
### Note


## Commit #513
### Hash
[55da07d3c42ac48f16c7a587ab42dcc73ef507d2](https://github.com/PX4/PX4-Autopilot/commit/55da07d3c42ac48f16c7a587ab42dcc73ef507d2)

### Message
mc_att_control: fix computation of yaw weight for attitude control

Previously, the yaw weight was based on the tilt angle of the attitude
setpoint (R_sp(2, 2) == cos(tilt angle)). This makes no sense, it means
the weight is low for high tilt angles even if there is no roll-pitch error
at all.

This patch changes the weight computation to be based on the tilt angle
error: the yaw weight is 1 if there is no roll-pitch error (independent
from current tilt angle), and is reduced for higher tilt angle errors.

The weight was added in 05e9a30573f50dd271f10, without any explanation or
derivation of how and why the weight is chosen that way.

However this patch works much better in practice. The yaw control is
improved, though it can be a bit slow to converge if you do continuous &
fast roll-pitch motions (which is expected).
### Antipattern Category

### Keyword
slow
### Note


## Commit #514
### Hash
[f5d9155ab29ffbb7413bd05b0e50567447cfc3f4](https://github.com/PX4/PX4-Autopilot/commit/f5d9155ab29ffbb7413bd05b0e50567447cfc3f4)

### Message
mc_att_control params: reduce default max acro rates from 360 to 120 deg/s

360 is too fast if you just want to hover. Next step is to add expo(),
so that we still have fine-grained control at the center and high rates
at the edges.
### Antipattern Category

### Keyword
fast
### Note


## Commit #515
### Hash
[98893c9f4f80de7eaa194adce09cfb5717b3b8df](https://github.com/PX4/PX4-Autopilot/commit/98893c9f4f80de7eaa194adce09cfb5717b3b8df)

### Message
mc_att_control params: increase max roll/pitch/yaw rates to 1800

If you want to go to the limit of what the vehicle can do, you need to be
able to set it so large that it is guaranteed that it's never limited by
software.

Tests showed that it's not a problem to increase it to very high numbers.
### Antipattern Category

### Keyword
increase
### Note


## Commit #516
### Hash
[29e85edac8311ccd6de5db63c3436a9e2d12da31](https://github.com/PX4/PX4-Autopilot/commit/29e85edac8311ccd6de5db63c3436a9e2d12da31)

### Message
Revert "param MPC_MAN_TILT_MAX: decrease maximum from 90 to 85 degrees"

This reverts commit d6df692b7a69460642f1efaad967538f8b6ef1c2.

The changes to attitude controller improve this a lot.
### Antipattern Category

### Keyword
decrease
### Note


## Commit #517
### Hash
[2246b54e2bf9a41afb6323434fefc7bd190e549a](https://github.com/PX4/PX4-Autopilot/commit/2246b54e2bf9a41afb6323434fefc7bd190e549a)

### Message
FMUv5: Increase USB buffer to increase transfer rates
### Antipattern Category

### Keyword
increase
### Note


## Commit #518
### Hash
[791e420d420e005154c6c66e531bad68e2ee99f8](https://github.com/PX4/PX4-Autopilot/commit/791e420d420e005154c6c66e531bad68e2ee99f8)

### Message
increase max num params per block because of ekf2
### Antipattern Category

### Keyword
increase
### Note


## Commit #519
### Hash
[d096ec0b6107cea5a7c0c34e41e207f53ad66ea7](https://github.com/PX4/PX4-Autopilot/commit/d096ec0b6107cea5a7c0c34e41e207f53ad66ea7)

### Message
vdev_posix: change filemap into a static list of objects instead of pointers

to avoid dynamic memory allocations & frees (specifically in orb_exists)
### Antipattern Category

### Keyword
memory
### Note


## Commit #520
### Hash
[d930ad4e9e50007505ab8d6f8c5e2a4faf8d1b76](https://github.com/PX4/PX4-Autopilot/commit/d930ad4e9e50007505ab8d6f8c5e2a4faf8d1b76)

### Message
mavlink_orb_subscription: reduce orb_exists() check from 10Hz to 3Hz

Checking with 3Hz for new topics should be fast enough.
### Antipattern Category

### Keyword
fast
### Note


## Commit #521
### Hash
[44839208f747c5b1eba95103983dacefc3281b76](https://github.com/PX4/PX4-Autopilot/commit/44839208f747c5b1eba95103983dacefc3281b76)

### Message
jmavsim_run.sh: add more aggressive GC option

This reduces memory usage by roughly 100MB on my laptop
### Antipattern Category

### Keyword
memory
### Note


## Commit #522
### Hash
[b569a8c2b9f6cc1a6f3b5d440f43f0519a744f08](https://github.com/PX4/PX4-Autopilot/commit/b569a8c2b9f6cc1a6f3b5d440f43f0519a744f08)

### Message
fw_pos_control_l1 increase stack by 110 Bytes (#8348)
### Antipattern Category

### Keyword
increase
### Note


## Commit #523
### Hash
[4f5d70bbe55af9d0a38a2c19d410789ccc7d7369](https://github.com/PX4/PX4-Autopilot/commit/4f5d70bbe55af9d0a38a2c19d410789ccc7d7369)

### Message
Increase fixed-wing l1 navigation radius limit
### Antipattern Category

### Keyword
increase
### Note


## Commit #524
### Hash
[66d4a1b3fd5cae58b67ace2d4a1860d06cd9937c](https://github.com/PX4/PX4-Autopilot/commit/66d4a1b3fd5cae58b67ace2d4a1860d06cd9937c)

### Message
Jenkins increase timeout to 30 minutes for now
### Antipattern Category

### Keyword
increase
### Note


## Commit #525
### Hash
[f63c8218e48eed6614dffc4c343a3d3ffca7f1e0](https://github.com/PX4/PX4-Autopilot/commit/f63c8218e48eed6614dffc4c343a3d3ffca7f1e0)

### Message
Jenkins increase test timeout
### Antipattern Category

### Keyword
increase
### Note


## Commit #526
### Hash
[fedc9abb02d8fdc558c05f3d87c5d3cb7bf30350](https://github.com/PX4/PX4-Autopilot/commit/fedc9abb02d8fdc558c05f3d87c5d3cb7bf30350)

### Message
vtol_att_control increase stack by 30 Bytes (1200 -> 1230)
### Antipattern Category

### Keyword
increase
### Note


## Commit #527
### Hash
[ddc544aabe80ae1266d9becf97d49c71079f2dcc](https://github.com/PX4/PX4-Autopilot/commit/ddc544aabe80ae1266d9becf97d49c71079f2dcc)

### Message
Jenkinsfile parallel builds fail fast
### Antipattern Category

### Keyword
fast
### Note


## Commit #528
### Hash
[86ad2ada71360baa7d8f6817dce8416770465f9b](https://github.com/PX4/PX4-Autopilot/commit/86ad2ada71360baa7d8f6817dce8416770465f9b)

### Message
Jenkins remove fast fail

 - this saves build resources, but makes finding the actual failure rather hard (with the current blue ocean gui).
### Antipattern Category

### Keyword
fast
### Note


## Commit #529
### Hash
[eeff52cda7e7be5b1393ecaba3c4e6069c2e5590](https://github.com/PX4/PX4-Autopilot/commit/eeff52cda7e7be5b1393ecaba3c4e6069c2e5590)

### Message
uorb_graph: add .gitignore, change graph file for sitl runtime config
### Antipattern Category

### Keyword
runtime
### Note


## Commit #530
### Hash
[ec57832a8fc2e848264ecb56c402916eff0ee655](https://github.com/PX4/PX4-Autopilot/commit/ec57832a8fc2e848264ecb56c402916eff0ee655)

### Message
FW land detector increase trigger time and cleanup (#8486)
### Antipattern Category

### Keyword
increase
### Note


## Commit #531
### Hash
[f69a6af9899a280ff6ce9960fee901defbb9bbc9](https://github.com/PX4/PX4-Autopilot/commit/f69a6af9899a280ff6ce9960fee901defbb9bbc9)

### Message
Commander: increase stack to ensure enough margin remains
### Antipattern Category

### Keyword
increase
### Note


## Commit #532
### Hash
[2eb3392c39cba63fa9afb7d8b471c9daad64d3fc](https://github.com/PX4/PX4-Autopilot/commit/2eb3392c39cba63fa9afb7d8b471c9daad64d3fc)

### Message
PWM out sim: Increase stack as needed
### Antipattern Category

### Keyword
increase
### Note


## Commit #533
### Hash
[c8a1050323c89f8e776c1ad5f3689505d7130710](https://github.com/PX4/PX4-Autopilot/commit/c8a1050323c89f8e776c1ad5f3689505d7130710)

### Message
libled: allow infinite flashing mode
### Antipattern Category

### Keyword
infinite
### Note


## Commit #534
### Hash
[976b890c56f2028d33a86ad5f5ea19366eb49c9d](https://github.com/PX4/PX4-Autopilot/commit/976b890c56f2028d33a86ad5f5ea19366eb49c9d)

### Message
commander increase stack by 90 bytes (3160 -> 3250)
### Antipattern Category

### Keyword
increase
### Note


## Commit #535
### Hash
[0b9025b2d228e899625b2975efa79250efe2dcca](https://github.com/PX4/PX4-Autopilot/commit/0b9025b2d228e899625b2975efa79250efe2dcca)

### Message
px4fmu-v2: Build individual distance sensors

We are running out of flash memory in px4fmu-v2 so removing all the
distance sensors from binary and adding then individually.
Right now only LeddarOne is not being buid.
### Antipattern Category

### Keyword
memory
### Note


## Commit #536
### Hash
[4bf1980ff64ab49f50a9e57219b6032dd8b7b706](https://github.com/PX4/PX4-Autopilot/commit/4bf1980ff64ab49f50a9e57219b6032dd8b7b706)

### Message
MC_ROLL_P, MC_PITCH_P: increase maximum value to 12

- use the same value for both
- lower control latency allows increasing these gains
### Antipattern Category

### Keyword
increase
### Note


## Commit #537
### Hash
[40675bd1f432490d76a5fe741572c28510f1d8c3](https://github.com/PX4/PX4-Autopilot/commit/40675bd1f432490d76a5fe741572c28510f1d8c3)

### Message
logger: fix potential semaphore counter overflow

When the timer callback is called at a higher rate than the logger can
execute the main loop (which is never the case under normal conditions),
the semaphore counter will increase unbounded, and eventually lead to
an assertion failure in NuttX.
The maximum semaphore counter is 0x7FFF, and when the logger runs at
default rate (3.5ms), the logger task must be blocked for 0x7FFF*3.5/1000
= 114 seconds continuously for an overflow to happen.

I see 2 cases where that could happen:
- the logger execution blocks somehow, or busy-loops in an inner loop
- a higher-prio task runs busy and hogs the CPU over a long period of time
### Antipattern Category

### Keyword
increase
### Note


## Commit #538
### Hash
[bf097d7fa4fcc7a1f35951e4e3180171e8bfad25](https://github.com/PX4/PX4-Autopilot/commit/bf097d7fa4fcc7a1f35951e4e3180171e8bfad25)

### Message
convergence config: increase idle speed in mc mode

- this makes sure that all motors are idling in mc mode. having this too
low can lead to a motor stopping in flight which is critical for
attitude control
- experienced loss of attitude control in RTL during descent prior to this
change

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #539
### Hash
[5a7885610d4a70e99864cdb8e7c9bf7aaa05256c](https://github.com/PX4/PX4-Autopilot/commit/5a7885610d4a70e99864cdb8e7c9bf7aaa05256c)

### Message
fmu: fix PPM publication if RC_SERIAL_PORT is not defined

Before, the RC channel was published as fast as the fmu was running
(around 200Hz in unarmed state).

And fix code style.
### Antipattern Category

### Keyword
fast
### Note


## Commit #540
### Hash
[ff66605a8a09d4c6034dcf2988cea34038650bba](https://github.com/PX4/PX4-Autopilot/commit/ff66605a8a09d4c6034dcf2988cea34038650bba)

### Message
Fix: Increase pwmsim module stack by 100 bytes again because load_mon was giving warning about low stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #541
### Hash
[2bcc5cf3e58a5f29ca13b025e28bb64627a5d04b](https://github.com/PX4/PX4-Autopilot/commit/2bcc5cf3e58a5f29ca13b025e28bb64627a5d04b)

### Message
imu filter defaults: set IMU_GYRO_CUTOFF to 80 and MC_DTERM_CUTOFF to 30

tested on at least 5 different vehicles, including AeroFC. The values
should be conservative, good setups (with low vibrations) can increase
these values even further.

increasing IMU_GYRO_CUTOFF allows for better tuning gains (increased P).
### Antipattern Category

### Keyword
increase
### Note


## Commit #542
### Hash
[cb30d66cefee4052e3fcc7b37fa919967175779b](https://github.com/PX4/PX4-Autopilot/commit/cb30d66cefee4052e3fcc7b37fa919967175779b)

### Message
convergence config: increase multirotor idle speed

- increase the minimum pwm value for multirotor mode since we experienced
the rear motor stalling in certain situations when throttle was low

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #543
### Hash
[b5aded0db2c680ce8e95260c6cc6b69c69d3975d](https://github.com/PX4/PX4-Autopilot/commit/b5aded0db2c680ce8e95260c6cc6b69c69d3975d)

### Message
update vtol mission tests to increase length
### Antipattern Category

### Keyword
increase
### Note


## Commit #544
### Hash
[01340df54521f06dc4a69070abd34cda9b941efc](https://github.com/PX4/PX4-Autopilot/commit/01340df54521f06dc4a69070abd34cda9b941efc)

### Message
Jenkins cleanup build creation

 - cleanup workspace when done and increase retention
### Antipattern Category

### Keyword
increase
### Note


## Commit #545
### Hash
[8a4d51c630fc7d09842464cd79efa7b9e5995666](https://github.com/PX4/PX4-Autopilot/commit/8a4d51c630fc7d09842464cd79efa7b9e5995666)

### Message
FlightTasks: replaced all hrt_elapsed() calls and unneeded hrt_ calls to safe performance
### Antipattern Category

### Keyword
performance
### Note


## Commit #546
### Hash
[b5ecf9824d9dd7db7e9709dac614af64906626a3](https://github.com/PX4/PX4-Autopilot/commit/b5ecf9824d9dd7db7e9709dac614af64906626a3)

### Message
flight tasks: use placement new to reduce memory overhead and the need for dynamic allocations

In addition, we will need some shared data structure for the uorb
subscriptions.
### Antipattern Category

### Keyword
memory
### Note


## Commit #547
### Hash
[2b6e356c9175743f4b43c425ad527da4a4e361ab](https://github.com/PX4/PX4-Autopilot/commit/2b6e356c9175743f4b43c425ad527da4a4e361ab)

### Message
FlightTaskManual: fix for the sideways oscillations in fast foward flight when using the vehicle yaw estimate
### Antipattern Category

### Keyword
fast
### Note


## Commit #548
### Hash
[59f3de192f8c553a45aa8f1c54c1ee840df57d60](https://github.com/PX4/PX4-Autopilot/commit/59f3de192f8c553a45aa8f1c54c1ee840df57d60)

### Message
ManualSmoothingXY: velocity as criteria for direction change to prenvent fast acceleration at low spped
### Antipattern Category

### Keyword
fast
### Note

## Commit #549
### Hash
[7ac3c97aad041bd38b601db33d0f905a91878014](https://github.com/PX4/PX4-Autopilot/commit/7ac3c97aad041bd38b601db33d0f905a91878014)

### Message
Improve the Crazyflie MAVLink tunnel to increase efficiency

This change fragments MAVLink packets more efficiently and therefore increases the net throughput. This in turn makes the connection significantly more stable and the Crazyflie experience overall more usable.
### Antipattern Category

### Keyword
increase
### Note


## Commit #550
### Hash
[da57dbbce0c6985a51bba156d72d6a833d4bcac1](https://github.com/PX4/PX4-Autopilot/commit/da57dbbce0c6985a51bba156d72d6a833d4bcac1)

### Message
Increase the MavLink module stack size
### Antipattern Category

### Keyword
increase
### Note


## Commit #551
### Hash
[c16e17f47b5ac50c72ca90c37ac6a5936f782027](https://github.com/PX4/PX4-Autopilot/commit/c16e17f47b5ac50c72ca90c37ac6a5936f782027)

### Message
mag_calibration: only allocate as much memory as needed
### Antipattern Category

### Keyword
memory
### Note


## Commit #552
### Hash
[e7e791fb1a9a8b06e33f58661bbf03dab080c622](https://github.com/PX4/PX4-Autopilot/commit/e7e791fb1a9a8b06e33f58661bbf03dab080c622)

### Message
tailsitter: use forward transition throttle for climb-rate controlled mode

- the mc pos controller will decrease throttle during the transition
and thus the vehicle will not pick up enough airspeed to complete the
transition

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category

### Keyword
decrease
### Note


## Commit #553
### Hash
[694df08b37fa14b520ad3b61f8bcb924926e3d9b](https://github.com/PX4/PX4-Autopilot/commit/694df08b37fa14b520ad3b61f8bcb924926e3d9b)

### Message
posix-configs: better tailsitter front transition parameters

- reduce height increase during front transition

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #554
### Hash
[7fa91ad3dd29816ff11bd85103b67604fdeb5f9f](https://github.com/PX4/PX4-Autopilot/commit/7fa91ad3dd29816ff11bd85103b67604fdeb5f9f)

### Message
posix-configs: increase tailsitter land speed

Signed-off-by: Roman <bapstroman@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #555
### Hash
[58c757a9db1b93051416f4919df7adb4d92db410](https://github.com/PX4/PX4-Autopilot/commit/58c757a9db1b93051416f4919df7adb4d92db410)

### Message
mc_att_control_params: increase max acro rates to 1800

This matches the maximum rates for the attitude controller.
### Antipattern Category

### Keyword
increase
### Note


## Commit #556
### Hash
[f2703abce0f3f689f3791ea6534e6c469df7e6d9](https://github.com/PX4/PX4-Autopilot/commit/f2703abce0f3f689f3791ea6534e6c469df7e6d9)

### Message
top: increase process priority to 255

Helps debugging busy-looping tasks.
### Antipattern Category

### Keyword
increase
### Note


## Commit #557
### Hash
[f49fd2acc75608bc9962897435ab84f4d57e35c6](https://github.com/PX4/PX4-Autopilot/commit/f49fd2acc75608bc9962897435ab84f4d57e35c6)

### Message
crazyflie: increase imu reading rate
### Antipattern Category

### Keyword
increase
### Note


## Commit #558
### Hash
[8b54346d52c4b3af9893b95b329fe1896e4104fd](https://github.com/PX4/PX4-Autopilot/commit/8b54346d52c4b3af9893b95b329fe1896e4104fd)

### Message
mpu9250: decrease sampling rate when using i2c
### Antipattern Category

### Keyword
decrease
### Note


## Commit #559
### Hash
[384028aa7bae5e2461739caf2ba5add3aba66d4d](https://github.com/PX4/PX4-Autopilot/commit/384028aa7bae5e2461739caf2ba5add3aba66d4d)

### Message
decrease rollrate P gain due to gimbal oscillations
### Antipattern Category

### Keyword
decrease
### Note


## Commit #560
### Hash
[aee05d0ac5dae6aae0827210b5ca1d87abbf3cc9](https://github.com/PX4/PX4-Autopilot/commit/aee05d0ac5dae6aae0827210b5ca1d87abbf3cc9)

### Message
FMU: Increase stack space as needed (shown by instrumentation) to retain a 300 bytes buffer.
### Antipattern Category

### Keyword
increase
### Note


## Commit #561
### Hash
[a76c82f5f2e8455cd1db36b3145357b1d3f04221](https://github.com/PX4/PX4-Autopilot/commit/a76c82f5f2e8455cd1db36b3145357b1d3f04221)

### Message
airframes: update 4050 generic 250 racer defaults

- P and D gains are too high for a racer
- default I gain is too low (0.25 is still quite low)
- use the thrust curve param instead of TPA
- improve responsiveness in Manual & increase max tilt angle to 60 degrees
- enable one-shot
- enable high-rate logging profile
- disable RC filter
### Antipattern Category

### Keyword
increase
### Note


## Commit #562
### Hash
[fc29e789781f62880ae998fdcc35068cc5f19c23](https://github.com/PX4/PX4-Autopilot/commit/fc29e789781f62880ae998fdcc35068cc5f19c23)

### Message
Update submodule ecl to latest Sat Jun  9 15:26:38 CDT 2018

    - ecl in PX4/Firmware (f7937d783496e954efc52439148ef66824d9c80a): https://github.com/PX4/ecl/commit/1fdf33b343e361de6410515a0359f3cb7f34d499
    - ecl current upstream: https://github.com/PX4/ecl/commit/d177e96508d2572f6fa8eb7ff41852749c882548
    - Changes: https://github.com/PX4/ecl/compare/1fdf33b343e361de6410515a0359f3cb7f34d499...d177e96508d2572f6fa8eb7ff41852749c882548

    d177e96 2018-06-08 Paul Riseborough - EKF: Fix bug causing slow drift when high rate flow data is used
ee2dc7d 2018-05-30 Paul Riseborough - EKF: Rework optical flow selection logic
e383b6a 2018-05-29 Paul Riseborough - EKF: rework optical flow selection logic
487e6a0 2018-05-28 Paul Riseborough - EKF: enable user selection of auto mag free operation
6bdbe03 2018-05-28 Paul Riseborough - EKF: Fallback to optical flow for all in-flight loss of navigation scenarios
b4d2b8c 2018-05-19 Mohammed Kabir - EKF : introduce new architechture for navigation limits
8a71339 2018-05-19 Paul Riseborough - EKF: Improve ground effect compensation
39697f1 2018-05-18 Paul Riseborough - EKF: rework optical flow switching
1cfe845 2018-05-18 Paul Riseborough - EKF: rework GPS quality check
99a8038 2018-05-18 Paul Riseborough - EKF: improve optical flow GPS quality checking
7f36add 2018-05-18 Paul Riseborough - EKF: scale GPS vertical accuracy check when using optical flow
fc9f532 2018-05-18 Paul Riseborough - EKF: relax range finder data continuity check
93c456f 2018-05-18 Paul Riseborough - EKF: Improve protection against badly conditioned dVel bias covariances
225057a 2018-05-18 Paul Riseborough - EKF: Fix bug preventing use of terrain estimator
adb4a09 2018-05-17 Paul Riseborough - EKF: Fix bug causing large yaw innovations when GPS is lost
f59cd0f 2018-05-16 Paul Riseborough - EKF: Don't make detection of indoor operation dependent on optical flow
1562a82 2018-05-16 Paul Riseborough - EKF: Add parameter to adjust on-ground movement detector sensitivity
ea9e824 2018-05-16 Paul Riseborough - EKF: Improve detection of indoor flight condition
565f992 2018-05-16 Paul Riseborough - EKF: Reduce effect of yaw gyro bias when using optical flow indoors
e10798b 2018-05-16 Paul Riseborough - EKF: Add on ground movement detector
2d3b652 2018-05-15 Paul Riseborough - EKF: Reset yaw gyro bias learning when resuming use of magnetometer
8191068 2018-05-15 Paul Riseborough - EKF: Don't start using mag if optical flow use is interrupted
4889e84 2018-05-15 Paul Riseborough - EKF: Don't fuse multi rotor drag if yaw angle is bad
092a8d8 2018-05-15 Paul Riseborough - EKF: Fix GPS validity time check error
0160aaa 2018-05-15 Paul Riseborough - EKF: Don't use magnetometer with optical flow only nav if GPS checks are failing
8451676 2018-05-14 Paul Riseborough - EKF: Use stricter GPS accuracy test when optical flow is being used
a80b3ab 2018-05-27 Daniel Agar - set MODULE define for each library
### Antipattern Category

### Keyword
slow
### Note


## Commit #563
### Hash
[753ad0e0dff612a424652d8dfcaff397dfd903de](https://github.com/PX4/PX4-Autopilot/commit/753ad0e0dff612a424652d8dfcaff397dfd903de)

### Message
Fixed-wing autoland: Fix bug that could cause a steep pitch increase and thus aircraft stall during the flare (#9674)
### Antipattern Category

### Keyword
increase
### Note


## Commit #564
### Hash
[84841236cbe26fdfdcd9ac05af93ad8bd0c9f45a](https://github.com/PX4/PX4-Autopilot/commit/84841236cbe26fdfdcd9ac05af93ad8bd0c9f45a)

### Message
mavlink: allow resetting mavlink streams to default via MAV_CMD_SET_MESSAGE_INTERVAL

This implementation does not need more resources.
It's not super efficient in terms of runtime, but it's also not something
that is called often.
### Antipattern Category

### Keyword
runtime
### Note


## Commit #565
### Hash
[bb8e653469e67afb43dbb9ecf3899cf50ef6162f](https://github.com/PX4/PX4-Autopilot/commit/bb8e653469e67afb43dbb9ecf3899cf50ef6162f)

### Message
mc_att_control: keep integral enabled based on land detector

Previously the rate controller disabled updating the integral below 20%
throttle. This is not ideal for several reasons:
- some racers already hover with 20% throttle.
- for acro it is important to always keep the integral enabled, it has a
  noticeable effect on flight performance.
### Antipattern Category

### Keyword
performance
### Note


## Commit #566
### Hash
[8825bbed298a234087db2410393553cd491f1da8](https://github.com/PX4/PX4-Autopilot/commit/8825bbed298a234087db2410393553cd491f1da8)

### Message
Increase the stack size for the IridiumSBD driver
### Antipattern Category

### Keyword
increase
### Note


## Commit #567
### Hash
[a76c4c55d43122b769b9e114e1c0b39ba06e7147](https://github.com/PX4/PX4-Autopilot/commit/a76c4c55d43122b769b9e114e1c0b39ba06e7147)

### Message
Decrease default flare altitude. The previous value was way too high for any small aircraft. It was also unsafe because after the flar, pitch is currently controlled open-loop, which means that stall can potentially happen during the flare
### Antipattern Category

### Keyword
decrease
### Note


## Commit #568
### Hash
[74c20a0fd536e1b8725c4e91a3ba28c6baf9ecce](https://github.com/PX4/PX4-Autopilot/commit/74c20a0fd536e1b8725c4e91a3ba28c6baf9ecce)

### Message
ADIS16477 reset on init and increase delay
### Antipattern Category

### Keyword
increase
### Note


## Commit #569
### Hash
[1feccfcc817220707adec19486ac03a649a9d2e9](https://github.com/PX4/PX4-Autopilot/commit/1feccfcc817220707adec19486ac03a649a9d2e9)

### Message
frsky_telemetry: increase stack size by 52 bytes

As indicated in previous logs (268 bytes left).
### Antipattern Category

### Keyword
increase
### Note


## Commit #570
### Hash
[21cc34befbf18c52d4f9add0466044592638d89e](https://github.com/PX4/PX4-Autopilot/commit/21cc34befbf18c52d4f9add0466044592638d89e)

### Message
GPS driver increase stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #571
### Hash
[e1a74727389a9e3abf1021128960476fe72eea71](https://github.com/PX4/PX4-Autopilot/commit/e1a74727389a9e3abf1021128960476fe72eea71)

### Message
MavlinkOrbSubscription::update: improve performance & fix corner case

- reorders operations, such that the most expensive one (orb_copy) is done
  only when really needed.
- corner case: when the topic was not advertised yet, orb_stat() would fail
  and then update() was called, which succeeds for the first advertisement.
  In that case the timestamp was incorrectly set to 0 and true was
  returned.
  The next call would again return true, because the timestamp was updated,
  but the topic data was still the same.

Reduces CPU load by ~2% on a Pixracer.
### Antipattern Category

### Keyword
performance
### Note


## Commit #572
### Hash
[9362f844f498dd41ae26889570f7fd1d9555867f](https://github.com/PX4/PX4-Autopilot/commit/9362f844f498dd41ae26889570f7fd1d9555867f)

### Message
position control: fix failsafe thrust

invert direction to point upwards and increase to 70% of throttle range between min and hover
### Antipattern Category

### Keyword
increase
### Note


## Commit #573
### Hash
[1db1155697d8ea7ff9a33d82401df39290a11d5a](https://github.com/PX4/PX4-Autopilot/commit/1db1155697d8ea7ff9a33d82401df39290a11d5a)

### Message
px4fmu-v5:Comment and define SAFETY LED and Button so FMU can use

  Safety Switch is HW version dependent on having an PX4IO
  So we init to a benign state with the _INIT definition
  and provide the the non _INIT one for the driver to make a run time
  decision to use it.

  We also define the FMU GPIO_BTN_SAFETY and GPIO_LED_SAFETY alias
  so the px4fmu will drrive will be built with the safety switch
  code at compile time and have runtime control via the manifest
### Antipattern Category

### Keyword
runtime
### Note


## Commit #574
### Hash
[3ea3c1f537171a9a790a2b18384b4d1ec1bf0523](https://github.com/PX4/PX4-Autopilot/commit/3ea3c1f537171a9a790a2b18384b4d1ec1bf0523)

### Message
px4fmu-v5:Runtime Safety LED support.

   Safety Switch is HW version dependent on having an PX4IO
   So we init to a benign state with the _INIT definition
   and use the non _INIT verion in the driver if the run time
   decision is we do not have a PX4IO
### Antipattern Category

### Keyword
runtime
### Note


## Commit #575
### Hash
[fc16dce8f1856f9b9ae26e32bc0e65d15dde7a70](https://github.com/PX4/PX4-Autopilot/commit/fc16dce8f1856f9b9ae26e32bc0e65d15dde7a70)

### Message
spektrum_rssi: initialize rssi lookup as constexpr

Rather than initializing the rssi percentage lookup table at runtime
on the heap, we would like it to be stored in flash.

This change pre-computes the rssi lookup table.
### Antipattern Category

### Keyword
runtime
### Note


## Commit #576
### Hash
[7753dd4b4e5a8e72caede3a1c066ee9d9c1de347](https://github.com/PX4/PX4-Autopilot/commit/7753dd4b4e5a8e72caede3a1c066ee9d9c1de347)

### Message
refactor uorb: inline orb_publish_auto

It is a very small core function that needs to be fast.
### Antipattern Category

### Keyword
fast
### Note


## Commit #577
### Hash
[c6190093645b5e926cfb66dfb91e8062c8ffb4d1](https://github.com/PX4/PX4-Autopilot/commit/c6190093645b5e926cfb66dfb91e8062c8ffb4d1)

### Message
FlightTask StraightLine: replace powf(x,2) with x*x

Apparently this is faster
### Antipattern Category

### Keyword
faster
### Note


## Commit #578
### Hash
[d7b2b48baddfea9a65fbd30ed3312aab660836a0](https://github.com/PX4/PX4-Autopilot/commit/d7b2b48baddfea9a65fbd30ed3312aab660836a0)

### Message
tap_esc increase stack 1100 -> 1180 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #579
### Hash
[0069141ffc38f277f53a20860e2ab5a9bfc0e476](https://github.com/PX4/PX4-Autopilot/commit/0069141ffc38f277f53a20860e2ab5a9bfc0e476)

### Message
px4fmu increase actuator controls poll timeout
### Antipattern Category

### Keyword
increase
### Note


## Commit #580
### Hash
[00ebffb0dd9796a6dea0d24b82a0c33159316041](https://github.com/PX4/PX4-Autopilot/commit/00ebffb0dd9796a6dea0d24b82a0c33159316041)

### Message
uorb tests: run at max priority & increase stack size

- running at max priority significantly decreases jitter for the latency
  test, providing more consistent results
- stack size increase is required for the latency test
### Antipattern Category

### Keyword
increase
### Note


## Commit #581
### Hash
[e989c80205e22d11e5346bda3d11f90cdf294dfc](https://github.com/PX4/PX4-Autopilot/commit/e989c80205e22d11e5346bda3d11f90cdf294dfc)

### Message
replay: fix potential invalid memory access

_subscriptions is a vector that is resized when needed. However there could
still be references to elements in the vector when the resize happens.
These references then become invalid.
Using a vector of pointers fixes that.
### Antipattern Category

### Keyword
memory
### Note


## Commit #582
### Hash
[9551dcb49714c6783b449774f81af4287ade05d5](https://github.com/PX4/PX4-Autopilot/commit/9551dcb49714c6783b449774f81af4287ade05d5)

### Message
logger increase log_writer_file stack 1072 -> 1150
### Antipattern Category

### Keyword
increase
### Note


## Commit #583
### Hash
[f414d0c41377e7846a7e5b7d23e9266f3f27e08d](https://github.com/PX4/PX4-Autopilot/commit/f414d0c41377e7846a7e5b7d23e9266f3f27e08d)

### Message
SYS_COMPANION: add 1500000 baud to metadata & increase the data rate
### Antipattern Category

### Keyword
increase
### Note


## Commit #584
### Hash
[30fb82d9b4157b74c741ec7e1e16d7408e5dfa3f](https://github.com/PX4/PX4-Autopilot/commit/30fb82d9b4157b74c741ec7e1e16d7408e5dfa3f)

### Message
fmu-v5 defconfig: increase USART3 from 1500 to 3000

This is needed for companions with high baudrate and high data rate.
Tested with 1500000 Baudrate and mavlink TX rate of ~120KB/s: no drops.

I did not test the exact limit, something like 2500 might be enough. But
we (still) have enough free RAM on FMU-v5.
### Antipattern Category

### Keyword
increase
### Note


## Commit #585
### Hash
[e356fd89b01d5c120f090e114c0048c620daa491](https://github.com/PX4/PX4-Autopilot/commit/e356fd89b01d5c120f090e114c0048c620daa491)

### Message
CI mission tests add FW and cleanup (#10250)

* jenkins: decrease VTOL mission alt and FW mission use simple land wps

* startup: decrease min airspeed scaling factor for landing

* jenkins: FW mission include loiter_to_alt cmd
### Antipattern Category

### Keyword
decrease
### Note


## Commit #586
### Hash
[a24fdb93c38cdedc91041bdc81238815b9d4b023](https://github.com/PX4/PX4-Autopilot/commit/a24fdb93c38cdedc91041bdc81238815b9d4b023)

### Message
FlightTaskManual: increase rc timeout to 1.5 x COM_RC_LOSS_T
### Antipattern Category

### Keyword
increase
### Note


## Commit #587
### Hash
[4f2aa517679bf442adf2b506b2ae7784cabf0a6e](https://github.com/PX4/PX4-Autopilot/commit/4f2aa517679bf442adf2b506b2ae7784cabf0a6e)

### Message
px4_impl_os:Use the defconfig CONFIG_ARMV7M_STACKCHECK

  To enable coherent runtime stack checking use the boards
  CONFIG_ARMV7M_STACKCHECK setting
### Antipattern Category

### Keyword
runtime
### Note


## Commit #588
### Hash
[1b6e933176cf0e011f9f8a720b9007654997e082](https://github.com/PX4/PX4-Autopilot/commit/1b6e933176cf0e011f9f8a720b9007654997e082)

### Message
Make.defs.in:Runtime Stack Checking in Nuttx Build

  Use CONFIG_ARMV7M_STACKCHECK to add the instrumentation
  for runtime stack checking
### Antipattern Category

### Keyword
runtime
### Note


## Commit #589
### Hash
[ac298664c7f451f13f938b900e6a463fd39b58ef](https://github.com/PX4/PX4-Autopilot/commit/ac298664c7f451f13f938b900e6a463fd39b58ef)

### Message
nuttx-configs increase idle thread stack size to 750 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #590
### Hash
[b75fa645cef4c3cafb0a44a0c253423cad5c8231](https://github.com/PX4/PX4-Autopilot/commit/b75fa645cef4c3cafb0a44a0c253423cad5c8231)

### Message
bmp280 increase MAIN stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #591
### Hash
[2dd71fa73c76977f3a68ebd98cd82000f9d32d4c](https://github.com/PX4/PX4-Autopilot/commit/2dd71fa73c76977f3a68ebd98cd82000f9d32d4c)

### Message
mpu6000 increase MAIN stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #592
### Hash
[1a0472dfab6d3d62e38f3aeeca6962084e8e1d8a](https://github.com/PX4/PX4-Autopilot/commit/1a0472dfab6d3d62e38f3aeeca6962084e8e1d8a)

### Message
sensors increase MAIN stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #593
### Hash
[ea73284a1fce0a43ac757200da2530743f6f2a95](https://github.com/PX4/PX4-Autopilot/commit/ea73284a1fce0a43ac757200da2530743f6f2a95)

### Message
uORB tests increase stack sizes
### Antipattern Category

### Keyword
increase
### Note


## Commit #594
### Hash
[6abd0c2672db415b5f62dc36942e58f84a08ae7e](https://github.com/PX4/PX4-Autopilot/commit/6abd0c2672db415b5f62dc36942e58f84a08ae7e)

### Message
BMI055 increase MAIN stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #595
### Hash
[ee90eb6c92b03c27f6a123f5c36d2df9b9bedc7e](https://github.com/PX4/PX4-Autopilot/commit/ee90eb6c92b03c27f6a123f5c36d2df9b9bedc7e)

### Message
IST8310 increase MAIN stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #596
### Hash
[2dbc95382edf08eb125e775b6fc69dc545e019c0](https://github.com/PX4/PX4-Autopilot/commit/2dbc95382edf08eb125e775b6fc69dc545e019c0)

### Message
rgbled increase MAIN stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #597
### Hash
[d6fd1c48115c8849d593216e65de4983a40ebda3](https://github.com/PX4/PX4-Autopilot/commit/d6fd1c48115c8849d593216e65de4983a40ebda3)

### Message
rgbled_pwm increase MAIN stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #598
### Hash
[d7580aa676b502b755281a0c7a7e5780b1df9066](https://github.com/PX4/PX4-Autopilot/commit/d7580aa676b502b755281a0c7a7e5780b1df9066)

### Message
px4fmu-v5 increase CONFIG_USERMAIN_STACKSIZE slightly
### Antipattern Category

### Keyword
increase
### Note


## Commit #599
### Hash
[3996ab1fc551140dc91b7d92500662ca98d00e0b](https://github.com/PX4/PX4-Autopilot/commit/3996ab1fc551140dc91b7d92500662ca98d00e0b)

### Message
frsky_telemetry increase MAIN stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #600
### Hash
[066ca50ddff7d0552437ad9909b4ae04e5b0a5d9](https://github.com/PX4/PX4-Autopilot/commit/066ca50ddff7d0552437ad9909b4ae04e5b0a5d9)

### Message
mission test temporarily increase landed timeout 60s -> 120s (#10596)

 - revert once #10590 is resolved properly
### Antipattern Category

### Keyword
increase
### Note


## Commit #601
### Hash
[72f85e4b2d9addf893aeee24e778855ed7054d65](https://github.com/PX4/PX4-Autopilot/commit/72f85e4b2d9addf893aeee24e778855ed7054d65)

### Message
ekf2: Handle blending of dissimilar rate GPS data (#10570)

A filtered update update interval is calculated for each receiver.

If dissimilar interval data is detected, blending occurs when data is received from the slower of the receivers.

If similar interval data is detected, blending occurs when receiver data with similar time stamps is available.

If no data is received from either receiver for longer than 300msec, then no blending will be performed and the most recent data will be used instead.
### Antipattern Category

### Keyword
slower
### Note


## Commit #602
### Hash
[b83cb795960c7ad752586f74b60cac7231bb7d39](https://github.com/PX4/PX4-Autopilot/commit/b83cb795960c7ad752586f74b60cac7231bb7d39)

### Message
Update submodule DriverFramework to latest Sun Sep 30 08:37:23 EDT 2018 (#10604)

    - DriverFramework in PX4/Firmware (1ce7e8d89a16262afe07d7487e55a2ec05985627): https://github.com/PX4/DriverFramework/commit/721ace3e797f141f0950144bace6a30f6aa1325a

    - DriverFramework current upstream: https://github.com/PX4/DriverFramework/commit/9f456acb3c8d70df3cd8906123388935dd6303f6

    - Changes: https://github.com/PX4/DriverFramework/compare/721ace3e797f141f0950144bace6a30f6aa1325a...9f456acb3c8d70df3cd8906123388935dd6303f6



    9f456ac 2018-09-30 Bart Slinger - Increase DriverFramework priority to SCHED_PRIORITY_MAX
### Antipattern Category

### Keyword
increase
### Note


## Commit #603
### Hash
[6647471238280fae789927f451e15258a286159a](https://github.com/PX4/PX4-Autopilot/commit/6647471238280fae789927f451e15258a286159a)

### Message
ekf2: increase maximum of EKF2_MAG_YAWLIM. This is needed on some fw platforms
in order to not constantly switch mag fusion mode in gusty winds.
### Antipattern Category

### Keyword
increase
### Note


## Commit #604
### Hash
[d6e820fe671922813d17ac190a6bd2232ea61c6f](https://github.com/PX4/PX4-Autopilot/commit/d6e820fe671922813d17ac190a6bd2232ea61c6f)

### Message
logger: add mission file to LogWriterFile backend

Not used yet, it should not affect anything, except for slight RAM
increase.
### Antipattern Category

### Keyword
increase
### Note


## Commit #605
### Hash
[234ec7f2a21d408251784b8653bd42f2803db530](https://github.com/PX4/PX4-Autopilot/commit/234ec7f2a21d408251784b8653bd42f2803db530)

### Message
logger: add mission log to frontend, configurable via SDLOG_MISSION

- mission logs are stored in a separate directory mission_log
- It's disabled by default
- Does not increase RAM usage if disabled (if enabled, only 300 bytes)
- Log rotate does not apply to the mission logs
### Antipattern Category

### Keyword
increase
### Note


## Commit #606
### Hash
[95cc6a06f310061c3261bfb422f97a14187166ad](https://github.com/PX4/PX4-Autopilot/commit/95cc6a06f310061c3261bfb422f97a14187166ad)

### Message
mc_att_control: separate attitude controller from rate controller update

This will allow to run the rate controller faster than the attitude
controller.
### Antipattern Category

### Keyword
faster
### Note


## Commit #607
### Hash
[bec43b0b28e6817fb23e0ef323ed929ce65360ed](https://github.com/PX4/PX4-Autopilot/commit/bec43b0b28e6817fb23e0ef323ed929ce65360ed)

### Message
mc_att_control: run rate controller first and increase fmu prio by one

The rate controller is now run directly after a gyro publication, and
as soon as it publishes the actuator controls, the output driver (fmu/...)
runs.

Test on a Pixracer:
Reduces fmu control latency from 219us to 134us.
If we run the rate controller last (same order as before, just increase
the prio), the latency is 201us.

CPU load is unchanged.

The drawback is that the attitude to rate setpoint generation is delayed
by one cycle (4ms), but it will be reduced to 1ms as soon as we run at
1kHz.
### Antipattern Category

### Keyword
increase
### Note


## Commit #608
### Hash
[428c2f72bded828499e4113d4392be258d114e2f](https://github.com/PX4/PX4-Autopilot/commit/428c2f72bded828499e4113d4392be258d114e2f)

### Message
mavlink: always acknowledge a param write

This change has two effects:
1. We always acknowledge a param write no matter if the value was
   actually changed or not. This is according to the spec:
   https://mavlink.io/en/services/parameter.html#write-parameters
2. This fixes the bug where int32 parameters were not actually acked
   because the memory of the param value was casted directly to float
   and then compared. In the case of a int32 parameter set from 0 to 1
   it would mean that the cast to float of the memory representation
   was still 0 and therefore it was assumed to be "no change" and the
   ack was omitted.
### Antipattern Category

### Keyword
memory
### Note


## Commit #609
### Hash
[e91db7b4d2694cd7a1c11b07e979fbbbb5561e99](https://github.com/PX4/PX4-Autopilot/commit/e91db7b4d2694cd7a1c11b07e979fbbbb5561e99)

### Message
uORBDeviceNode: move flags from SubscriberData to UpdateIntervalData

As there is only one bit used in 'flags', and it is only used in case
update_interval is not null, we can move the bit to UpdateIntervalData.

The size of UpdateIntervalData does not increase (on 32 bit).

Reduces RAM usage by 3.6KB (tested on a Pixracer).
### Antipattern Category

### Keyword
increase
### Note


## Commit #610
### Hash
[c9e52d43862b6854d4396b2190cb4b9f1b957c0b](https://github.com/PX4/PX4-Autopilot/commit/c9e52d43862b6854d4396b2190cb4b9f1b957c0b)

### Message
MPC_MAN_TILT_MAX: increase max limit from 90 to 180 degrees

This is especially useful for testing (the vehicle must behave correctly
even at high tilt angles).
### Antipattern Category

### Keyword
increase
### Note


## Commit #611
### Hash
[d852ce20e6504abc02e6aba38b9755540f5de101](https://github.com/PX4/PX4-Autopilot/commit/d852ce20e6504abc02e6aba38b9755540f5de101)

### Message
MPC - Increase max velocity integral gain to 3.0
### Antipattern Category

### Keyword
increase
### Note


## Commit #612
### Hash
[8566b6b53e95ad8f4b16acb9e48308ecf7ef5040](https://github.com/PX4/PX4-Autopilot/commit/8566b6b53e95ad8f4b16acb9e48308ecf7ef5040)

### Message
AV-X increase logger buffer
### Antipattern Category

### Keyword
increase
### Note


## Commit #613
### Hash
[93802c27102dc4c06c2128c5939605676ad09750](https://github.com/PX4/PX4-Autopilot/commit/93802c27102dc4c06c2128c5939605676ad09750)

### Message
hysteresis test increase time on cygwin (#10958)
### Antipattern Category

### Keyword
increase
### Note


## Commit #614
### Hash
[cf6665625847e2ec237e78ce971b4ddd8098fa03](https://github.com/PX4/PX4-Autopilot/commit/cf6665625847e2ec237e78ce971b4ddd8098fa03)

### Message
mixer multirotor: add unit-tests

To run:
cd src/lib/mixer
make tests

This will validate the C++ implementation by taking the python
implementation as ground-truth. It runs through various actuator control
command values for all airmode variations and several mixer types.

The python script also allows to prototype new mixer algorithms.

It is not integrated into the existing build system, because it's easier
to use that way, with less dependencies, and faster testing workflow.
It could however be a bit more integrated.

Reference: https://github.com/Auterion/Flight_Control_Prototyping_Scripts/tree/master/control_allocation
### Antipattern Category

### Keyword
faster
### Note


## Commit #615
### Hash
[d676325ea50288b8d106a2ccc83f5783d9dfb445](https://github.com/PX4/PX4-Autopilot/commit/d676325ea50288b8d106a2ccc83f5783d9dfb445)

### Message
Update Nuttx with env out of memory fix
### Antipattern Category

### Keyword
memory
### Note


## Commit #616
### Hash
[3b3752b753c09a587646505dd89f1d6b2de888f6](https://github.com/PX4/PX4-Autopilot/commit/3b3752b753c09a587646505dd89f1d6b2de888f6)

### Message
pmw3901 increase publish rate and max_ground_distance (#11066)

* increase pmw3901 publish rate and max_ground_distance

* set work queue to high priority
### Antipattern Category

### Keyword
increase
### Note


## Commit #617
### Hash
[8cdb65eed90371029bad943a6d1dd912eb5d46ec](https://github.com/PX4/PX4-Autopilot/commit/8cdb65eed90371029bad943a6d1dd912eb5d46ec)

### Message
lockstep_scheduler: simplify LockstepScheduler::cond_timedwait & reduce locking

- the loop is not needed
- we optimize for the fast case and lock only if really needed
### Antipattern Category

### Keyword
fast
### Note


## Commit #618
### Hash
[ecbe2a3e0bf422dc6a4504762bc57757cd602869](https://github.com/PX4/PX4-Autopilot/commit/ecbe2a3e0bf422dc6a4504762bc57757cd602869)

### Message
drv_hrt posix: improve performance for hrt_absolute_time()

Previously hrt_absolute_time() was at around 5% of the total CPU usage, now
it's around 0.35%.
### Antipattern Category

### Keyword
performance
### Note


## Commit #619
### Hash
[95eff332632f59ad3584a25169ce92691f7b0222](https://github.com/PX4/PX4-Autopilot/commit/95eff332632f59ad3584a25169ce92691f7b0222)

### Message
GPS increase task stack 1530 -> 1600 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #620
### Hash
[b7bcec2d8c06ce8f1797a24d21229bc4b0dc1d28](https://github.com/PX4/PX4-Autopilot/commit/b7bcec2d8c06ce8f1797a24d21229bc4b0dc1d28)

### Message
HRT: Create new separate call for atomic HRT elapsed time calculation
This call rarely needs to be truly atomic and the involved CPU overhead in making it atomic was unnecessary and introduces a lot of IRQ jitter with no value-add. The call has been moved to be non-atomic and the codebase will be inspected and changed in follow-up commits for the few instances where it is truly needed.
### Antipattern Category

### Keyword
overhead
### Note


## Commit #621
### Hash
[46390a150833be226a7ab298aa414b748580cea9](https://github.com/PX4/PX4-Autopilot/commit/46390a150833be226a7ab298aa414b748580cea9)

### Message
HRT: Drop volatile specifier from function call for non-atomic mode

This allows the compiler to optimize better without loosing any performance / accuracy.
### Antipattern Category

### Keyword
performance
### Note


## Commit #622
### Hash
[88d0b163b52803a38e9c316f1ccaf43b4ffd3818](https://github.com/PX4/PX4-Autopilot/commit/88d0b163b52803a38e9c316f1ccaf43b4ffd3818)

### Message
common:board_crashdump must end in reset!

   Upstream changes defer the board reset based on the vaule of
   CONFIG_BOARD_RESET_ON_ASSERT
      0 (or not defined) Do not reset on assert
      >= 1 reset if assertion is in an interrupt handler or the idle task
      >= 2 on any asertion.

  up_assert is called from up_hardfault or an asertion failure.
  Part 1 of up_assert will call out to the board_crashdump
  Part 2 on return from board_crashdump will then perform
  the reset.

  board_crashdump needs a chunk of ram to save the complete
  context in. It uses  &_sdata which is the lowest memory and
  it will corrupt that memeory.  We can therfore can not allow
  return to the OS, as it could depend on that area of RAM.

  So all boards need to do a reset at the end of board_crashdump
### Antipattern Category

### Keyword
memory
### Note


## Commit #623
### Hash
[e7bf0e03d29edbe962e0d432e71884d291a3d93b](https://github.com/PX4/PX4-Autopilot/commit/e7bf0e03d29edbe962e0d432e71884d291a3d93b)

### Message
px4_nuttx_tasks:Support future removal of env.

   CONFIG_DISABLE_ENVIRON can prevent task having to allocate
   memory for the env.
### Antipattern Category

### Keyword
memory
### Note


## Commit #624
### Hash
[d49f6a3acadcc96f0173eb2b4915bf977bdd3dd9](https://github.com/PX4/PX4-Autopilot/commit/d49f6a3acadcc96f0173eb2b4915bf977bdd3dd9)

### Message
mavlink increase STACK_MAIN and STACK_MAX

 - needed if NuttX networking enabled
### Antipattern Category

### Keyword
increase
### Note


## Commit #625
### Hash
[6f9a9b3d2c90faca79ff42b7dd08df6e97051c00](https://github.com/PX4/PX4-Autopilot/commit/6f9a9b3d2c90faca79ff42b7dd08df6e97051c00)

### Message
px4_fmu-v4: add runtime external SPI4 detection to support pmw3901 (#11301)

 * The build is built with SPI4. At run time the signal GPIO_8266_GPIO2 it tested. If it is low the SPI4 is configured. If it is high SPI4 is not configured.

 * board_common: Add Notion of Board has bus manifest
### Antipattern Category

### Keyword
runtime
### Note


## Commit #626
### Hash
[298049b0fb8382a43baeefd9c190888f95b01c01](https://github.com/PX4/PX4-Autopilot/commit/298049b0fb8382a43baeefd9c190888f95b01c01)

### Message
px4_fmu-v4_stackcheck sync with default and increase pmw3901 main stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #627
### Hash
[c6e60c21893e026ec5a7d005681526a266f92487](https://github.com/PX4/PX4-Autopilot/commit/c6e60c21893e026ec5a7d005681526a266f92487)

### Message
Update submodule ecl to latest Sun Feb  3 07:37:55 EST 2019

    - ecl in PX4/Firmware (0dc2ccb130e891b387b4e0d6ea4492473339e142): https://github.com/PX4/ecl/commit/721f5e61a5965a08a34b2875d2bdc0b5d3b80601
    - ecl current upstream: https://github.com/PX4/ecl/commit/dd58e695494acab73fb6fcec7074291edb5c226b
    - Changes: https://github.com/PX4/ecl/compare/721f5e61a5965a08a34b2875d2bdc0b5d3b80601...dd58e695494acab73fb6fcec7074291edb5c226b

    dd58e69 2019-01-30 Paul Riseborough - EKF: Ensure FW yaw alignment method is used on first in-air reset
3accab1 2019-01-28 Paul Riseborough - EKF: protect declination fusion from badly conditioned earth field estimates
7bddbd1 2019-01-28 Paul Riseborough - EKF: Update cleaned up autocode fragment with sign error fix and missing LD
fe378fd 2019-01-22 Paul Riseborough - EKF: Prevent unwanted declination fusion when re-starting 3-axis fusion
bd1647a 2019-01-22 Paul Riseborough - EKF: Rework use of fuseDeclination()
d52f536 2019-01-17 Paul Riseborough - EKF: Save mag field covariance data before reset
82ce7a8 2019-01-17 Paul Riseborough - EKF: Save mag field covariance information on startup
708c79e 2019-01-17 Paul Riseborough - EKF: Ensure mag field state covariance data is always available for re-use
8839e4e 2019-01-17 Paul Riseborough - EKF: Don't discard declination certainty information when resuming 3-axis fusion.
25148e1 2019-01-17 Paul Riseborough - EKF: Prevent rapid changes in declination estimate after a reset
6e7c119 2019-01-16 CarlOlsson - EKF: limit yaw variance increase to 0.01 rad^2 to prevent a badly conditioned covariance matrix
0896f7b 2019-01-16 CarlOlsson - EKF: Also fill in lower part of covariance matrix in increaseQuatYawErrVariance()
4b3140e 2019-01-16 Paul Riseborough - EKF: Fix rebase error
911d4d8 2019-01-16 Paul Riseborough - EKF: Fix sign error in increaseQuatYawErrVariance function
a0b9cb0 2018-12-24 Paul Riseborough - EKF: Use consistent method for recording completion of in-flight yaw alignment
ef5a87c 2018-12-21 Paul Riseborough - EKF: Rework quaternion yaw reset.
fc2a089 2018-12-21 Paul Riseborough - EKF: Add function to un-correlate quaternion states
bce1b96 2018-12-21 Paul Riseborough - EKF: Add function enabling yaw variance to be increased
bf1f3a2 2018-12-21 Paul Riseborough - EKF: Derive equations enabling yaw variance to be increased
81eabc1 2019-01-29 Daniel Agar - Jenkins update all containers to latest tag 2019-01-28
a5e6191 2019-01-29 Daniel Agar - EKF add clarity brackets to avoid potential confusion
### Antipattern Category

### Keyword
increase
### Note


## Commit #628
### Hash
[daae9e85b89a035faad32f6e2458c5bdbb54887b](https://github.com/PX4/PX4-Autopilot/commit/daae9e85b89a035faad32f6e2458c5bdbb54887b)

### Message
Jenkins hardware increase test timeout and update container version
### Antipattern Category

### Keyword
increase
### Note


## Commit #629
### Hash
[2b16be92813ba5a136b07d5a0b48ca30c085ea94](https://github.com/PX4/PX4-Autopilot/commit/2b16be92813ba5a136b07d5a0b48ca30c085ea94)

### Message
Jenkins hardware test remove px4_fmu-v4 stackcheck

- the stackcheck build is too slow to be useful

- will be recreated with fmu-v5
### Antipattern Category

### Keyword
slow
### Note


## Commit #630
### Hash
[6a08c1b6f16365fd2d3d59da64eb0b10aabe266b](https://github.com/PX4/PX4-Autopilot/commit/6a08c1b6f16365fd2d3d59da64eb0b10aabe266b)

### Message
Jenkins SITL tests increase test history from 2 -> 5
### Antipattern Category

### Keyword
increase
### Note


## Commit #631
### Hash
[b01e470ff9b72665d157881f8d49141d19eaa4db](https://github.com/PX4/PX4-Autopilot/commit/b01e470ff9b72665d157881f8d49141d19eaa4db)

### Message
refactor ecl ekf analysis (#11412)

* refactor ekf analysis part 1: move plotting to functions



* add plot_check_flags plot function



* put plots in seperate file



* use object-oriented programming for plotting



* move functions for post processing and pdf report creation to new files



* add in_air_detector and description as a csv file



* refactor metrics and checks into separate functions



* refactor metrics into seperate file, seperate plotting



* ecl-ekf tools: re-structure folder and move results table generation



* ecl-ekf-tool: fix imports and test_results_table



* ecl-ekf tools: bugfix output observer tracking error plot



* ecl-ekf-tools: update batch processing to new api, fix exception handling



* ecl-ekf-tools: use correct in_air_detector



* ecl-ekf-tools: rename csv file containing the bare test results table



* ecl-tools: refactor for improving readability



* ecl-ekf tools: small plotting bugfixes



* ecl-ekf tools: small bugfixes in_air time, on_ground_trans, filenames



* ecl-ekf-tools: fix amber metric bug



* ecl-ekf-tools: remove custom function in inairdetector



* ecl-ekf-tools: remove import of pandas



* ecl-ekf-tools: add python interpreter to the script start



* ecl-ekf-tools pdf_report: fix python interpreter line



* px4-dev-ros-kinetic: update container tag to 2019-02-13



* ecl-ekf-tools python interpreter line: call python3 bin directly



* ecl-ekf-tools: change airtime from namedtuple to class for python 3.5



* ecl-ekf-tools: update docker image px4-dev-ros-kinetic



* ecl-ekf-tools: fix memory leak by correctly closing matplotlib figures
### Antipattern Category

### Keyword
memory
### Note


## Commit #632
### Hash
[703e28f7a8544fe12e70d9ec012d6a94e79a8db6](https://github.com/PX4/PX4-Autopilot/commit/703e28f7a8544fe12e70d9ec012d6a94e79a8db6)

### Message
Jenkins increase history retention
### Antipattern Category

### Keyword
increase
### Note


## Commit #633
### Hash
[12d442e8ddf9e3d13b99a15d662f4ac8dcd1d287](https://github.com/PX4/PX4-Autopilot/commit/12d442e8ddf9e3d13b99a15d662f4ac8dcd1d287)

### Message
px4_fmuv5:Stack Check build Increase to 2624

   The cause of the stack detection fault is because of the
   level of nesting in the start up script. We need to
   determine the worst case configuration and set the
   bar there.

   This fault occurred some 42 calls deep due to script
   calling script (repeat).

   The HW stack check requires as a margin of 204 bytes. That is
   ISR HW stacking of CPU(8) FPU(18) registers and SW stacking of
   CPU(11) and FPU(16) registers. Total CPU(19) registers is
   68 bytes and the total FPU(34) registers is 136 bytes.  On
   a system with a separate ISR stack This only needs to be 104
   so there is 100 bytes of headroom. But as coded the detection
   will give a false positive detection and fault. This does not
   mean that the stack will be corrupted.

   Adjustments to that stack can have no effect due to rounding.
   A stack size of 2608 and 2616 can yield the exact same size stack.
   So even when the failure is due to a 4 byte overflow, it can take
   greater than a 16 bytes increase to fix it. Because the final
   stack size is calculated with an 8 byte alignment after a 4 byte
   decrease. So 2624 becomes 2620 at runtime and will boot
   with SYS_AUTOSTART=4001.
### Antipattern Category

### Keyword
runtime
### Note


## Commit #634
### Hash
[63a6ab34f7e37c6eac48fae85fb84c84c5d77b97](https://github.com/PX4/PX4-Autopilot/commit/63a6ab34f7e37c6eac48fae85fb84c84c5d77b97)

### Message
FlightTaskManualAltitude: slow down when landing manually
### Antipattern Category

### Keyword
slow
### Note


## Commit #635
### Hash
[f794ee0c8a1ed033549e436ddd10031dc97839eb](https://github.com/PX4/PX4-Autopilot/commit/f794ee0c8a1ed033549e436ddd10031dc97839eb)

### Message
FlightTaskManualAltitude: add slow upwards start

when still close to ground
### Antipattern Category

### Keyword
slow
### Note


## Commit #636
### Hash
[c9d32578e358b2f24dba4ec86527ef6ed286dd9f](https://github.com/PX4/PX4-Autopilot/commit/c9d32578e358b2f24dba4ec86527ef6ed286dd9f)

### Message
fix bmi055: increase DLPF from 62.5 to 500

With a DLPF of 62.5 Hz, the sampling rate is apperently not 1 kHz anymore,
because the driver got duplicate samples and published only at 128 Hz.
We have to increase the filter back to 500 Hz so that we get 1 kHz sampling
rate, with 250 Hz publications.
### Antipattern Category

### Keyword
increase
### Note


## Commit #637
### Hash
[6648937789fbcab9e2e0591e39f5935e38c9a7a5](https://github.com/PX4/PX4-Autopilot/commit/6648937789fbcab9e2e0591e39f5935e38c9a7a5)

### Message
logger increase stack 3600 -> 3700 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #638
### Hash
[7a27284d750b9a642a1f35660b47cfdefb394fa0](https://github.com/PX4/PX4-Autopilot/commit/7a27284d750b9a642a1f35660b47cfdefb394fa0)

### Message
Update submodule ecl to latest Thu Apr  4 00:38:15 UTC 2019

    - ecl in PX4/Firmware (3a004d13dc13d81403ae3873d5109c0503a4f964): https://github.com/PX4/ecl/commit/a892ececf8490b21aa8917bc243b2bc441af6a87
    - ecl current upstream: https://github.com/PX4/ecl/commit/f95cd4b3584d029c35b288a39180ddf25b2dd004
    - Changes: https://github.com/PX4/ecl/compare/a892ececf8490b21aa8917bc243b2bc441af6a87...f95cd4b3584d029c35b288a39180ddf25b2dd004

    f95cd4b 2019-01-22 Roman - ground effect: removed dependency on local position
7845ff4 2019-01-23 CarlOlsson - EKF: increase wind process noise scaler to 0.5
32ca6f7 2018-10-24 CarlOlsson - ekf: scale wind process noise with low pass filtered height rate
938c8ad 2019-02-04 CarlOlsson - EKF: use hagl estimate if valid for when to trigger yaw reset on takeoff
8b4ae48 2019-03-05 Hamish Willee - README: Fix link to EKF/ECL tuning guide
f0889c1 2019-03-18 Carl Olsson - EKF: fixed some comment typos
6e77b19 2019-03-14 Todd Stellanova - Add DataValidatorGroup tests, add more DataValidator tests (#592)
### Antipattern Category

### Keyword
increase
### Note


## Commit #639
### Hash
[911df49045b97544eb362447efdf8470886e5f8f](https://github.com/PX4/PX4-Autopilot/commit/911df49045b97544eb362447efdf8470886e5f8f)

### Message
increase stacks in drivers identified by stackcheck builds
### Antipattern Category

### Keyword
increase
### Note


## Commit #640
### Hash
[1454694bddd0a40a9da3c4170b0d28f5ab1efcf5](https://github.com/PX4/PX4-Autopilot/commit/1454694bddd0a40a9da3c4170b0d28f5ab1efcf5)

### Message
FlightTaskAuto: separate default speed and limit

It wasn't possible to fly faster than cruise speed even if planned
in the mission.

Limiting the planned cruise speed is necessary because
the smoothed trajectory mission plans to the _mc_cruise_speed and
if that's higher than the maximum it gets capped for safety by the
position controller and the result is a jerky flight.
### Antipattern Category

### Keyword
faster
### Note


## Commit #641
### Hash
[dc3341db59feb30ada0901141e7170071e5ad6da](https://github.com/PX4/PX4-Autopilot/commit/dc3341db59feb30ada0901141e7170071e5ad6da)

### Message
Fix uninitialized memory found using Valgrind
### Antipattern Category

### Keyword
memory
### Note


## Commit #642
### Hash
[4c56994d7a84268ea3b29930e0ad814db5fcd3e0](https://github.com/PX4/PX4-Autopilot/commit/4c56994d7a84268ea3b29930e0ad814db5fcd3e0)

### Message
mavlink_system: set update_counter for safe points

This variable was not set and lead to uninitialized memory being written
to dataman.
### Antipattern Category

### Keyword
memory
### Note


## Commit #643
### Hash
[ffeeedc310a1026057b8364322fd556053fa8423](https://github.com/PX4/PX4-Autopilot/commit/ffeeedc310a1026057b8364322fd556053fa8423)

### Message
init.d-posix: raise timeouts for fast SITL

When simulating with lockstep we can raise the speed by setting the env
variable `PX4_SIM_SPEED_FACTOR`. Some inputs like RC, MAVLink heartbeats
from a ground station, or offboard controls via MAVLink are still at the
normal speed which leads to timeouts getting detected in PX4.

To work around this issue we can automatically multiply the timeout
parameters by the speed factor.
### Antipattern Category

### Keyword
fast
### Note


## Commit #644
### Hash
[fac3e1c3f9e30c911208d799a999e3a413e6843c](https://github.com/PX4/PX4-Autopilot/commit/fac3e1c3f9e30c911208d799a999e3a413e6843c)

### Message
mc_pos_control: switch back to velocity ramp

But fix the two crucial problems:
- When to begin the ramp?
There's a calculation now for the velocity ramp initial value
such that the resulting thrust is zero at the beginning.
- When to end the ramp?
The ramp is applied to the upwards velocity constraint and it
just ramps from the initial value to the velocity constraint
which is applied during flight. Slower/going down is always possible.
### Antipattern Category

### Keyword
slower
### Note


## Commit #645
### Hash
[d68dcb9cf725ac35d5b56a4efe29361d0a08df6c](https://github.com/PX4/PX4-Autopilot/commit/d68dcb9cf725ac35d5b56a4efe29361d0a08df6c)

### Message
log_writer_file: increase stack size by 20 bytes

Seems to be due to the console buffer.
### Antipattern Category

### Keyword
increase
### Note


## Commit #646
### Hash
[26e041c43c1cf5345a863089c5e0d9ca58cef9be](https://github.com/PX4/PX4-Autopilot/commit/26e041c43c1cf5345a863089c5e0d9ca58cef9be)

### Message
WQ increase stacks from 1200 to 1250 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #647
### Hash
[0655f7603bf32c908bda2ccaa0cb26bbe19501f5](https://github.com/PX4/PX4-Autopilot/commit/0655f7603bf32c908bda2ccaa0cb26bbe19501f5)

### Message
FailureDetector - Increase min value of FD_FAIL_P/R to 60 degrees
### Antipattern Category

### Keyword
increase
### Note


## Commit #648
### Hash
[fcec3b3efcbfb954b80340fc49d994a37d84be9c](https://github.com/PX4/PX4-Autopilot/commit/fcec3b3efcbfb954b80340fc49d994a37d84be9c)

### Message
px4_fmu-v4: increase uart buffer sizes for vision algorithms (#12199)
### Antipattern Category

### Keyword
increase
### Note


## Commit #649
### Hash
[bef7a9ba8e9382a1497cf35cfe2f9a4b5ff97a28](https://github.com/PX4/PX4-Autopilot/commit/bef7a9ba8e9382a1497cf35cfe2f9a4b5ff97a28)

### Message
NuttX boards increase task limit 32 -> 64 (#12230)
### Antipattern Category

### Keyword
increase
### Note


## Commit #650
### Hash
[5f20d3cf3b13ce9b57837f7a122bacdea0489499](https://github.com/PX4/PX4-Autopilot/commit/5f20d3cf3b13ce9b57837f7a122bacdea0489499)

### Message
Jenkins HIL increase boot timeout for stackcheck build

 - px4_fmu-v5_stackcheck remove extra drivers (to try and get the system
usuable)
### Antipattern Category

### Keyword
increase
### Note


## Commit #651
### Hash
[ea31f34d09b542fcad7087aa9c9d9c27ddad6ce9](https://github.com/PX4/PX4-Autopilot/commit/ea31f34d09b542fcad7087aa9c9d9c27ddad6ce9)

### Message
mc rate controller: add I term reduction factor

Reduce the I gain for high rate errors to reduce bounce-back effects after
flips. Up to 200 degrees the gain is almost not reduced (<25%), so this
will only take noticeable effects for large errors (setpoint changes),
where we actually want to have an effect.

This allows to increase the MC_*RATE_I parameters w/o negative effects
when doing flips (i.e. bounce-back after flips).

The 400 degrees limit and the x^2 are empirical.

The better the rate tracking in general (high P gain), the less this is
required (because of the lower tracking error). At the same time it also
does not harm, as the i_factor will always be close to 1.
### Antipattern Category

### Keyword
increase
### Note


## Commit #652
### Hash
[64ac8c18d2549b7c165a5a62346281867c893dfa](https://github.com/PX4/PX4-Autopilot/commit/64ac8c18d2549b7c165a5a62346281867c893dfa)

### Message
mc airframes: increase I gains a bit

Previous commit allows to increase them again.
Partially reverts commit 6c3e79f3614f0060d5998c39be358512101252ff.
### Antipattern Category

### Keyword
increase
### Note


## Commit #653
### Hash
[5002b13bda7fd679d29fe8210ebac8766616aa8a](https://github.com/PX4/PX4-Autopilot/commit/5002b13bda7fd679d29fe8210ebac8766616aa8a)

### Message
mc_att_control: Increase default rate integral gain

@bkueang and me realized that on every frame we tune the integral gain for
the roll and pitch rate controller is much too low. Usually it needs to be
increased to 0.3 or even 0.4 to have better "locked in" flight performance
and 0.2 seems like a good compromise for a safe default.
### Antipattern Category

### Keyword
performance
### Note


## Commit #654
### Hash
[7f9415ba4615200cf0c21487e79cb4509ad06620](https://github.com/PX4/PX4-Autopilot/commit/7f9415ba4615200cf0c21487e79cb4509ad06620)

### Message
systemcmds/top: increase stack 200 bytes

 - this is necessary after most boards increased CONFIG_MAX_TASKS 32 -> 64
### Antipattern Category

### Keyword
increase
### Note


## Commit #655
### Hash
[9b46c1d8a90315419876fb62114b2dea1e1fa36c](https://github.com/PX4/PX4-Autopilot/commit/9b46c1d8a90315419876fb62114b2dea1e1fa36c)

### Message
Upated Babyshark VTOL config and vtol_defaults

Updated the babyshark default  parameters for improved flight performance,
as well as two MPC parameters in vtol_defaults for smoother hovering with VTOLS"

Signed-off-by: Silvan Fuhrer <silvan@auterion.com>
### Antipattern Category

### Keyword
performance
### Note


## Commit #656
### Hash
[7ace66a2b9b7ddc91f1f8460a168ebf5a397b050](https://github.com/PX4/PX4-Autopilot/commit/7ace66a2b9b7ddc91f1f8460a168ebf5a397b050)

### Message
Jenkins hardware increase timeout 10 -> 20 minutes
### Antipattern Category

### Keyword
increase
### Note


## Commit #657
### Hash
[4e5974f1ca27df11b6f23dd8c6a556454ba81479](https://github.com/PX4/PX4-Autopilot/commit/4e5974f1ca27df11b6f23dd8c6a556454ba81479)

### Message
srf02 driver: Move member variable initialization to declarations, standardize against other drivers and format. (#11891)

* Migrate variable initialization from constructor list to declarations, standardize whitespace formatting, and alphabetize/organize order of methods and variables in srf02.cpp.



* Increase stack allocation size for the srf02 driver main.
### Antipattern Category

### Keyword
increase
### Note


## Commit #658
### Hash
[8aad10526545a8d67a7e6e239b4c753f832b03c9](https://github.com/PX4/PX4-Autopilot/commit/8aad10526545a8d67a7e6e239b4c753f832b03c9)

### Message
mc_pos_control: increase stack size by 100 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #659
### Hash
[c15e54445efe710bd70cea591935d64bde29caa4](https://github.com/PX4/PX4-Autopilot/commit/c15e54445efe710bd70cea591935d64bde29caa4)

### Message
increase cutoff margin for alias matching
### Antipattern Category

### Keyword
increase
### Note


## Commit #660
### Hash
[f0cdd9be6091e15cc2a6cc434cf4409647bcd3a5](https://github.com/PX4/PX4-Autopilot/commit/f0cdd9be6091e15cc2a6cc434cf4409647bcd3a5)

### Message
MPC_Z_VEL_I: changed default from 0.02 to 0.1
- generally better attitude tracking
- much better altitude control immediately after takeoff (hover throttle offset)
- faster landing detection

Signed-off-by: RomanBapst <bapstroman@gmail.com>
### Antipattern Category

### Keyword
faster
### Note


## Commit #661
### Hash
[a8071589bc87d97fd31cb810a93ee425c839275e](https://github.com/PX4/PX4-Autopilot/commit/a8071589bc87d97fd31cb810a93ee425c839275e)

### Message
increase default fixed wing rate controller I term

Signed-off-by: RomanBapst <bapstroman@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #662
### Hash
[0e949a36ee104b8ace10eedaa1fcd83a00e3265a](https://github.com/PX4/PX4-Autopilot/commit/0e949a36ee104b8ace10eedaa1fcd83a00e3265a)

### Message
task_stack_info increase task_name length to match NuttX CONFIG_TASK_NAME_SIZE
### Antipattern Category

### Keyword
increase
### Note


## Commit #663
### Hash
[e0893c383d8dc1f3cc1cacea00454d43d1defb08](https://github.com/PX4/PX4-Autopilot/commit/e0893c383d8dc1f3cc1cacea00454d43d1defb08)

### Message
increase mc_pos_control stack from 1300 to 1500
### Antipattern Category

### Keyword
increase
### Note


## Commit #664
### Hash
[5421ef5535d79b5f5108a8545def46f9e5e9358f](https://github.com/PX4/PX4-Autopilot/commit/5421ef5535d79b5f5108a8545def46f9e5e9358f)

### Message
NuttX increase HPWORK and LPWORK stack by 256 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #665
### Hash
[d70b024ec7a6d72de87f4ddc7de087d716929144](https://github.com/PX4/PX4-Autopilot/commit/d70b024ec7a6d72de87f4ddc7de087d716929144)

### Message
GTest functional tests that include parameters and uORB messaging (#12521)

* Add kdevelop to gitignore



* Add test stubs



* Rename px4_add_gtest to px4_add_unit_gtest



* Add infrastructure to run functional tests



* Add example tests with parameters and uorb messages



* Fix memory issues in destructors in uORB manager and CDev



* Add a more real-world test of the collision prevention
### Antipattern Category

### Keyword
memory
### Note


## Commit #666
### Hash
[166639be3a21be00ef80eb619aa23fbc8751ac3e](https://github.com/PX4/PX4-Autopilot/commit/166639be3a21be00ef80eb619aa23fbc8751ac3e)

### Message
logger: unconditionally call _writer.notify()

The file writer thread could get into a state where it blocked infinitely
on pthread_cond_wait() (or rather until the logging stops).

This is very rare and the following conditions must be met:
- the buffer is almost empty (<4KB filled), so that the writer thread does
  not write anything.
- an fsync call is scheduled (happens once every second)
- the fsync call takes a long time (several 100ms), during which time the
  complete log buffer fills up.

The main thread would then get into dropout state where it does not call
_writer.notify() anymore.

Notifying the writer thread on every loop update of the main thread fixes
that.

It does not increase resource usage.
### Antipattern Category

### Keyword
increase
### Note


## Commit #667
### Hash
[ccdc2dffa976c480e76a96a3afb3caa6933077a5](https://github.com/PX4/PX4-Autopilot/commit/ccdc2dffa976c480e76a96a3afb3caa6933077a5)

### Message
WQ decrease att_pos_ctrl stack
### Antipattern Category

### Keyword
decrease
### Note


## Commit #668
### Hash
[690aeef1868380f96ab774fe676557714e39c3c2](https://github.com/PX4/PX4-Autopilot/commit/690aeef1868380f96ab774fe676557714e39c3c2)

### Message
drivers/gps: increase task stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #669
### Hash
[78ef8aab2df33cd00e2c969bbff37ffd82bcf385](https://github.com/PX4/PX4-Autopilot/commit/78ef8aab2df33cd00e2c969bbff37ffd82bcf385)

### Message
STACK_MAIN increase default 1024 -> 2048
### Antipattern Category

### Keyword
increase
### Note


## Commit #670
### Hash
[891aae03774e4fb2f59aad526eb0147972e93a0b](https://github.com/PX4/PX4-Autopilot/commit/891aae03774e4fb2f59aad526eb0147972e93a0b)

### Message
commander increase cpu overload threshold

 * the large 20% margin is no longer appropriate now that nearly all work in the system is

scheduled (moved out of ISRs) and represented in the load percentage

 * closes https://github.com/PX4/Firmware/issues/12753
### Antipattern Category

### Keyword
increase
### Note


## Commit #671
### Hash
[c67a7536d464b7f788cf20c8be0decb19b2d82ee](https://github.com/PX4/PX4-Autopilot/commit/c67a7536d464b7f788cf20c8be0decb19b2d82ee)

### Message
Update submodule matrix to latest Sun Sep 22 08:37:30 EDT 2019

    - matrix in PX4/Firmware (8b1f9546aabfe6ab2a0431f1d5af6dcc976d4f59): https://github.com/PX4/Matrix/commit/60c9c99dcc44ea12bed0c3f9b95d01e2aa6d7d9e
    - matrix current upstream: https://github.com/PX4/Matrix/commit/c34e8dc98fd05ea55dcd4c9fc551b11a3d23a601
    - Changes: https://github.com/PX4/Matrix/compare/60c9c99dcc44ea12bed0c3f9b95d01e2aa6d7d9e...c34e8dc98fd05ea55dcd4c9fc551b11a3d23a601

    c34e8dc 2019-09-17 Matthias Grob - helper: consider matrices with the same NANs and INFINITYs equal
bbaa938 2019-09-17 Matthias Grob - helper: consider NAN equal to NAN such that vectors can be compared exactly
33a6291 2019-09-17 Matthias Grob - Matrix: add proper print function testing
b0b7d72 2019-09-17 Matthias Grob - Multiplication test: fix division resulting in NAN
3747232 2019-09-17 Matthias Grob - LeastSquaresSolver: Fix nasty GCC compile optimization error
5844b0e 2019-09-16 Matthias Grob - Implement one float equality check and use it everywhere
1e80807 2019-09-16 Matthias Grob - test: Add uncovered equality checks with NAN and INFINITE
a374f37 2019-09-16 Matthias Grob - Include helper_functions like all other library components
### Antipattern Category

### Keyword
infinite
### Note


## Commit #672
### Hash
[07d656e971a72d1202651dfd3b4642736fb078d7](https://github.com/PX4/PX4-Autopilot/commit/07d656e971a72d1202651dfd3b4642736fb078d7)

### Message
Guidance feature for Collision Prevention (#13017)

* add guidance



* remove COL_PREV_ANG and replace with COL_PREV_CNG



* safe max ranges per bin



* increase default value for colprev delay to account for tracking delay



* update parameter description



* fix and extend testing



* add handling for overlapping sensor data



* fix decision process for overlapping sensors
### Antipattern Category

### Keyword
increase
### Note


## Commit #673
### Hash
[637d52c74fa8725b1a787f8b9ac093bc42b6c565](https://github.com/PX4/PX4-Autopilot/commit/637d52c74fa8725b1a787f8b9ac093bc42b6c565)

### Message
frsky_telemetry: increase stack by 60 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #674
### Hash
[69c10dcaaca2d343aa045328dec80737c0dffbf2](https://github.com/PX4/PX4-Autopilot/commit/69c10dcaaca2d343aa045328dec80737c0dffbf2)

### Message
dshot: move implementation to a separate directory & library

So that the static memory overhead is not added to targets w/o dshot
### Antipattern Category

### Keyword
memory
### Note


## Commit #675
### Hash
[182efaa7576ccbf682d892ebac93105059e52793](https://github.com/PX4/PX4-Autopilot/commit/182efaa7576ccbf682d892ebac93105059e52793)

### Message
dshot: reduce static buffer size

And handle failures of up_dshot_init().

On Omnibus: reduces memory usage if dshot is enabled by ~1.0KB.
The buffer is roughly 1KB in size.
### Antipattern Category

### Keyword
memory
### Note


## Commit #676
### Hash
[17551a99f8d414bbb22a637f14274214cb7a4eca](https://github.com/PX4/PX4-Autopilot/commit/17551a99f8d414bbb22a637f14274214cb7a4eca)

### Message
io_timer: fix potential invalid memory access
### Antipattern Category

### Keyword
memory
### Note


## Commit #677
### Hash
[25aded36ec9337e274062eb7b4a46eb104ada021](https://github.com/PX4/PX4-Autopilot/commit/25aded36ec9337e274062eb7b4a46eb104ada021)

### Message
WorkQueue: avoid potential semaphore counter overflow

This could happen in the following cases:
- IRQ/publisher rate is faster than the processing rate, and therefore
  WorkQueue::Add is called at a higher rate
- a long-running or stuck task that blocks the work queue a long time

Both cases are not expected to happen under 'normal' circumstances (if the
system runs as expected).
### Antipattern Category

### Keyword
faster
### Note


## Commit #678
### Hash
[687a3a15c572f2e9787274a244016df927882700](https://github.com/PX4/PX4-Autopilot/commit/687a3a15c572f2e9787274a244016df927882700)

### Message
top: decrease priority below IMU sensor WQ threads

 - otherwise top can potentially disrupt with sensor sampling
### Antipattern Category

### Keyword
decrease
### Note


## Commit #679
### Hash
[981f8d5d904f303c14348dea7d183cd8ecba456a](https://github.com/PX4/PX4-Autopilot/commit/981f8d5d904f303c14348dea7d183cd8ecba456a)

### Message
systemcmds/tests: IntrusiveQueue and List fix memory leaks
### Antipattern Category

### Keyword
memory
### Note


## Commit #680
### Hash
[f7e62349b39c111b65cc7062a9bfe9efc1ebfd8b](https://github.com/PX4/PX4-Autopilot/commit/f7e62349b39c111b65cc7062a9bfe9efc1ebfd8b)

### Message
px4_posix: increase posix stack overhead (mostly for ASan)

 - sync address sanitizer SITL tests
### Antipattern Category

### Keyword
increase
### Note


## Commit #681
### Hash
[e2cf501f9d5bc947a683086e9f20bd2a2d7e99b6](https://github.com/PX4/PX4-Autopilot/commit/e2cf501f9d5bc947a683086e9f20bd2a2d7e99b6)

### Message
boards: increase CONFIG_MAX_TASKS 32->64 on all F7s (#13285)

On more complicated setups it's still possible to exceed 32 tasks. For example fmu-v5 with mavlink on every telem (+ USB), external spi usage (pmw3901), gimbal (vmount), multiple i2c sensors, and camera feedback is 35 tasks (with top running). This is a fairly extreme case, so I'm only going to increase CONFIG_MAX_TASKS on newer F7 boards.
### Antipattern Category

### Keyword
increase
### Note


## Commit #682
### Hash
[d545825bf0a53d412db449614c950a377f79d192](https://github.com/PX4/PX4-Autopilot/commit/d545825bf0a53d412db449614c950a377f79d192)

### Message
clang-tidy: enable performance-unnecessary-value-param and fix
### Antipattern Category

### Keyword
performance
### Note


## Commit #683
### Hash
[5491f9b8f953664273c63547a8ee5ce794b3c3c7](https://github.com/PX4/PX4-Autopilot/commit/5491f9b8f953664273c63547a8ee5ce794b3c3c7)

### Message
px_uploader.py: increase estimated erase time

The 9 seconds to erase a board probably still come from the FMU-v1 and
Pixhawks with only 1 MB flash. By now, many targets have 2 MB flash and
take a bit longer to erase. Therefore, we can increase the estimated
time a bit and don't need to resort to the timeout notice.
### Antipattern Category

### Keyword
increase
### Note


## Commit #684
### Hash
[32359168d6f3af80470a2b541dadee9298faedc2](https://github.com/PX4/PX4-Autopilot/commit/32359168d6f3af80470a2b541dadee9298faedc2)

### Message
smbus: fix invalid memory access in read_word()

read_word() expected 3 bytes (uint16_t + PEC byte), but was passed an
address to an uint16_t value.

write_word() is changed to be type-safe as well.
### Antipattern Category

### Keyword
memory
### Note


## Commit #685
### Hash
[11287712f8bfc1ce896cc618323a2fb318ca1731](https://github.com/PX4/PX4-Autopilot/commit/11287712f8bfc1ce896cc618323a2fb318ca1731)

### Message
fmuk66-v3:Fix hang on SDIO card removal/reinsertion

   The interrupt driven card detect logic was enabled
   but the auto mounter was not. That interrupt was
   calling mmcsd_mediachange.

   There is a reentrancy issues in the kinetis callback logic.
   Toplevel calls mmcsd_mediachange calls SDIO_CALLBACKENABLE
   that calls kinetis_callbackenable that calls kinetis_callback
   that calls mmcsd_mediachange.
### Antipattern Category

### Keyword
hang
### Note


## Commit #686
### Hash
[69694ab000f923106931612fa34f8d689b1732fc](https://github.com/PX4/PX4-Autopilot/commit/69694ab000f923106931612fa34f8d689b1732fc)

### Message
px4io-v2:Resonable Def config memory - verified by inspection
### Antipattern Category

### Keyword
memory
### Note


## Commit #687
### Hash
[8ce2f30aa6894cf0e2bfadfbc9c787029599cfd1](https://github.com/PX4/PX4-Autopilot/commit/8ce2f30aa6894cf0e2bfadfbc9c787029599cfd1)

### Message
NuttX cmake improve dependencies between configure and runtime

 - attempting to make the build slightly more robust to incomplete configures or other bad states.
### Antipattern Category

### Keyword
runtime
### Note


## Commit #688
### Hash
[82fac4a0a7f5ea28a6402dd14daa846431f7ad10](https://github.com/PX4/PX4-Autopilot/commit/82fac4a0a7f5ea28a6402dd14daa846431f7ad10)

### Message
cmake NuttX linker print memory usage
### Antipattern Category

### Keyword
memory
### Note


## Commit #689
### Hash
[cbea76f62a80caff29b2db3457c42b84ad1ef7ad](https://github.com/PX4/PX4-Autopilot/commit/cbea76f62a80caff29b2db3457c42b84ad1ef7ad)

### Message
navigator: fix triplet resetting/publication logic (#13534)

The navigator has a notion of resetting the triplets which means the

triplet setpoints are set to invalid and therefore not to be used by

downstream modules such as flight tasks.



However, before this patch, the triplets were not published if invalid

meaning that a valid triplet would stay the truth until a new valid

triplet would get published.



E.g. this lead to the corner case case where we publish a valid triplet

with an IDLE setpoint on ground in HOLD and then don't update the

triplet while flying in POSCTL mode. Later, when RTL is engaged, the

flight task will use IDLE until navigator (which runs slower) has

published the next triplet.



The fix involves two main changes:

- Publish invalid triplets to avoid stale triplets.

- Avoid publishing the triplet on every iteration in manual modes by not

  setting `_pos_sp_triplet_published_invalid_once = false`.



When testing this I realized that a mission upload during RTL would stop

RTL. This is because the mission is updated while the mission navigation

mode is not active and reset_triplets() is called from there. This is

now only done for the case where we are actually in mission navigation

mode. The fact that a mission is updated when not active also seems

wrong and is something to fix another time.
### Antipattern Category

### Keyword
slower
### Note


## Commit #690
### Hash
[2811307293a9bc6118f861d87f6a3a840a795b98](https://github.com/PX4/PX4-Autopilot/commit/2811307293a9bc6118f861d87f6a3a840a795b98)

### Message
px4_work_queue: increase wq:hp_default stack 1500->1800 bytes (found by stackcheck)
### Antipattern Category

### Keyword
increase
### Note


## Commit #691
### Hash
[1cbcb445abb21e69c5af2b590147b5c72601b823](https://github.com/PX4/PX4-Autopilot/commit/1cbcb445abb21e69c5af2b590147b5c72601b823)

### Message
gyro calibration: speedup from 20s to 1s

It's not required to take that many samples, 1 second is enough.
This is confirmed by looking at the standard deviation over 10 calibrations:
it is in the same order as with 20 seconds (the effect of temperature
increase has a bigger effect).
### Antipattern Category

### Keyword
increase
### Note


## Commit #692
### Hash
[4e7dedede79872401f50c733bd74e5ddf1fa41f1](https://github.com/PX4/PX4-Autopilot/commit/4e7dedede79872401f50c733bd74e5ddf1fa41f1)

### Message
bloaty show full demangle, increase number of lines, and combine segments + sections
### Antipattern Category

### Keyword
increase
### Note


## Commit #693
### Hash
[634e8d206a7651b09930f9091839b5df7b8e7420](https://github.com/PX4/PX4-Autopilot/commit/634e8d206a7651b09930f9091839b5df7b8e7420)

### Message
tiltrotor SITL config: increase transition time from 1.5 to 5 seconds
- avoids tilting the motors forward too fast

Signed-off-by: RomanBapst <bapstroman@gmail.com>
### Antipattern Category

### Keyword
fast
### Note


## Commit #694
### Hash
[31456419e9a77c26e4e4c5b8efe2f1c6472653bd](https://github.com/PX4/PX4-Autopilot/commit/31456419e9a77c26e4e4c5b8efe2f1c6472653bd)

### Message
px4_fmu-v5x:Add 4096 for ism330dlc to BOARD_DMA_ALLOC_POOL_SIZE

   ISM330DLC uses 4096 of memory allocated from DMA pool.
   This depleted the pool to the point the next allocation
   for FAT would fail. Unfortuanly this is the logger
   on a later open.
### Antipattern Category

### Keyword
memory
### Note


## Commit #695
### Hash
[1d3f722201c39dfc14dfd85c80875c57427a2fbb](https://github.com/PX4/PX4-Autopilot/commit/1d3f722201c39dfc14dfd85c80875c57427a2fbb)

### Message
px4_work_queue: increase hp_default stack 1800 -> 1900 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #696
### Hash
[808061519141d0bcf8ef8c77a3e4b945c2f78ddb](https://github.com/PX4/PX4-Autopilot/commit/808061519141d0bcf8ef8c77a3e4b945c2f78ddb)

### Message
PreFlightChecker: add spike limit argument for innovation check and
increase optical flow test limits.
### Antipattern Category

### Keyword
increase
### Note


## Commit #697
### Hash
[735749e341e51c31abe843593da7ba8f3bc97e0d](https://github.com/PX4/PX4-Autopilot/commit/735749e341e51c31abe843593da7ba8f3bc97e0d)

### Message
Revert "SITL shell: Do math using the shell"

This reverts commit be35c4857be2483050d9a34987aeda3c6935b516.

This would only work for integer math, so for simulation speed-up. For
speeds slower than realtime we need floating point.
### Antipattern Category

### Keyword
slower
### Note


## Commit #698
### Hash
[3387c9599cc09c1171a41617d1d30c4c7b01fd22](https://github.com/PX4/PX4-Autopilot/commit/3387c9599cc09c1171a41617d1d30c4c7b01fd22)

### Message
mavsdk_tests: don't constrain speed factor to int

Speed factors slower than 1 should also be possible.
### Antipattern Category

### Keyword
slower
### Note


## Commit #699
### Hash
[4d831707463628ec61af99bd0caac29fe08492f9](https://github.com/PX4/PX4-Autopilot/commit/4d831707463628ec61af99bd0caac29fe08492f9)

### Message
mc_pos_control: do not ignore EKF vz with terrain following

This caused bad altitude control performance when enabling
terrain following. It even leads to complete vertical control
instability in case dist_bottom is inaccurate.

Relying on the estimator states is the way to go instead of
silently using one altitude source as state.
### Antipattern Category

### Keyword
performance
### Note


## Commit #700
### Hash
[dc05ceaad2d3786d1c4929dbe867c044fbffe1dd](https://github.com/PX4/PX4-Autopilot/commit/dc05ceaad2d3786d1c4929dbe867c044fbffe1dd)

### Message
create temperature_compensation module

 - this is a new module for temperature compensation that consolidates the functionality previously handled in the sensors module (calculating runtime thermal corrections) and the events module (online thermal calibration)

 - by collecting this functionality into a single module we can optionally disable it on systems where it's not used and save some flash (if disabled at build time) or memory (disabled at run time)
### Antipattern Category

### Keyword
memory
### Note


## Commit #701
### Hash
[0d8ac51bcccce3bf7885e7608200dc862cd68797](https://github.com/PX4/PX4-Autopilot/commit/0d8ac51bcccce3bf7885e7608200dc862cd68797)

### Message
Coverage tests: Run faster
We want the coverage tests to run at the maximum speedup factor the CI machine can deliver.
### Antipattern Category

### Keyword
faster
### Note


## Commit #702
### Hash
[962716a7c3073df28dbc66d1402a47746c672d4d](https://github.com/PX4/PX4-Autopilot/commit/962716a7c3073df28dbc66d1402a47746c672d4d)

### Message
nxp_fmurt1062-v1:Performance tuning
### Antipattern Category

### Keyword
performance
### Note


## Commit #703
### Hash
[78c7f98ef199b48e8ab90a915ada3c07124baf07](https://github.com/PX4/PX4-Autopilot/commit/78c7f98ef199b48e8ab90a915ada3c07124baf07)

### Message
nxp_fmurt1062-v1:Memory Reorg
### Antipattern Category

### Keyword
memory
### Note


## Commit #704
### Hash
[c78572b47149919f661f026b3313ac662998be16](https://github.com/PX4/PX4-Autopilot/commit/c78572b47149919f661f026b3313ac662998be16)

### Message
px4io: fix array regs[] size (#14135)

may cause memory override if _max_controls larger then _max_actuators
### Antipattern Category

### Keyword
memory
### Note


## Commit #705
### Hash
[22499effb976e75c5be01a14b6bf38d0ed61993d](https://github.com/PX4/PX4-Autopilot/commit/22499effb976e75c5be01a14b6bf38d0ed61993d)

### Message
invensense icm20602 improvements

 - checked register mechanism and simple watchdog
    - driver checks for errors gradually and can reconfigure itself
 - respect IMU_GYRO_RATEMAX at the driver level
 - fixed sensor INT16_MIN and INT16_MAX handling (y & z axis are flipped before publishing)
 - increased sensor_gyro_fifo max size (enables running the driver much slower, but still transferring all raw data)
 - PX4Accelerometer/PX4Gyroscope remove unnecessary memsets
### Antipattern Category

### Keyword
slower
### Note


## Commit #706
### Hash
[d7e502ec72af023b870fd41a83e1ec6e86561768](https://github.com/PX4/PX4-Autopilot/commit/d7e502ec72af023b870fd41a83e1ec6e86561768)

### Message
uORB_tests increase stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #707
### Hash
[d7a9b123e6b84df4a7c01daaac64706c39abd3d7](https://github.com/PX4/PX4-Autopilot/commit/d7a9b123e6b84df4a7c01daaac64706c39abd3d7)

### Message
logger: fix thread deadlock
### Antipattern Category

### Keyword
deadlock
### Note


## Commit #708
### Hash
[505afc6063b39adb29c360447b9b6cf97d6f2b9e](https://github.com/PX4/PX4-Autopilot/commit/505afc6063b39adb29c360447b9b6cf97d6f2b9e)

### Message
boards: increase LPWORKSTACKSIZE 1536 -> 1600
### Antipattern Category

### Keyword
increase
### Note


## Commit #709
### Hash
[9585055e9e87ef565efd19fa429e175423ac81e3](https://github.com/PX4/PX4-Autopilot/commit/9585055e9e87ef565efd19fa429e175423ac81e3)

### Message
uORB: add bitset for faster orb_exists check and remove uORB::Subscription lazy subscribe hack/optimization

 - add PX4 bitset and atomic_bitset with testing

 - add uORB::Subscription constructor to take ORB_ID enum

 - move orb test messages into msg/
### Antipattern Category

### Keyword
faster
### Note


## Commit #710
### Hash
[190ee042eb65f0301c32c5ad70cf49bb063902e9](https://github.com/PX4/PX4-Autopilot/commit/190ee042eb65f0301c32c5ad70cf49bb063902e9)

### Message
Update submodule sitl_gazebo to latest Wed Mar 11 12:38:07 UTC 2020

    - sitl_gazebo in PX4/Firmware (88c9761f1fd6124955a9c218bdc5528a4ee15ab1): https://github.com/PX4/sitl_gazebo/commit/8569aec5bb709acb2fec7ccb5a5a4405f0cdec2a
    - sitl_gazebo current upstream: https://github.com/PX4/sitl_gazebo/commit/458e58f7973df2e211648e78b7277deefa59eca6
    - Changes: https://github.com/PX4/sitl_gazebo/compare/8569aec5bb709acb2fec7ccb5a5a4405f0cdec2a...458e58f7973df2e211648e78b7277deefa59eca6

    458e58f 2020-03-10 JaeyoungLim - Fix sweep cosine (Continuing #302) (#429)
ea2568d 2019-12-27 JaeyoungLim - Increase rudder angle limit
8b905c9 2019-12-27 JaeyoungLim - Add rudder control to sitl
08f8e6f 2020-03-10 Jan-Hendrik Ewers - Update README.md
de10edd 2020-03-10 iwishiwasaneagle - Fixes PX4/sitl_gazebo#424 for arch and ubuntu
4f596be 2020-03-10 Christian Clauss - Remove unused function isstring() in scripts/names.py (#346)
89db01c 2020-03-09 Matej Frančeškin - Handle MAV_CMD_SET_CAMERA_MODE
dae26ba 2020-03-08 JaeyoungLim - Handle videostream info and status
c13057d 2020-03-07 JaeyoungLim - Clear formatting and cleanups
639a6bb 2020-03-07 JaeyoungLim - Add parachute plugin
42d05bd 2020-03-09 RomanBapst - standard vtol: decrease rotorDragCoefficient to more realistic values
5669e5c 2020-03-07 leftytechie - Version check (#418)
82657d3 2020-03-07 Lorenz Meier - Fix geotagged images GPS position The GPS position was invalid, leading to incorrectly displayed geotag markers and to incorrect geotags in images.
8794a70 2020-03-02 Julian Oes - cmake: remove warning
7aba744 2020-02-26 TSC21 - gazebo_mavlink_interface: use class enum; use binary notation with the bitmask operations
0dc43a4 2020-02-26 TSC21 - gazebo_mavlink_interface: make sure to always send gyro and accel data in the HIL_SENSOR msgs
0c954a2 2020-02-25 TSC21 - mavlink_interface: split groundtruth stream from sensor stream; only apply rotations where needed
bc92d96 2020-02-25 TSC21 - set baro rate at 50Hz (averaging the PX4 baro drivers ODR)
94d16e6 2020-02-25 TSC21 - update magnetometer rate to 100Hz (fitting the ODR in most of the support PX4 mag drivers)
6cae120 2020-02-25 TSC21 - mavlink_interface: send HIL_SENSOR messages with the bitmask correctly defined IOT set each sensor stream rate separately
### Antipattern Category

### Keyword
increase
### Note


## Commit #711
### Hash
[9cd8bb4f889f1cda33941a99056061b0e5d2b9bf](https://github.com/PX4/PX4-Autopilot/commit/9cd8bb4f889f1cda33941a99056061b0e5d2b9bf)

### Message
sensors: move to WQ

Running the sensors module out of the same WQ thread as the estimator, position, and attitude controllers is a bit safer and prevents potential priority and starvation issues. There is a very small increase in latency (~50 us) between sensors and ekf2 execution (on average). This also saves a little bit of memory (~ 3 kB) and cpu (~1-1.5% depending on the board).
### Antipattern Category

### Keyword
memory
### Note


## Commit #712
### Hash
[46a09b711f1d669ee130de38c3988189638b98e7](https://github.com/PX4/PX4-Autopilot/commit/46a09b711f1d669ee130de38c3988189638b98e7)

### Message
boards: increase STDIO buffer size where we can afford it
### Antipattern Category

### Keyword
increase
### Note


## Commit #713
### Hash
[4b9e6964f4d3b620b685744e32b162c5cb22c600](https://github.com/PX4/PX4-Autopilot/commit/4b9e6964f4d3b620b685744e32b162c5cb22c600)

### Message
uavcan:Support runtime setting of CAN interfaces
### Antipattern Category

### Keyword
runtime
### Note


## Commit #714
### Hash
[39e473f988638e1ca35c958334fbbfe62c99dfbf](https://github.com/PX4/PX4-Autopilot/commit/39e473f988638e1ca35c958334fbbfe62c99dfbf)

### Message
Gazebo plane model: Enable tighter turns
This helps to fly smaller / faster test missions.
### Antipattern Category

### Keyword
faster
### Note


## Commit #715
### Hash
[1bf791ba3fc2f1230a6ef950dd6e17c3d5b869c0](https://github.com/PX4/PX4-Autopilot/commit/1bf791ba3fc2f1230a6ef950dd6e17c3d5b869c0)

### Message
MC_HTE: Stability improvements

- Use a low-passed value of the signed innovation test ratio to trigger
the state variance boost. The threshold of 0.2 has been chosen using log
replay and simulation scenarii.
- Do not reset the learned accel noise during a state variance boost.
After a few tests, this does not seem to help at all.
- Continue to learn the accel noise even if the measurement got rejected
to avoid ignoring sudden changes of noise
- Lower the acceleration noise time constant and increase min/max
values to avoid learning quickly a small variance that could temporarly
destabilize the filter
- Update filter time constants. Increasing the speed of the residual lpf
improves the quality of the learned accel noise
### Antipattern Category

### Keyword
increase
### Note


## Commit #716
### Hash
[6ccf55b6fd67d8cc93c7cf0b5cffcba724b15fef](https://github.com/PX4/PX4-Autopilot/commit/6ccf55b6fd67d8cc93c7cf0b5cffcba724b15fef)

### Message
MPC: add updateHoverThrust function

This function updates the vertical velocity integrator with the change
in hover thrust to avoid propagating discontinuities through the
controller when changing the hover thrust.
This is also important when using the hover thrust estimator as its
estimate has unconstrained dynamics and can cause drops or kicks when
the estimate updates faster than the velocity integrator.
### Antipattern Category

### Keyword
faster
### Note


## Commit #717
### Hash
[f851f65f8dd0a9281aad7dcf57ceeb370ebad487](https://github.com/PX4/PX4-Autopilot/commit/f851f65f8dd0a9281aad7dcf57ceeb370ebad487)

### Message
i2c spi: add type to I2CSPIInstance

Needed to distinguish runtime instance types of the same driver (e.g.
bmi055 accel vs gyro).
### Antipattern Category

### Keyword
runtime
### Note


## Commit #718
### Hash
[83b6f6456b89feebaf3f3ca35edfda3e1664e890](https://github.com/PX4/PX4-Autopilot/commit/83b6f6456b89feebaf3f3ca35edfda3e1664e890)

### Message
refactor I2CSPIInstance: store running instances in a global linked list

instead of a static per-driver array.

Reduces BSS RAM usage by a couple of 100 Bytes (linear increase with num
drivers).

Downsides:
- a bit more runtime overhead
- less isolation, locking required
- a bit more complex
### Antipattern Category

### Keyword
runtime
### Note


## Commit #719
### Hash
[8f3ba81c4ab3b6173de5bc0e36b2421d97ba58d0](https://github.com/PX4/PX4-Autopilot/commit/8f3ba81c4ab3b6173de5bc0e36b2421d97ba58d0)

### Message
refactor atxxxx: use driver base class

and increase update rate to 20Hz
### Antipattern Category

### Keyword
increase
### Note


## Commit #720
### Hash
[3233e0794d0856ace2016133983bfc726409276a](https://github.com/PX4/PX4-Autopilot/commit/3233e0794d0856ace2016133983bfc726409276a)

### Message
navigator: fix edge case with valid idle setpoint

This is an attempt to fix an edge case in the triplet publication which
can lead to crashes on autopilots with slow SD cards.

The sequence of events before this patch is:
1. Switch to POSCTL when disarmed. At this point current valid with
   setpoint idle is published.
2. Arm, takeoff, and fly using joystick/RC.
3. Switch to RTL (or trigger RTL using RC loss). At this point the
   setpoint is valid but still idle and the motors will shut off.
4. Once navigator has published the new setpoint (which can take up to
   1.5 seconds on slow SD cards) we will hopefully recover.

With this patch we omit this edge case, so we never publish this idle
setpoint when landed. The assumption is that this idle setpoint is no
longer required with the current flight task code, however, that needs
to be further verified.
### Antipattern Category

### Keyword
slow
### Note


## Commit #721
### Hash
[8738c26426c243040dd02cf546096bc81bd97b6a](https://github.com/PX4/PX4-Autopilot/commit/8738c26426c243040dd02cf546096bc81bd97b6a)

### Message
boards: enable NuttX SPI DMA buffers

 - update to NuttX with stm32f4 and stm32f7 SPI DMA internal buffers

 - remove explicit DMA buffer allocations from new IMU drivers

 - restore original BOARD_DMA_ALLOC_POOL_SIZE

 - decrease SPI DMA thresholds based on fmu-v2/v3/v4/v5 bench testing
### Antipattern Category

### Keyword
decrease
### Note


## Commit #722
### Hash
[404e781cd9b4a8b66f5a230f0cbfa0da62aeb15e](https://github.com/PX4/PX4-Autopilot/commit/404e781cd9b4a8b66f5a230f0cbfa0da62aeb15e)

### Message
px4_work_queue: increase SPI stack uniformly to silence warnings
### Antipattern Category

### Keyword
increase
### Note


## Commit #723
### Hash
[dc38930bb2232b4bc3b4481e42ab4538b1451789](https://github.com/PX4/PX4-Autopilot/commit/dc38930bb2232b4bc3b4481e42ab4538b1451789)

### Message
AutoSmoothVel: desynchronize XY from Z for small changes in speed

This fixes the issue that makes the drone slow-down even in straight
lines due to the Z component being constrained to a really small value
### Antipattern Category

### Keyword
slow
### Note


## Commit #724
### Hash
[2b82b471c1ec4baf9fa4aeacb6788bf0109c1db4](https://github.com/PX4/PX4-Autopilot/commit/2b82b471c1ec4baf9fa4aeacb6788bf0109c1db4)

### Message
sensor_accel_fifo increase to 32 samples
### Antipattern Category

### Keyword
increase
### Note


## Commit #725
### Hash
[3bcd8c63f8cf8e9b7134dce435af9aec970db9bc](https://github.com/PX4/PX4-Autopilot/commit/3bcd8c63f8cf8e9b7134dce435af9aec970db9bc)

### Message
SMBus battery (a.k.a. smart battery) enhancement. (#14496)

 * Enhancement: State of health, and max_error value is added. Both shows battery health of SMBUS smart battery.

 * Enhancement: BAT_C_MULT parameter is introduced. This is for high-current capable SMBUS-based battery.

As SMBUS only provides 16-bit for current, it could only be +-32768mA which is about +-32A.

But with proper treatment, it could be extended with little accuracy loss.

This factor can be set for individual battery system with available information.

    * Relative SOC introduced. Proper SMBUS battery should provide percentage of remaining battery

directly. Therefore it does not have to be computed like before.

    * State of Health introduced. Proper SMBUS battery should provide SOH value.

    * Max error: this shows estimation error of BMS.

 * Enhancement: With smart battery, precise estimation of time remaining is provided

with impedance track. It is unit of minute, so 60 seconds multiplied.

Update rate of this is not fast, but very useful.



Co-authored-by: Hyon Lim <lim@uvify.com>
### Antipattern Category

### Keyword
fast
### Note


## Commit #726
### Hash
[0d8d4cd6e0e090a90537ac1265033f52b8ff3d86](https://github.com/PX4/PX4-Autopilot/commit/0d8d4cd6e0e090a90537ac1265033f52b8ff3d86)

### Message
SITL configs: improve L1 tracking and increase backtransition duration
-decrease L1 period for tighter mission tracking in fw mode
- increase backtransition duration, we can now do this is we have active
deceleration control

Signed-off-by: RomanBapst <bapstroman@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #727
### Hash
[0a7cde48197f2cfd6c1dcd14f70de0b11599585c](https://github.com/PX4/PX4-Autopilot/commit/0a7cde48197f2cfd6c1dcd14f70de0b11599585c)

### Message
arch.sh: use binary repository for gazebo

This makes installation a lot faster and less error prone.
### Antipattern Category

### Keyword
faster
### Note


## Commit #728
### Hash
[a89bba470a289e4369b325a8ad7fbd30f3e967d2](https://github.com/PX4/PX4-Autopilot/commit/a89bba470a289e4369b325a8ad7fbd30f3e967d2)

### Message
boards: STM32F76xxx/STM32F77xxx linker add ITCM RAM and .ramfuncs handling

 - this doesn't currently change anything, but gets us ready to start
experimenting with using the small amount of instruction tightly memory
on STM32F7
 - the .ramfuncs section works with NuttX CONFIG_ARCH_RAMFUNCS
### Antipattern Category

### Keyword
memory
### Note


## Commit #729
### Hash
[66eacd24bc8ba26f6d22a4596c16040e841d5dc3](https://github.com/PX4/PX4-Autopilot/commit/66eacd24bc8ba26f6d22a4596c16040e841d5dc3)

### Message
px4_fmu-v5_stackcheck: update stack sizes and add to Jenkins

 - increase stack sizes to run cleanly under stackcheck

     - this is likely overkill for most boards, but using stackcheck to set our minimum ensures we have a very safe margin on regular builds and it's something we can currently afford

 - remove holybro_durandal-v1_stackcheck from test rack (there's only one unit)
### Antipattern Category

### Keyword
increase
### Note


## Commit #730
### Hash
[d5e0a52f3fcd5967ee07550feb9404354c8b1010](https://github.com/PX4/PX4-Autopilot/commit/d5e0a52f3fcd5967ee07550feb9404354c8b1010)

### Message
Jenkins: increase history for remaining builds
### Antipattern Category

### Keyword
increase
### Note


## Commit #731
### Hash
[7c7ee115e3bbbb51e1807dcee44b52f5f6fab088](https://github.com/PX4/PX4-Autopilot/commit/7c7ee115e3bbbb51e1807dcee44b52f5f6fab088)

### Message
boards: px4_io-v2 defconfig optimizations to save memory

* disable CONFIG_ARMV7M_MEMCPY to save flash

* disable CONFIG_LIB_BOARDCTL

* remove unnecessary pthread and task settings

* reduce preallocated watchdogs

* reduce console buffer size

* reduce IDLE thread stack

* reduce user main stack



Co-Authored-By: David Sidrane <David.Sidrane@Nscdg.com>
### Antipattern Category

### Keyword
memory
### Note


## Commit #732
### Hash
[70329ce396dc9187144363c7433415bc059c4b57](https://github.com/PX4/PX4-Autopilot/commit/70329ce396dc9187144363c7433415bc059c4b57)

### Message
Update submodule nuttx to latest Sat Apr 25 12:38:14 UTC 2020

    - nuttx in PX4/Firmware (2c938af28051250f90baf7c411179b9b01dc5d0c): https://github.com/PX4/NuttX/commit/7fffab1610d2ea08a95383febd0579e0037b6b51
    - nuttx current upstream: https://github.com/PX4/NuttX/commit/66b4f2c4f2128994f8e8a908d4888f6d37565cfd
    - Changes: https://github.com/PX4/NuttX/compare/7fffab1610d2ea08a95383febd0579e0037b6b51...66b4f2c4f2128994f8e8a908d4888f6d37565cfd

    66b4f2c4f2 2020-04-21 Peter van der Perk - [Backport] Added S32K1XX progmem driver to use the FlexNVM memory
1b3fc1c668 2020-04-10 Peter van der Perk - Added net_trylock so we can call can_input while being in a interrupt handler
### Antipattern Category

### Keyword
memory
### Note


## Commit #733
### Hash
[97bdfd9cece22b71417af8d468f5a6117029dce3](https://github.com/PX4/PX4-Autopilot/commit/97bdfd9cece22b71417af8d468f5a6117029dce3)

### Message
Update submodule ecl to latest Mon Apr 27 12:39:40 UTC 2020

    - ecl in PX4/Firmware (27232514fcaf04924ecb405e144615c23ac6e2e0): https://github.com/PX4/ecl/commit/8a9d961f0d7b0cf6371ab1fcd6d0d2ccb581d3d1
    - ecl current upstream: https://github.com/PX4/ecl/commit/8b6d665a1331f94091caf2f262e09d508eb8975c
    - Changes: https://github.com/PX4/ecl/compare/8a9d961f0d7b0cf6371ab1fcd6d0d2ccb581d3d1...8b6d665a1331f94091caf2f262e09d508eb8975c

    8b6d665 2020-04-26 kamilritz - Avoid subtraction of two uint
70d65ea 2020-04-16 kamilritz - Test:Increase GPS jump need for rejection
c19f40e 2020-04-15 Kamil Ritz - Add reset position test for GPS and VISION
78a6b9f 2020-04-15 Kamil Ritz - SensorSimulator: Fix GPS horizontal position step
050298f 2020-04-08 Kamil Ritz - Improve matrix library usage
5749273 2020-04-08 Kamil Ritz - refactor resetPosition
### Antipattern Category

### Keyword
increase
### Note


## Commit #734
### Hash
[682aa700bb6da790969906ebe925b1be6dbb4a2c](https://github.com/PX4/PX4-Autopilot/commit/682aa700bb6da790969906ebe925b1be6dbb4a2c)

### Message
px4_work_queue: increase wq:attitude_ctrl stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #735
### Hash
[1175c08829a44c5b69fa843baa88845984446fb4](https://github.com/PX4/PX4-Autopilot/commit/1175c08829a44c5b69fa843baa88845984446fb4)

### Message
bmm150: more explicit data conversion & reduce to 30Hz

- 30Hz is the sensors max update rate in continous mode
  (though not in forced mode as we are using it)
- 30Hz allows to increase the quality of the measurements
### Antipattern Category

### Keyword
increase
### Note


## Commit #736
### Hash
[71b942392d3cff66bbf006b3d14ab35bcd4b8028](https://github.com/PX4/PX4-Autopilot/commit/71b942392d3cff66bbf006b3d14ab35bcd4b8028)

### Message
bmm150: cleanup, slightly increase data accuracy

- increased REP_XY and REP_Z: improves accuracy a bit, while increasing
  measurement time (still allows to go to 50Hz, previous max was 100Hz)
- avoid extra transfer in measure()
- extend regdump output
- general code style cleanup
### Antipattern Category

### Keyword
increase
### Note


## Commit #737
### Hash
[6d846143dc7461d9a8ca4fd377763a9f1c04d55c](https://github.com/PX4/PX4-Autopilot/commit/6d846143dc7461d9a8ca4fd377763a9f1c04d55c)

### Message
pwm_out: update pwm outputs up to twice as fast as actual pwm frequency

 - this is done to minimize real end-to-end latency
 - actual pulse width only updated for next period regardless of output module
 - add cycle interval perf counter
### Antipattern Category

### Keyword
fast
### Note


## Commit #738
### Hash
[b933557f56c7287d4338b3f112310eb2a999431d](https://github.com/PX4/PX4-Autopilot/commit/b933557f56c7287d4338b3f112310eb2a999431d)

### Message
Update submodule ecl to latest Tue May 12 00:39:54 UTC 2020

    - ecl in PX4/Firmware (286bf4f0b911fcc040788117ea79c432f6a95a83): https://github.com/PX4/ecl/commit/97b437233e6aad5ddb8a4511697a38ced7bc9b87
    - ecl current upstream: https://github.com/PX4/ecl/commit/03191847f9c162dedc2cb45ff775b75cbc9c8b36
    - Changes: https://github.com/PX4/ecl/compare/97b437233e6aad5ddb8a4511697a38ced7bc9b87...03191847f9c162dedc2cb45ff775b75cbc9c8b36

    0319184 2020-05-11 kritz - Fix ev_pos_obs_var(1) entry (#809)
440383f 2020-05-09 Kamil Ritz - Increase matrix library usage and remove white line
### Antipattern Category

### Keyword
increase
### Note


## Commit #739
### Hash
[3897030c6f378ad5e4e911c111d654a454d3838a](https://github.com/PX4/PX4-Autopilot/commit/3897030c6f378ad5e4e911c111d654a454d3838a)

### Message
Support odometry velocity in body and local frame (#14703)

* Update submodule ECL



* increase lower bound on EVV param
### Antipattern Category

### Keyword
increase
### Note


## Commit #740
### Hash
[9c6f42a8676f5d6250869d1851828e420f491219](https://github.com/PX4/PX4-Autopilot/commit/9c6f42a8676f5d6250869d1851828e420f491219)

### Message
v5x defconfig: increase TELEM2 UART TX buffer size to 3000

Required for very high-rate log streaming @3MBit baudrate.
### Antipattern Category

### Keyword
increase
### Note


## Commit #741
### Hash
[8ee0a5d328ebe59ce65d37bbe48ab4e10fbe1665](https://github.com/PX4/PX4-Autopilot/commit/8ee0a5d328ebe59ce65d37bbe48ab4e10fbe1665)

### Message
px4_work_queue: minor status changes

 - only record start time on first run rather than init
 - increase name length
 - round average interval to nearest microsecond
 - basic formatting consistency (google style guide)
### Antipattern Category

### Keyword
increase
### Note


## Commit #742
### Hash
[05856c102949841387c0fc510f6e5e357f8f66fc](https://github.com/PX4/PX4-Autopilot/commit/05856c102949841387c0fc510f6e5e357f8f66fc)

### Message
ROMFS: holybro s500 decrease filter defaults
### Antipattern Category

### Keyword
decrease
### Note


## Commit #743
### Hash
[0ec48cfef369bce210a32bcc9c0def35c1b0ec45](https://github.com/PX4/PX4-Autopilot/commit/0ec48cfef369bce210a32bcc9c0def35c1b0ec45)

### Message
ekf2: increase default baro noise 2 -> 3.5 m
### Antipattern Category

### Keyword
increase
### Note


## Commit #744
### Hash
[11585dfb6756fc6a27058a19d0604c6baf7b8aab](https://github.com/PX4/PX4-Autopilot/commit/11585dfb6756fc6a27058a19d0604c6baf7b8aab)

### Message
ekf2: decrease default GPS horizontal velocity noise
### Antipattern Category

### Keyword
decrease
### Note


## Commit #745
### Hash
[31fe7af45453394feda9d253fb056be9ba7a1999](https://github.com/PX4/PX4-Autopilot/commit/31fe7af45453394feda9d253fb056be9ba7a1999)

### Message
selectively increase optimization -Os -> -O2

 - targetted at modules/libraries that benefit without drastically
increasing flash usage
 - ignored on boards with CONSTRAINED_FLASH set
### Antipattern Category

### Keyword
increase
### Note


## Commit #746
### Hash
[a1b0634258b8c35c847e2ce681c6907992e99c28](https://github.com/PX4/PX4-Autopilot/commit/a1b0634258b8c35c847e2ce681c6907992e99c28)

### Message
Jenkins HIL test fix sensor timeouts

 - stop logger when running tests
 - decrease test priorities
 - hrt test don't flush output
### Antipattern Category

### Keyword
decrease
### Note


## Commit #747
### Hash
[5286ed3a1179900ed2a15cd98bcf5910781fe9e4](https://github.com/PX4/PX4-Autopilot/commit/5286ed3a1179900ed2a15cd98bcf5910781fe9e4)

### Message
imu/invensense/mpu6000: minor improvements

 - at start perform full sensor signal path reset and wait for max time
 - issue full sensor reset on any error
 - only allocate DRDY perf counter if GPIO is available
 - allow running faster than accel ODR (safe limit of 2 kHz in place)
### Antipattern Category

### Keyword
faster
### Note


## Commit #748
### Hash
[10afcdce2e9a49d7a2e54999414e200abc816a3d](https://github.com/PX4/PX4-Autopilot/commit/10afcdce2e9a49d7a2e54999414e200abc816a3d)

### Message
Hex/Proficnc Cube Yellow: align firmware location in flash memory to be able to use the default bootloader
### Antipattern Category

### Keyword
memory
### Note


## Commit #749
### Hash
[588d551098bd238d26f49f2c74bb4676ba64eda4](https://github.com/PX4/PX4-Autopilot/commit/588d551098bd238d26f49f2c74bb4676ba64eda4)

### Message
mc_pos_control_params: set the ground slow down speed to the default maximum speed

This results in no change with defaults but a slow down to 10m/s if the maxiumum speed is set higher than that.
### Antipattern Category

### Keyword
slow
### Note


## Commit #750
### Hash
[be2081a2a2101dc9a7761b350c1b08b662f42a03](https://github.com/PX4/PX4-Autopilot/commit/be2081a2a2101dc9a7761b350c1b08b662f42a03)

### Message
wq:attitude_ctrl small stack increase
### Antipattern Category

### Keyword
increase
### Note


## Commit #751
### Hash
[0eea814ca1874b802a4093ed5702c5f79b6c9e61](https://github.com/PX4/PX4-Autopilot/commit/0eea814ca1874b802a4093ed5702c5f79b6c9e61)

### Message
decrease all wq:SPIx stack
### Antipattern Category

### Keyword
decrease
### Note


## Commit #752
### Hash
[dc69d9976428131c99f1c242af98886ad3dafec2](https://github.com/PX4/PX4-Autopilot/commit/dc69d9976428131c99f1c242af98886ad3dafec2)

### Message
add support to FastRTPS 2.0.0 (Fast-DDS)
### Antipattern Category

### Keyword
fast
### Note


## Commit #753
### Hash
[38588f0c37f4512ab4c5f32d2ce4efc838dede46](https://github.com/PX4/PX4-Autopilot/commit/38588f0c37f4512ab4c5f32d2ce4efc838dede46)

### Message
Update submodule ecl to latest Tue Jun 30 00:38:47 UTC 2020

    - ecl in PX4/Firmware (bd4d3f2b9929271b2616d2e1d6952059a7e8bc72): https://github.com/PX4/ecl/commit/e4b44f704bb641fa93bedc81734c5249fcd9ed42
    - ecl current upstream: https://github.com/PX4/ecl/commit/5356077a3244a9a29adfae4aeaaab900cd28e9e8
    - Changes: https://github.com/PX4/ecl/compare/e4b44f704bb641fa93bedc81734c5249fcd9ed42...5356077a3244a9a29adfae4aeaaab900cd28e9e8

    5356077 2020-06-21 kamilritz - Make flow_innov/-var a matrix Vector2f
c2801eb 2020-06-21 kamilritz - Add const modifier and increase matrix library usage
d9afc2f 2020-06-21 kamilritz - Remove repeated division by same value
d16b43a 2020-06-21 kamilritz - Get rid of non functional piece of code
c3653e6 2020-06-21 kamilritz - Add const modifier
48f0eb1 2020-06-21 kamilritz - Remove uninformative comments
4a69b41 2020-06-21 kamilritz - Increase matrix library usage even more
630be60 2020-06-21 kamilritz - Increase matrix library usage
22274b1 2020-06-21 kamilritz - Add const modifier
61c139e 2020-06-21 kamilritz - Remove unused variable
afd4f3f 2020-06-21 kamilritz - Fix typo
a3706fd 2020-06-21 kamilritz - Make relative wind computation more compact
b8f9376 2020-06-21 kamilritz - Make mag_innov/-var a Matrix::Vector3f
0ea7cd8 2020-06-25 Kamil Ritz - Attempt to fix CI firmware build test
2927132 2020-06-25 Daniel Agar - clang-format set BreakBeforeBraces to Linux style
b96c62e 2020-06-25 sevenbill - Optionalized build dependency on git
794e6ec 2020-06-25 Bill Morris - Enforce tabs via editorcofig
### Antipattern Category

### Keyword
increase
### Note


## Commit #754
### Hash
[96a6b5c914afa44a01aa782944dce034ce6b4a2b](https://github.com/PX4/PX4-Autopilot/commit/96a6b5c914afa44a01aa782944dce034ce6b4a2b)

### Message
load_mon: decrease warning threshold for stack check builds

 - enabling stack check increases stack usage and will assert if there's
any overflow
### Antipattern Category

### Keyword
decrease
### Note


## Commit #755
### Hash
[4ad7ea6c1a7e8e2837e24dcd2c9546486e19de80](https://github.com/PX4/PX4-Autopilot/commit/4ad7ea6c1a7e8e2837e24dcd2c9546486e19de80)

### Message
mavsdk_tests: increase the poll time resolution

With only 10 steps for e.g. 60 seconds we are likely to miss updates.
### Antipattern Category

### Keyword
increase
### Note


## Commit #756
### Hash
[079c5a11c2e2eefe88cd1bf7a9a92b74a1222cf5](https://github.com/PX4/PX4-Autopilot/commit/079c5a11c2e2eefe88cd1bf7a9a92b74a1222cf5)

### Message
FlightTaskAuto: allow rc assist to stop descend

Before the autohority was only enough to slow down the descend but not
stop to zero vertical velocity.
### Antipattern Category

### Keyword
slow
### Note


## Commit #757
### Hash
[fd66d429064bf7f515431873e9efa28d1cf6a070](https://github.com/PX4/PX4-Autopilot/commit/fd66d429064bf7f515431873e9efa28d1cf6a070)

### Message
load_mon updates

 - increase rate
 - cpu load calculation grab timestamp atomically
 - only check one task per cycle (but cycle at a higher rate)
 - decrease available FD threshold
 - minor cleanup
### Antipattern Category

### Keyword
increase
### Note


## Commit #758
### Hash
[bdb4251fa4a8f758b00c03f76f48cc621772bf1b](https://github.com/PX4/PX4-Autopilot/commit/bdb4251fa4a8f758b00c03f76f48cc621772bf1b)

### Message
fw_pos_control_l1: if using air data (baro) copy every cycle

 - vehicle_air_data won't necessary have an update every iteration and these adjusted throttle values aren't stored

 - this only would have worked in the past because the vast majority of systems were using the ms5611 barometer with a publication rate that's faster than the controller
### Antipattern Category

### Keyword
faster
### Note


## Commit #759
### Hash
[42493b3d59d9a7f69e43ff74b81810d78cd73856](https://github.com/PX4/PX4-Autopilot/commit/42493b3d59d9a7f69e43ff74b81810d78cd73856)

### Message
logger: add full commander and safety logging by default

 - increase battery_status rate to be useful
### Antipattern Category

### Keyword
increase
### Note


## Commit #760
### Hash
[b54dea0ccdec72290733233ffb439de82756febe](https://github.com/PX4/PX4-Autopilot/commit/b54dea0ccdec72290733233ffb439de82756febe)

### Message
wq:attitude_ctrl: small stack increase to silence warning
### Antipattern Category

### Keyword
increase
### Note


## Commit #761
### Hash
[26021b01cb68c3d1b77ff1db1adae07f793bab00](https://github.com/PX4/PX4-Autopilot/commit/26021b01cb68c3d1b77ff1db1adae07f793bab00)

### Message
Tools: abort SITL start if gzserver fails

Sometimes gzserver seems to not start or not start fast enough. In this
case, instead of stalling forever, it would be nice to abort.
### Antipattern Category

### Keyword
fast
### Note


## Commit #762
### Hash
[9426c68a13fd9c167352dea864672e03307fa9c1](https://github.com/PX4/PX4-Autopilot/commit/9426c68a13fd9c167352dea864672e03307fa9c1)

### Message
cmake: only allow gold linker for posix builds

 - the gold linker doesn't currently work for NuttX builds
 - NuttX skip --print-memory-usage if using the GOLD linker
 - fixes #15400
### Antipattern Category

### Keyword
memory
### Note


## Commit #763
### Hash
[1b30bd328e3d40170f1e875b52813b4af65d1acb](https://github.com/PX4/PX4-Autopilot/commit/1b30bd328e3d40170f1e875b52813b4af65d1acb)

### Message
logger: decrease try subsribe interval 1000 ms -> 20 ms
### Antipattern Category

### Keyword
decrease
### Note


## Commit #764
### Hash
[e4fa7597f4916185d0b1e97bc334b605fcde713c](https://github.com/PX4/PX4-Autopilot/commit/e4fa7597f4916185d0b1e97bc334b605fcde713c)

### Message
logger: SDLOG_PROFILE remove estimator replay from default to minimize log rate

 - log full sensor_combined by default for now

 - small decrease to input_rc rate (manual_control_setpoint is no longer filtered)

 - sensor_correction can be logged at full rate (low publication rate)
### Antipattern Category

### Keyword
decrease
### Note


## Commit #765
### Hash
[3345bf39b8d990acf817a27750ca1142689ab565](https://github.com/PX4/PX4-Autopilot/commit/3345bf39b8d990acf817a27750ca1142689ab565)

### Message
cdev: remove unnecessary virtuals and increase opt level

 - poll, poll_notify, register_class_devname, unregister_class_devname aren't virtual
 - increase max optimization level on platforms that aren't flash constrained (MAX_CUSTOM_OPT_LEVEL)
### Antipattern Category

### Keyword
increase
### Note


## Commit #766
### Hash
[0c91a29c3f401ebe567ff25ba6a21e95c5be507a](https://github.com/PX4/PX4-Autopilot/commit/0c91a29c3f401ebe567ff25ba6a21e95c5be507a)

### Message
wq:attitude_ctrl increase stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #767
### Hash
[ad3e6ee5ddeb534d04392ae614c7bcfc9c2f8f01](https://github.com/PX4/PX4-Autopilot/commit/ad3e6ee5ddeb534d04392ae614c7bcfc9c2f8f01)

### Message
wq:attitude_ctrl increase stack by 16 bytes (again)
### Antipattern Category

### Keyword
increase
### Note


## Commit #768
### Hash
[7958586f35e31b8f2a17e2dcfde010ac36f7a5b8](https://github.com/PX4/PX4-Autopilot/commit/7958586f35e31b8f2a17e2dcfde010ac36f7a5b8)

### Message
Only use roll/pitch not centered for RC override, and increase override threshold
### Antipattern Category

### Keyword
increase
### Note


## Commit #769
### Hash
[2bb04f2261c75cb48d36ed9f826414871ccfaf2b](https://github.com/PX4/PX4-Autopilot/commit/2bb04f2261c75cb48d36ed9f826414871ccfaf2b)

### Message
commander: increase COM_ARM_MAG_ANG 35 -> 45 degrees

 - in practice this is mostly useful for identifying incorrect rotations
which we mostly have in 45 degree increments
 - handling a vehicle on the ground can easily disturb one mag by more than 30 degrees, so this is often distracting noise
### Antipattern Category

### Keyword
increase
### Note


## Commit #770
### Hash
[dd9676b73e0ffb79a4bfd4afd7cb97c8689e0de0](https://github.com/PX4/PX4-Autopilot/commit/dd9676b73e0ffb79a4bfd4afd7cb97c8689e0de0)

### Message
boards: px4/fmu-v5_debug increase interrupt stack 512 -> 768 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #771
### Hash
[7c2bb6a983509ae4ba5133898b76f9f373122a91](https://github.com/PX4/PX4-Autopilot/commit/7c2bb6a983509ae4ba5133898b76f9f373122a91)

### Message
Jenkins: hardware increase timeout
### Antipattern Category

### Keyword
increase
### Note


## Commit #772
### Hash
[3fa9ff6d20ba33ebc4d6e888bfd703da5612a7f3](https://github.com/PX4/PX4-Autopilot/commit/3fa9ff6d20ba33ebc4d6e888bfd703da5612a7f3)

### Message
boards: px4_fmu-v5_debug increase LPWORK stack 1632 -> 1728 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #773
### Hash
[e906106ea267450b706f0e80d294b8c5acb16135](https://github.com/PX4/PX4-Autopilot/commit/e906106ea267450b706f0e80d294b8c5acb16135)

### Message
gps: fix memory leak on module exit (delete _helper)
### Antipattern Category

### Keyword
memory
### Note


## Commit #774
### Hash
[a5a577a6c469b52bfb84f56349f4231e637b2141](https://github.com/PX4/PX4-Autopilot/commit/a5a577a6c469b52bfb84f56349f4231e637b2141)

### Message
mavsdk_tests: use speed factor, increase timeouts

We had not actually properly adjusted the timeout to the lockstep speed
factor. Once we did that, we had to increase the timeouts quite a bit to
have the tests pass.
### Antipattern Category

### Keyword
increase
### Note


## Commit #775
### Hash
[f8f03835ad76529a70f8225d21f82f59a4996570](https://github.com/PX4/PX4-Autopilot/commit/f8f03835ad76529a70f8225d21f82f59a4996570)

### Message
mavsdk_tests: increase timeouts yet again

This is after using PX4 time to check for timeouts.
### Antipattern Category

### Keyword
increase
### Note


## Commit #776
### Hash
[d2cb27e0de2fc9d447a4557e2e1ab1d58e9ad098](https://github.com/PX4/PX4-Autopilot/commit/d2cb27e0de2fc9d447a4557e2e1ab1d58e9ad098)

### Message
mavsdk_tests: try with faster RC rate
### Antipattern Category

### Keyword
faster
### Note


## Commit #777
### Hash
[012763e5f1876c27f0dbbfd2029888755c7d59a0](https://github.com/PX4/PX4-Autopilot/commit/012763e5f1876c27f0dbbfd2029888755c7d59a0)

### Message
mavsdk_tests: fly forward a bit longer

Hopefully, that's long enough for slow VTOLs.
### Antipattern Category

### Keyword
slow
### Note


## Commit #778
### Hash
[44b4a6eb74c407fb26923ed36714bd80944a409b](https://github.com/PX4/PX4-Autopilot/commit/44b4a6eb74c407fb26923ed36714bd80944a409b)

### Message
mavsdk_tests: increase time for manual tests
### Antipattern Category

### Keyword
increase
### Note


## Commit #779
### Hash
[d676e65294b27b592e06381a12b0f3b40b6139f0](https://github.com/PX4/PX4-Autopilot/commit/d676e65294b27b592e06381a12b0f3b40b6139f0)

### Message
logger: log_writer_file increase stack 1170 -> 1472 bytes (#15765)
### Antipattern Category

### Keyword
increase
### Note


## Commit #780
### Hash
[0dc8bb9c864dc49bbbe255ea0177480b46522d7d](https://github.com/PX4/PX4-Autopilot/commit/0dc8bb9c864dc49bbbe255ea0177480b46522d7d)

### Message
uORB: increase ORB_MULTI_MAX_INSTANCES 4 -> 10

 - put more realistic bounds on maximum number of battery instances, gps, etc
### Antipattern Category

### Keyword
increase
### Note


## Commit #781
### Hash
[60252dde08ac33a97bda3b8497035483b250097b](https://github.com/PX4/PX4-Autopilot/commit/60252dde08ac33a97bda3b8497035483b250097b)

### Message
Jenkins: SITL tests disable ninja build to reduce build parallelism

 - test slaves have limited memory
### Antipattern Category

### Keyword
memory
### Note


## Commit #782
### Hash
[e792c46f20bb6709afc4a1151df29546b165d1d1](https://github.com/PX4/PX4-Autopilot/commit/e792c46f20bb6709afc4a1151df29546b165d1d1)

### Message
mavlink: increase stack 2650 -> 2848 bytes (#15821)
### Antipattern Category

### Keyword
increase
### Note


## Commit #783
### Hash
[c648d529090e3ba6f26b3e1bca3a03757ce3a758](https://github.com/PX4/PX4-Autopilot/commit/c648d529090e3ba6f26b3e1bca3a03757ce3a758)

### Message
uavcan: Increase uavcan main stack size

I observed stack overflows when executing `uavcan params list`, so the
stack size probably needs to be increased.

Signed-off-by: Alex Mikhalev <alexmikhalevalex@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #784
### Hash
[84455ac9e35f872db88b67dce5b08be7923b9b00](https://github.com/PX4/PX4-Autopilot/commit/84455ac9e35f872db88b67dce5b08be7923b9b00)

### Message
logger: increase logging rate of airspeed_validated from 1Hz to 5Hz

Signed-off-by: Silvan Fuhrer <silvan@auterion.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #785
### Hash
[5c2cc531343638da15a9b33af804618e087d8d8e](https://github.com/PX4/PX4-Autopilot/commit/5c2cc531343638da15a9b33af804618e087d8d8e)

### Message
Revert "logger: log_writer_file increase stack 1170 -> 1472 bytes (#15765)"

This reverts commit d676e65294b27b592e06381a12b0f3b40b6139f0.
### Antipattern Category

### Keyword
increase
### Note


## Commit #786
### Hash
[34ad85557e8ffc26dd882bfca186fbafb8126516](https://github.com/PX4/PX4-Autopilot/commit/34ad85557e8ffc26dd882bfca186fbafb8126516)

### Message
Revert "mavlink: increase stack 2650 -> 2848 bytes (#15821)"

This reverts commit e792c46f20bb6709afc4a1151df29546b165d1d1.
### Antipattern Category

### Keyword
increase
### Note


## Commit #787
### Hash
[614a0ac2a20ac4292ff29b1def1eb8c79e84bfb1](https://github.com/PX4/PX4-Autopilot/commit/614a0ac2a20ac4292ff29b1def1eb8c79e84bfb1)

### Message
experimental/gyro_fft: improve peak detection, add start parameter

 - add new parameter `IMU_GYRO_FFT_EN` to start

 - add 75% overlap in buffer to increase FFT update rate

 - space out FFT calls (no more than 1 per cycle)

 - increase `IMU_GYRO_FFT_MIN` default

 - decrease main stack usage
### Antipattern Category

### Keyword
increase
### Note


## Commit #788
### Hash
[ea2fced6ad18fdc3ce7e0c63e69e92863780b982](https://github.com/PX4/PX4-Autopilot/commit/ea2fced6ad18fdc3ce7e0c63e69e92863780b982)

### Message
Tools/check_submodules.sh: always update if within vscode cmake configure

 - the interactive portion of check_git_submodule with hang waiting for user input
### Antipattern Category

### Keyword
hang
### Note


## Commit #789
### Hash
[e6ad321ab2df10b8585d4ae4140b5ff5765966a9](https://github.com/PX4/PX4-Autopilot/commit/e6ad321ab2df10b8585d4ae4140b5ff5765966a9)

### Message
gps: add GPS_{1,2}_PROTOCOL param to select protocol, default to u-blox

u-blox is the most widely used GPS, so module detection should be a bit
faster in general.
### Antipattern Category

### Keyword
faster
### Note


## Commit #790
### Hash
[91d1825fcf25bfe7f4f98379f0501bcde41ef51c](https://github.com/PX4/PX4-Autopilot/commit/91d1825fcf25bfe7f4f98379f0501bcde41ef51c)

### Message
Fix non-determinstic boot hang with crashdumps

On boot, if board_hardfault_init finds a hardfault stored in BBSRAM, it
checks if there is any data available on stdin to see if there is
somebody there to respond to a prompt. But on boards such as cubeorange
where there is not a serial console by default, the ioctl fails and
bytesWaiting is uninitialized. So it will non-deterministally hang the
boot process with no outside feedback if that value is not zero.

Signed-off-by: Alex Mikhalev <alexmikhalevalex@gmail.com>
### Antipattern Category

### Keyword
hang
### Note


## Commit #791
### Hash
[c60743b306a510a6e9059c96cc6b9c9c7d6ae702](https://github.com/PX4/PX4-Autopilot/commit/c60743b306a510a6e9059c96cc6b9c9c7d6ae702)

### Message
boards: NuttX increase file name max 32 -> 40
### Antipattern Category

### Keyword
increase
### Note


## Commit #792
### Hash
[7ba73b46ca11cfb2167541d18a3e353681f43305](https://github.com/PX4/PX4-Autopilot/commit/7ba73b46ca11cfb2167541d18a3e353681f43305)

### Message
uORB: tests decrease stack

 - save a bit of memory for running on older boards
### Antipattern Category

### Keyword
memory
### Note


## Commit #793
### Hash
[963d101375d3dc6646b3d0e2fe432e4706a32fa1](https://github.com/PX4/PX4-Autopilot/commit/963d101375d3dc6646b3d0e2fe432e4706a32fa1)

### Message
boards: fmu-v5 debug and stackcheck increase interrupt stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #794
### Hash
[ad4068f472e8c8416899d3437f5892f86956d126](https://github.com/PX4/PX4-Autopilot/commit/ad4068f472e8c8416899d3437f5892f86956d126)

### Message
platforms/posix: mlockall() support

 * add basic mlock support to increase stability when system is under high load and RAM is almost full

 * mainly about minimizing or completely eliminating RAM page swap time
### Antipattern Category

### Keyword
increase
### Note


## Commit #795
### Hash
[ed8a30d73ef3306b5bc18f8993600e5d0f85e148](https://github.com/PX4/PX4-Autopilot/commit/ed8a30d73ef3306b5bc18f8993600e5d0f85e148)

### Message
mavlink: STATUSTEXT directly use mavlink_log subscription

 - ORB_ID(mavlink_log) increase queue depth now that mavlink ringbuffer is gone
### Antipattern Category

### Keyword
increase
### Note


## Commit #796
### Hash
[e1168070d1065d406af90f37c36baef33e7312cf](https://github.com/PX4/PX4-Autopilot/commit/e1168070d1065d406af90f37c36baef33e7312cf)

### Message
mavlink: decrease task stack
### Antipattern Category

### Keyword
decrease
### Note


## Commit #797
### Hash
[e69aea0a9bc830bbdae38d2325de45fd6279c2a0](https://github.com/PX4/PX4-Autopilot/commit/e69aea0a9bc830bbdae38d2325de45fd6279c2a0)

### Message
parameters: don't keep in memory if set to default
### Antipattern Category

### Keyword
memory
### Note


## Commit #798
### Hash
[229f02a4f9491ca557b83f7e36160821b825e362](https://github.com/PX4/PX4-Autopilot/commit/229f02a4f9491ca557b83f7e36160821b825e362)

### Message
mtd:Reduce functionality on memory constrained systems
### Antipattern Category

### Keyword
memory
### Note


## Commit #799
### Hash
[8d8a31c56da788792490e7a275d2eff237edc831](https://github.com/PX4/PX4-Autopilot/commit/8d8a31c56da788792490e7a275d2eff237edc831)

### Message
WorkQueueManager:Increase stack size
### Antipattern Category

### Keyword
increase
### Note


## Commit #800
### Hash
[1dd22acd128622550bc6c074c3704d7da254bbac](https://github.com/PX4/PX4-Autopilot/commit/1dd22acd128622550bc6c074c3704d7da254bbac)

### Message
nxp_fmurt1062-v1:Fix memory overflow
### Antipattern Category

### Keyword
memory
### Note


## Commit #801
### Hash
[0433f4d33c27c066d4d710317256eab396228d9a](https://github.com/PX4/PX4-Autopilot/commit/0433f4d33c27c066d4d710317256eab396228d9a)

### Message
land_detector: decrease default LNDFW_AIRSPD_MAX 8 -> 6 m/s
### Antipattern Category

### Keyword
decrease
### Note


## Commit #802
### Hash
[690c1158addf03cfd29be10945dca644707309e7](https://github.com/PX4/PX4-Autopilot/commit/690c1158addf03cfd29be10945dca644707309e7)

### Message
HTE: do not update the estimator during fast up/down motions

Drag and prop wash effects produce significant forces at high speed
that can bias the estimator when applied for an extended period of time
### Antipattern Category

### Keyword
fast
### Note


## Commit #803
### Hash
[c253badba4dfb52bc7e4a114d0f0646ccae320da](https://github.com/PX4/PX4-Autopilot/commit/c253badba4dfb52bc7e4a114d0f0646ccae320da)

### Message
HTE: remove dist_bottom validity check

Without range finder, the validity flag goes to false quite quickly and
if can be that a vehicle never starts HTE is the takeoff is too slow.
In this specific context of takeoff detection, since
the exact value is not important, we can safely ignore the validity flag.
### Antipattern Category

### Keyword
slow
### Note


## Commit #804
### Hash
[ec793615484370ab7fd1aacd42cc05c6a4b0ccb4](https://github.com/PX4/PX4-Autopilot/commit/ec793615484370ab7fd1aacd42cc05c6a4b0ccb4)

### Message
Update submodule sitl_gazebo to latest Mon Dec 21 00:39:43 UTC 2020

    - sitl_gazebo in PX4/Firmware (5868463d069eb652ff341427d3714133dde3c19d): https://github.com/PX4/PX4-SITL_gazebo/commit/563f0876a52d5c0fba1b7cd1aa420c613ec7025b
    - sitl_gazebo current upstream: https://github.com/PX4/PX4-SITL_gazebo/commit/4043287bbe07a9d091d579b755796e70d45058e8
    - Changes: https://github.com/PX4/PX4-SITL_gazebo/compare/563f0876a52d5c0fba1b7cd1aa420c613ec7025b...4043287bbe07a9d091d579b755796e70d45058e8

    4043287 2020-12-20 Silvan Fuhrer - tiltrotor: increase wing area to 0.5 per side (#678)
f004811 2020-12-20 JaeyoungLim - Update mavsdk version for SITL tests (#673)
### Antipattern Category

### Keyword
increase
### Note


## Commit #805
### Hash
[565da15f2f8176999077fac1933a4d5ba7010080](https://github.com/PX4/PX4-Autopilot/commit/565da15f2f8176999077fac1933a4d5ba7010080)

### Message
MAVSDK test: Increase timeout
### Antipattern Category

### Keyword
increase
### Note


## Commit #806
### Hash
[6c9072720e01b02c43b9077d648325d936b0f5da](https://github.com/PX4/PX4-Autopilot/commit/6c9072720e01b02c43b9077d648325d936b0f5da)

### Message
invensense/icm42688p: use full 20 bit data, increase ODR, disable all filters
### Antipattern Category

### Keyword
increase
### Note


## Commit #807
### Hash
[c6af260a41acaf3e3586465656953847bb349fe2](https://github.com/PX4/PX4-Autopilot/commit/c6af260a41acaf3e3586465656953847bb349fe2)

### Message
log_message increase queue depth 2->4
### Antipattern Category

### Keyword
increase
### Note


## Commit #808
### Hash
[70e503cb919928493ee6acefaf22ce0a529e2cdb](https://github.com/PX4/PX4-Autopilot/commit/70e503cb919928493ee6acefaf22ce0a529e2cdb)

### Message
rotation: use Dcmf for all rotations that aren't direct swaps

 - increase optimization to ${MAX_CUSTOM_OPT_LEVEL} (max per board)
### Antipattern Category

### Keyword
increase
### Note


## Commit #809
### Hash
[967d35a6b69cda58be5154598433ba8ce9afb73c](https://github.com/PX4/PX4-Autopilot/commit/967d35a6b69cda58be5154598433ba8ce9afb73c)

### Message
rate limit most parameter_update subscriptions

 - parameter updates can be quite expensive because they trigger nearly all modules to reload all of their parameters immediately

 - limit modules from updating faster than once per second
### Antipattern Category

### Keyword
faster
### Note


## Commit #810
### Hash
[1ac70cc72f1409a84c78da809f35324a426f83de](https://github.com/PX4/PX4-Autopilot/commit/1ac70cc72f1409a84c78da809f35324a426f83de)

### Message
can-gps-v1:Correct Memory size used by app and bootloader size
### Antipattern Category

### Keyword
memory
### Note


## Commit #811
### Hash
[037c8211421ce28b6b227bce26a138b42c2a67b3](https://github.com/PX4/PX4-Autopilot/commit/037c8211421ce28b6b227bce26a138b42c2a67b3)

### Message
ROMFS: increase max distance between waypoints for VTOL and FW to 5km

Signed-off-by: Silvan Fuhrer <silvan@auterion.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #812
### Hash
[920d6d84b5d7a046971e20f307a3fad6d45a1121](https://github.com/PX4/PX4-Autopilot/commit/920d6d84b5d7a046971e20f307a3fad6d45a1121)

### Message
rtps: increase non-alias ID range by reducing the alias space ID
### Antipattern Category

### Keyword
increase
### Note


## Commit #813
### Hash
[0e86ab47f645415854915ca251ef237344f4469d](https://github.com/PX4/PX4-Autopilot/commit/0e86ab47f645415854915ca251ef237344f4469d)

### Message
fix control_allocator: use 'delete' instead of 'free', guard against out-of-memory
### Antipattern Category

### Keyword
memory
### Note


## Commit #814
### Hash
[cea8ad4236b77c36669d9208db1a4869773c32b5](https://github.com/PX4/PX4-Autopilot/commit/cea8ad4236b77c36669d9208db1a4869773c32b5)

### Message
Control Zero F7 - RSSI Fix - SBUS Only/PPM Partial

This fixes RSSI for the Control Zero F7 but I have noticed that while this works perfectly for SBUS receivers, for PPM receivers it does not decrease the RSSI visual value in QGC when removing the RC transmitter connection.



When a PPM receiver is connected and the connection is lost the autopilot goes into RC Scan Mode (in the RC Update Module) to determine what is connected (even though something already is connected).



The main issue with this is that PPM receivers don't go into RC Failsafe but I don't think it is an issue with this autopilot. It looks to be an issue with the RC Update Module and how it is handled at the module level for non I/O coprocessor autopilots. 





Tested with an X8R (SBUS) and a Dragonlink (PPM) as well as a Dragonlink set to SBUS as the output. SBUS worked as intended. See screenshots below.
### Antipattern Category

### Keyword
decrease
### Note


## Commit #815
### Hash
[d5c7e243a9923ad1d31797aa16f1afe1bb80f5ea](https://github.com/PX4/PX4-Autopilot/commit/d5c7e243a9923ad1d31797aa16f1afe1bb80f5ea)

### Message
vehicle_command: increase queue depth 4 -> 8

 - prevent slower modules from missing commands
### Antipattern Category

### Keyword
slower
### Note


## Commit #816
### Hash
[15cbe8c09aa2cdcbd26d4f9fe524e8ab17792d5b](https://github.com/PX4/PX4-Autopilot/commit/15cbe8c09aa2cdcbd26d4f9fe524e8ab17792d5b)

### Message
px4_work_queue: wq:nav_and_controllers increase stack 1730 -> 1760 bytes
### Antipattern Category

### Keyword
increase
### Note


## Commit #817
### Hash
[a4745c6825e0dc10356f8151f969d93345175e8f](https://github.com/PX4/PX4-Autopilot/commit/a4745c6825e0dc10356f8151f969d93345175e8f)

### Message
Simulator: Fix for arg count increase breaking remote host option.

The number of arguments was increased by one, see: https://github.com/PX4/PX4-Autopilot/commit/1719ff9892f3c3d034f2b44e94d15527ab09cec6

Because the above commit was merged before https://github.com/PX4/PX4-Autopilot/pull/15443 . It broke support for the remote host option.

This has been fixed in this commit by increasing all argv's by one.

Signed-off-by: Peter Blom <peterblom.mail@gmail.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #818
### Hash
[14cb98a6b4642751041b22c06c13654a828c0644](https://github.com/PX4/PX4-Autopilot/commit/14cb98a6b4642751041b22c06c13654a828c0644)

### Message
Increase corridor check thresholds for mission tests
### Antipattern Category

### Keyword
increase
### Note


## Commit #819
### Hash
[27138578f09560eabb9461e5b72304e91f756b02](https://github.com/PX4/PX4-Autopilot/commit/27138578f09560eabb9461e5b72304e91f756b02)

### Message
Disable unmaintained MAVROS tests
The overhead of the MAVROS setup means that most developers are not using it, leading to tests that are not suitable for day-to-day workflows. We are replacing these with MAVSDK tests that can be run locally pre-commit.
### Antipattern Category

### Keyword
overhead
### Note


## Commit #820
### Hash
[0c74028976ef13697522bacbc6ac13effc898db3](https://github.com/PX4/PX4-Autopilot/commit/0c74028976ef13697522bacbc6ac13effc898db3)

### Message
FMUK66 Decrease telnetd ram usage
### Antipattern Category

### Keyword
decrease
### Note


## Commit #821
### Hash
[e2e5fc85f8f3c3ad64eddf79ec20f702ed6e72ad](https://github.com/PX4/PX4-Autopilot/commit/e2e5fc85f8f3c3ad64eddf79ec20f702ed6e72ad)

### Message
state_machine_helper: fix infinite delay with intermittent failsafes
### Antipattern Category

### Keyword
infinite
### Note


## Commit #822
### Hash
[44872807b370b7c319451290be19de0e5f1ff48a](https://github.com/PX4/PX4-Autopilot/commit/44872807b370b7c319451290be19de0e5f1ff48a)

### Message
MC auto: add parameter to set the trajectory slow-down

In some cases e.g.: (VTOL in wind) a good tracking cannot be
achieved. This condition then needs to be relaxed, otherwise the
drone cannot land properly.
### Antipattern Category

### Keyword
slow
### Note


## Commit #823
### Hash
[72e34e02ef28eaa6a46791d43897209d70753440](https://github.com/PX4/PX4-Autopilot/commit/72e34e02ef28eaa6a46791d43897209d70753440)

### Message
VTOL defaults: increase tracking tolerance for VTOL planes
### Antipattern Category

### Keyword
increase
### Note


## Commit #824
### Hash
[f8989fe5aa376388a017ad33dbefc2b4763611f2](https://github.com/PX4/PX4-Autopilot/commit/f8989fe5aa376388a017ad33dbefc2b4763611f2)

### Message
mavlink: speed up ftp transfers on POSIX

Around 900 KB/s - not fast, but should be fast enough for the use-cases.
### Antipattern Category

### Keyword
fast
### Note


## Commit #825
### Hash
[c63107bb5795b1a63ba320536c2fcc73fd144de1](https://github.com/PX4/PX4-Autopilot/commit/c63107bb5795b1a63ba320536c2fcc73fd144de1)

### Message
uORB: tests increase priorities to minimize failures with stackcheck/debug enabled

 - also relax the maximum mean by 50%
### Antipattern Category

### Keyword
increase
### Note


## Commit #826
### Hash
[b8b13bb882cbeed672addfd3140114d699b0b566](https://github.com/PX4/PX4-Autopilot/commit/b8b13bb882cbeed672addfd3140114d699b0b566)

### Message
parameters runtime defaults
### Antipattern Category

### Keyword
runtime
### Note


## Commit #827
### Hash
[48b00ff67881f4f2cfeffa18980191e38f896fd3](https://github.com/PX4/PX4-Autopilot/commit/48b00ff67881f4f2cfeffa18980191e38f896fd3)

### Message
Support for gimbal v2 protocol

- add command to request a message
- add gimbal attitude message

mavlink_receiver handle GIMBAL_MANAGER_SET_ATTITUDE

first implementation of new vmount input MavlinkGimbalV2
- setup class
- decode gimbal_manager_set_attitude in ControlData

add gimbal information message

add gimbal manager information and vehicle command ack

mavlink messages: add stream for GIMBAL_MANAGER_INFORMATION

mavlink_receiver: handle GIMBAL_DEVICE_INFORMATION

remove mavlink cmd handling from vmount input MavlinkGimbalV2

complete gimbal manager:
- send out fake gimbal_device_information for dummy gimbals
- complete ROI handling with nudging

small fixes

fix typos

cleanup
- gimbal device information
- flags lock
- check sanity of string

add support for CMD_DO_GIMBAL_MANAGER_ATTITUDE

stream GimbalDeviceAttitudeStatus for dummy gimbals
- add uROB gimbal_attitude_status
- fill status in vmount output_rc for dummy gimbals not able to send the
status themselves
- stream mavlink GimbalDeviceAttitudeStatus

better handle the request for gimbal infomation request

clean up

bring gimbal information back on vmount init

add new gimbal message to mavlink normal stream

fix publication of gimbal device information

rename gimbal_attitude_status to gimbal_device_attitude_status

stream gimbal_manager_status at 5Hz

mavlink: send information only on request

Sending the information message once on request should now work and we
don't need to keep publishing it.

mavlink: debug output for now

make sure to copy over control data

mavlink: add missing copyright header, pragma once

mavlink: address review comments

mavlink: handle stream not updated

Our answer does not just depend on whether the stream was found but
whether we actually were able to send out an update.

mavlink: remove outdated comment

vmount: add option for yaw stabilization only

The stabilize flag is used for gimbals which do not have an internal IMU
and need the autopilot's attitude in order to do stabilization. These
gimbals are probably quite rare by now but it makes sense to keep the
functionality given it can e.g. be used by simple servo gimbals for
sensors other than highres cameras.

The stabilize flag can also be re-used for gimbals which are capable of
stabilizing pitch and roll but not absolute yaw (e.g. locked to North).
For such gimbals we can now set the param MNT_DO_STAB to 2.

We still support configuring which axes are stabilized by the
MAVLink command DO_MOUNT_CONFIGURE, however, this is generally not
recommended anymore.

vmount: fix incorrect check for bit flag

mavlink_messages: remove debug message

Signed-off-by: Claudio Micheli <claudio@auterion.com>

use device id

remove debug print

gimbal attitude fix mistake

clang tidy fix

split:
- gimbal_attitude -> gimbal_device_set_attitude, gimbal_manager_set_attitude
- gimbal_information -> gimbal_device_informatio, gimbal_manager_information

add gimbal protocol messages to rtps msg ids

support set attitude for gimbal directly speaking mavlink

clean up gimbal urob messages

vmount: address a few small review comments

vmount: split output into v1 and v2 protocol

This way we can continue to support the MAVLink v1 protocol. Also, we
don't send the old vehicle commands when actually using the new v2
protocol.

vmount: config via ctor instead of duplicate param

vmount: use loop to poll all topics

Otherwise we might give up too soon and miss some data, or run too fast
based on commands that have nothing to do with the gimbal.

typhoon_h480: use gimbal v2 protocol, use yaw stab

Let's by default use the v2 protocol with typhoon_h480 and enable yaw
lock mode by stabilizing yaw.
### Antipattern Category

### Keyword
fast
### Note


## Commit #828
### Hash
[17dce18b32a1f0fc3aa144a34ab03078bde1e161](https://github.com/PX4/PX4-Autopilot/commit/17dce18b32a1f0fc3aa144a34ab03078bde1e161)

### Message
mavlink: reduce GIMBAL_MANAGER_STATUS message rate

This was way too fast.
### Antipattern Category

### Keyword
fast
### Note


## Commit #829
### Hash
[6672be040ae51a17546927d25a26127f2ec4c1da](https://github.com/PX4/PX4-Autopilot/commit/6672be040ae51a17546927d25a26127f2ec4c1da)

### Message
mavlink: limit mavlink channels based on memory
### Antipattern Category

### Keyword
memory
### Note


## Commit #830
### Hash
[8747b343d9e62f7234c436b4aa183ffb50e3cb89](https://github.com/PX4/PX4-Autopilot/commit/8747b343d9e62f7234c436b4aa183ffb50e3cb89)

### Message
Non-compliant nodes support

WorkQueueManager:Increase UAVCAN stack size
### Antipattern Category

### Keyword
increase
### Note


## Commit #831
### Hash
[8c2678bca12c7ade5ac0126a6d0738ebdb8998e7](https://github.com/PX4/PX4-Autopilot/commit/8c2678bca12c7ade5ac0126a6d0738ebdb8998e7)

### Message
uavcan_servers:Reworked file naming and use ROM fs as fall back

   Supporting direct down loads from ROMFS with preferece give to the
   files fould on the SD card first. This will allow a user to provide
   an updated uavcan firware on the SD card, and there is no overhead
   of coping files from the ROM FS to the SD card.
### Antipattern Category

### Keyword
overhead
### Note


## Commit #832
### Hash
[93b1a148b7b4df9eebe6ab261d0ce256ca9ee78f](https://github.com/PX4/PX4-Autopilot/commit/93b1a148b7b4df9eebe6ab261d0ce256ca9ee78f)

### Message
batt_smbus: Pass device address to base class

Fixes a warning printed at runtime

Signed-off-by: Alex Mikhalev <alex@corvus-robotics.com>
### Antipattern Category

### Keyword
runtime
### Note


## Commit #833
### Hash
[6bd4dff51fe241c08e46b3442f95f0efd783e1bf](https://github.com/PX4/PX4-Autopilot/commit/6bd4dff51fe241c08e46b3442f95f0efd783e1bf)

### Message
drivers/smbus: Increase max block size to 34

batt_smbus for BQ40Z80 transfers up to 34 bytes (32 byte block + 2 byte
address), but this was overflowing and failing the PEC check.
So increase the buffer size

Signed-off-by: Alex Mikhalev <alex@corvus-robotics.com>
### Antipattern Category

### Keyword
increase
### Note


## Commit #834
### Hash
[382e0cbaecfa7805edab25833902cf2cd6533170](https://github.com/PX4/PX4-Autopilot/commit/382e0cbaecfa7805edab25833902cf2cd6533170)

### Message
px4_work_queue: increase wq:nav_and_controllers stack 1760->1824
### Antipattern Category

### Keyword
increase
### Note


## Commit #835
### Hash
[4a65ad914864b607eb5b2dbb5e29759a74da2e39](https://github.com/PX4/PX4-Autopilot/commit/4a65ad914864b607eb5b2dbb5e29759a74da2e39)

### Message
github actions decrease max ccache size

 - lower compression level to 5 as recommended by ccache manual
### Antipattern Category

### Keyword
decrease
### Note


## Commit #836
### Hash
[e38560b928acac52c178b421e8fec46c4d47ddb7](https://github.com/PX4/PX4-Autopilot/commit/e38560b928acac52c178b421e8fec46c4d47ddb7)

### Message
sensor_calibration: increase threshold for updating calibration offsets or scale

 - this is to minimize needlessly writing negligible parameter changes and triggering unnecessary estimator bias resets
### Antipattern Category

### Keyword
increase
### Note


## Commit #837
### Hash
[1be4163506021f44a5cc36bafd545ccf1a36feba](https://github.com/PX4/PX4-Autopilot/commit/1be4163506021f44a5cc36bafd545ccf1a36feba)

### Message
mc_pos_control_params: increase velocity limits a bit

I hit those on my vehicle
### Antipattern Category

### Keyword
increase
### Note


## Commit #838
### Hash
[836c7c65755ab8f0fd3b0fd42fb06bdb903721b4](https://github.com/PX4/PX4-Autopilot/commit/836c7c65755ab8f0fd3b0fd42fb06bdb903721b4)

### Message
StickAccelerationXY: brake a bit faster

The drag is based on max_acc/max_vel, which means that increasing the
maximum velocity leads to slower braking (at the same starting speed).

Especially a combination of small max_acc (slow responsiveness) with high
max_vel led to an exceedingly high braking distance.
This improves that while still being smooth.
### Antipattern Category

### Keyword
slow
### Note


## Commit #839
### Hash
[dd3c3098f2dde5e64d99cb0c0959ae10970b2cac](https://github.com/PX4/PX4-Autopilot/commit/dd3c3098f2dde5e64d99cb0c0959ae10970b2cac)

### Message
nxp_ucans32k146:Add Can Bootloader build

nxp_ucans32k146:Relocation for Bootloader

nxp_ucans32k146:can_boot enable CAN

nxp_ucans32k146:Save Space use Non Optimize memcpy

nxp_ucans32k146:Increase to 24K

nxp/ucans32k146:Canbootloader LED Driver

nxp_ucans32k146:Can bootloader shut down CAN

nxp_ucans32k146:Use NVMEEPROM for Paramaters

nxp_ucans32k146:Use bootloader AppDescriptor

px4 mtd:Support onchip emulated eeprom
### Antipattern Category

### Keyword
increase
### Note


## Commit #840
### Hash
[70ff6703b7a071216acf1424c42cac3f02b9f093](https://github.com/PX4/PX4-Autopilot/commit/70ff6703b7a071216acf1424c42cac3f02b9f093)

### Message
uavcan_v1: More work on subscribers and reg access

Now running into issues with running out of stack frame memory
For now I'm going to leave the relevant code in so it's at least
readable, but in its current state it will not compile
### Antipattern Category

### Keyword
memory
### Note


## Commit #841
### Hash
[b88e8b6684df34e85232860e4cc32baeb439c36e](https://github.com/PX4/PX4-Autopilot/commit/b88e8b6684df34e85232860e4cc32baeb439c36e)

### Message
uavcan_v1: Increase stack size

Also increases stack frame size limit, which was what the compiler was
throwing an error on.
### Antipattern Category

### Keyword
increase
### Note


## Commit #842
### Hash
[4d9e88141e5f341c331e795cde0cc8c8847dfed2](https://github.com/PX4/PX4-Autopilot/commit/4d9e88141e5f341c331e795cde0cc8c8847dfed2)

### Message
px4_work_queue: increase wq:nav_and_controllers stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #843
### Hash
[1eff1aa83c881f92467d79c9b5c3198cb59bf0a7](https://github.com/PX4/PX4-Autopilot/commit/1eff1aa83c881f92467d79c9b5c3198cb59bf0a7)

### Message
Update submodule sitl_gazebo to latest Sat Mar  6 00:39:04 UTC 2021

    - sitl_gazebo in PX4/Firmware (263b00b65fc89c7fd9383f0364760fceb15ea12a): https://github.com/PX4/PX4-SITL_gazebo/commit/bebb9a95f0b61bf9e4c3de345fab70985c1329b3
    - sitl_gazebo current upstream: https://github.com/PX4/PX4-SITL_gazebo/commit/c7524aa977539d8cc972d9336355bc82e2f2cfa5
    - Changes: https://github.com/PX4/PX4-SITL_gazebo/compare/bebb9a95f0b61bf9e4c3de345fab70985c1329b3...c7524aa977539d8cc972d9336355bc82e2f2cfa5

    c7524aa 2021-02-28 Jaeyoung-Lim - Fix MAVSDK SITL tests
f4d5594 2021-02-28 JaeyoungLim - Increase rover model realtime factor (#715)
### Antipattern Category

### Keyword
increase
### Note


## Commit #844
### Hash
[a991e78e18575cd19f5f4821c2fa47b2a3fe4f29](https://github.com/PX4/PX4-Autopilot/commit/a991e78e18575cd19f5f4821c2fa47b2a3fe4f29)

### Message
parameters: fix runtime default edge case
### Antipattern Category

### Keyword
runtime
### Note


## Commit #845
### Hash
[c356181f9066bc6361825b2ae17212aae01cd55f](https://github.com/PX4/PX4-Autopilot/commit/c356181f9066bc6361825b2ae17212aae01cd55f)

### Message
px4_work_queue: increase wq:rate_ctrl stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #846
### Hash
[3665f9a3c49a16ca0d7019b368bfb544d87f0781](https://github.com/PX4/PX4-Autopilot/commit/3665f9a3c49a16ca0d7019b368bfb544d87f0781)

### Message
gyro_fft: increase default range and length to improve test data
### Antipattern Category

### Keyword
increase
### Note


## Commit #847
### Hash
[00016e53fac8af3dcf7935cd823692f924a951d4](https://github.com/PX4/PX4-Autopilot/commit/00016e53fac8af3dcf7935cd823692f924a951d4)

### Message
boards: holybro/kakutef7 disable CONSTRAINED_FLASH to increase optimization
### Antipattern Category

### Keyword
increase
### Note


## Commit #848
### Hash
[2c5342acd4e77f7aa74f9a3dffd4f482339f8f92](https://github.com/PX4/PX4-Autopilot/commit/2c5342acd4e77f7aa74f9a3dffd4f482339f8f92)

### Message
commander: increase nav_test_failed hysteresis time

This is to avoid race condition with the yaw emergency estimator having
the same trigger delay of 1 second. Commander will now give more time to
EKF2 to reset itself before switching to altitude mode.
### Antipattern Category

### Keyword
increase
### Note


## Commit #849
### Hash
[6874e9fba03bbec52da09f134563f644f9299ca8](https://github.com/PX4/PX4-Autopilot/commit/6874e9fba03bbec52da09f134563f644f9299ca8)

### Message
boards: NuttX disable all NSH memory debug commands (mb, mh, mw) by default

 - closes https://github.com/PX4/PX4-Autopilot/issues/17062
### Antipattern Category

### Keyword
memory
### Note


## Commit #850
### Hash
[9171a843245e55a6deea74c62c111107bfc8a0ee](https://github.com/PX4/PX4-Autopilot/commit/9171a843245e55a6deea74c62c111107bfc8a0ee)

### Message
IMU_DGYRO_CUTOFF increase default 10 -> 20 Hz
### Antipattern Category

### Keyword
increase
### Note


## Commit #851
### Hash
[1ec8ce58c7e544e96cbda711d85c7f3b21731b9b](https://github.com/PX4/PX4-Autopilot/commit/1ec8ce58c7e544e96cbda711d85c7f3b21731b9b)

### Message
Commander: Increase auto-disarm timeout to 25 seconds after arming
### Antipattern Category

### Keyword
increase
### Note


## Commit #852
### Hash
[1e88939605c99ebb056bb4e473ac076ef1d4aca7](https://github.com/PX4/PX4-Autopilot/commit/1e88939605c99ebb056bb4e473ac076ef1d4aca7)

### Message
mavsdk_tests: report speed factor every second

This helps in debugging slow CI.
### Antipattern Category

### Keyword
slow
### Note


## Commit #853
### Hash
[31b9efdaebe76937cf7ecda95014946ed98fcdc8](https://github.com/PX4/PX4-Autopilot/commit/31b9efdaebe76937cf7ecda95014946ed98fcdc8)

### Message
sensors/vehicle_imu: increase threshold for clipping warning
### Antipattern Category

### Keyword
increase
### Note


## Commit #854
### Hash
[f9d8c613b048f58eb3110e9af13cb3a89c4c866f](https://github.com/PX4/PX4-Autopilot/commit/f9d8c613b048f58eb3110e9af13cb3a89c4c866f)

### Message
px4_work_queue: increase nav_and_controllers stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #855
### Hash
[59b70a881d5d5eed93ebe97889a1ae7886a9520a](https://github.com/PX4/PX4-Autopilot/commit/59b70a881d5d5eed93ebe97889a1ae7886a9520a)

### Message
commander: temporarily increase worker thread stack substantially
### Antipattern Category

### Keyword
increase
### Note


## Commit #856
### Hash
[32d354e5fef79fc19ad6c1e135712e22056049ca](https://github.com/PX4/PX4-Autopilot/commit/32d354e5fef79fc19ad6c1e135712e22056049ca)

### Message
Update submodule ecl to latest Sun May  2 12:39:08 UTC 2021

    - ecl in PX4/Firmware (cb999f37d4891ebfbbc21b4ce9b3851888b39ad4): https://github.com/PX4/PX4-ECL/commit/5d34d7a24ef72b826c320a3259ee0ec68b1936df
    - ecl current upstream: https://github.com/PX4/PX4-ECL/commit/a7b8afe420f438554ad90bcba0f1f4872325e75b
    - Changes: https://github.com/PX4/PX4-ECL/compare/5d34d7a24ef72b826c320a3259ee0ec68b1936df...a7b8afe420f438554ad90bcba0f1f4872325e75b

    a7b8afe 2021-04-30 Eike - Allow rangefinder fusion in vision height mode (Fix for #994) (#999)
4ac57d3 2021-04-25 Daniel Agar - EKF: increase fault flags value size to fit current flag bits (> 16)
### Antipattern Category

### Keyword
increase
### Note


## Commit #857
### Hash
[c28533677dbcbdc772524c3126921a6d322dd29b](https://github.com/PX4/PX4-Autopilot/commit/c28533677dbcbdc772524c3126921a6d322dd29b)

### Message
MulticopterLandDetector: use setpoint generation to infer decend intent

For any normal use case where a downwards velocity setpoint is set
this works exactly the same as before.
E.g. autonomous landing, landing in Altitude or Position mode

The advantage is that the very common case where a vehicle tries
to hold a constant altitude but fails to do so e.g. during a hard brake
with too much lift the resulting downwards velocity was interpreted
as descend intent and since the vehicle already struggled to hold altitude
with low thrust and was not moving fast anymore because it was braking
this lead to a lot more false positives on certain vehicle types.

The disadvantage is that not setting a downwards velocity setpoint but
just moving the position setpoint into the ground does not result in
land detection anymore. We do not use this method of landing anymore for
quite a while. It's not recommended and I wonder if there's some rare use
case like offboard where this is done.

We could add an additional case for the specific case to land with a
position setpoint only.
### Antipattern Category

### Keyword
fast
### Note


## Commit #858
### Hash
[3b7ce61901f6ec01439b10aae7fab75eb3719a74](https://github.com/PX4/PX4-Autopilot/commit/3b7ce61901f6ec01439b10aae7fab75eb3719a74)

### Message
px4_work_queue: increase wq:rate_ctrl stack slightly
### Antipattern Category

### Keyword
increase
### Note


## Commit #859
### Hash
[e265ebabc59575c1bd217f24b2d64a955aad1715](https://github.com/PX4/PX4-Autopilot/commit/e265ebabc59575c1bd217f24b2d64a955aad1715)

### Message
Update submodule ecl to latest Thu May  6 12:39:12 UTC 2021

    - ecl in PX4/Firmware (a300d32523e24df3f366a0d564b764261e1c1909): https://github.com/PX4/PX4-ECL/commit/a7b8afe420f438554ad90bcba0f1f4872325e75b
    - ecl current upstream: https://github.com/PX4/PX4-ECL/commit/29243ac5cbb5d27ac71744e88afcd786df6f748d
    - Changes: https://github.com/PX4/PX4-ECL/compare/a7b8afe420f438554ad90bcba0f1f4872325e75b...29243ac5cbb5d27ac71744e88afcd786df6f748d

    29243ac 2021-05-05 bresch - yaw_reset: reduce minimum vector length to compute yaw error
aad4840 2021-05-02 Kabir Mohammed - EKF: increase allowed difference between flow and gyro ODRs
### Antipattern Category

### Keyword
increase
### Note


## Commit #860
### Hash
[f15eefcc9503d2abe0713defe7f017519e337b0b](https://github.com/PX4/PX4-Autopilot/commit/f15eefcc9503d2abe0713defe7f017519e337b0b)

### Message
ekf2: selector increase status rate before potential instance change
### Antipattern Category

### Keyword
increase
### Note


## Commit #861
### Hash
[904f827df0e7b8c67b00635e4ecbf0433a9297a8](https://github.com/PX4/PX4-Autopilot/commit/904f827df0e7b8c67b00635e4ecbf0433a9297a8)

### Message
Jenkins: increase timeout and build history
### Antipattern Category

### Keyword
increase
### Note


## Commit #862
### Hash
[87b861d0f08a8ad036a1000a890ba6f56695b04c](https://github.com/PX4/PX4-Autopilot/commit/87b861d0f08a8ad036a1000a890ba6f56695b04c)

### Message
IMU_GYRO_CUTOFF and IMU_DGYRO_CUTOFF increase default slightly
### Antipattern Category

### Keyword
increase
### Note


## Commit #863
### Hash
[820a442fe3654353d5613efca1fcf4bcd0d23c10](https://github.com/PX4/PX4-Autopilot/commit/820a442fe3654353d5613efca1fcf4bcd0d23c10)

### Message
drivers/imu/analog_devices/adis16448: minor fixes and compatibility with older model

 - increase SPI stall time slightly

 - tolerate mag self test failure (could be due to local magnetic field)

 - register configuration compatible with older ADIS16448AMLZ

 - don't publish duplicate accel/gyro

 - only allocate CRC perf counter if using CRC
### Antipattern Category

### Keyword
increase
### Note


## Commit #864
### Hash
[3269ee8df13cfff055b272fb5b31bd57df7f1d1c](https://github.com/PX4/PX4-Autopilot/commit/3269ee8df13cfff055b272fb5b31bd57df7f1d1c)

### Message
sensors/vehicle_angular_velocity: accumualted notch filtering and reset improvements

 - apply sensor scaling immediately to keep things simple (FIFO vs regular)
 - inline filter helpers (minor performance improvement)
 - dynamic notch filtering
    - reorder by axis (applied per axis)
    - don't remove notch filters immediately if ESC or FFT data times out
    - constrain notch filter frequency and bandwidth to safe range (minimum bandwidth for flaot precision, Nyquist, etc)
 - add safe constraint on dt
### Antipattern Category

### Keyword
performance
### Note


## Commit #865
### Hash
[806b46293537f3e63279b24c841553ad36051e3a](https://github.com/PX4/PX4-Autopilot/commit/806b46293537f3e63279b24c841553ad36051e3a)

### Message
px4_work_queue: increase UART stack
### Antipattern Category

### Keyword
increase
### Note


## Commit #866
### Hash
[00229c4fd240f08e2b07ffb975249776cb217298](https://github.com/PX4/PX4-Autopilot/commit/00229c4fd240f08e2b07ffb975249776cb217298)

### Message
drv_pwm_output.h: increase highest max pwm limit from 2150 to 2500

 - servo linkages in vtol often need further travel of the servos to cover the full tilt travel
### Antipattern Category

### Keyword
increase
### Note



