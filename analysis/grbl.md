## Commit #1
### Hash
[b8ba8a4231676eb1bec9b73dd5862f18188c2977](https://github.com/gnea/grbl/commit/b8ba8a4231676eb1bec9b73dd5862f18188c2977)

### Message
Added runtime configurable global settings with eeprom persitence
### Antipattern Category
X
### Keyword
runtime
### Note
This commit does not change any performance-related features. More configurations for terminal.

## Commit #2
### Hash
[e409f10047fb8e3d2265513abb2d8144b00d9b78](https://github.com/gnea/grbl/commit/e409f10047fb8e3d2265513abb2d8144b00d9b78)

### Message
moved all strings to pgm-memory
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Strings moved to pgm-memory, reason not specified.

## Commit #3
### Hash
[937c70cb50e0eb0c91f5f1c7ed2d3c470cb30962](https://github.com/gnea/grbl/commit/937c70cb50e0eb0c91f5f1c7ed2d3c470cb30962)

### Message
Grbl can now take advantage of the extra memory in the 328
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
memory
### Note
Bunch of variables regarding memory buffer changed, also sleep 1 sec instead of 5.

## Commit #4
### Hash
[ef61efbf704af5ca736e87905155fefedea8be83](https://github.com/gnea/grbl/commit/ef61efbf704af5ca736e87905155fefedea8be83)

### Message
makes sure steppers cruise at exactly nominal rate to eliminate rounding errors. Possibly fixes the problem where some moves have a long tail of slow steps. (Untested)
### Antipattern Category
New:rounded_numbers
### Keyword
slow
### Note
Rounding errors possible cause for the problem where some moves have a long tail of slow steps.

## Commit #5
### Hash
[c02a6e23664511b01f0d7859c4432c79a3050feb](https://github.com/gnea/grbl/commit/c02a6e23664511b01f0d7859c4432c79a3050feb)

### Message
possible improvement on the long, slow tail problem
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features, ceil() function replaced with floor().

## Commit #6
### Hash
[1ed2195e11c4aae1797b49fae2ed8c7883d5b3ed](https://github.com/gnea/grbl/commit/1ed2195e11c4aae1797b49fae2ed8c7883d5b3ed)

### Message
a new (slightly inelegant) stab at eliminating the slow tail problem
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features.

## Commit #7
### Hash
[ea5b8942db2616e93fc0478922010c3bab7c0481](https://github.com/gnea/grbl/commit/ea5b8942db2616e93fc0478922010c3bab7c0481)

### Message
Moved comment and block delete handling to be done in protocol.c rather than gcode.c. Prevents these from being held in memory. Also, fixes bug when comments and block delete character are mixed with g-code.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. New commit throws away characters that are after the last position in buffer.


## Commit #8
### Hash
[a2837943c014590704e57bca8597b9d8654f1b17](https://github.com/gnea/grbl/commit/a2837943c014590704e57bca8597b9d8654f1b17)

### Message
Revert "Moved comment and block delete handling to be done in protocol.c rather than gcode.c. Prevents these from being held in memory. Also, fixes bug when comments and block delete character are mixed with g-code."

This reverts commit ea5b8942db2616e93fc0478922010c3bab7c0481.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Revert of previous commit.

## Commit #9
### Hash
[896a6b9199395eb9dbfd42134d84ba40a332eb36](https://github.com/gnea/grbl/commit/896a6b9199395eb9dbfd42134d84ba40a332eb36)

### Message
Moved comment and block delete handling into protocol.c from gcode.c. Fixes bug when comment and block delete are not isolated. Blank lines ignored.

Comments, block delete characters, and blank lines are no longer passed
to the gcode parser and should free up some memory by ignoring these
characters. Gcode parser now expects clean gcode only. There was a bug
if there were block deletes or comments not in the first character (i.e.
spindle on/off for proofing geode without turning it on, or a NXX
followed by a comment). This should fix it by bypassing the problem.
Left a commented line for easily turning on and off block deletes for a
later feature, if desired.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. New commit throws away characters that are after the last position in buffer.

## Commit #10
### Hash
[badb638df925924c05b3b5e49880590e53faa759](https://github.com/gnea/grbl/commit/badb638df925924c05b3b5e49880590e53faa759)

### Message
Moved comment and block delete handling into protocol.c from gcode.c. Fixes bug when comment and block delete are not isolated. Blank lines ignored.

Comments, block delete characters, and blank lines are no longer passed
to the gcode parser and should free up some memory by ignoring these
characters. Gcode parser now expects clean gcode only. There was a bug
if there were block deletes or comments not in the first character (i.e.
spindle on/off for proofing geode without turning it on, or a NXX
followed by a comment). This should fix it by bypassing the problem.
Left a commented line for easily turning on and off block deletes for a
later feature, if desired.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. New commit throws away characters that are after the last position in buffer.

## Commit #11
### Hash
[d75ad82e4932aea166c189e4160e197e4710c191](https://github.com/gnea/grbl/commit/d75ad82e4932aea166c189e4160e197e4710c191)

### Message
Minor update for memory savings in ring buffer and fleshed out commenting.

No changes in functionality. Path vectors moved from ring buffer to
local planner static variables to save 3*(BUFFER_SIZE - 1) doubles in
memory. Detailed comments. Really need to stop micro-updating. Should be
the last until a planner optimization (ala Jens Geisler) has been
completed.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Updates mostly in comments.

## Commit #12
### Hash
[ffcc3470a31411b63aa57d12cc58cc306a1fb660](https://github.com/gnea/grbl/commit/ffcc3470a31411b63aa57d12cc58cc306a1fb660)

### Message
Optimized planner re-write. Significantly faster. Full arc support enabled by rotation matrix approach.

- Significant improvements in the planner. Removed or reordered
repetitive and expensive calculations by order of importance:
recalculating unchanged blocks, trig functions [sin(), cos(), tan()],
sqrt(), divides, and multiplications. Blocks long enough for nominal
speed to be guaranteed to be reached ignored by planner. Done by
introducing two uint8_t flags per block. Reduced computational overhead
by an order of magnitude.   - Arc motion generation completely
re-written and optimized. Now runs with acceleration planner. Removed
all but one trig function (atan2) from initialization. Streamlined
computations. Segment target locations generated by vector
transformation and small angle approximation. Arc path correction
implemented for accumulated error of approximation and single precision
calculation of Arduino. Bug fix in message passing.
### Antipattern Category
Smith:General:Unnecessary_Processing
### Keyword
faster
### Note
Computational overhead reduced by simplifying expensive mathematical operations and not recalculating unchanged blocks.

## Commit #13
### Hash
[4d03c4febc94eaaaa6906a70c99ebb7c7e4947b1](https://github.com/gnea/grbl/commit/4d03c4febc94eaaaa6906a70c99ebb7c7e4947b1)

### Message
Further planner improvements and misc minor bug fixes. Memory savings and increased buffer size.

- Update grbl version and settings version to automatically reset
eeprom. FYI, this will reset your grbl settings. - Saved
3*BLOCK_BUFFER_SIZE doubles in static memory by removing obsolete
variables: speed_x, speed_y, and speed_z. - Increased buffer size
conservatively to 18 from 16. (Probably can do 20). - Removed expensive!
modulo operator from block indexing function. Reduces significant
computational overhead. - Re-organized some sqrt() calls to be more
efficient during time critical planning cases, rather than non-time
critical. - Minor bug fix in planner max junction velocity logic. -
Simplified arc logic and removed need to multiply for CW or CCW
direction.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Some calculations simplified and sqrt() calls cut out, fewer variables used.

## Commit #14
### Hash
[110faae986eef6c4398c166a81c91cbd1d5a3bf4](https://github.com/gnea/grbl/commit/110faae986eef6c4398c166a81c91cbd1d5a3bf4)

### Message
More '%' modulo opertor removals and some housecleaning.

- Serial functions contained quite a few modulo operations that would
be executed with high frequency when streaming. AVR processors are very
slow when operating these. In one test on the Arduino forums, it showed
about a 15x slow down compared to a simple if-then statement. -
Clarified some variable names and types and comments.
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features. Variables renamed and a % operation removed.

## Commit #15
### Hash
[e8a6bfd179a594fd8237f5f9720bb337f758760c](https://github.com/gnea/grbl/commit/e8a6bfd179a594fd8237f5f9720bb337f758760c)

### Message
Position reporting, refactored system variables, serial print fixes, updated streaming scripts.

- Added machine position reporting to status queries. This will be
further developed with part positioning/offsets and maintaining
location upon reset.

- System variables refactored into a global struct for better
readability.

- Removed old obsolete Ruby streaming scripts. These were no longer
compatible. Updated Python streaming scripts.

- Fixed printFloat() and other printing functions.

- Decreased planner buffer back to 18 blocks and increased TX serial
buffer to 64 bytes. Need the memory space for future developments.

- Begun adding run-time modes to grbl, where block delete toggle, mm/in
reporting modes, jog modes, etc can be set during runtime. Will be
fleshed out and placed into EEPROM when everything is added.
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
memory
### Note
BLOCK_BUFFER_SIZE param decreased from 20 to 18.
STEPPER_IDLE_LOCK_TIME defined to 25 ms.

## Commit #16
### Hash
[79e0fd594b4481fc74eac9c6669fef1a994c6b48](https://github.com/gnea/grbl/commit/79e0fd594b4481fc74eac9c6669fef1a994c6b48)

### Message
Added step pulse delay after direction set (Compile-time option only). Updated read me.

Added a compile-time only experimental feature that creates a
user-specified time delay between a step pulse and a direction pin set
(in config.h). This is for users with hardware-specific issues
(opto-couplers) that need more than a few microseconds between events,
which can lead to slowly progressing step drift after many many
direction changes. We suggest to try the hack/fix posted in the Wiki
before using this, as this experimental feature may cause Grbl to take
a performance hit at high step rates and about complex curves.
### Antipattern Category
New:Hard-coded-timing
### Keyword
performance
### Note
STEPPER_IDLE_LOCK_TIME defined to 25 ms.

## Commit #17
### Hash
[d30cb906f886e71987ce986effbd1c9368aca479](https://github.com/gnea/grbl/commit/d30cb906f886e71987ce986effbd1c9368aca479)

### Message
Updated limit/homing routine. Works, but needs more TLC.

- Added acceleration to the homing routine.

- Homing now accounts for different step rates when moving multiple
axes without exceeding acceleration limits.

- Homing now updates all internal positioning variables to machine zero
after completion.

- "Poor-man's" debounce delay added.

- Updated the delay_us() function to perform faster and more accurate
microsecond delays. Previously, the single increments would add
noticeable time drift for larger delays.

- Fix a bug in the stepper.c prescalar calculations that was changed in
the last commit.

- Other minor fixes.
### Antipattern Category
New:Hard-coded-timing
### Keyword
faster
### Note
Homing cycle delay was changed from the hard coded value of 500000 to settings.default_feed_rate.

## Commit #18
### Hash
[9b4e1089058411b2b2889cdbc45a0c2a737b6320](https://github.com/gnea/grbl/commit/9b4e1089058411b2b2889cdbc45a0c2a737b6320)

### Message
(2x) speed increase in printFloat() function. Decimal places setting added.

- printFloat() function execution doubled in speed. This is a precursor
to status reporting, since GUIs may query real-time position rapidly.

- Decimal places added to settings (for now). This may disappear in
future pushes, but here for testing purposes.
### Antipattern Category
X
### Keyword
increase
### Note
The improvement comes from parsing the number of decimals with a factor of 2 instead of 1 and printing a char[] instead of each decimal. Doesn't fall under any performance related anti-pattern.

## Commit #19
### Hash
[34f6d2eb4b3e25aec008889451e6fd4276ee055b](https://github.com/gnea/grbl/commit/34f6d2eb4b3e25aec008889451e6fd4276ee055b)

### Message
Minor updates, improvements, and bug fixes.

- Allowed status_message function to be called by others. This is to
centralize all feedback into protocol.c.

- Fixed a bug where line number words 'N' were causing the parser to
error out.

- Allowed homing routine feed rates to move slower than the
MINIMUM_STEP_RATE parameter in config.h.

- Homing performs idle lock at the end of the routine.

- Stepper idle lock time will now not disable the steppers when the
value is set at 255. This is accomodate users who prefer to keep their
axes enabled at all times.

- Moved some defines around to where they need to be.
### Antipattern Category
X
### Keyword
slower
### Note
This commit does not change any performance-related features. Some limits added and a bug fix.

## Commit #20
### Hash
[df5bb70b2515b8bc05ca7c90abf1b221f63aeafe](https://github.com/gnea/grbl/commit/df5bb70b2515b8bc05ca7c90abf1b221f63aeafe)

### Message
Hard limits, homing direction, pull-off limits after homing, status reports in mm or inches, system alarm, and more.

- Thank you statement added for Alden Hart of Synthetos.

- Hard limits option added, which also works with homing by pulling off
the switches to help prevent unintended triggering. Hard limits use a
interrupt to sense a falling edge pin change and immediately go into
alarm mode, which stops everything and forces the user to issue a reset
(Ctrl-x) or reboot.

- Auto cycle start now a configuration option.

- Alarm mode: A new method to kill all Grbl processes in the event of
something catastrophic or potentially catastropic. Just works with hard
limits for now, but will be expanded to include g-code errors (most
likely) and other events.

- Updated status reports to be configurable in inches or mm mode. Much
more to do here, but this is the first step.

- New settings: auto cycle start, hard limit enable, homing direction
mask (which works the same as the stepper mask), homing pulloff
distance (or distance traveled from homed machine zero to prevent
accidental limit trip).

- Minor memory liberation and calculation speed ups.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Some configurable options added, log printing changed and force kill for all processes added.

## Commit #21
### Hash
[e0a9054e32f6e00cf6931552b11b9f201e240bf0](https://github.com/gnea/grbl/commit/e0a9054e32f6e00cf6931552b11b9f201e240bf0)

### Message
New report module. 6 persistent work coordinates. New G-codes and settings. README and minor bug updates

(NOTE: This push is likely buggy so proceed with caution. Just
uploading to let people know where we're going.)

- New report.c module. Moved all feedback functions into this module to
centralize these processes. Includes realtime status reports, status
messages, feedback messages.

- Official support 6 work coordinate systems (G54-G59), which are
persistently held in EEPROM memory.

- New g-code support: G28.1, G30.1 stores current machine position as a
home position into EEPROM. G10 L20 Px stores current machine position
into work coordinates without needing to explicitly send XYZ words.

- Homing performed with '$H' command. G28/G30 no longer start the
homing cycle. This is how it's supposed to be.

- New settings: Stepper enable invert and n_arc correction installed.

- Updated and changed up some limits and homing functionality. Pull-off
travel will now move after the homing cycle regardless of hard limits
enabled. Fixed direction of pull-off travel (went wrong way).

- Started on designing an internal Grbl command protocol based on the
'$' settings letter. Commands with non numeric characters after '$'
will perform switch commands, homing cycle, jogging, printing
paramters, etc. Much more to do here.

- Updated README to reflect all of the new features.
### Antipattern Category
X
### Keyword
memory
### Note
Bug fixes, this commit does not change any performance-related features.

## Commit #22
### Hash
[303cf59f5246b46d0775b31290c04b5712ff4b2c](https://github.com/gnea/grbl/commit/303cf59f5246b46d0775b31290c04b5712ff4b2c)

### Message
Added block delete, opt stop, single block mode. New parser state and parameter feedback. Overhauled '$' command.

NOTE: Another incremental update. Likely buggy, still a ways to go
before everything is installed, such as startup blocks.

- Changed the '$' command to print help. '$$' now prints Grbl settings.
The help now instructs the user of runtime commands, switch toggling,
homing, etc. Jogging will be added to these in v0.9.

- Added switches: block delete, opt stop, and single block mode.

- Now can print the g-code parser state and persistent parameters
(coord sys) to view what Grbl has internally.

- Made the gc struct in the g-code parser global to be able to print
the states. Also moved coordinate system tracking from sys to gc struct.

- Changed up the welcome flag and updated version to v0.8c.

- Removed spindle speed from gcode parser. Not used.
### Antipattern Category
X
### Keyword
runtime
### Note
This commit does not change any performance-related features. Change in '$' and '$' functionality. Somecode moved around.

## Commit #23
### Hash
[4c711a4af7a21b1005bd2ac59a423b021ae831fb](https://github.com/gnea/grbl/commit/4c711a4af7a21b1005bd2ac59a423b021ae831fb)

### Message
New startup script setting. New dry run, check gcode switches. New system state variable. Lots of reorganizing.

(All v0.8 features installed. Still likely buggy, but now thourough
testing will need to start to squash them all. As soon as we're done,
this will be pushed to master and v0.9 development will be started.
Please report ANY issues to us so we can get this rolled out ASAP.)

- User startup script! A user can now save one (up to 5 as compile-time
option) block of g-code in EEPROM memory. This will be run everytime
Grbl resets. Mainly to be used as a way to set your preferences, like
G21, G54, etc.

- New dry run and check g-code switches. Dry run moves ALL motions at
rapids rate ignoring spindle, coolant, and dwell commands. For rapid
physical proofing of your code. The check g-code switch ignores all
motion and provides the user a way to check if there are any errors in
their program that Grbl may not like.

- Program restart! (sort of). Program restart is typically an advanced
feature that allows users to restart a program mid-stream. The check
g-code switch can perform this feature by enabling the switch at the
start of the program, and disabling it at the desired point with some
minimal changes.

- New system state variable. This state variable tracks all of the
different state processes that Grbl performs, i.e. cycle start, feed
hold, homing, etc. This is mainly for making managing of these task
easier and more clear.

- Position lost state variable. Only when homing is enabled, Grbl will
refuse to move until homing is completed and position is known. This is
mainly for safety. Otherwise, it will let users fend for themselves.

- Moved the default settings defines into config.h. The plan is to
eventually create a set of config.h's for particular as-built machines
to help users from doing it themselves.

- Moved around misc defines into .h files. And lots of other little
things.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Prints changed, some if and switch cases added.

## Commit #24
### Hash
[9cabc915ef9096b470e236679db70834f6fc9e7a](https://github.com/gnea/grbl/commit/9cabc915ef9096b470e236679db70834f6fc9e7a)

### Message
Runtime command pinned out! Re-organized coolant pins.

- Pinned out cycle start(A2), feed hold(A1), and reset(A0) runtime
commands. These pins are held high with the internal pull-up resistor
enabled. All you have to do is connect a normally-open switch to the
pin and ground. That's it.

- Moved the coolant control pins to A3 (and the optional mist control
to A4).

- Moved all of the MASK defines into the config.h file to centralize
them.
### Antipattern Category
X
### Keyword
runtime
### Note
This commit does not change any performance-related features. Some changes in PINs configuration.

## Commit #25
### Hash
[f41dd6927378c7a2600b2b177aadd59a2fc83ad3](https://github.com/gnea/grbl/commit/f41dd6927378c7a2600b2b177aadd59a2fc83ad3)

### Message
Tweaks and bug fixes. Increase to 3 startup blocks. Remove purge/added unlock command

- Increased the number of startup blocks to 3 for no good reason other
than it doesn't increase the flash size.

- Removed the purge buffer command and replaced with an disable homing
lock command.

- Homing now blocks all g-code commands (not system commands) until the
homing cycle has been performed or the disable homing lock is sent.
Homing is required upon startup or if Grbl loses it position. This is
for safety reasons.

- Cleaned up some of the Grbl states and re-organized it to be little
more cohesive.

- Cleaned up the feedback and status messages to not use so much flash
space, as it's a premium now.

 - Check g-code and dry run switches how are mutually exclusive and
can't be enabled when the other is. And automatically resets Grbl when
disabled.

- Some bug fixes and other minor tweaks.
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features.

## Commit #26
### Hash
[3082fdbb6d7e24527915ebc16d5dcf545bc2929c](https://github.com/gnea/grbl/commit/3082fdbb6d7e24527915ebc16d5dcf545bc2929c)

### Message
Planner execution time halved and bug fixes. Increased step rate limit to 30kHz.

- Planner execute speed has been more than halved from 4ms to 1.9ms
when computing a plan for a single line segment during arc generation.
This means that Grbl can now run through an arc (or complex curve)
twice as fast as before without starving the buffer. For 0.1mm arc
segments, this means about the theoretical feed rate limit is about
3000mm/min for arcs now.

- Increased the Ranade timer frequency to 30kHz, as there doesn't seem
to be any problems with increasing the frequency. This means that the
maximum step frequency is now back at 30kHz.

- Added Zen Toolworks 7x7 defaults.
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
fast
### Note
Frequency increased from 20Hz to 30Hz.

## Commit #27
### Hash
[4f273db8058f6c8a83fc9b7dac2ee0542b80dfd6](https://github.com/gnea/grbl/commit/4f273db8058f6c8a83fc9b7dac2ee0542b80dfd6)

### Message
(Another) Planner bug fix.

- Oops again. Thought the new planner changes made things much better,
but there was a bug. Improvements we on the order of 20% execution time
reduction, rather than half. The increase to 30kHz Ranade timer
frequency also increased the overall overhead, so the total planner
change? Zero. But, it's still better.
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features.

## Commit #28
### Hash
[a1397f61c4862f95f85f12e5facc103b0d836f54](https://github.com/gnea/grbl/commit/a1397f61c4862f95f85f12e5facc103b0d836f54)

### Message
Max velocity axes independence installed. Fixed intermittent slow trailing steps. Timer0 disable fix.

- Maximum velocity for each axis is now configurable in settings. All
rapids/seek move at these maximums. All feed rates(including rapids)
may be limited and scaled down so that no axis does not exceed their
limits.

- Moved around auto-cycle start. May change later, but mainly to ensure
the planner buffer is completely full before cycle starting a streaming
program. Otherwise it should auto-start when there is a break in the
serial stream.

- Reverted old block->max_entry_speed_sqr calculations. Feedrate
overrides not close to ready at all.

- Fixed intermittent slow trailing steps for some triangle velocity
profile moves. The acceleration tick counter updating was corrected to
be exact for that particular transition. Should be ok for normal
trapezoidal profiles.

- Fixed the Timer0 disable after a step pulse falling edge. Thanks
@blinkenlight!
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
slow
### Note
Frequency decreased from 30Hz to 20Hz.

## Commit #29
### Hash
[c8b53b9d0a341e978d6faa02359e409159f4a388](https://github.com/gnea/grbl/commit/c8b53b9d0a341e978d6faa02359e409159f4a388)

### Message
Slow trailing steps fix. Added more defaults.

- Fixed an issue (hopefully) with slow trailing steps after a
triangular velocity profile move. Sets the trapezoid tick cycle counter
to the correct value for an accurate reproduction of the deceleration
curve. Keeps it from arriving too early to the target position, which
causes the slow trailing steps.

- Added Zen Toolworks 7x7 to default settings.

- Updated readme with new edge build.
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features.

## Commit #30
### Hash
[3dfffa622d53e7727600249123ddc0c7db4f8954](https://github.com/gnea/grbl/commit/3dfffa622d53e7727600249123ddc0c7db4f8954)

### Message
Arc mm_per_segment removed, now in terms of tolerance. Stepper ramp counter variable type corrected.

- Arc mm_per_segment parameter was removed and replaced with an
arc_tolerance parameter, which scales all arc segments automatically to
radius, such that the line segment error doesn't exceed the tolerance.
Significantly improves arc performance through larger radius arc,
because the segments are much longer and the planner buffer has more to
work with.

- Moved n_arc correction from the settings to config.h. Mathematically
this doesn't need to be a setting anymore, as the default config value
will work for all known CNC applications. The error does not accumulate
as much anymore, since the small angle approximation used by the arc
generation has been updated to a third-order approximation and how the
line segment length scale with radius and tolerance now. Left in
config.h for extraneous circumstances.

- Corrected the st.ramp_count variable (acceleration tick counter) to a
8-bit vs. 32-bit variable. Should make the stepper algorithm just a
touch faster overall.
### Antipattern Category
X
### Keyword
performance
### Note
This commit does not change any performance-related features.

## Commit #31
### Hash
[5e7c25d4801d79a84e45b42da24b5f5f0db56426](https://github.com/gnea/grbl/commit/5e7c25d4801d79a84e45b42da24b5f5f0db56426)

### Message
Updated README. Max step rate back at 30kHz. Acceleration minor bug fix.

- Returned the max step rate to 30kHz. The new arc algorithm works uses
so much less CPU overhead, because the segments are longer, that the
planner has no problem computing through them.

- Fixed an issue with the acceleration independence scaling. Should now
work with accelerations above 400mm/sec^2 or so.

- Updated README
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
overhead
### Note
Frequency increased from 20Hz to 30Hz.

## Commit #32
### Hash
[3c9c516a4770b3a7d7d63b4d51cbb5b28c1131fd](https://github.com/gnea/grbl/commit/3c9c516a4770b3a7d7d63b4d51cbb5b28c1131fd)

### Message
Untested! Soft limits, max travel, homing changes, new settings.

- WARNING: Completely untested. Will later when there is time. Settings
WILL be overwritten, as there are new settings.

- Soft limits installed. Homing must be enabled for soft limits to work
correctly. Errors out much like a hard limit, locking out everything
and bringing up the alarm mode. Only difference is it forces a feed
hold before doing so. Position is not lost.

- IMPORTANT: Homing had to be updated so that soft limits work better
with less CPU overhead. When homing completes, all axes are assumed to
exist in negative space. If your limit switch is other side, the homing
cycle with set this axis location to the max travel value, rather than
zero.

- Update mc_line() to accept an array, rather than individual variables.

- Added an mc_auto_cycle_start() function handle this feature.
Organization only.

-
### Antipattern Category
X
### Keyword
overhead
### Note
This commit does not change any performance-related features. Some limits added, switch cases and prints changed.

## Commit #33
### Hash
[1fa3dad20617b4673765d7846208807345aa82cd](https://github.com/gnea/grbl/commit/1fa3dad20617b4673765d7846208807345aa82cd)

### Message
Updates to edge/dev. Line buffer increased/planner buffer decreased. Line overflow feedback.

- Increased g-code parser line buffer to 70 characters (from 50) to
prevent some long arc commands from getting truncated.

- Decreased planner buffer from 18 to 17 blocks to free up memory for
line buffer.

- Added a line buffer overflow feedback error (Thanks @BHSPitMonkey!)
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
memory
### Note
G-code parser buffer increased to 70 from 50 to prevent recent added arc commands from getting truncated, planner buffer decreased from 18 blocks to 17.

## Commit #34
### Hash
[8a10654b1cb694f4b24f7fd247acc345f3275d28](https://github.com/gnea/grbl/commit/8a10654b1cb694f4b24f7fd247acc345f3275d28)

### Message
New stepper subsystem bug fixes.

- New stepper algorithm with the new optimized planner seems to be
working nearly twice as fast as the previous algorithm.

- For one, the planner computation overhead is probably a fraction of
what it used to be with the worst case being about half still.

- Secondly, anytime the planner plans back to the first executing
block, it no longer overwrites the block conditions and allows it to
complete without lost steps. So no matter if the streams slows, the
protected planner should keep the steppers moving without risk of lost
steps (although this still needs to be tested thoroughly and may
audibly sound weird when this happens.)

- It now seems that the bottleneck is the serial baudrate (which is
good!)
### Antipattern Category
X
### Keyword
fast
### Note
This commit does not change any performance-related features. A bug fix and edit on comments.

## Commit #35
### Hash
[0cb5756b5310b8bf0cbc554393d14e86a0186c05](https://github.com/gnea/grbl/commit/0cb5756b5310b8bf0cbc554393d14e86a0186c05)

### Message
Fine tuning of new stepper algorithm with protected planner. Adaptive step prediction for segment buffer.

- Cleaned up the new stepper algorithm code with more commenting and
better logic flow.

- The new segment buffer now predicts the number of steps each segment
should have to execute over about 8 milliseconds each (based on the
ACCELERATION_TICKS_PER_SECOND setting). So, for when the whole segment
buffer is full, the stepper algorithm has roughly 40 milliseconds of
steps queued before it needs to refilled by the main program.

- Readjusted the max supported step rate back to 30kHz from the lower
development 20kHz. Everything still works amazing great and the test
CNC machine still runs twice as fast with the new stepper algorithm and
planner.

- Upped the standard serial baudrate to 115200 baud, as it is clear
that the bottleneck is the serial interface. Will now support this, as
well as the old 9600 baud, in new firmware builds.
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
fast
### Note
Frequency increased from 20Hz to 30Hz.
DEFAULT_RAPID_FEEDRATE increased from 2500 to 4000.
DEFAULT_ACCELERATION increased from 150*60*60 to 400*60*60.

## Commit #36
### Hash
[b36e30de2eab858b5840b49b62753c18844608f8](https://github.com/gnea/grbl/commit/b36e30de2eab858b5840b49b62753c18844608f8)

### Message
Yet another major stepper algorithm and planner overhaul.

- Overhauled the stepper algorithm and planner again. This time
concentrating on the decoupling of the stepper ISR completely. It is
now dumb, relying on the segment generator to provide the number of
steps to execute and how fast it needs to go. This freed up lots of
memory as well because it made a lot tracked variables obsolete.

- The segment generator now computes the velocity profile of the
executing planner block on the fly in floating point math, instead of
allowing the stepper algorithm to govern accelerations in the previous
code. What this accomplishes is the ability and framework to (somewhat)
easily install a different physics model for generating a velocity
profile, i.e. s-curves.

- Made some more planner enhancements and increased efficiency a bit.

- The changes also did not increase the compiled size of Grbl, but
decreased it slightly as well.

- Cleaned up a lot of the commenting.

- Still much to do, but this push works and still is missing feedholds
(coming next.)
### Antipattern Category
X
### Keyword
memory
### Note
Couldn't find any performace-related antipatterns. This commit focuses on decoupling the stepper ISR from the rest of the classes that in turn reduces the number of tracked variables.

## Commit #37
### Hash
[2f6663a0b9d983ba857e400997f91a6fd93abe30](https://github.com/gnea/grbl/commit/2f6663a0b9d983ba857e400997f91a6fd93abe30)

### Message
Reinstated feed holds into new stepper algorithm and planner. Rough draft, but working.

- Reinstated the feed hold feature with the new stepper algorithm and
new optimized planner. It works, but will be re-factored a bit soon to
clean up the code.

- At this point, feedrate overrides may need to be installed in the
v1.0 version of grbl, while this version will likely be pushed to the
edge branch soon and pushed to master after the bugs have been squashed.

- Measured the overall performance of the new planner and stepper
algorithm on an oscilloscope. The new planner is about 4x faster than
before, where it is completing a plan in around 1ms. The stepper
algorithm itself is minutely faster, as it is a little lighter. The
trade-off in the increased planner performance comes from the new step
segment buffer. However, even in the worse case scenario, the step
segment buffer generates a new segment with a typical 0.2 ms, and the
worse case is 1ms upon a new block or replanning the active block.
Added altogether, it’s argubly still twice as efficient as the old one.
### Antipattern Category
X
### Keyword
performance
### Note
This commit does not change any performance-related features. New algorithm that increased the performance.

## Commit #38
### Hash
[b562845d9d20bd09426f8d20647ed334eeb7491f](https://github.com/gnea/grbl/commit/b562845d9d20bd09426f8d20647ed334eeb7491f)

### Message
Deceleration to zero speed improvements. Update defaults.

- A minor issue with deceleration ramps when close to zero velocity.
Should be virtually unnoticeable for most CNC systems, but fixed in
this push and accurate to physics.

- Updated some of the junction deviation defaults. Because the new
stepper algorithm can easily maximize a CNC machine’s capabilities or
simply go much faster, this means the speed in which it enters
junctions has to be a little more constrained. Meaning that, we have to
slow a little bit down more so that we don’t exceed the acceleration
limits of the stepper motors.
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features.

## Commit #39
### Hash
[3054b2df774c8baa19d56421466c0f3c44c00041](https://github.com/gnea/grbl/commit/3054b2df774c8baa19d56421466c0f3c44c00041)

### Message
Revamped homing cycle. Axis limits and max travel bug fixes. Build info. Refactored config.h.

- Revamped and improved homing cycle. Now tied directly into the main
planner and stepper code, which enables much faster homing seek rates.
Also dropped the compiled flash size by almost 1KB, meaning 1KB more
for other features.

- Refactored config.h. Removed obsolete defines and configuration
options. Moved lots of “advanced” options into the advanced area of the
file.

- Updated defaults.h with the new homing cycle. Also updated the
Sherline 5400 defaults and added the ShapeOko2 defaults per user
submissions.

- Fixed a bug where the individual axes limits on velocity and
acceleration were not working correctly. Caused by abs() returning a
int, rather than a float. Corrected with fabs(). Duh.

- Added build version/date to the Grbl welcome message to help indicate
which version a user is operating on.

- Max travel settings were not being defaulted into the settings EEPROM
correctly. Fixed.

- To stop a single axis during a multi-axes homing move, the stepper
algorithm now has a simple axis lock mask which inhibits the desired
axes from moving. Meaning, if one of the limit switches engages before
the other, we stop that one axes and keep moving the other.
### Antipattern Category
New:Hard-coded-fine-tuning, New:Hard-coded-timing
### Keyword
faster
### Note
Homing debounce delay increased from 100 to 250.

## Commit #40
### Hash
[5ab2bb7767730ee32960fd53793721ec27f91fd9](https://github.com/gnea/grbl/commit/5ab2bb7767730ee32960fd53793721ec27f91fd9)

### Message
Incomplete dev code push, but working. Lots of updates/fixes/improvements. Much still to polish.

- Ugh. Github just erased my list of improvements and changes due to a
conflict and forcing me to resolve it. Hope this goes through.

- Major stepper algorithm change. Trashed the old v0.9 edge
branch-style stepper algorithm. It’s fine, but it was susceptible to
aliasing noise when moving very slow or very fast. It also had a bit of
CPU overhead. It was written to solve a standing issue with v0.8
master, where it couldn’t generate a smooth acceleration abocve
10-15kHz. But, with new step segment buffer in v0.9c, it inadvertently
fixed the acceleration problem with v0.8 stepper algorithm. So, what
does it mean for you? Smoother stepper pulses and likely higher step
frequencies.

- Stepper algorithm now uses Timer1 and Timer2, instead of Timer0 and
Timer2. Timers 0 and 2 can be swapped if there is an issue.

- With the old v0.8 stepper algorithm, the STEP_DELAY_PULSE
configuration option is also back.

- NEW! Hard limit software debouncing. Grbl now employs the AVR’s
watchdog timer as a way to monitor the hard limit pins and checking
their states after a delay. This is a simple software debouncing
technique and may help alleviate some of the false trigger some users
have been complaining about. BUT, this won’t fix electric noise issues!

- Fixed an issue with the new homing cycle routine where it wasn’t
honoring the acceleration and axis speed limits depending on the homing
cycle mask. Now does. Also, updated the homing direction mask code to
be a little cleaner.

- Moved the main part of the homing cycle control and execution to
motion_control.c, where it fits better.

- Removed the STATE_INIT system state as it was redundant. Made the
system states into bitflags so multiple system states can be checked
via one if statement.

- Reorganized the power-up routine to work with the new system states.
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features. Only a variable deleted.

## Commit #41
### Hash
[47cd40c8dce6fac545119508459a4f2f0610f9ee](https://github.com/gnea/grbl/commit/47cd40c8dce6fac545119508459a4f2f0610f9ee)

### Message
Incomplete push but working. Lots more stuff. More to come.

- NEW! An active multi-axis step smoothing algorithm that automatically
adjusts dependent on step frequency. This solves the long standing
issue to aliasing when moving with multiple axes. Similar in scheme to
Smoothieware, but more advanced in ensuring a more consistent CPU
overhead throughout all frequencies while maintaining step exactness.

- Switched from Timer2 to Timer0 for the Step Port Reset Interrupt.
Mainly to free up hardware PWM pins.

- Seperated the direction and step pin assignments, so we can now move
them to seperate ports. This means that we can more easily support 4+
axes in the future.

- Added a setting for inverting the limit pins, as so many users have
request. Better late than never.

- Bug fix related to EEPROM calls when in cycle. The EEPROM would kill
the stepper motion. Now protocol mandates that the system be either in
IDLE or ALARM to access or change any settings.

- Bug fix related to resuming the cycle after a spindle or dwell
command if auto start has been disabled. This fix is somewhat temporary
or more of a patch. Doesn’t work with a straight call-response
streaming protocol, but works fine with serial buffer pre-filling
streaming that most clients use.

- Renamed the pin_map.h to cpu_map.h to more accurately describe what
the file is.

- Pushed an auto start bug fix upon re-initialization.

- Much more polishing to do!
### Antipattern Category
X
### Keyword
overhead
### Note
This commit does not change any performance-related features. A bug fix, code cleanup and some pins modified.

## Commit #42
### Hash
[cc9afdc195da0b2e71eda71ea24ddbd14378ceb1](https://github.com/gnea/grbl/commit/cc9afdc195da0b2e71eda71ea24ddbd14378ceb1)

### Message
Lots of re-organization and cleaning-up. Some bug fixes.

- Added a new source and header file called system. These files contain
the system commands and variables, as well as all of the system headers
and standard libraries Grbl uses. Centralizing some of the code.

- Re-organized the include headers throughout the source code.

- ENABLE_M7 define was missing from config.h. Now there.

- SPINDLE_MAX_RPM and SPINDLE_MIN_RPM now defined in config.h. No
uncommenting to prevent user issues. Minimum spindle RPM now provides
the lower, near 0V, scale adjustment, i.e. some spindles can go really
slow so why use up our 256 voltage bins for them?

- Remove some persistent variables from coolant and spindle control.
They were redundant.

- Removed a VARIABLE_SPINDLE define in cpu_map.h that shouldn’t have
been there.

- Changed the DEFAULT_ARC_TOLERANCE to 0.002mm to improve arc tracing.
Before we had issues with performance, no longer.

- Fixed a bug with the hard limits and the software debounce feature
enabled. The invert limit pin setting wasn’t honored.

- Fixed a bug with the homing direction mask. Now is like it used to
be. At least for now.

- Re-organized main.c to serve as only as the reset/initialization
routine. Makes things a little bit clearer in terms of execution
procedures.

- Re-organized protocol.c as the overall master control unit for
execution procedures. Not quite there yet, but starting to make a
little more sense in how things are run.

- Removed updating of old settings records. So many new settings have
been added that it’s not worth adding the code to migrate old user
settings.

- Tweaked spindle_control.c a bit and made it more clear and consistent
with other parts of Grbl.

- Tweaked the stepper disable bit code in stepper.c. Requires less
flash memory.
### Antipattern Category
New:Fixed_Communication_Rate, New:Hard-coded-fine-tuning
### Keyword
performance
### Note
DEFAULT_HOMING_SEEK_RATE increased from 500 to 635 mm/min.

## Commit #43
### Hash
[50fbc6e2972acadbe5db944ddf33d12a8d94f4a0](https://github.com/gnea/grbl/commit/50fbc6e2972acadbe5db944ddf33d12a8d94f4a0)

### Message
Refactoring and lots of bug fixes. Updated homing cycle.

WARNING: There are still some bugs to be worked out. Please use caution
if you test this firmware.

- Feed holds work much better, but there are still some failure
conditions that need to be worked out. This is the being worked on
currently and a fix is planned to be pushed next.

- Homing cycle refactoring: Slight adjustment of the homing cycle to
allow for limit pins to be shared by different axes, as long as the
shared limit pins are not homed on the same cycle. Also, removed the
LOCATE_CYCLE portion of the homing cycle configuration. It was
redundant.

- Limit pin sharing: (See above). To clear up one or two limit pins for
other IO, limit pins can now be shared. For example, the Z-limit can be
shared with either X or Y limit pins, because it’s on a separate homing
cycle. Hard limit will still work exactly as before.

- Spindle pin output fixed. The pins weren’t getting initialized
correctly.

- Fixed a cycle issue where streaming was working almost like a single
block mode. This was caused by a problem with the spindle_run() and
coolant_run() commands and issuing an unintended planner buffer sync.

- Refactored the cycle_start, feed_hold, and other runtime routines
into the runtime command module, where they should be handled here
only. These were redundant.

- Moved some function calls around into more appropriate source code
modules.

- Fixed the reporting of spindle state.
### Antipattern Category
X
### Keyword
runtime
### Note
This commit does not change any performance-related features. Mostly code formatting, more comemnts added and some pin operations changed.

## Commit #44
### Hash
[3df61e0ec5f7cb0b4c09a847558ecf14a8697802](https://github.com/gnea/grbl/commit/3df61e0ec5f7cb0b4c09a847558ecf14a8697802)

### Message
Homing and feed hold bug fixes.

WARNING: Bugs may still exist. This branch is a work in progress and
will be pushed to the edge branch when at beta stability. Use at your
own risk.

- Homing freezing issue fixed. Had to do with the cycle stop flag being
set incorrectly after the homing cycles and before the pull-off
maneuver. Now resets the stepper motors before this can happen.

- Fixed an issue with a rare feed hold failure. Had to do with feed
hold ending exactly at the end of a block. The runtime protocol now
sets the QUEUED and IDLE states appropriately when this occurs. Still
need to clean this code up however, as it’s patched rather than written
well.

- Updated version build via $I command.

- Forgot to comment on a new feature for the last commit. Since steps
are integers and millimeters traveled are floats, the old step segment
generator ignored the step fraction differences in generating the
segment velocities. Didn’t see like it would be much of a big deal, but
there were instances that this would be a problem, especially for very
slow feed rates. The stepper algorithm now micro-adjusts the segment
velocities based on the step fractions not executed from the previous
segment. This ensures that Grbl generates the velocity profiles EXACTLY
and noticeably improves overall acceleration performance.
### Antipattern Category
X
### Keyword
performance
### Note
This commit does not change any performance-related features. Bug fix and some code formatting.

## Commit #45
### Hash
[8f8d8e2887f69b86990b8cf71bc7505a071ae831](https://github.com/gnea/grbl/commit/8f8d8e2887f69b86990b8cf71bc7505a071ae831)

### Message
Added grbl planner Matlab simulator for test reference. Updated line number compile-time option.

- Added a grbl planner simulation tool that was written in Matlab and
Python. It was used to visualize the inner workings of the planner as a
program is streamed to it. The simulation assumes that the planner
buffer is empty, then filled, and kept filled. This is mainly for users
to see how the planner works.

- Updated some of the compile-time ifdefs when enabling line numbers.
The leaving the un-used line numbers in the function calls eats a
non-neglible amount of flash memory. So the new if-defs remove them.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Configuration editted and some tests added.

## Commit #46
### Hash
[76ab1b6a4282ec09df7b2c1dd534b83e61b1251c](https://github.com/gnea/grbl/commit/76ab1b6a4282ec09df7b2c1dd534b83e61b1251c)

### Message
G38.2 probe feature rough draft installed. Working but needs testing.

- G38.2 straight probe now supported. Rough draft. May be tweaked more
as testing ramps up.

- G38.2 requires at least one axis word. Multiple axis words work too.
When commanded, the probe cycle will move at the last ‘F’ feed rate
specified in a straight line.

- During a probe cycle: If the probe pin goes low (normal high), Grbl
will record that immediate position and engage a feed hold. Meaning
that the CNC machine will move a little past the probe switch point, so
keep federates low to stop sooner. Once stopped, Grbl will issue a move
to go back to the recorded probe trigger point.

- During a probe cycle: If the probe switch does not engage by the time
the machine has traveled to its target coordinates, Grbl will issue an
ALARM and the user will be forced to reset Grbl. (Currently G38.3 probe
without error isn’t supported, but would be easy to implement later.)

- After a successful probe, Grbl will send a feedback message
containing the recorded probe coordinates in the machine coordinate
system. This is as the g-code standard on probe parameters specifies.

- The recorded probe parameters are retained in Grbl memory and can be
viewed with the ‘$#’ print parameters command. Upon a power-cycle, not
a soft-reset, Grbl will re-zero these values.

- Moved ‘$#’ command to require IDLE or ALARM mode, because it accesses
EEPROM to fetch the coordinate system offsets.

- Updated the Grbl version to v0.9d.

- The probe cycle is subject to change upon testing or user-feedback.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features.

## Commit #47
### Hash
[532c359a11c71827895085e9355ba01dbad439fb](https://github.com/gnea/grbl/commit/532c359a11c71827895085e9355ba01dbad439fb)

### Message
Major g-code parser overhaul. 100%* compliant. Other related updates.

- Completely overhauled the g-code parser. It’s now 100%* compliant. (*
may have some bugs). Being compliant, here are some of the major
differences.

- SMALLER and JUST AS FAST! A number of optimizations were found that
sped things up and allowed for the more thorough error-checking to be
installed without a speed hit. Trimmed a lot of ‘fat’ in the parser and
still was able to make it significantly smaller than it was.

- No default feed rate setting! Removed completely! This doesn’t exist
in the g-code standard. So, it now errors out whenever it’s undefined
for motions that require it (G1/2/3/38.2).

- Any g-code parser error expunges the ENTIRE block. This means all
information is lost and not passed on to the running state. Before some
of the states would remain, which could have led to some problems.

- If the g-code block passes all of the error-checks, the g-code state
is updated and all motions are executed according to the order of
execution.

- Changes in spindle speed, when already running, will update the
output pin accordingly. This fixes a bug, where it wouldn’t update the
speed.

- Update g-code parser error reporting. Errors now return detailed
information of what exact went wrong. The most common errors return a
short text description. For less common errors, the parser reports
‘Invalid gcode ID:20’, where 20 is a error ID. A list of error code IDs
and their descriptions will be documented for user reference elsewhere
to save flash space.

- Other notable changes:

- Added a print integer routine for uint8 variables. This saved
significant flash space by switching from a heavier universal print
integer routine.

- Saved some flash space with our own short hypotenuse calculation

- Some arc computation flash and memory optimizations.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Multiple switch and if conditions modified and debug output.

## Commit #48
### Hash
[015d5fa19105f90694ca46986fa264893bc7155a](https://github.com/gnea/grbl/commit/015d5fa19105f90694ca46986fa264893bc7155a)

### Message
Fixed atomic access to flags in sys.execute.

This seems to fix the bug that caused Grbl to hang during some operations,
especially jogging.
### Antipattern Category
X
### Keyword
hang
### Note
This commit does not change any performance-related features. Bit operations modified.

## Commit #49
### Hash
[e455faaeef61b4b094d4e2b63725cb3e31a1a603](https://github.com/gnea/grbl/commit/e455faaeef61b4b094d4e2b63725cb3e31a1a603)

### Message
New G43.1/G49 gcodes. Not working yet!!

- Pushed this uncompleted code to merge a conflicting pull request.

- New G43.1 and G49 g-codes to be installed. The beginnings of it are
in place. These g-codes are intended to be used in conjunction with
probing and allow GUIs to set tool length offsets without Grbl needing
to store a tool table.

- G43.1 is defined as a dynamic tool length offset that is not stored
in memory. Rather, when commanded, these are applied to the work
coordinates until a reset or disabled by G49. This works much like G92.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. A switch case added and some variables defined.

## Commit #50
### Hash
[71f333ddca8ab18be5fbc49c731984f0b8d2670e](https://github.com/gnea/grbl/commit/71f333ddca8ab18be5fbc49c731984f0b8d2670e)

### Message
Settings refactoring. Bug fixes. Misc new features.

This is likely the last major change to the v0.9 code base before push
to master. Only two minor things remain on the agenda (CoreXY support,
force clear EEPROM, and an extremely low federate bug).

- NEW! Grbl is now compile-able and may be flashed directly through the
Arduino IDE. Only minor changes were required for this compatibility.
See the Wiki to learn how to do it.

- New status reporting mask to turn on and off what Grbl sends back.
This includes machine coordinates, work coordinates, serial RX buffer
usage, and planner buffer usage. Expandable to more information on user
request, but that’s it for now.

- Settings have been completely renumbered to allow for future new
settings to be installed without having to constantly reshuffle and
renumber all of the settings every time.

- All settings masks have been standardized to mean bit 0 = X, bit 1 =
Y, and bit 2 = Z, to reduce confusion on how they work. The invert
masks used by the internal Grbl system were updated to accommodate this
change as well.

- New invert probe pin setting, which does what it sounds like.

- Fixed a probing cycle bug, where it would freeze intermittently, and
removed some redundant code.

- Homing may now be set to the origin wherever the limit switches are.
Traditionally machine coordinates should always be in negative space,
but when limit switches on are on the opposite side, the machine
coordinate would be set to -max_travel for the axis. Now you can always
make it [0,0,0] via a compile-time option in config.h. (Soft limits
routine was updated to account for this as well.)

 - Probe coordinate message immediately after a probing cycle may now
be turned off via a compile-time option in config.h. By default the
probing location is always reported.

- Reduced the N_ARC_CORRECTION default value to reflect the changes in
how circles are generated by an arc tolerance, rather than a fixed arc
segment setting.

- Increased the incoming line buffer limit from 70 to 80 characters.
Had some extra memory space to invest into this.

- Fixed a bug where tool number T was not being tracked and reported
correctly.

- Added a print free memory function for debugging purposes. Not used
otherwise.

- Realtime rate report should now work during feed holds, but it hasn’t
been tested yet.

- Updated the streaming scripts with MIT-license and added the simple
streaming to the main stream.py script to allow for settings to be sent.

- Some minor code refactoring to improve flash efficiency. Reduced the
flash by several hundred KB, which was re-invested in some of these new
features.
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Code cleanup, switch cases and pin variables modified.

## Commit #51
### Hash
[9b9abf1b2f109b705ec4caf1ce31c4e8675d2262](https://github.com/gnea/grbl/commit/9b9abf1b2f109b705ec4caf1ce31c4e8675d2262)

### Message
Fixed bug related to very very low feed rates.

- A very very low feed rate command like `G1 X100 F0.01`  would cause
some floating-point round-off error and freeze Grbl into an infinite
loop. To fix it, introduced a MINIMUM_FEED_RATE parameter in config.h
to ensure motions always complete.

- MINIMUM_FEED_RATE is set at 1.0 mm/min by default. It’s recommended
that no rates are below this value, but 0.1mm/min may be ok in some
situations.
### Antipattern Category
New:rounded_numbers
### Keyword
infinite
### Note
A small rounding error in feed rate would freeze Grbl so a minimum value was added to fix this.

## Commit #52
### Hash
[b0e9a315fe39a1efcd0f2f172cd69f1a83f8f631](https://github.com/gnea/grbl/commit/b0e9a315fe39a1efcd0f2f172cd69f1a83f8f631)

### Message
Final minor updates for master release.

- Updated ShapeOko2 defaults based on machine testing of the basic
model provided by Inventables. (or close to it.) Should be pretty
conservative but much faster than before. For example, X and Y axes are
set at (10x) faster at 5000mm/min. It can run much faster than this,
but this seems like a safe speed for everyone.

- Updated README for master release.

- Added some new settings methods for clearing the EEPROM when changing
versions. Needs some more work, but it should ok for master release.
Should work on it more for the next version.
### Antipattern Category
New:Hard-coded-fine-tuning
### Keyword
faster
### Note
DEFAULT_X_MAX_TRAVEL, DEFAULT_Y_MAX_TRAVEL, DEFAULT_Z_MAX_TRAVEL increased from 200.0 to 290 // mm
DEFAULT_Z_MAX_RATE increased from 500 to 750 mm/min.

## Commit #53
### Hash
[9be7b3d9304a0968e238b5ef2ab8e2292aa5e351](https://github.com/gnea/grbl/commit/9be7b3d9304a0968e238b5ef2ab8e2292aa5e351)

### Message
Lot of refactoring for the future. CoreXY support.

- Rudimentary CoreXY kinematics support. Didn’t test, but homing and
feed holds should work. See config.h. Please report successes and
issues as we find bugs.

- G40 (disable cutter comp) is now “supported”. Meaning that Grbl will
no longer issue an error when typically sent in g-code program header.

- Refactored coolant and spindle state setting into separate functions
for future features.

- Configuration option for fixing homing behavior when there are two
limit switches on the same axis sharing an input pin.

- Created a new “grbl.h” that will eventually be used as the main
include file for Grbl. Also will help simply uploading through the
Arduino IDE

- Separated out the alarms execution flags from the realtime (used be
called runtime) execution flag variable. Now reports exactly what
caused the alarm. Expandable for new alarms later on.

- Refactored the homing cycle to support CoreXY.

- Applied @EliteEng updates to Mega2560 support. Some pins were
reconfigured.

- Created a central step to position and vice versa function. Needed
for non-traditional cartesian machines. Should make it easier later.

- Removed the new CPU map for the Uno. No longer going to used. There
will be only one configuration to keep things uniform.
### Antipattern Category
X
### Keyword
runtime
### Note
This commit does not change any performance-related features. Lot of code deleted, somebit operations changed, code refactored and a config option added.

## Commit #54
### Hash
[76730176da0ddee2f31aea3e28e2df54342629c9](https://github.com/gnea/grbl/commit/76730176da0ddee2f31aea3e28e2df54342629c9)

### Message
Arduino IDE compatibility and minor homing fixes

- Added an include in the right spot, if a user tries to compile and
upload Grbl through the Arduino IDE with the old way.

- Fixed a minor bug with homing max travel calculations. It was causing
simultaneous axes homing to move slow than it did before.
### Antipattern Category
X
### Keyword
slow
### Note
This commit does not change any performance-related features. Support for Arduino added.

## Commit #55
### Hash
[12f48a008a2432df99771ff3223ba3f98578acc1](https://github.com/gnea/grbl/commit/12f48a008a2432df99771ff3223ba3f98578acc1)

### Message
Grbl v1.0e huge beta release. Overrides and new reporting.

- Feature: Realtime feed, rapid, and spindle speed overrides. These
alter the running machine state within tens of milliseconds!
    - Feed override: 100%, +/-10%, +/-1% commands with values 1-200% of
programmed feed
    - Rapid override: 100%, 50%, 25% rapid rate commands
    - Spindle speed override: 100%, +/-10%, +/-1% commands with values
50-200% of programmed speed
    - Override values have configurable limits and increments in
config.h.
- Feature: Realtime toggle overrides for spindle stop, flood coolant,
and optionally mist coolant
    - Spindle stop: Enables and disables spindle during a feed hold.
Automatically restores last spindles state.
    - Flood and mist coolant: Immediately toggles coolant state until
next toggle or g-code coolant command.
- Feature: Jogging mode! Incremental and absolute modes supported.
    - Grbl accepts jogging-specific commands like $J=X100F50. An axis
word and feed rate are required. G20/21 and G90/G91 commands are
accepted.
    - Jog motions can be canceled at any time by a feed hold `!`
command. The buffer is automatically flushed. (No resetting required).
    - Jog motions do not alter the g-code parser state so GUIs don’t
have to track what they changed and correct it.
- Feature: Laser mode setting. Allows Grbl to execute continuous
motions with spindle speed and state changes.
- Feature: Significantly improved status reports. Overhauled to cram in
more meaningful data and still make it smaller on average.
    - All available data is now sent by default, but does not appear if
it doesn’t change or is not active.
    - Machine position(MPos) or work position(WPos) is reported but not
both at the same time. Instead, the work coordinate offsets (WCO)are
sent intermittently whenever it changes or refreshes after 10-30 status
reports. Position vectors are easily computed by WPos  = MPos - WCO.
    - All data has changed in some way. Details of changes are in the
markdown documents and wiki.
- Feature: 16 new realtime commands to control overrides. All in
extended-ASCII character space.
    - While they are not easily typeable and requires a GUI, they can’t
be accidentally triggered by some latent character in the g-code
program and have tons of room for expansion.
- Feature: New substates for HOLD and SAFETY DOOR. A `:x` is appended
to the state, where `x` is an integer and indicates a substate.
    - For example, each integer of a door state describes in what phase
the machine is in during parking. Substates are detailed in the
documentation.
- Feature: With the alarm codes, homing and probe alarms have been
expanded with more codes to provide more exact feedback on what caused
the alarm.
- Feature: New hard limit check upon power-up or reset. If detected, a
feedback message to check the limit switches sent immediately after the
welcome message.
    - May be disabled in config.h.

- OEM feature: Enable/disable `$RST=` individual commands based on
desired behavior in config.h.
- OEM feature: Configurable EEPROM wipe to prevent certain data from
being deleted during firmware upgrade to a new settings version or
`RST=*` command.
- OEM feature: Enable/disable the `$I=` build info write string with
external EEPROM write example sketch.
    - This prevents a user from altering the build info string in
EEPROM. This requires the vendor to write the string to EEPROM via
external means. An Arduino example sketch is provided to accomplish
this. This would be useful for contain product data that is
retrievable.

- Tweak: All feedback has been drastically trimmed to free up flash
space for the v1.0 release.
    - The `$` help message is just one string, listing available
commands.
    - The `$$` settings printout no longer includes descriptions. Only
the setting values. (Sorry it’s this or remove overrides!)
    - Grbl `error:` and `ALARM:` responses now only contain codes. No
descriptions. All codes are explained in documentation.
    - Grbl’s old feedback style may be restored via a config.h, but
keep in mind that it will likely not fit into the Arduino’s flash space.
- Tweak: Grbl now forces a buffer sync or stop motion whenever a g-code
command needs to update and write a value to EEPROM or changes the work
coordinate offset.
    - This addresses two old issues in all prior Grbl versions. First,
an EEPROM write requires interrupts to be disabled, including stepper
and serial comm. Steps can be lost and data can be corrupted. Second,
the work position may not be correlated to the actual machine position,
since machine position is derived from the actual current execution
state, while work position is based on the g-code parser offset state.
They are usually not in sync and the parser state is several motions
behind. This forced sync ensures work and machine positions are always
correct.
    - This behavior can be disabled through a config.h option, but it’s
not recommended to do so.
- Tweak: To make status reports standardized, users can no longer
change what is reported via status report mask, except for only
toggling machine or work positions.
    - All other data fields are included in the report and can only be
disabled through the config.h file. It’s not recommended to alter this,
because GUIs will be expecting this data to be present and may not be
compatible.
- Tweak: Homing cycle and parking motion no longer report a negative
line number in a status report. These will now not report a line number
at all.
- Tweak: New `[Restoring spindle]` message when restoring from a
spindle stop override. Provides feedback what Grbl is doing while the
spindle is powering up and a 4.0 second delay is enforced.
- Tweak: Override values are reset to 100% upon M2/30. This behavior
can be disabled in config.h
- Tweak: The planner buffer size has been reduced from 18 to 16 to free
up RAM for tracking and controlling overrides.
- Tweak: TX buffer size has been increased from 64 to 90 bytes to
improve status reporting and overall performance.
- Tweak: Removed the MOTION CANCEL state. It was redundant and didn’t
affect Grbl’s overall operation by doing so.
- Tweak: Grbl’s serial buffer increased by +1 internally, such that 128
bytes means 128, not 127 due to the ring buffer implementation. Long
overdue.
- Tweak: Altered sys.alarm variable to be set by alarm codes, rather
than bit flags. Simplified how it worked overall.
- Tweak: Planner buffer and serial RX buffer usage has been combined in
the status reports.
- Tweak: Pin state reporting has been refactored to report only the
pins “triggered” and nothing when not “triggered”.
- Tweak: Current machine rate or speed is now included in every report.
- Tweak: The work coordinate offset (WCO) and override states only need
to be refreshed intermittently or reported when they change. The
refresh rates may be altered for each in the config.h file with
different idle and busy rates to lessen Grbl’s load during a job.
- Tweak: For temporary compatibility to existing GUIs until they are
updated, an option to revert back to the old style status reports is
available in config.h, but not recommended for long term use.
- Tweak: Removed old limit pin state reporting option from config.h in
lieu of new status report that includes them.
- Tweak: Updated the defaults.h file to include laser mode, altered
status report mask, and fix an issue with a missing invert probe pin
default.

- Refactor: Changed how planner line data is generated and passed to
the planner and onto the step generator. By making it a struct
variable, this saved significant flash space.
- Refactor: Major re-factoring of the planner to incorporate override
values and allow for re-calculations fast enough to immediately take
effect during operation. No small feat.
- Refactor: Re-factored the step segment generator for re-computing new
override states.
- Refactor: Re-factored spindle_control.c to accommodate the spindle
speed overrides and laser mode.
- Refactor: Re-factored parts of the codebase for a new jogging mode.
Still under development though and slated to be part of the official
v1.0 release. Hang tight.
- Refactor: Created functions for computing a unit vector and value
limiting based on axis maximums to free up more flash.
- Refactor: The spindle PWM is now set directly inside of the stepper
ISR as it loads new step segments.
- Refactor: Moved machine travel checks out of soft limits function
into its own since jogging uses this too.
- Refactor: Removed coolant_stop() and combined with
coolant_set_state().
- Refactor: The serial RX ISR forks off extended ASCII values to
quickly assess the new override realtime commands.
- Refactor: Altered some names of the step control flags.
- Refactor: Improved efficiency of the serial RX get buffer count
function.
- Refactor: Saved significant flash by removing and combining print
functions. Namely the uint8 base10 and base2 functions.
- Refactor: Moved the probe state check in the main stepper ISR to
improve its efficiency.
- Refactor: Single character printPgmStrings() went converted to direct
serial_write() commands to save significant flash space.

- Documentation: Detailed Markdown documents on error codes, alarm
codes, messages, new real-time commands, new status reports, and how
jogging works. More to come later and will be posted on the Wiki as
well.
- Documentation: CSV files for quick importing of Grbl error and alarm
codes.

- Bug Fix: Applied v0.9 master fixes to CoreXY homing.
- Bug Fix: The print float function would cause Grbl to crash if a
value was 1e6 or greater. Increased the buffer by 3 bytes to help
prevent this in the future.
- Bug Fix: Build info and startup string EEPROM restoring was not
writing the checksum value.
- Bug Fix: Corrected an issue with safety door restoring the proper
spindle and coolant state. It worked before, but breaks with laser mode
that can continually change spindle state per planner block.
- Bug Fix: Move system position and probe position arrays out of the
system_t struct. Ran into some compiling errors that were hard to track
down as to why. Moving them out fixed it.
### Antipattern Category
X
### Keyword
performance
### Note
From the notes this commit it doesn't seem to tackle any performance-related antipattern.

## Commit #56
### Hash
[ed790c9fa298b77529ec87b917d19f249cff976b](https://github.com/gnea/grbl/commit/ed790c9fa298b77529ec87b917d19f249cff976b)

### Message
v1.1d: Tweaked interface a bit. Added realtime spindle speed and build option data. Minor bug fixes.

- Increment to v1.1d due to interface tweaks.

- Based on GUI dev feedback, the toggle overrides report was removed
and replace with showing “accessory state”. This shows a character if a
particular accessory is enabled, like the spindle or flood coolant.
These can be directly altered by the toggle overrides, so when they
execute, a GUI will be able to observe the state altering as feedback.

- Altered the real-time feed rate to show real-time spindle speed as
well. It was an over-sight on my part. It’s needed because it’s hard to
know what the current spindle speed is when overrides are altering it.
Especially during something like a laser cutting job when its important
to know how spindle speed overrides are effecting things.

- Real-time spindle speed is not shown if VARIABLE_SPINDLE is disabled.
The old real-time feed rate data field will show instead.

- Compile-time option data is now included in another message
immediately following the build info version string, starting with
`[OPT:`. A character code follows the data type name with each
indicating a particular option enabled or disabled. This will help
immensely with debugging Grbl as well as help GUIs know exactly how
Grbl was compiled.

- These interface changes are detailed in the updated documentation.

- Reduced the default planner buffer size from 17 to 16. Needed to free
up some memory…

- For increasing the serial TX buffer size from 90 to 104 bytes. The
addition of real-time spindle speeds and accessory enable data required
a bigger buffer. This is to ensure Grbl is performing at optimal levels.

- Refactored parts of the spindle and coolant control code to make it
more consistent to each other and how it was called. It was a little
messy. The changes made it easier to track what each function call was
doing based on what was calling it.

- Created a couple of new get_state functions for the spindle and
coolant. These are called by the accessory state report to look
directly at the pin state, rather than track how it was set. This
guarantees that the state is reported correctly.

- Updated the g-code parser, parking motion, sleep mode, and spindle
stop calls to refactored spindle and coolant code.

- Added a compile-time option to enable homing individual axes, rather
than having only the main homing cycle. The actual use case for this is
pretty rare. It’s not recommended you enable this, unless you have a
specific application for it. Otherwise, just alter the homing cycle
itself.

- Refactored the printFloat() function to not show a decimal point if
there are no trailing values after it. For example, `1.` now shows `1`.

- Fixed an issue regarding spindle speed overrides no being applied to
blocks without motions.

- Removed the toggle_ovr_mask system variable and replaced with
spindle_stop_ovr system variable. Coolant toggles don’t need to be
tracked.

- Updated README
### Antipattern Category
X
### Keyword
memory
### Note
This commit does not change any performance-related features. Interface tweakes, comments added, printFloat refactor , if conditions added.

## Commit #57
### Hash
[e8b717604b094ff5d4fb747f2f19065b8fd004cd](https://github.com/gnea/grbl/commit/e8b717604b094ff5d4fb747f2f19065b8fd004cd)

### Message
Spindle speed overrides behavior tweak. New experimental laser dynamic power mode.

- Spindle speed overrides now update immediately if they are changed
while in a HOLD state. Previously, they would update after exiting the
HOLD, which isn’t correct.

- New experimental dynamic laser power mode that adjusts laser power
based on current machine speed. Enabled by uncommenting
LASER_CONSTANT_POWER_PER_RATE in config.h

  - It assumes the programmed rate is the intended power/rate for the
motion.
  - Feed rate overrides (FRO) do not effect the power/rate. Meaning
that spindle PWM will automatically lower with lower FRO and increase
with higher FRO to keep it the same.
  - Spindle speed overrides (SSO) will directly increase and decrease
the power/rate. So 150% SSO will increase the PWM output by 150% for
the same speed.
  - The combination of FRO and SSO behaviors should allow for subtle
and highly flexible tuning of how the laser cutter is operating in
real-time and during the job.

- Re-factored planner block rapid rate handling for the dynamic laser
power feature. Should have had no effect on how Grbl operates.
### Antipattern Category
X
### Keyword
increase
### Note
This commit does not change any performance-related features.

## Commit #58
### Hash
[b753c542c7f708a5b86b73e87328615223c5c8be](https://github.com/gnea/grbl/commit/b753c542c7f708a5b86b73e87328615223c5c8be)

### Message
v1.1e: New laser features. G-code parser refactoring. CoreXY homing fix.

- Increment to v1.1e due to new laser features.

- After several discussions with some prominent laser people, a few
tweaks to the new laser mode has been installed.

- LASER: M3 behaves in a constant power mode.

- LASER: M4 behaves in a dynamic power mode, where the laser power is
automatically adjusted based on how fast Grbl is moving relative to the
programmed feed rate. This is the same as the  CONSTANT_POWER_PER_RATE
config.h option in the last version. NOTE: When not in motion in M4,
Grbl automatically turns off the laser. Again, it only operates while
moving!

- LASER: Only G1, G2, and G3 motion modes will turn on the laser. So,
this means that G0, G80 motion modes will always keep the laser
disabled. No matter if M3/M4 are active!

- LASER: A spindle stop override is automatically invoked when a laser
is put in a feed hold. This behavior may be disabled by a config.h
option.

- Lots of little tweaks to the g-code parser to help streamline it a
bit. It should no effect how it operates. Generally just added a parser
flag to track and execute certain scenarios a little more clearly.

- Jog motions now allow line numbers to be passed to it and will be
displayed in the status reports.

- Fixed a CoreXY homing bug.

- Fixed an issue when $13 is changed, WCO isn’t sent immediately.

- Altered how spindle PWM is set in the stepper ISR. Updated on a step
segment basis now. May need to change this back if there are any
oddities from doing this.

- Updated some documentation. Clarified why M0 no longer showing up in
$G and why a `1.` floating point values are shown with no decimals,
like so `1`.
### Antipattern Category
X
### Keyword
fast
### Note
This commit does not change any performance-related features. Mostly comments and error checking for commands.

## Commit #59
### Hash
[864d1306b93285645599e33063c0805e6c8ff905](https://github.com/gnea/grbl/commit/864d1306b93285645599e33063c0805e6c8ff905)

### Message
Fixed homing fail alarm handling. Re-integrated software debouncing.

- [bug] Fixed a homing fail issue, where the alarm was not being set
right, not cleared correctly. It would report the wrong code and enter
an infinite alarm loop. This was due to how alarm codes were altered a
while back. Now updated and fixed to show the right codes.

- [feature] Re-installed optional software debouncing for hard limit
switches. By request.
### Antipattern Category
X
### Keyword
infinite
### Note
This commit does not change any performance-related features.

## Commit #60
### Hash
[921e5a9799691118ffe5d4ecf5ccce68efe8a3f8](https://github.com/gnea/grbl/commit/921e5a9799691118ffe5d4ecf5ccce68efe8a3f8)

### Message
Clean up and new streaming script check-mode feature.

[new] The stream.py streaming script now has a check-mode option, where it will place Grbl in $C check mode automatically and then stream the g-code program. It's a very fast way to check if the g-code program has any errors.

[fix] The debug variable was not initialized if the debug option was enabled in config.h

[fix] Updated error_codes CSV file to the same format as the others.
### Antipattern Category
X
### Keyword
fast
### Note
This commit does not change any performance-related features.

## Commit #61
### Hash
[b75e5571eeaeb22a88304716fb1e7411f9c28be0](https://github.com/gnea/grbl/commit/b75e5571eeaeb22a88304716fb1e7411f9c28be0)

### Message
Dual motor support for self-squaring gantry homing.

- New dual motor support feature for gantry CNC machines. An axis motor is  efficiently mirrored to a dedicated set of step and direction pins (D12/D13 or A3/A4) with no detectable loss of performance. Primarily used to independently home both sides of a dual-motor gantry with a pair of limit switches (second shared with Z-axis limit pin). When the limit switches are setup correctly, Grbl will self-square the gantry (and stay square if $1=255 is programmed). Beware use at your own risk! Grbl is not responsible for any damage to any machines.

- Dual axis motors is only supported on the X-axis or Y-axis. And deletes the spindle direction(D13) and optional coolant mist (A4) features to make room for the dual motor step and direction pins.

- Dual axis homing will automatically abort homing if one limit switch triggers and travels more than 5% (default) of the non-dual axis max travel setting. For example, if the X-axis has dual motors and one X-axis triggers during homing, Grbl will abort 5% of the Y-axis max travel and the other X-axis limit fails to trigger. This will help keep any misconfigurations or failed limit switches from damaging the machine, but not completely eliminate this risk. Please take all precautions and test thouroughly before using this.

- Dual axis motors supports two configurations:

- Support for Arduino CNC shield clones. For these, step/dir on pins D12/D13, and spindle enable is moved to A3 (old coolant enable), while coolant enable is moved to A4 (SDA pin). Variable spindle/laser mode option is NOT supported for this shield.

- Support for Protoneer CNC Shield v3.51. Step/dir on pins A3/A4, and  coolant enable is moved to D13 (old spindle direction pin). Variable spindle/laser mode option IS supported for this shield.

- Added Bob's CNC E3 and E4 CNC machine defaults.
### Antipattern Category
X
### Keyword
performance
### Note
This commit does not change any performance-related features. Dual motor support implemented.

