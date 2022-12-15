# AirSim

## Result

x

## Words/Topics

|Word 	 		| 	Topic	|
|---------------|-----------|
|time			|	8		|
|thread			|	7, 13	|

time	14 commits (17 hits)
5bb434435a8b505605b1159d636d20d6bbba2e84 - update time - update setParam
672a8350dc03de6a1b537d62557b0b2446762e57 Support for adding vehicles dynamically at run-time via RPC
589c708e0ca616a2abf026a1c5577342250a7912 Support for adding vehicles dynamically at run-time via RPC
918f4b511fb7ae47de3c6ef890e1e762e4cc9868 [linux] fixes to package blocks binary in linux [linux] make AirLib compile time lower by using all CPU cores
6aa642483dd3e47664bf6057be5e7d30f3bacda6 Removed a cast to float to fix a bug where the time delta was being calculated incorrectly.
1a7592cfc75f9f1715944f54a8c1c6ff91c00e75 rollback lookahead time out to 100
7c18f3548e1b025c29f8b174764993c7665c6619 use fixed ints instead of long, init time for physics body

thread	21 commits
Not many interesting commits.
0f3b9104f2629d8e4a850a728a7598a97c8c373f Fix bug in UDP socket failing with WSAECONNRESET in the read thread if it tries to read to soon.  The fix is to put a retry count in the UdpClientPort where it automatically reconnects up to 10 times.  Also fixed a null ref crash on mav_vehicle_ that happens in some cases like if you kill px4 process while drone is flying.
Line 2370: 05902c89726a7135af3b768d8d4260fd6bfcabf1 removed timeout for render thread

      Topic 1           Topic 2                               Topic 3        Topic 4                         Topic 5         Topic 6           Topic 7   
 [1,] "request"         "script"                              "update"       "master"                        "update"        "update"          "request" 
 [2,] "issue"           "updated"                             "check"        "httpsgithubcommicrosoftairsim" "request"       "multiple"        "apis"    
 [3,] "linux"           "httpsgithubcommicrosoftairsimissues" "version"      "link"                          "documentation" "drones"          "setting" 
 [4,] "functions"       "removed"                             "info"         "car"                           "ue"            "env"             "support" 
 [5,] "parameter"       "msg"                                 "readme"       "githubcommicrosoftairsim"      "linux"         "include"         "windows" 
 [6,] "position"        "version"                             "rpclib"       "scene"                         "commit"        "names"           "typo"    
 [7,] "microsoftmaster" "install"                             "view"         "remove"                        "detection"     "replace"         "thread"  
 [8,] "wrapper"         "pixhawk"                             "avoid"        "info"                          "logging"       "gcc"             "refactor"
 [9,] "commit"          "car"                                 "function"     "publish"                       "issues"        "feedback"        "type"    
[10,] "typo"            "remove"                              "messages"     "links"                         "python"        "camera"          "missing" 
[11,] "plugin"          "cmake"                               "method"       "unity"                         "car"           "print"           "rc"      
[12,] "details"         "ubuntu"                              "upgrade"      "simpleflight"                  "clean"         "version"         "const"   
[13,] "folder"          "dependencies"                        "simpleflight" "docstring"                     "libc"          "type"            "format"  
[14,] "bad"             "gazebodrone"                         "command"      "wrapper"                       "refactoring"   "ubuntu"          "folder"  
[15,] "windows"         "restore"                             "cmake"        "bugs"                          "model"         "laurelkeyspatch" "client"  
[16,] "format"          "position"                            "joystick"     "airsim"                        "zimmyfix"      "compilation"     "change"  
[17,] "macos"           "distortion"                          "wrapper"      "include"                       "remove"        "errors"          "existing"
[18,] "control"         "building"                            "imageapismd"  "broken"                        "plugin"        "custom"          "correct" 
[19,] "fixing"          "json"                                "revert"       "includes"                      "method"        "instructions"    "source"  
[20,] "hturkipatch"     "video"                               "object"       "lidar"                         "cmake"         "external"        "paper"   

      Topic 8                             Topic 9                               Topic 10                              Topic 11         Topic 12       Topic 13       Topic 14       
 [1,] "update"                            "request"                             "settings"                            "camera"         "px"           "typos"        "remove"       
 [2,] "minor"                             "microsoftjonymarinopatch"            "default"                             "rename"         "bugs"         "solve"        "ros"          
 [3,] "readmemd"                          "sensor"                              "httpsgithubcommicrosoftairsimissues" "upstreammaster" "mavlink"      "update"       "unity"        
 [4,] "httpsgithubcommicrosoftairsimpull" "unreal"                              "crash"                               "remotetracking" "support"      "info"         "missing"      
 [5,] "version"                           "httpsgithubcommicrosoftairsimissues" "params"                              "delete"         "scripts"      "mode"         "unused"       
 [6,] "pythonclient"                      "zimmyfix"                            "depthnav"                            "control"        "update"       "image"        "cleanup"      
 [7,] "support"                           "change"                              "vehicle"                             "setup"          "log"          "bugs"         "files"        
 [8,] "cleanup"                           "gcc"                                 "enable"                              "unreal"         "typo"         "unreal"       "airsim"       
 [9,] "distance"                          "refactor"                            "mode"                                "apis"           "connection"   "minor"        "boost"        
[10,] "lidar"                             "loop"                                "install"                             "request"        "sitl"         "refactoring"  "pythonclient" 
[11,] "review"                            "return"                              "release"                             "fixes"          "client"       "support"      "dependency"   
[12,] "time"                              "codingguidelinesmd"                  "multiple"                            "vehicles"       "simpleflight" "ue"           "updated"      
[13,] "sensor"                            "port"                                "minor"                               "disable"        "path"         "link"         "simpleflight" 
[14,] "coordinates"                       "issues"                              "constructor"                         "location"       "macos"        "changelogmd"  "issue"        
[15,] "methods"                           "win"                                 "logviewer"                           "compute"        "depth"        "recording"    "telemetry"    
[16,] "cmake"                             "reset"                               "commands"                            "drone"          "osx"          "thread"       "message"      
[17,] "object"                            "avoid"                               "class"                               "airsim"         "guidelines"   "apismd"       "unimplemented"
[18,] "apismd"                            "rename"                              "review"                              "standard"       "json"         "segmentation" "zimmyfix"     
[19,] "changed"                           "faq"                                 "setting"                             "link"           "vehicle"      "comments"     "methods"      
[20,] "worldsimapi"                       "detection"                           "unity"                               "plotting"       "style"        "position"     "cmake"        

      Topic 15   Topic 16       Topic 17                            Topic 18          Topic 19     Topic 20    
 [1,] "update"   "api"          "request"                           "fixes"           "files"      "clang"     
 [2,] "api"      "change"       "unity"                             "change"          "drone"      "compile"   
 [3,] "python"   "request"      "adding"                            "apply"           "function"   "error"     
 [4,] "vehicle"  "support"      "change"                            "clangformat"     "recording"  "linux"     
 [5,] "mode"     "segmentation" "image"                             "car"             "command"    "warnings"  
 [6,] "ue"       "record"       "environment"                       "style"           "tested"     "errors"    
 [7,] "reset"    "material"     "external"                          "changed"         "airsim"     "warning"   
 [8,] "create"   "issue"        "removed"                           "errors"          "switch"     "compiler"  
 [9,] "script"   "sensor"       "readme"                            "issues"          "unreal"     "mavlinkcom"
[10,] "image"    "engine"       "cleanup"                           "update"          "log"        "travis"    
[11,] "fixes"    "remove"       "script"                            "crash"           "parameters" "request"   
[12,] "messages" "update"       "usage"                             "microsoftmaster" "demo"       "cmake"     
[13,] "publish"  "removed"      "comments"                          "controls"        "depth"      "apis"      
[14,] "remove"   "texture"      "revert"                            "multirotor"      "updated"    "hil"       
[15,] "bugs"     "controller"   "gps"                               "naming"          "style"      "mode"      
[16,] "boxd"     "list"         "osx"                               "common"          "easier"     "delete"    
[17,] "joystick" "simplify"     "vectorr"                           "asset"           "projects"   "revert"    
[18,] "adding"   "sample"       "config"                            "socket"          "handling"   "type"      
[19,] "option"   "images"       "git"                               "udp"             "px"         "dependency"
[20,] "images"   "lidar"        "httpsgithubcommicrosoftairsimpull" "sitl"            "ability"    "llvm"      
> 