## Commit #1
### Hash
[d1025b6b5d98686abdf9d8c450f07da27e3b6012](https://github.com/espressif/arduino-esp32commit/d1025b6b5d98686abdf9d8c450f07da27e3b6012)

### Message
Update esp32-hal-i2c.c

wait for data to be latched and increase timeout in attempt to fix clock stretch issues

Connected issues:

http://esp32.com/viewtopic.php?f=19&t=632&p=2832#p2801

https://github.com/espressif/arduino-esp32/issues/81

https://github.com/espressif/arduino-esp32/issues/53

https://github.com/espressif/arduino-esp32/issues/11
### Antipattern Category

### Keyword
increase
### Note


## Commit #2
### Hash
[51a4432ca8e71be202358ceb068f3047bb8ad762](https://github.com/espressif/arduino-esp32commit/51a4432ca8e71be202358ceb068f3047bb8ad762)

### Message
HTTPClient Port (#347)

* Fix possible infinite loop in the example



* Remove workaround of sockets always return -76 



Remove workaround of sockets always return -76 (because it's fixed on IDF now)

Remove delay during handshake (improving stability)



* Remove unusable mbedtls_net of context creation



* Fix bad destructor



* Compatibility with WiFiClient for HTTPClient



* Initial port from ESP8266



Changed SHA1 fingerprint by Root CA verification

Changed log system



* Remove deprecated function
### Antipattern Category

### Keyword
infinite
### Note


## Commit #3
### Hash
[dcdf8132d6b8aaf146ad16f5e5c60a93c887ad6b](https://github.com/espressif/arduino-esp32commit/dcdf8132d6b8aaf146ad16f5e5c60a93c887ad6b)

### Message
Increase partition size to 1.25MB so BT and WiFi can fit

Fixes: https://github.com/espressif/arduino-esp32/issues/339
### Antipattern Category

### Keyword
increase
### Note


## Commit #4
### Hash
[4495659ac53bcdc4f8e59d6918b3e472903d63a7](https://github.com/espressif/arduino-esp32commit/4495659ac53bcdc4f8e59d6918b3e472903d63a7)

### Message
Increase the memory for loop task
### Antipattern Category

### Keyword
memory
### Note


## Commit #5
### Hash
[e3a5ae439bb94ae13bd970d9484d4665e1df4972](https://github.com/espressif/arduino-esp32commit/e3a5ae439bb94ae13bd970d9484d4665e1df4972)

### Message
clean up faster (fixes #828) (#1087)

flush tcp buffer instead of reading it byte by byte.
### Antipattern Category

### Keyword
faster
### Note


## Commit #6
### Hash
[a59eafbc9dfa3ce818c110f996eebf68d755be24](https://github.com/espressif/arduino-esp32commit/a59eafbc9dfa3ce818c110f996eebf68d755be24)

### Message
Update IDF to aaf1239 (#1539)

* fix sdmmc config



* Fix warnings in EEPROM



from @Curclamas



* remove leftover TAG in EEPROM



* Initial add of @stickbreaker i2c



* Add log_n



* fix warnings when log is off



* i2c code clean up and reorganization



* add flags to interrupt allocator



* fix sdmmc config



* Fix warnings in EEPROM



from @Curclamas



* remove leftover TAG in EEPROM



* fix errors with latest IDF



* fix debug optimization (#1365)



incorrect optimization for debugging tick markers.



* Fix some missing BT header



* Change BTSerial log calls



* Update BLE lib



* Arduino-ESP32 release management scripted (#1515)



* Calculate an absolute path for a custom partitions table (#1452)



* * Arduino-ESP32 release management scripted

(ready-to-merge)



* * secure env for espressif/arduino-esp32



* * build tests enabled

* gitter webhook enabled



* * gitter room link fixed

* better comment



* * filepaths fixed



* BT Serial adjustments



* * don't run sketch builds & tests for tagged builds



* Return false from WiFi.hostByName() if hostname is not resolved



* Free BT Memory when BT is not used



* WIFI_MODE_NULL is not supported anymore



* Select some key examples to build with PlatformIO to save some time



* Update BLE lib



* Fixed BLE lib



* Major WiFi overhaul



- auto reconnect on connection loss now works

- moved to event groups

- some code clean up and procedure optimizations

- new methods to get a more elaborate system ststus



* Add cmake tests to travis



* Add initial AsyncUDP



* Add NetBIOS lib and fix CMake includes



* Add Initial WebServer



* Fix WebServer and examples



* travis not quiting on build fail



* Try different travis build



* Update IDF to aaf1239



* Fix WPS Example



* fix script permission and add some fail tests to sketch builder



* Add missing space in WiFiClient::write(Stream &stream)
### Antipattern Category

### Keyword
memory
### Note


## Commit #7
### Hash
[28a410dd503c2ae0f5bb82d471097b9abafe2e90](https://github.com/espressif/arduino-esp32commit/28a410dd503c2ae0f5bb82d471097b9abafe2e90)

### Message
Spurious Interrupts Temporary fix 20180711 (#1625)

the 'eject' ERROR is and indication of an interrupt triggering without an source.  I am working to eliminate these serviceable interrupt.  This update increase stability on a HelTek Wifi Lora 32 board. with a SSD1306 OLED.  This update fixes a glaring error in the interrupt allocation code, the Interrupt mask was wrong.  I also dynamically adjust the FiFo thresholds based on Bus clockrate. The change to FiFo thresholds has reduced the number for 'eject' events.  I also change 'eject' from and ERROR to DEBUG.  An 'eject' event does not compromise i2c transmissions. It happens after a transaction has completed. 



Chuck.
### Antipattern Category

### Keyword
increase
### Note


## Commit #8
### Hash
[8d7fb58672c3e506660268de4a69759a36d1cceb](https://github.com/espressif/arduino-esp32commit/8d7fb58672c3e506660268de4a69759a36d1cceb)

### Message
Fix for spurious interrupts during I2C communications (#1665)

This version no longer needs an interrupt for each byte transferred. It only needs interrupts for START, STOP, FIFO empty/Full or error conditions.  This dramatically reduces the interrupt overhead.  I think the prior version was causing an interrupt overload condition where the ISR was not able to process every interrupt as they happened.
### Antipattern Category

### Keyword
overhead
### Note


## Commit #9
### Hash
[328523f5e3289de193e04aaf4bf13f9672078fd6](https://github.com/espressif/arduino-esp32commit/328523f5e3289de193e04aaf4bf13f9672078fd6)

### Message
Memory leak (#1672)

When a package of size 0 arrives, "buf" is created, but never released. (Sorry, that was my mistake in the last patch)
### Antipattern Category

### Keyword
memory
### Note


## Commit #10
### Hash
[80c110ece70b179ddfe686e8ee45b6c808779454](https://github.com/espressif/arduino-esp32commit/80c110ece70b179ddfe686e8ee45b6c808779454)

### Message
Add more methods to access memory properties
### Antipattern Category

### Keyword
memory
### Note


## Commit #11
### Hash
[a0f0bd930cfd2d607bf3d3288f46e2d265dd2e11](https://github.com/espressif/arduino-esp32commit/a0f0bd930cfd2d607bf3d3288f46e2d265dd2e11)

### Message
Fix BTserial memory leaks (#1801)

- Delete queue at end

- Close BT connection before end

- DeInit SPP
### Antipattern Category

### Keyword
memory
### Note


## Commit #12
### Hash
[b37f4069e481b9c8ce0d18a107eb9a99374f82a5](https://github.com/espressif/arduino-esp32commit/b37f4069e481b9c8ce0d18a107eb9a99374f82a5)

### Message
Increase _network_event_task priority (#2184)

Fixes https://github.com/espressif/arduino-esp32/issues/1595
### Antipattern Category

### Keyword
increase
### Note


## Commit #13
### Hash
[c827bb4177702ce202ca3c966f3ce7564444df5b](https://github.com/espressif/arduino-esp32commit/c827bb4177702ce202ca3c966f3ce7564444df5b)

### Message
CPU and APB Frequency support (#2220)

* Add support to HAL for APB frequencies different than 80MHz



* Add support for CPU frequencies in the IDE board menu



* Switch to fast set_config



* Add method to uart so debug can be reassigned after apb frequency switch



* Return real APB frequency
### Antipattern Category

### Keyword
fast
### Note


## Commit #14
### Hash
[229d9b7366deee0d8a90fb69c19119f7287c9d1d](https://github.com/espressif/arduino-esp32commit/229d9b7366deee0d8a90fb69c19119f7287c9d1d)

### Message
[WiFiClientSecure] Shows only free internal heap on logs (#2252)

* Shows only free internal heap on logs



Since Mbedtls is running only on internal heap, show internal + PSRAM available memory on logs can confuse the users



* Clarify logs
### Antipattern Category

### Keyword
memory
### Note


## Commit #15
### Hash
[9a7946e6859130146e56231c27a4aa177d9175a1](https://github.com/espressif/arduino-esp32commit/9a7946e6859130146e56231c27a4aa177d9175a1)

### Message
I2C fix READ of zero bytes hardware hang (#2301)

The i2c peripheral will hang if a READ request is issued with a zero data length.  The peripheral

drops into a continuous timeout interrupt response.  The STOP command can not be set out to the I2C

bus. The SLAVE device correctly ACK'd the address byte, with READ bit set, it has control of the SDA

 pin.  The ESP32 send out the next SCL HIGH pulse but, since the SLAVE is in READ Mode, and the First

bit it is sending happened to be a ZERO, the ESP32 cannot send the STOP.  When it releases SDA during

the SCL HIGH, the pin does not change state.  The pin stays low because the SLAVE is outputing a LOW!

The ESP32 drops into a perminent WAIT state waiting for SDA to go HIGH (the STOP).



**esp32-hal-i2c.c**

* add databuff length checks to `i2cRead()` and `i2cWrite()`
### Antipattern Category

### Keyword
hang
### Note


## Commit #16
### Hash
[a87b2ec69054ce43a48bd042599b4185267ebc1d](https://github.com/espressif/arduino-esp32commit/a87b2ec69054ce43a48bd042599b4185267ebc1d)

### Message
Fix AsyncUDP receive memory leak (#2607)

If _handler is set, pbuf_free is not called. ~AsyncUDPPacket() calls pbuf_free once but only after calling pbuf_ref in it's constructor. The refcount never reaches zero and the memory allocated for pbuf is never released.
### Antipattern Category

### Keyword
memory
### Note


## Commit #17
### Hash
[619568db5bcc219091c653a5ced5e378b3a5643b](https://github.com/espressif/arduino-esp32commit/619568db5bcc219091c653a5ced5e378b3a5643b)

### Message
Converted EEPROM library to use nvs instead of partition.   (#2678)

* Converted EEPROM library to use nvs instead of partition.  Removed eeprom partition from all partition table CSV files.

* Changed variable names, added some comments, formatting as per me-no-dev's requests

* Checks for memory on malloc

* Moved include nvs.h from header to code

* Reworked the extra example to make it more clear how to actually use the library and persist data
### Antipattern Category

### Keyword
memory
### Note


## Commit #18
### Hash
[ab309e40d5f7a593f36f456976973ed7589a1f04](https://github.com/espressif/arduino-esp32commit/ab309e40d5f7a593f36f456976973ed7589a1f04)

### Message
Copy ESP8266 String w/SSO to ESP32 repo (#2715)

I redid the ESP8266 WString library to enable small string optimization

(SSO) a while back, and think it would be helpful even on the ESP32 with

its higher memory complement.



SSO avoids lots of tiny mallocs() on the heap which cause fragmentation

by using the memory in the class object itself to store the actual

string and only mallocing() for buffers that are larger than what can

fit in thie class object.  Modern C++ std::string implementations have

this optimization as well, but since we're using Arduino strings we had

to roll our own.
### Antipattern Category

### Keyword
memory
### Note


## Commit #19
### Hash
[e1548e9b7e0b6e519a7f59052817152bfb16ab59](https://github.com/espressif/arduino-esp32commit/e1548e9b7e0b6e519a7f59052817152bfb16ab59)

### Message
Fix hang on client disconnect during upload (#2914)
### Antipattern Category

### Keyword
hang
### Note


## Commit #20
### Hash
[390da0d09080ac6689a6337f0085f4cd2dc3ffb9](https://github.com/espressif/arduino-esp32commit/390da0d09080ac6689a6337f0085f4cd2dc3ffb9)

### Message
bump CONFIG_ESP32_WIFI_STATIC_RX_BUFFER_NUM to improve RX performance (#3119)
### Antipattern Category

### Keyword
performance
### Note


## Commit #21
### Hash
[b3ba80d57036aa57469653d23cab7cc9029d2ff2](https://github.com/espressif/arduino-esp32commit/b3ba80d57036aa57469653d23cab7cc9029d2ff2)

### Message
nvs_handle is an int, was assigning NULL.  Also cleaned up end to ensure no memory leak. (#3246)
### Antipattern Category

### Keyword
memory
### Note


## Commit #22
### Hash
[5bff89f0be51da3a6306a342e75517f861ba61c9](https://github.com/espressif/arduino-esp32commit/5bff89f0be51da3a6306a342e75517f861ba61c9)

### Message
Fixed issue-3153 - Allocating enough memory to construct the entire UUID as a String. (#3297)
### Antipattern Category

### Keyword
memory
### Note


## Commit #23
### Hash
[38c4c0610846b7193e908b474e2c8db06ae981ba](https://github.com/espressif/arduino-esp32commit/38c4c0610846b7193e908b474e2c8db06ae981ba)

### Message
Support for Master mode, Pin and SSP (#3219)

* 20190916 - initial: support for Master mode, Pin and SSP



* 20190916 - initial: Add example app for Master mode



* 20190916 - initial: Force another build



* 20190916 - connect would use resolved address as preference and remove now redundant _remote_address



* 20190916 - rework set/reset/default pin logic



* 20190916 - cleanup: remove static vars, add/use constants, fix typos



* 20190916 - fix build issues and implement geoup events for status verification.



* 20190916 - remove extra lines,misc



* 20190916 - rework ESP_BT_GAP_DISC_RES_EVT, added SPP_DISCONNECTED bit for disconnect event. + timeout for disconnect()



* 20190916 - Small log change to improve log sequencing



* 20190916 - remove static from local vars



* 20190916 - Limited scope and duration for the scan, log device address during scan in info mode as it is very difficult to find out sometimes. Fixed get_name_from_eir() not resetting the name when called.



* 20190916 - break property for loop during scan when name matches.



* 20190916 - misc



* 20190916 - SPP_DISCONNECT state updates



* 20190916 - formatting, remove some strange syntax from initiator code



* 20190916 - Add comments to the example about connect(...) usage and timeouts



* 20190916 - fix disconnect() without timeout



* 20190916 - Add example comment to view BT address and name during connect(name)



* 20190916 - wording in example comments



* 20190916 - rework connect() and disconnect() methods to help with concurrency and more authoritative status returned back to caller. Automatic disconnect in connect() methods



* 20190916 - optimize code



* 20190916 - optimize code - more



* 20190916 - add timeout for pin set



* 20190916 - change scan mode to ESP_BT_SCAN_MODE_CONNECTABLE_DISCOVERABLE



* 20190916 - update example code slightly



* 20190916 - increase READY_TIMEOUT to 10 secs



* 20190916 - typo in example and move waitForConnect() to static area



* 20190916 - update example comments



* 20190916 - update example comments



* 20190916 - update example comments



* 20190916 - add new example to remove paired devices from ESP32



* 20190916 - correct typo in example



* 20190916 - update example comment, add remove_bond_device() method for convenience.



* 20190916 - reword example comment.



* 20190916 - rename remove_bond_device()



* 20190916 - rename removePairedDevice() to unpairDevice()



* 20190916 - code review changes



* 20190916 - fix return value in setup() od example
### Antipattern Category

### Keyword
increase
### Note


## Commit #24
### Hash
[cec3fca4ad4a39feb463f9298ab3238819732d50](https://github.com/espressif/arduino-esp32commit/cec3fca4ad4a39feb463f9298ab3238819732d50)

### Message
Fix BluetoothSerial crash when restart (#3471)

* Update esp32-hal-bt.c



BluetoothSerial crash when restart:  this is because the BT controller remains in state  ESP_BT_CONTROLLER_STATUS_INITED instead of state  ESP_BT_CONTROLLER_STATUS_IDLE after the end() method.

in file esp_bt.h it is specified



> @brief Enable BT controller.

>                Due to a known issue, you cannot call esp_bt_controller_enable() a second time

>                 to change the controller mode dynamically. To change controller mode, call

>                esp_bt_controller_disable() and then call esp_bt_controller_enable() with the new mode.



after **esp_bt_controller_disable()** the controller remains in state INITED so we do call the **esp_bt_controller_deinit()** function to put the controller into state IDLE.



i have modified the **esp32-hal-bt.c** file

line 57 and next

(i have insert the esp_bt_controller_deinit() function so the controller go into Idle state)

```c++

bool btStop(){

    if(esp_bt_controller_get_status() == ESP_BT_CONTROLLER_STATUS_IDLE){

		log_i("bt stopped");

        return true;

    }

    if(esp_bt_controller_get_status() == ESP_BT_CONTROLLER_STATUS_ENABLED){

		log_i("bt enabled");

        if (esp_bt_controller_disable()) {

            log_e("BT Disable failed");

            return false;

        }

        while(esp_bt_controller_get_status() == ESP_BT_CONTROLLER_STATUS_ENABLED);

    }

    if(esp_bt_controller_get_status() == ESP_BT_CONTROLLER_STATUS_INITED){

		log_i("inited");

		if (esp_bt_controller_deinit()) {

			log_e("BT deint failed");

			return false;

		}

		while (esp_bt_controller_get_status() == ESP_BT_CONTROLLER_STATUS_INITED);

        return true;

    }

    log_e("BT Stop failed");

    return false;

}

```



* Update esp32-hal-bt.c



remove while to avoid infinite loop
### Antipattern Category

### Keyword
infinite
### Note


## Commit #25
### Hash
[9ad860758cedfa5d2fa7d7c7ba0870e91f7d5fec](https://github.com/espressif/arduino-esp32commit/9ad860758cedfa5d2fa7d7c7ba0870e91f7d5fec)

### Message
Fix Memory leak in addApbChangeCallback()  (#3560)

* `ledcWriteTone()` added a `apbcallback()` evertime the tone value was non zero.  

* `addApbChangeCallback()` did not detect duplicate callbacks.

* changed the apbcallback list to a double link to support roll forward, roll back execution.  This made the sequences of clock change callback start with the newest registered -> to oldest on the `before` then oldest -> newest after the clock change.  This made the UART debug log output have minimal gibberish during the clock change.

* change how the UART callback handled the MUTEX because if any `apbchangeCallback()` executed a `log_x()` a deadlock would occur.



This fixes #3555
### Antipattern Category

### Keyword
memory
### Note


## Commit #26
### Hash
[89351e3ade9a62edd891e363de08c124395dc0ad](https://github.com/espressif/arduino-esp32commit/89351e3ade9a62edd891e363de08c124395dc0ad)

### Message
Update WiFiClient.cpp (#3608)

fixed the connected() function so that it only checks errno if recv returns a value of -1.



"in the even of an error, errno is set to indicate the error" --manpage



This fixes the ESP32 Webserver when dealing with a modern webserver with a slow SD card.
### Antipattern Category

### Keyword
slow
### Note


## Commit #27
### Hash
[32d5654aa66f52054d500501decf3f0d281021f6](https://github.com/espressif/arduino-esp32commit/32d5654aa66f52054d500501decf3f0d281021f6)

### Message
Implement rmtLoop to be able to continuously send pulses (#3650)

Number of pulses is limited to the reserved RMT memory for the channel. Very useful for PWM, Servo and other repeatable signals.
### Antipattern Category

### Keyword
memory
### Note


## Commit #28
### Hash
[80f9f9aeec393ec29b343cee111528f2c026f8c4](https://github.com/espressif/arduino-esp32commit/80f9f9aeec393ec29b343cee111528f2c026f8c4)

### Message
fix removeApbChangeCallback() error in spiStopBus() (#3675)

* fix removeApbChangeCallback() error in spiStopBus()



spiStartBus() was using spiStopBus() to init the hardware, one of spiStopBus() functions is to unregister the runtime CPU clock speed change callback. But, spiStartBus() only wanted to init the hardware.  This patch separates the hardware init into a standalone function spiInitBus() that both spiStartBus() and spiStopBus() call.



* Update esp32-hal-spi.c



capitalization problem
### Antipattern Category

### Keyword
runtime
### Note


## Commit #29
### Hash
[b2c678877c04428f06ec5f1f59cc4d204bcd05ec](https://github.com/espressif/arduino-esp32commit/b2c678877c04428f06ec5f1f59cc4d204bcd05ec)

### Message
std::shared_ptr Memory Leak (#3680)

* std::shared_ptr Memory Leak



clientSocketHande and _rxBuffer are std::shared_ptr, the stop() call was not correctly releasing them and the operator= had similar problems fix for #3679



* operator= second attempt



* operator= third time
### Antipattern Category

### Keyword
memory
### Note


## Commit #30
### Hash
[109ba7a3b44cf0d89068aa0ec812271d3bc4acbc](https://github.com/espressif/arduino-esp32commit/109ba7a3b44cf0d89068aa0ec812271d3bc4acbc)

### Message
Revert "std::shared_ptr Memory Leak (#3680)" (#3682)

This reverts commit b2c678877c04428f06ec5f1f59cc4d204bcd05ec.
### Antipattern Category

### Keyword
memory
### Note


## Commit #31
### Hash
[ab23e8a65678d62323e023f4b9069378a3053bd2](https://github.com/espressif/arduino-esp32commit/ab23e8a65678d62323e023f4b9069378a3053bd2)

### Message
Greatly reduces error rate (half, or 0 zero errors, depends on in/out ranges) for round-trip mapping at the same performance. (#3655)

(Based on "improved_map" from ESP8266's Servo.cpp)
### Antipattern Category

### Keyword
performance
### Note


## Commit #32
### Hash
[e4b2ce4e8149f4afe823e870378b25ca2049a54b](https://github.com/espressif/arduino-esp32commit/e4b2ce4e8149f4afe823e870378b25ca2049a54b)

### Message
DNS resolving timeout change to prevent stack overlapping (#3731)

Real DNS resolving timeout used by lwip library is 14[s] (7[s] for DNS1 + 7[s] for DNS2). Function WiFiGenericClass::hostByName() has timeout set to lower value (only 4[s]), so callback function may be called after this low timeout and it may overlappe stack memory used now by other function.

Fixes #3722
### Antipattern Category

### Keyword
memory
### Note


## Commit #33
### Hash
[c917ed25049714a6761a8cb5e16a1fb869e88507](https://github.com/espressif/arduino-esp32commit/c917ed25049714a6761a8cb5e16a1fb869e88507)

### Message
shallow clone to make installation faster (#4246)

shallow clone (board and submodules) to make installation faster
### Antipattern Category

### Keyword
faster
### Note


## Commit #34
### Hash
[dccb4e8608a580cd9d27a29da85fa36c316482e2](https://github.com/espressif/arduino-esp32commit/dccb4e8608a580cd9d27a29da85fa36c316482e2)

### Message
improve & fix BLEScan when wantDuplicates (#3995)

* improve & fix BLEScan when too many BLE devices

- when wantDuplicates, no need to check duplicate and no more insert into vector

- delete advertisedDevice when not insert into vector, fix memory leak

- add showParse when you just want raw advertised data
### Antipattern Category

### Keyword
memory
### Note


## Commit #35
### Hash
[e4b008e712101f0e0cb3301b4bc80e23fa31dae2](https://github.com/espressif/arduino-esp32commit/e4b008e712101f0e0cb3301b4bc80e23fa31dae2)

### Message
Handle stream timeouts properly, for slow HTTP/HTTPS links (#3752)

This patch fixes update timeouts (error #6) on slow HTTP/HTTPS links.
### Antipattern Category

### Keyword
slow
### Note


## Commit #36
### Hash
[c6a8da61f78452573df857cb95edb3a5ecd0365f](https://github.com/espressif/arduino-esp32commit/c6a8da61f78452573df857cb95edb3a5ecd0365f)

### Message
Allow faster reuse of socket, to be able to restart WifiServer. (#4306)

See #3960 for more details of the problem and the solution. I only implemented what was proposed in this ticket, as it solves my problem, which was the same as in this ticket. Credits for the code going to @etrinh ;-)



This also is a more consistence behaviour compared to esp8266, where it also is possible to restart the wifiserver immediately on the same port.
### Antipattern Category

### Keyword
faster
### Note


## Commit #37
### Hash
[7e8993fc838db37f4d47c7836c002f60ff73d39a](https://github.com/espressif/arduino-esp32commit/7e8993fc838db37f4d47c7836c002f60ff73d39a)

### Message
Speed up upload by a factor of 17 (#4787)

* Speed up upload by a factor of 17



Uploads are very slow because of an unnecessary "client.connected()" check in _uploadReadByte().



Here is what happens:

client.connected() is called for every byte read.  WiFiClient::connected() calls recv(fd(), &dummy, 0, MSG_DONTWAIT); which takes a relatively long time, so the optimized path of returning a buffered byte via client.read() is effectively nullified.



Removing the one line changed the upload speed for a 2 MB file (discarding the received data) from 22 KB/sec (before) to 367 KB/sec (after).



The change is safe in the face of disconnects because client.read(), when it no longer has buffered data, calls (WiFiClient)  fillBuffer(), which calls recv(), so the disconnection will be detected in due course.



* Move disconnect check into the timeout loop
### Antipattern Category

### Keyword
slow
### Note


## Commit #38
### Hash
[e831680a41d4c96769cae7277501ce41abe69eee](https://github.com/espressif/arduino-esp32commit/e831680a41d4c96769cae7277501ce41abe69eee)

### Message
Fixed a memory leak in BLE (issue #4753) (#4761)

* Fixed crash on delete after disconnect



* Fixed memory leak when getting characteristics



* Removed guard



Co-authored-by: ushiboy <ushiboy.dev@gmail.com>
### Antipattern Category

### Keyword
memory
### Note


## Commit #39
### Hash
[8134a42162f11cb01155038a2465848d6b2b84bc](https://github.com/espressif/arduino-esp32commit/8134a42162f11cb01155038a2465848d6b2b84bc)

### Message
Fix leak of memory and possible crashes in AsyncUDP
### Antipattern Category

### Keyword
memory
### Note


## Commit #40
### Hash
[560c0f45f58b907f0d699f65408b87fe54650854](https://github.com/espressif/arduino-esp32commit/560c0f45f58b907f0d699f65408b87fe54650854)

### Message
Fix dropped SSL connection when buffer gets full. (#4820)

mbedTLS requires repeated calls to mbedtls_ssl_write() whenever it returns MBEDTLS_ERR_SSL_WANT_READ or MBEDTLS_ERR_SSL_WANT_WRITE. this happens when the client sends data faster then the server or the connection can handle.
### Antipattern Category

### Keyword
faster
### Note


## Commit #41
### Hash
[dd834b3372d97193f3e82e923eb2f59d9c6da12d](https://github.com/espressif/arduino-esp32commit/dd834b3372d97193f3e82e923eb2f59d9c6da12d)

### Message
Ensure that String::setLen() is always after any memory operation

Since `String::setLen()` is now modifying the buffer, this change is required to ensure that the proper buffer is changed.
### Antipattern Category

### Keyword
memory
### Note


## Commit #42
### Hash
[9a0762ad2a3773ccf919631203aa24cd311109a0](https://github.com/espressif/arduino-esp32commit/9a0762ad2a3773ccf919631203aa24cd311109a0)

### Message
[BLE Client] Fix Deadlock when calling writeValue after registerForNotify

Fixes: https://github.com/espressif/arduino-esp32/issues/4952
### Antipattern Category

### Keyword
deadlock
### Note


## Commit #43
### Hash
[81b7c47203b7558cc634ab2b22f966aa4bbc9ce1](https://github.com/espressif/arduino-esp32commit/81b7c47203b7558cc634ab2b22f966aa4bbc9ce1)

### Message
Serial::end hang (#5047)

workaround for #5043. There is a timing issue with HardwareSerial::end. I'm not sure what is hung, but it should be possible to see this in jtag, as it does cause a reboot if you let it. The delay needs to be before you detach the device!?
### Antipattern Category

### Keyword
hang
### Note


