# openpilot

## Result

usage (1)
9a78378b81a66b5ea6c5f0a9c211e24210233327 add timeout on procLog socket for CPU usage test

## Words/Topics

|Word 	 		| 	Topic	|
|---------------|-----------|
|speed			|	2		|
|memory			|	7, 20	|
|usage	?		|	17		|
|cpu			|	17		|
|processes		|	19		|

speed	50 commits
Mainly UI speed options and vehicle speed.
False positive.

memory	31 commits
7e83d9a61849950dcd7a4db3cd8ab7e9668dda2d camerad: Out of bounds memory write (#23534)

usage	60 commits
9a78378b81a66b5ea6c5f0a9c211e24210233327 add timeout on procLog socket for CPU usage test
The word "timeout" might be more interesting.

cpu	65 commits
Lot of cpu usage tests. And CPU usage trackers.
776516d72b85c5cdf4f0c40992dcedb03d06638c Qt/spinner: reduce cpu usage from 12% to 9% (#21552)
b7f8c6ad03e70b9b73ef67238c7a5946b315483e qt/spinner: reduce CPU usage from 17% to 12% (#21495)

processes	9 commits
ec414e2eb1e27eac04582ffbdc88f8022bfb34cc set nice values for non RT processes (#20812)
68531b071cde6fa5856d9b68bed63ecb50e03c2a Reduce scheduler latency for realtime processes (#1638)

      Topic 1        Topic 2       Topic 3      Topic 4    Topic 5    Topic 6        Topic 7        Topic 8    Topic 9      Topic 10       Topic 11      Topic 12      Topic 13    
 [1,] "release"      "alert"       "fw"         "log"      "update"   "replay"       "tests"        "revert"   "update"     "honda"        "hyundai"     "check"       "script"    
 [2,] "notes"        "cleanup"     "missing"    "remove"   "readme"   "nav"          "car"          "fixes"    "increase"   "civic"        "fingerprint" "refactor"    "setup"     
 [3,] "update"       "speed"       "engine"     "time"     "agnos"    "process"      "mazda"        "support"  "timeout"    "toyota"       "car"         "controlsd"   "boardd"    
 [4,] "files"        "camera"      "toyota"     "model"    "readmemd" "route"        "boardd"       "tici"     "jenkins"    "bosch"        "port"        "params"      "reset"     
 [5,] "cleanup"      "startup"     "hybrid"     "params"   "neos"     "handle"       "disable"      "sound"    "scons"      "dbc"          "fw"          "cache"       "installer" 
 [6,] "model"        "alerts"      "versions"   "cleanup"  "values"   "segment"      "cruise"       "disable"  "ui"         "check"        "kia"         "network"     "function"  
 [7,] "longitudinal" "steer"       "lexus"      "nissan"   "manager"  "improvements" "cars"         "typo"     "typo"       "signal"       "sonata"      "git"         "install"   
 [8,] "ui"           "upload"      "corolla"    "error"    "static"   "athena"       "models"       "cleanup"  "releasesmd" "carstate"     "hybrid"      "remove"      "setting"   
 [9,] "replay"       "offroad"     "tss"        "training" "acados"   "pass"         "mode"         "soundd"   "avoid"      "longitudinal" "ev"          "type"        "debug"     
[10,] "fingerprint"  "button"      "rav"        "gps"      "sounds"   "const"        "memory"       "function" "param"      "gas"          "ioniq"       "fingerprint" "lateral"   
[11,] "genesis"      "adding"      "firmware"   "camerad"  "valid"    "map"          "improvements" "rename"   "return"     "controls"     "pacifica"    "limit"       "cleanup"   
[12,] "type"         "remove"      "rx"         "comma"    "increase" "ublox"        "simplify"     "cache"    "simplify"   "supported"    "hkg"         "class"       "locationd" 
[13,] "openpilot"    "crash"       "camry"      "sim"      "github"   "reference"    "unit"         "setup"    "info"       "pilot"        "santa"       "readme"      "priority"  
[14,] "variable"     "lag"         "version"    "rdx"      "clean"    "improve"      "unnecessary"  "updated"  "env"        "checks"       "niro"        "revert"      "path"      
[15,] "improved"     "malfunction" "highlander" "output"   "start"    "function"     "framereader"  "model"    "fp"         "qt"           "fe"          "settings"    "branches"  
[16,] "external"     "device"      "esp"        "android"  "remove"   "lib"          "remove"       "steering" "thneed"     "brake"        "elantra"     "interface"   "pipenv"    
[17,] "logic"        "faster"      "eps"        "neos"     "refactor" "cameraqcom"   "comment"      "alerts"   "pc"         "cleanup"      "support"     "display"     "wait"      
[18,] "enable"       "refactor"    "chr"        "loggerd"  "signals"  "support"      "tici"         "apk"      "ssh"        "pressed"      "kona"        "hardware"    "monitoring"
[19,] "accord"       "functions"   "prius"      "limit"    "valuespy" "lexus"        "capnp"        "lgtm"     "testing"    "common"       "bsm"         "log"         "acados"    
[20,] "palisade"     "networking"  "fwdcamera"  "bootlog"  "webcam"   "param"        "carstate"     "refactor" "clean"      "crv"          "correct"     "save"        "ssh"       

      Topic 14       Topic 15      Topic 16     Topic 17      Topic 18       Topic 19     Topic 20  
 [1,] "remove"       "vw"          "bump"       "usage"       "change"       "ui"         "tici"    
 [2,] "unused"       "mqb"         "panda"      "cpu"         "subaru"       "qt"         "loggerd" 
 [3,] "check"        "fw"          "cereal"     "locationd"   "model"        "onroad"     "frame"   
 [4,] "function"     "volkswagen"  "opendbc"    "revert"      "camerad"      "offroad"    "error"   
 [5,] "fingerprints" "golf"        "version"    "improve"     "longitudinal" "settings"   "pc"      
 [6,] "mpc"          "values"      "submodules" "reduce"      "support"      "cleanup"    "modeld"  
 [7,] "mode"         "support"     "laika"      "thermald"    "lane"         "close"      "default" 
 [8,] "update"       "plotjuggler" "fixups"     "script"      "toggle"       "wifi"       "status"  
 [9,] "support"      "škoda"       "refactor"   "paramsd"     "default"      "updated"    "path"    
[10,] "redundant"    "signal"      "pc"         "logging"     "match"        "screen"     "offset"  
[11,] "dashcam"      "network"     "openpilot"  "flag"        "panda"        "minor"      "params"  
[12,] "size"         "event"       "upload"     "replace"     "mac"          "processes"  "memory"  
[13,] "header"       "angle"       "encodeidx"  "offroad"     "stock"        "params"     "video"   
[14,] "buffer"       "tiguan"      "removed"    "abstraction" "detection"    "starting"   "warning" 
[15,] "variables"    "audi"        "current"    "duplicate"   "impreza"      "clip"       "rotation"
[16,] "fault"        "fpv"         "carla"      "brightness"  "include"      "multiple"   "camerad" 
[17,] "modem"        "timeout"     "rednose"    "athena"      "networking"   "onboarding" "fail"    
[18,] "logging"      "class"       "eta"        "device"      "ui"           "lines"      "alert"   
[19,] "community"    "capnp"       "update"     "tici"        "fixes"        "widget"     "lkas"    
[20,] "variable"     "cleanup"     "bounds"     "message"     "signals"      "fixup"      "qlog"    
> 