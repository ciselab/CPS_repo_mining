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
Smith:General:Falling_Dominoes 


### Keyword
Increase

### Note
The failure to change timezone on time (i.e., it can take about 10 seconds) leads to the failure of the entire connection.
Commit description:
It looks like sometimes set_timezone takes ~1s to execute in some cases.
We have time. Increase timeout so it doesn't take the entire connection down.
