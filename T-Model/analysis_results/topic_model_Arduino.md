|Word 	 		| 	Topic		|
|---------------|---------------|
|cpu			|	12			|
|timer			|	12			|
|clock			|	12			|
|speed			|	12			|
|flash			|	8, 15		|
|memory			|	20			|
|wait			|	5			|
|timeout		|	3, 5, 10	|
|ram			|	6, 16		|
|heap			|	18, 19		|

cpu	8 commits
9a2ed274f394eb1d91db569b1cbd1b7b2da6b3c9 polledTimeout: add option to use CPU count instead of millis() (#5870)
6620ec6e3610e30639d1eae1b6a3f60e93c26f70 Set CPU frequency before running setup
ddb2343bc029f5a7659cfeed2dffaee7f62dc949 Initial support for CPU frequency selection

timer	9 commits
03f35e44f06e9798338ee0b41156203ee094aca0 Don't use timer for zero delay

clock	20 commits
19554e563cc260b78474432ee2bd5210a587ddf2 add higher I2C freqs for 160MHz core clock
2eea25873dbc2bc57aa9f6ff6f2c74f2eff855f2 fix SPI speed calculation @160Mhz Clock
27f45a205abfb9efb28df419bf85b00e71e1e6d8 SD:  - optimize SPI usage 148% write speed (24kB/s -> 37kB/s) and 127% read speed (121kB/s -> 155kB/s) at 8MHz  - add clock frequency as parameter for begin(csPin, frequency)  - SD @80MHz write: 84kB/s read: 231kB/s
d7a88c3ea388eb802109ea8c629f2c183d1c6ed9 use a function to calculate best match clock register for SPI

speed	21 commits
bc3daef76d4d14cfbacb465ff4bdc59f67db0de7 WIFI_RESUME improve speed and example (#7877)
8ffe1aa2e2727c015d299efe5c8aef71835787b1 Speed up writePattern() a bit more
659c33a114cccbe152d266c4464805eb0961eaa4 Set default WifInfo board speed to 160MHz
8847d7ab1af8e4572b4a2afe5fcc0443cf22b338 added ESPino to dox/boards.md and package_esp8266com_index.template.json. removed flash speed selection
2eea25873dbc2bc57aa9f6ff6f2c74f2eff855f2 fix SPI speed calculation @160Mhz Clock
27f45a205abfb9efb28df419bf85b00e71e1e6d8 SD:  - optimize SPI usage 148% write speed (24kB/s -> 37kB/s) and 127% read speed (121kB/s -> 155kB/s) at 8MHz  - add clock frequency as parameter for begin(csPin, frequency)  - SD @80MHz write: 84kB/s read: 231kB/s
070f2b3a14aebb164b20c1462b0f599a6c075702 many speed optimizations in Adafruit_ILI9341 lib (3x times faster)
dcc899a1b5db2b894f28ac3c417608a80b8394af some speed optimizations
8ce762db166c2a39c2bd8aa72d5765283382a446 increase SD Card SPI Speed
89fc25aed8184b317f6462e74ddee3bc18288605 Upload speed selection for ESP01

flash	76 commits
7c008e31bb60caf69be18e04c5b9efbc6a3e1c6d Flash size reduction for mime-type (#7312)
a49f0470963a5282d87a6fe662ba55b1ab308c2d - Move all Strings to flash and optimize String usage, saving 4-5 kB of RAM.
244dbd7713338a127be3f53ba2fa1c3915c3ba98 Add 20/26MHz Flash frequencies for slow/cheap flash chips on the Generic ESP board (#6552)
3d70f43277aea997f66c78c6e0495a3e71324683 cleanup/unify flash sector size define value (#5327)
de2a3821f6de7a3fc298a1b671a103ccc0671f61 lower lwip2 ram and flash footprint (by disabling old asserts)
1b932181bdc25de84408354230356a48a656e5f2 enable 8M and 16M flash sizes for generic board
f50a6c0a8afa2cd311f1098af189cc992ba89df3 Add support for 8 and 16 MB Flash (#2351)
4b9323d79bf8616db2a53a857ca431cadc876969 Fix boards Flash size; Explained about custom FLASH/SPIFFS
f57ab609ecc5a63ac23d2363db1916405bf56ab1 move flash size check to a function in ESP class, allow real size bigger the IDE for Update
8847d7ab1af8e4572b4a2afe5fcc0443cf22b338 added ESPino to dox/boards.md and package_esp8266com_index.template.json. removed flash speed selection
ba65783177ac8ca9be3c8b93a0c3cc7474b2f31e add method to get the actual size of the flash
540fdb0f8c6e73df2aec8bfba4b190d64cda32e0 add flash splits depending on the flash size
ae1b53cafb054aedc2ce24281939256bb844ff87 remove unused flash size
c5eb40e36d1af377e17909afc97fa5662a33fcd4 remove unused flash size
f611bba7a7ce96bf8783f603efc7491e91958b87 set correct flash size
5c915ff38578f71684967a62220912cd9347ed46 add Winbond flash chip Ids

memory	23 commits
79ea883fb3099e86030e69f867648dfabcd270b5 New flash writing method with offset/memory/size alignment handling (#7514)
12c71aa8995b481faf09ebcf21d7bbaf9309c588 memory housekeeping
Lot of commits not related to performance.

wait	9 commits
f382fc9d77a868fae7e6f467c994406a83e33367 Refactoring to PolledTimeout or optimistic_yield on the grounds that these are not wait loops on slow input.
453eb2d0642fd12a73327ee5e8cdad885b014aa6 Add wait loop at the end of mode, refactor can_yield (#6721)
ace974aede0489b70d9292f84b4dd05f736b56f1 let's not wait 
93f215cb2e123294cdfc1e12a3a20dafdd128a3f add wait time after reset
5b5deb5a7784702b0c71a5bea1cfa15bac9b7256 improve os_printf handling when buffer full.  - wait for free buffer in hw fifo

timeout	27 commits
16312949c976629db948b1daa635948064cfd037 Add timeout to STA::waitForConnectResult (#5371)
dc03293d82e5eb8f37b269aa09f54035f25cd8e8 (re)introduce timeout in HardwareSerial::readBytes(buffer, size) (#5558)
38fe6fc488d5a4b1a99f1694fa20f66123a830fe Add timeout to WiFi connection loop in WiFiMulti (#4146)
89e5a481a7edbd07040483ebc7d058cfb8ffb066 increase HTTP SEND/POST timeout to 5s (#3971)
684b5f16294cc9fa99c9e83adc5225280d1282d0 WiFiClient: set default timeout to 5000ms for compatibility
81859c5df63549e39b3840713e76596ab523fdec Changed timeout logic
cc0037682bc4d94391ea51eb629a5b4087377123 add CHUNKED encoding support too http client (#1324) HTTP Client - fix examples increase default timeout to 5000ms
80857e3f8795d2a0f65c4a1655a03d9b1ee6a53d Also set timeout on already existing connections
d1a6b32133f281b64d84d194a30546b7a4069563 Allow setting TCP timeout
03a2b4808b240ac4b7825857dc74f3d31b0c3fdb add 10 seconds timeout for waiting on ESP to start the update

ram	21 commits
false positive

heap	17 commits
false positive

      Topic 1            Topic 2     Topic 3         Topic 4      Topic 5      Topic 6         Topic 7         Topic 8   Topic 9        Topic 10              Topic 11    Topic 12   
 [1,] "esp"              "remove"    "lwip"          "server"     "debug"      "request"       "library"       "flash"   "remove"       "request"             "host"      "write"    
 [2,] "remotetracking"   "request"   "fixes"         "mdns"       "error"      "exception"     "return"        "size"    "buffer"       "espesp"              "emulation" "change"   
 [3,] "remotesespmaster" "typo"      "functions"     "progmem"    "disable"    "udp"           "link"          "board"   "typo"         "linksmaster"         "missing"   "spiffs"   
 [4,] "espmaster"        "string"    "client"        "support"    "improve"    "spi"           "rename"        "boards"  "default"      "linksesp"            "support"   "speed"    
 [5,] "remotesespesp"    "function"  "gcc"           "method"     "output"     "stream"        "update"        "menu"    "stack"        "ficetoesp"           "include"   "clock"    
 [6,] "httpclient"       "clean"     "platformtxt"   "options"    "wifi"       "support"       "function"      "upload"  "bit"          "enable"              "python"    "read"     
 [7,] "ficetoesp"        "updates"   "prevent"       "revert"     "handling"   "implement"     "method"        "generic" "interrupt"    "krzychbmaster"       "minor"     "timer"    
 [8,] "remotesficetoesp" "python"    "git"           "strings"    "interrupts" "default"       "wifi"          "option"  "breaking"     "loop"                "ota"       "mode"     
 [9,] "included"         "api"       "documentation" "httpclient" "wificlient" "const"         "spi"           "script"  "espwebserver" "kb"                  "tests"     "servo"    
[10,] "spiffs"           "sdk"       "issue"         "wificlient" "option"     "reset"         "type"          "fs"      "changed"      "remove"              "patch"     "cpu"      
[11,] "arduinoota"       "functions" "ssl"           "port"       "revert"     "crash"         "static"        "remove"  "versions"     "timeout"             "ap"        "path"     
[12,] "wstring"          "reference" "correct"       "pio"        "save"       "mode"          "board"         "mode"    "ic"           "revert"              "link"      "parameter"
[13,] "tests"            "class"     "note"          "macro"      "httpclient" "examples"      "esphttpclient" "nodemcu" "wifi"         "espivankravetspatch" "variables" "generated"
[14,] "api"              "arduino"   "management"    "string"     "esp"        "ram"           "multiple"      "content" "bytes"        "style"               "functions" "release"  
[15,] "compilation"      "random"    "switch"        "deploy"     "list"       "menodevesp"    "bool"          "usage"   "send"         "update"              "size"      "macros"   
[16,] "avoid"            "info"      "class"         "names"      "wait"       "fatal"         "espmdns"       "ota"     "log"          "implementation"      "arduinoh"  "include"  
[17,] "custom"           "handler"   "timeout"       "char"       "timeout"    "hallardmaster" "pins"          "variant" "byte"         "optimisticyield"     "ipv"       "missed"   
[18,] "sdfat"            "fs"        "dev"           "post"       "typo"       "wstring"       "espwifi"       "serial"  "obsolete"     "sample"              "arg"       "spi"      
[19,] "setting"          "ota"       "bump"          "interface"  "enable"     "improve"       "public"        "disable" "arduino"      "linkshttpupdate"     "supported" "check"    
[20,] "deprecated"       "libraries" "callback"      "examples"   "setting"    "functions"     "issue"         "stack"   "dev"          "namespace"           "implement" "yield"    

      Topic 13         Topic 14            Topic 15     Topic 16           Topic 17      Topic 18           Topic 19        Topic 20          
 [1,] "support"        "release"           "update"     "update"           "update"      "master"           "check"         "update"          
 [2,] "string"         "espsoftwareserial" "bearssl"    "warning"          "sdk"         "platformio"       "typos"         "version"         
 [3,] "uart"           "warnings"          "toolchain"  "version"          "readmemd"    "core"             "request"       "headers"         
 [4,] "functions"      "fixes"             "arduino"    "littlefs"         "readme"      "wificlientsecure" "definitions"   "check"           
 [5,] "hardwareserial" "iram"              "axtls"      "documentation"    "change"      "wifi"             "updater"       "memory"          
 [6,] "missing"        "minor"             "ssid"       "support"          "option"      "macro"            "spiffs"        "compatibility"   
 [7,] "adding"         "sketch"            "avoid"      "sntp"             "method"      "wifimeshupdate"   "class"         "mdns"            
 [8,] "version"        "files"             "lwip"       "wificlientsecure" "config"      "implement"        "update"        "rtc"             
 [9,] "access"         "library"           "header"     "links"            "libs"        "address"          "files"         "send"            
[10,] "mode"           "printf"            "flash"      "type"             "function"    "block"            "missing"       "minor"           
[11,] "webserver"      "ota"               "makefile"   "spiffs"           "issue"       "heap"             "updated"       "message"         
[12,] "header"         "process"           "python"     "ram"              "rework"      "certificate"      "boardstxt"     "core"            
[13,] "rx"             "include"           "libraries"  "pgmspace"         "mention"     "files"            "documentation" "mode"            
[14,] "script"         "boot"              "core"       "remove"           "master"      "lwip"             "heap"          "enabled"         
[15,] "current"        "softwareserial"    "readmemd"   "dhcp"             "version"     "espwebserver"     "axtls"         "frequency"       
[16,] "scheduled"      "format"            "travis"     "method"           "wifi"        "headers"          "errors"        "unused"          
[17,] "fixes"          "argument"          "comment"    "implementation"   "package"     "remove"           "eboot"         "ivankravetspatch"
[18,] "gpio"           "reset"             "connection" "function"         "esptool"     "ic"               "readmemd"      "control"         
[19,] "eeprom"         "clean"             "json"       "json"             "platform"    "logic"            "path"          "valid"           
[20,] "reference"      "object"            "issue"      "return"           "librariesmd" "properly"         "replace"       "esptool"         
> 