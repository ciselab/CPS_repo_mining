# Valetudo

### remote
https://github.com/Hypfer/Valetudo


## Commit #1 

### Hash
[ddc1c5f74ec06d63d2438932220e369678998342](https://github.com/Hypfer/Valetudo/commit/ddc1c5f74ec06d63d2438932220e369678998342)


### Message
applied some performance improvement

### Antipattern Category
Smith:General:How_Many_Times_Do_I_Have_to_Tell_You

### Keyword
performance

### Note
This modification saves the results of the method call to Jimp.rgbaToInt and saves it in variables. Then, it uses the value multiple times. In the previous version, the method was called each time the values were needed.


## Commit #2

### Hash
[0845ce1ba4d31eeaf723e21cae3744c638c0dc59](https://github.com/Hypfer/Valetudo/commit/0845ce1ba4d31eeaf723e21cae3744c638c0dc59) 

### Message
Change config file location to /mnt/data

### Antipattern Category
X

### Keyword
memory

### Note
Commit description:

If you flash a new firmware, the config in /etc/valetudo will be gone.
We should use the persitant flash memory for that.


This commit is not performance-related.

## Commit #3

### Hash
[9a847a42b8382288180c0b2335a8f3aba32d7bd0](https://github.com/Hypfer/Valetudo/commit/9a847a42b8382288180c0b2335a8f3aba32d7bd0)

### Message
Downgrade Build to Node 8 since Node 10 seems to be leaking memory
There was a memory leak in node version up to 11.12 iirc. Thats why Valetudo was downgraded to Node 8.
### Antipattern Category
X

### Keyword
memory

### Note
This is a change to the CI/CD travis.yml
It is due to a memory leak which is fixed in Commit #7. After the final fix, the nod version is changed back to 10.

## Commit #4

### Hash
[0ea6addff0aa945e55857289270cb8e22f3fae44](https://github.com/Hypfer/Valetudo/commit/0ea6addff0aa945e55857289270cb8e22f3fae44)

### Message
Changed Node Version to 8 + Memory Limit

### Antipattern Category
X

### Keyword
memory

### Note
This is a change to the CI/CD travis.yml.
It is due to a memory leak which is fixed in Commit #7. After the final fix, the nod version is changed back to 10.

## Commit #5

### Hash
[91088195f869d6d6f96bb612770e3bcc7a1d00b8](https://github.com/Hypfer/Valetudo/commit/91088195f869d6d6f96bb612770e3bcc7a1d00b8)

## PR
https://github.com/Hypfer/Valetudo/pull/198

### Message
Limit memory allocation

### Antipattern Category
Smith:General:Falling_Dominoes 

### Keyword
memory

### Note
There is a memory leak problem in the CPS and developers cannot detect why. Instead, they limit virtual memory allocation to make sure that this memory leak does not impact the other modules (player process) in the system. This memory leak is fixed later in Commit #7.

## Commit #6

### Hash
[2b8e4e354a092cdb5e7aa0c5f68ce00a58c57e17](https://github.com/Hypfer/Valetudo/commit/2b8e4e354a092cdb5e7aa0c5f68ce00a58c57e17)

### Message
Might fix memory leak

### Antipattern Category
X

### Keyword
memory

### Note
Did not fix the issue

## Commit #7
[a9fa64fcec23639b7367a0d3fa61b84cd07eaebe](https://github.com/Hypfer/Valetudo/commit/a9fa64fcec23639b7367a0d3fa61b84cd07eaebe)

### Message
More attempts to prevent Valetudo from going out of memory

### Antipattern Category
General:recreate_objects

### Keyword
memory

### Note
This commit fixes the issue that commits 5 and 6 could not fix it. The issue was rooted from the map object initializiation in classes WebServer and mqttClient. The solution creates on instance of the map object in the caller class (Valetudo.js) and pass it to the other objects wheneveer it is needed. 

## Commit #8

### Hash
[d96eb15c8f299ff49d98f9d6661c6f44225bc633](https://github.com/Hypfer/Valetudo/commit/d96eb15c8f299ff49d98f9d6661c6f44225bc633)

### Message
feat: Added debug config option to continuously log memory usage

### Antipattern Category
X

### Keyword
memory

### Note
This commit adds a feature to log the memory usage in the debug mode continuously.

## Commit #9

### Hash
[890120c76930bb8941459a7e0d1baa0af8577d83](https://github.com/Hypfer/Valetudo/commit/890120c76930bb8941459a7e0d1baa0af8577d83)

### Message
Fix map coloring 


### Antipattern Category
X

### Keyword
Increase

### Note
This is a UI-related commit. This commit is mistakenly considered as performance-related because its description contains the keyword "increase".

## Commit #10

### Hash
[a0fa7f49f7f0779357c3ce61d354badd5bac07ed](https://github.com/Hypfer/Valetudo/commit/a0fa7f49f7f0779357c3ce61d354badd5bac07ed)

### Message
fix(vendor.viomi): Fix basic control functionality


### Antipattern Category
X

### Keyword
Increase

### Note
This is a functionality-related commit. This commit is mistakenly considered as performance-related because its description contains the keyword "increase".

## Commit #11

### Hash
[a128a91499d94f0e75d17f87396571f6c889a7ac](https://github.com/Hypfer/Valetudo/commit/a128a91499d94f0e75d17f87396571f6c889a7ac)


### Message
fix(vendor.viomi): Increase timeout for set_timezone 


## PR
https://github.com/Hypfer/Valetudo/pull/806

### Antipattern Category
New:Impatient_requester


### Keyword
Increase

### Note

__Commit description:__
It looks like sometimes set_timezone takes ~1s to execute in some cases.
We have time. Increase timeout so it doesn't take the entire connection down.

__Analyzer note:__
The set_timezone is a command which the system send to a hardware (here, ([Viomi](https://www.viomi.com) robot vacuum)). Since this request has been sent with a small and inflexible timeout, the hrdware fails to response to many cases, and thereby it negatively impact the entire connection. Commit #13 is almost showing the same issue.


## Commit #12

### Hash
[a3905106347c1640f1817302e881de1dfce22133](https://github.com/Hypfer/Valetudo/commit/a3905106347c1640f1817302e881de1dfce22133)

### Message
feat!(mqtt): Homie-compatible implementation 


### Antipattern Category
X

### Keyword
Increase

### Note
This is not a performance-related commit.

## Commit #13

### Hash
[5f6068d7790a8f3f322f4825493608605ed80a63](https://github.com/Hypfer/Valetudo/commit/5f6068d7790a8f3f322f4825493608605ed80a63)

### Message
fix(vendor.viomi): Raise default miIO timeout


## PR
https://github.com/Hypfer/Valetudo/pull/817

### Antipattern Category
New:Impatient_requester

### Keyword
slow

### Note
__Commmit description:__

viomi: Raise default miIO timeout

Viomi is slow :/

viomi: Copy JSDoc to overridden sendCommand methods

__Analyzer note:__

This is an intersting case where the software tries to interact with the hardware ([Viomi](https://www.viomi.com) robot vacuum), but it does not have a accurate estimation about the hardware process speed. In this scenario, as developers mentioned in the [PR](https://github.com/Hypfer/Valetudo/pull/817
), "Viomi gets a shitload of random uncaught rejections caused by it being too slow replying to a lot of commands, especially during the initial connection. It does reply eventually, it just needs patience". This commit, same as commit 11, shows a new CPS-related antipattern where the code send a command to the hardware with a small and inflexible timeout.

## Commit #14

### Hash
[e6fd6e4534db0366078b7cd7797dc0f0051ade99](https://github.com/Hypfer/Valetudo/commit/e6fd6e4534db0366078b7cd7797dc0f0051ade99)

### Message
feat(mqtt): Remove increase/decrease from intensity capability

### Antipattern Category
X

### Keyword
Increase

### Note
This is not a performance-related commit.

## Commit #15

### Hash 
[f7b42edbb65e3860248e81e6c6b365d0f6be978c](https://github.com/Hypfer/Valetudo/commit/f7b42edbb65e3860248e81e6c6b365d0f6be978c)

### Message
refactor(vendor.roborock): Improve map parser performance

### Antipattern Category
General:Performance:for_if

### Keyword
performance
### Note
This commit addresses the known [for-if antipattern](https://devblogs.microsoft.com/oldnewthing/20111227-00/?p=8793). In this commit, the developer removed the unnecessary if condition form inside of the loop.

## Commit #16
### Hash 
[2f46d77a7d69c55cf744f78c47f1bec5681e8287](https://github.com/Hypfer/Valetudo/commit/2f46d77a7d69c55cf744f78c47f1bec5681e8287)

### Message
refactor(vendor.roborock): Further improve map parser performance

### Antipattern Category
X

### Keyword
performance

### Note
This is a general performance improvement by using ~~ instead of Math.floor, ~~ is slightly faster since it basically just casts to int. Although it improves the performance, this change does not expose any antipattern.

## Commit #17

### Hash
[a05dcfec6ad6de3732430d561f4c68cc485133f8](https://github.com/Hypfer/Valetudo/commit/a05dcfec6ad6de3732430d561f4c68cc485133f8)

### Message
chore(core): Increase the amount of allowed log requests

### Antipattern Category
X

### Keyword
increase

### Note
This is not a performance-related commit.

## Commit #18

### Hash
[98b2757aec0af94392038577eead7749ef659e17](https://github.com/Hypfer/Valetudo/commit/98b2757aec0af94392038577eead7749ef659e17)

### Message
feat(mqtt): Stream map serialization to improve memory usage with large maps

### Antipattern Category
X


### Keyword
memory

### Note
This is a general performance improvement by streaming the map objects.

## Commit #19

### Hash
[9000f51eaf818ca465ad0b2ef9f91ca421ac2da4](https://github.com/Hypfer/Valetudo/commit/9000f51eaf818ca465ad0b2ef9f91ca421ac2da4)

### Message
fix(webserver): Properly report memory info for kernels older than 3.14 but newer than 2.6

### Antipattern Category
X

### Keyword
memory

### Note
This commit improves the logging practices.

## Commit #20

### Hash
[6578a99344a6d087450a0e4b45a630398fb3a544](https://github.com/Hypfer/Valetudo/commit/6578a99344a6d087450a0e4b45a630398fb3a544)

### Message
fix: Try logging everything we can get about process memory before committing sudoku

### Antipattern Category
X

### Keyword
memory

### Note
This commit improves the logging practices.

## Commit #21

### Hash
[021213e8cd3b932685b590d896dcf640c311a2fc](https://github.com/Hypfer/Valetudo/commit/021213e8cd3b932685b590d896dcf640c311a2fc)

### Message
feat(vendor.dreame): Map fast mapping status

### Antipattern Category
X

### Keyword
fast

### Note
This is not a performance-related commit.


## Commit #22

### Hash
[51ee17d601a65e83e1bf81b7031e501a2195ca7b](https://github.com/Hypfer/Valetudo/commit/51ee17d601a65e83e1bf81b7031e501a2195ca7b)

### Message
Revert feat(mqtt): Stream map serialization to improve memory usage with large maps
### Antipattern Category
X
### Keyword
memory

### Note
Reverting Commit #18
## Commit #23

### Hash
[5202164714ae8cb9759529511fa9e9ec3c7eab7c](https://github.com/Hypfer/Valetudo/commit/5202164714ae8cb9759529511fa9e9ec3c7eab7c)

### Message
chore(build): Bump pkg version and allow reuse of the bundled runtime

### Antipattern Category
X

### Keyword
runtime

### Note
This is not a performance-related commit.
