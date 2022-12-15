|Word 	 		| 	Topic			|
|---------------|-------------------|
|time			| 	3				|
|corrected		|	5, 11, 12, 15	|
|timeout		|	7, 8, 15		|
|calibration	|	2, 6, 7			|
|adjustments	|	8				|
|battery		|	7, 13, 14, 17	|

time	6 commits (9 hits)
f2b2a2fe4c9bdb5c33dbd8d7c03db1e6637607a8 add blade time status, to reset time tap on blade status entry
c45691dbbfeb71fe78945de10946f7c8ce038fd4 sim: corrected sim time
83b55ea619e7aad69f912392c6d49810e24fe55b adjusted station roll time, fixed checkbutton

corrected	35 commits
Lot of less interesting commits
0d7212a113a169b9b7895bb982087447a46efcdb Corrected roll heading for STATE_ROLL
c9aa7201a77dd0f9ecdf321cb44371bfc6855851 corrected BT default settings
17ad02960bb80d3aaeb142b7b063d766d204ae24 corrected odometry ticks for Ardumower motors
f3d351b824a6e63ea96f24b608ab05c667b1e8de corrected sender pinout comments
ae9616ce58d109e6f19a096a3d07eee09ce5a8d5 corrected serial output lines
4106f0d8b614b0e851dca579b65aeaa1dcaa0a7b corrected odometry code reflecting actual wiki signal logic
3e2273108d49b217e75c9bcb839069ded2e72648 corrected odometry pins for PCB
517a3d24516a69274fe1c0f1cbe71d694665db88 corrected footprint
8a8361cc56751d0a183b80a10809d6ca84a038e6 corrected parts
5367d68fe85f5bcaa6730f80f3a6a81546a0f325 corrected odometry rpm measurement, added pfodapp motor control plot
92031d7edd280b94c202a78afb0e7b14a06ca36f corrected R value
bff7040ffb14c7cbdeac556187f138fff51d7fa8 corrected GND
b11f1a5aec1d1d2750fca6bb9904be1d3df0dd5e corrected SMD footprints
d6fa2705ee31ab9c3ff647e13e4f4a8d39cc4ca2 corrected ina169 breakout schematics

(also time)
c45691dbbfeb71fe78945de10946f7c8ce038fd4 sim: corrected sim time

debba3e528d7322125c71613f0d17b410c6d8ed5 perimeter: corrected filter quality
1b86351472325dbd0374986aa60ccefb2c62d3c0 corrected sample rate (Due)
0467182288e150ebdb9b1512221b690c1f72df3b corrected sample rate
41d74905d26647f73eddbe7ca3cc247f889af432 sender: corrected volt-to-ampere conversion
03a9f9384b66425c1b5ad36c9ed0018d8e991812 corrected mow motor control, deactivated mow motor error handling
4772a77dd27684aa5a72aa5ea9b62b00c21008c4 corrected duplicate pin mapping
a515e527d3420bc8a75d72637fffeb50f2d93c58 corrected duplicate pin mapping
7076af2539a8d80eb720ee6927b0f9105e1c6bb5 added RPM for drive motors; corrected issue with ArduRemote on battery slider

timeout	12 commits
be8a466199b128acad2d46f09cca760d7954a523 freewheel implementation timeout change
21a08bee13f76fee448ab214915d841d8af9ef6b Update on POUTREV: ends on Perimeter Inside or Timeout
33c4ad1653e55963f362cdf0565dfb9e41e4d17d Perimeter sender turns off after robot not in charging station timeout (github #65)
2e3383758adbb36b2d5c05079afe4d165ce3a461 set trigger timeout to zero
5a80a4a3bee0b20fb3367d02c76e1ba3a1bd1524 fixed perimeter timeout bug
1dd97fdcc3ff242bc6d3bce4f02795888244e3a9 state "perimeter find": added timeout (like in forward state)
ccfef82f5456c4abdabad97989533c2efb4134a0 pfodApp: added smag timeout option
3159b5d090d0811880686f7d9a88676967be5940 perimeter v2: improved timeout detection
d240c4e704b563bed5aefa4e21497be32567be7c tuned perimeter outside timeout
646747b0d67f0163783c237482c8f6d7641a2ecc added perimeter trigger timeout
3341ce681339e254cd59bbda1bfd25e88879fd24 added perimeter trigger timeout
02076744bf596e12cb5130d4ace2cc9d448084b6 added perimeter trigger timeout

calibration	20 commits
fd2a2849484b4be59b0636589751f3c9268a3857 fix ADC calibration crash
a46da5dae28fc71ea764be89e3ef6809fb89068c sender calibration bugfix
e5ac8eb3068a9e84fcbe30761c69b892f120355a set error state on missing calibration data
c06f3f489407083af342d81c1f09d83dc40dbe2c error counters for missing calibration data (imu, adc)
696ca895eb53e482df5ae636e4983c5e8c195aaf adjusted battery calibration for PCB
0ad0797cab06cacdf98b18d2b3f2d780daf04a04 IMU: improved compass calibration
1b20ee9b0b55f6609e25c55e0c3602d2396843ec new variant for motor sense calibration; removed unused entries in config.h;
1cddc59889d941553c2279c5a828a57918b71f5d new variant for pfodapp battery calibration

adjustments	6 commits
vague commit messages (some only have one word)
85dc85c61d470ac58d56ab120f92847cd3366c26 sender: adjustments for PCB
8996f79e1029c38215369b983cb6ef2627c80224 added velocity control for drive motors(speed is now set in rpm);some minor adjustments;

battery	34 commits
SOme vague commits messages.
77658f802ebf3536e86bab90b358cb7be5184083 change battery handling when mower is in station and beginn the charge sequenze
87d6b6886584d51c55a6ed6e1b796f0ffe3bdfdc original default battery values
d41c865afa2f3be7ab21d894309b6a4078c9b8ed battery default values calculations
696ca895eb53e482df5ae636e4983c5e8c195aaf adjusted battery calibration for PCB
7076af2539a8d80eb720ee6927b0f9105e1c6bb5 added RPM for drive motors; corrected issue with ArduRemote on battery slider


      Topic 1                    Topic 2                  Topic 3          Topic 4                  Topic 5     Topic 6          Topic 7                 
 [1,] "removed"                  "megashieldsvngeoeffnet" "perimeter"      "sim"                    "sender"    "rmcs"           "megashieldsvngeoeffnet"
 [2,] "improved"                 "imu"                    "tracking"       "improved"               "version"   "config"         "perimeter"             
 [3,] "switch"                   "motor"                  "mower"          "esp"                    "perimeter" "platine"        "ic"                    
 [4,] "imu"                      "adc"                    "values"         "sonar"                  "corrected" "request"        "mega"                  
 [5,] "pin"                      "calibration"            "adjusted"       "perimeter"              "charging"  "calibration"    "eeprom"                
 [6,] "megashieldsvngeschlossen" "issue"                  "files"          "pcb"                    "comment"   "sim"            "improved"              
 [7,] "adjusted"                 "request"                "pid"            "pfod"                   "signal"    "motor"          "schematics"            
 [8,] "kicad"                    "perimeter"              "time"           "sensor"                 "adjusted"  "bugfix"         "compilation"           
 [9,] "control"                  "ln"                     "station"        "odometry"               "missing"   "mower"          "default"               
[10,] "start"                    "pid"                    "relevant"       "calculation"            "pid"       "adjusted"       "correction"            
[11,] "default"                  "updated"                "fifo"           "class"                  "filter"    "signal"         "calibration"           
[12,] "dip"                      "cleanup"                "charge"         "behavior"               "optimized" "adcman"         "battery"               
[13,] "ardusatelino"             "variable"               "arduino"        "developer"              "regelung"  "update"         "warning"               
[14,] "dokumentation"            "mag"                    "correct"        "obstacle"               "reset"     "sensor"         "bugfix"                
[15,] "rpm"                      "angepasst"              "fixes"          "gps"                    "removed"   "mpu"            "missing"               
[16,] "change"                   "charging"               "fixme"          "median"                 "smooth"    "messages"       "timeout"               
[17,] "freewheel"                "current"                "note"           "megashieldsvngeoeffnet" "plot"      "releaseaazurit" "smooth"                
[18,] "ic"                       "minor"                  "mega"           "ros"                    "prototype" "enable"         "sample"                
[19,] "tracking"                 "app"                    "remotetracking" "params"                 "change"    "ardumower"      "ina"                   
[20,] "binary"                   "gelöscht"               "rc"             "app"                    "charge"    "handling"       "adcman"                

      Topic 8                                  Topic 9           Topic 10                 Topic 11          Topic 12                 Topic 13                                
 [1,] "console"                                "update"          "megashieldsvngeoeffnet" "pcb"             "odometry"               "pcb"                                   
 [2,] "output"                                 "readmemd"        "bugfix"                 "kicad"           "corrected"              "battery"                               
 [3,] "serial"                                 "minor"           "rssi"                   "perimeter"       "motor"                  "version"                               
 [4,] "filter"                                 "bugfix"          "arduino"                "changed"         "control"                "platine"                               
 [5,] "odometry"                               "settings"        "pin"                    "comments"        "ardumower"              "missing"                               
 [6,] "issue"                                  "filter"          "fixes"                  "comment"         "pid"                    "mini"                                  
 [7,] "changed"                                "motor"           "folder"                 "footprints"      "sample"                 "option"                                
 [8,] "port"                                   "change"          "configh"                "updated"         "bugfixes"               "ardumower"                             
 [9,] "timeout"                                "rmcs"            "meter"                  "ultrasonic"      "sender"                 "tests"                                 
[10,] "bugfixed"                               "station"         "ros"                    "option"          "workshop"               "stats"                                 
[11,] "reset"                                  "workaround"      "variables"              "corrected"       "megashieldsvngeoeffnet" "imu"                                   
[12,] "ros"                                    "check"           "unused"                 "bumperduino"     "menu"                   "updated"                               
[13,] "mini"                                   "default"         "holorattemaster"        "switch"          "values"                 "geschlossen"                           
[14,] "native"                                 "motors"          "pinout"                 "schleifensender" "error"                  "httpsgithubcomardumowerardumowerissues"
[15,] "errors"                                 "interrupt"       "conversion"             "footprint"       "trigger"                "sensor"                                
[16,] "adjustments"                            "aufbauanleitung" "files"                  "remove"          "pfodapp"                "factory"                               
[17,] "particle"                               "issue"           "handling"               "control"         "für"                    "konsole"                               
[18,] "warning"                                "values"          "compiler"               "events"          "status"                 "interrupt"                             
[19,] "megashieldsvngeoeffnetmachbarkeitstest" "gyro"            "dev"                    "ros"             "support"                "optimized"                             
[20,] "roll"                                   "license"         "console"                "improved"        "arduino"                "plot"                                  

      Topic 14                 Topic 15     Topic 16                           Topic 17       Topic 18                                 Topic 19                     Topic 20    
 [1,] "error"                  "updated"    "comments"                         "platine"      "pfodapp"                                "driver"                     "der"       
 [2,] "perimeter"              "changed"    "master"                           "und"          "ardumower"                              "moved"                      "den"       
 [3,] "battery"                "kicad"      "httpsgithubcomardumowerardumower" "hinzugefügt"  "megashieldsvngeoeffnet"                 "platine"                    "geändert"  
 [4,] "robot"                  "todo"       "develop"                          "für"          "eeprom"                                 "sim"                        "von"       
 [5,] "rtc"                    "bugfix"     "current"                          "auf"          "sensor"                                 "megashieldsvngeoeffnet"     "die"       
 [6,] "cleanup"                "rtc"        "imu"                              "umgeändert"   "missing"                                "adjusted"                   "fehler"    
 [7,] "display"                "ardumower"  "ardumower"                        "anschluss"    "sensors"                                "reset"                      "footprint" 
 [8,] "completed"              "behavior"   "megashieldsvngeschlossen"         "noch"         "minor"                                  "rc"                         "mit"       
 [9,] "gps"                    "floats"     "files"                            "werden"       "default"                                "revert"                     "und"       
[10,] "stucked"                "output"     "revert"                           "battery"      "ina"                                    "charging"                   "bei"       
[11,] "behavior"               "timeout"    "version"                          "diode"        "megashieldsvngeschlossen"               "aufbauanleitung"            "ordner"    
[12,] "untested"               "filter"     "angepasst"                        "der"          "comments"                               "mower"                      "noch"      
[13,] "detection"              "ultrasonic" "values"                           "leiterbahnen" "read"                                   "issue"                      "muss"      
[14,] "automatic"              "files"      "increased"                        "ic"           "unused"                                 "comments"                   "nicht"     
[15,] "stored"                 "master"     "simfpc"                           "aktualisiert" "remotetracking"                         "refsremotesardumowermaster" "zu"        
[16,] "pin"                    "charge"     "platine"                          "motor"        "updated"                                "activated"                  "ina"       
[17,] "controller"             "handling"   "factor"                           "pdf"          "config"                                 "options"                    "ist"       
[18,] "megashieldsvngeoeffnet" "issue"      "schaltplan"                       "wlan"         "bei"                                    "ideas"                      "änderungen"
[19,] "ardumowermaster"        "comments"   "inastromsensorvgeoeffnet"         "arduino"      "drvspinanoino"                          "files"                      "pid"       
[20,] "counter"                "corrected"  "bugfixes"                         "platz"        "megashieldsvnprototypinterngeschlossen" "update"                     "behoben"   
> 