|Word 	 		| 	Topic		|
|---------------|---------------|
|improved		|	8, 9, 12	|
|parameter		| 	9			|
|timer			|	10, 13, 20	|
|refactored		| 	15, 16, 17	|
|timing			|	4, 8, 11	|
|time			|	18			|

improved	13 commits
Commit messages don't have a good description, but might be interesting.
15a1fbc8d02fc610808f62494589d1cd2c4e2d93 Used IR_SEND_PIN to reduce code size and improved send timing for AVR.
94fa49a0f858c60b593d1437da59c873c6c3d547 Improved LG protocol and added class Aircondition_LG. Improved ir_DistanceProtocol.cpp to support more than 32 bits.
105e6fb695c8be3f2b67334baeaa7981e719e5c2 Fix send NEC 16 bit address bug. Improved SendDemo example for #760


parameter	3 commits
Interesting
4fb32a608c42727cc2d6d3529eafb229e70c437f disabled old results structure, added default receiver and sender objects, removed deprecated decoders with parameter,  added Stram like API with begin() -like Arduino Serial-, LED feedback now also for send
376301228aeabf18442edbe6392cec6977b1893d changed irsendraw parameter to const, #227

timer	8 commits
Interesting
8f665d60f065c139bf641a152518b078bec84437 Leonardo Support and Pinout/Timer cleanup, closes #694
6a1811e7e8559770d5eb9f5db0f6ff8168f57ce3 Leonardo Support and Pinout/Timer cleanup, closes #694
c2d25b4dd96563c3f38e5ca4f43ffc4715e38705 Added Sparkfun timer and pins information

refactored	6 commits
Interesting
1ce638b7f64cbb7abdf48fd41c87819ee252e0a8 RP2040 support added. - Refactored IRTimer.hpp. - Refactored IR_SEND_PIN and IrSender.sendPin handling. - Renamed IR_SEND_DUTY_CYCLE to IR_SEND_DUTY_CYCLE_PERCENT. - Fixed bugs for SEND_PWM_BY_TIMER active.
8deb5ea4e1f7eb253f47774f35229d29ca04db35 refactored board specific code
56bd4f587651a4797c58c49d28964a9483148781 refactored board specific code
babf91409fe0d212b3d10fa9669bebeda89284f5 refactored board specific code
a7c1c786e92b548cfda9d232a0f8846c7d7ecf80 Refactored receive state machine, RAW_BUFFER_LENGTH is now forced to be even; New function start(uint16_t aMillisToAddToGapCounter)

timing	6 commits
Interesting
3d1de339f3b771897a6ff3f7d158dbefbdf53ef7 Switched Bose internal protocol timing for 0 and 1 -> old 1 timing is now 0 and vice versa.
15a1fbc8d02fc610808f62494589d1cd2c4e2d93 Used IR_SEND_PIN to reduce code size and improved send timing for AVR.
85cd7fdd65d52601020dd0cb69d927e1530e7fd5 Adjusted JVC and LG timing, closes #347
d5d608c082280cae581ed15cbdddcdc9c07d3735 Samsung timing solved #705

time	2 commits
Interesting
27fa380bdabcffc1a24b532d8da7eb338ad8d184 Repeat detection gap time adjusted
88e243fe068e06d2ed602fefe6bd5effd07006e1 Broken the source in to manageable chunks - 2KLOC files are not fun to debug! Utterly failed to reduce the MARK_?? functions back down to MACROs - every time I try, the decoders start failing ...However, I have found a considerable number of bugs in the toolchain, so I'm starting to wonder if the fault is not mine.

   
      Topic 1          Topic 2         Topic 3         Topic 4                           Topic 5        Topic 6          Topic 7         Topic 8          Topic 9     Topic 10       
 [1,] "request"        "closes"        "renamed"       "support"                         "protocol"     "update"         "documentation" "request"        "send"      "atmega"       
 [2,] "version"        "protocol"      "documentation" "documentation"                   "api"          "esp"            "master"        "closes"         "lg"        "closes"       
 [3,] "tested"         "renamed"       "irremoteinth"  "readmemd"                        "updated"      "function"       "bumped"        "support"        "bit"       "support"      
 [4,] "function"       "lego"          "readme"        "formatting"                      "teensy"       "mark"           "update"        "documentation"  "changed"   "sendraw"      
 [5,] "moved"          "usecpertick"   "esp"           "timing"                          "frequency"    "method"         "template"      "improved"       "improved"  "changelog"    
 [6,] "standard"       "boarddefs"     "panasonic"     "platformio"                      "closes"       "modified"       "encoding"      "protocols"      "led"       "handling"     
 [7,] "change"         "bose"          "fixes"         "atmegau"                         "macro"        "cleanup"        "irsendpin"     "default"        "closes"    "documentation"
 [8,] "remotetracking" "irrecord"      "bumped"        "attiny"                          "usenosendpwm" "unsigned"       "reduce"        "examples"       "jvc"       "error"        
 [9,] "style"          "markexcess"    "active"        "header"                          "include"      "examples"       "extended"      "ztztpatch"      "enable"    "timer"        
[10,] "irrecvdumpvino" "credit"        "handling"      "tone"                            "improve"      "minor"          "output"        "irisrcpp"       "macro"     "library"      
[11,] "irrecvdumpv"    "integration"   "phase"         "compatible"                      "isr"          "dev"            "implemented"   "fixes"          "magiquest" "updated"      
[12,] "feedback"       "commenting"    "typo"          "usesoftsendpwm"                  "esp"          "beta"           "wrong"         "changed"        "parameter" "adding"       
[13,] "receive"        "changed"       "updated"       "implementation"                  "feedback"     "todo"           "names"         "check"          "comment"   "baud"         
[14,] "attiny"         "update"        "introduced"    "leonardo"                        "license"      "analysirmaster" "travis"        "included"       "commit"    "tests"        
[15,] "error"          "avr"           "bose"          "sending"                         "table"        "coding"         "sendsharp"     "implementation" "previous"  "micro"        
[16,] "lg"             "size"          "feedback"      "uintt"                           "pin"          "attiny"         "avr"           "changelog"      "loops"     "standardise"  
[17,] "functions"      "function"      "closes"        "httpsgithubcomztarduinoirremote" "release"      "including"      "print"         "timing"         "flag"      "dish"         
[18,] "compiler"       "decode"        "rp"            "isr"                             "issue"        "bugs"           "housekeeping"  "create"         "create"    "protocol"     
[19,] "output"         "library"       "version"       "boards"                          "magiquest"    "renamed"        "carrier"       "rp"             "license"   "renamed"      
[20,] "usesoftsendpwm" "configuration" "changed"       "update"                          "cpph"         "teensy"         "defined"       "boards"         "attiny"    "changed"      

      Topic 11         Topic 12     Topic 13       Topic 14     Topic 15        Topic 16        Topic 17                Topic 18           Topic 19        Topic 20    
 [1,] "changed"        "request"    "support"      "function"   "removed"       "documentation" "removed"               "closes"           "version"       "closes"    
 [2,] "handling"       "update"     "pronto"       "board"      "support"       "closes"        "sharp"                 "version"          "request"       "support"   
 [3,] "default"        "improved"   "macros"       "closes"     "update"        "merging"       "cleanup"               "update"           "functions"     "update"    
 [4,] "timing"         "pro"        "attiny"       "specific"   "irremotecpp"   "refactored"    "analysirmaster"        "debug"            "esp"           "timer"     
 [5,] "create"         "closes"     "release"      "info"       "request"       "comment"       "esp"                   "adjusted"         "typo"          "samsung"   
 [6,] "pin"            "typo"       "timer"        "led"        "fixes"         "send"          "nolegacycompatibility" "rc"               "attiny"        "attiny"    
 [7,] "template"       "nec"        "version"      "source"     "macro"         "removed"       "enabled"               "readmdfrenchmd"   "pronto"        "irtimerhpp"
 [8,] "function"       "option"     "switch"       "compiler"   "remove"        "pin"           "rename"                "ivankravetspatch" "revert"        "tabs"      
 [9,] "functions"      "master"     "matchmark"    "moved"      "boarddefsh"    "output"        "documentation"         "time"             "bump"          "feedback"  
[10,] "irrecv"         "separated"  "readmemd"     "updated"    "heating"       "cleanup"       "protocol"              "introduced"       "leonardo"      "fixes"     
[11,] "tested"         "support"    "revert"       "link"       "refactored"    "loop"          "send"                  "panasonic"        "contributors"  "flag"      
[12,] "doxygen"        "renamed"    "change"       "sendrawp"   "debug"         "esp"           "separated"             "sending"          "fixup"         "receive"   
[13,] "bit"            "boards"     "contributors" "changelog"  "error"         "changed"       "create"                "protocol"         "documentation" "bugs"      
[14,] "power"          "debug"      "interrupt"    "protocol"   "sendraw"       "lg"            "refactored"            "led"              "including"     "teensy"    
[15,] "irusetimertiny" "release"    "esp"          "boards"     "decoder"       "functions"     "housekeeping"          "create"           "bumped"        "files"     
[16,] "readme"         "avr"        "platformio"   "debug"      "gitignore"     "attinycore"    "bits"                  "support"          "changed"       "mark"      
[17,] "comments"       "reduce"     "template"     "platformio" "travis"        "decoder"       "functions"             "protocols"        "table"         "method"    
[18,] "fixes"          "unittest"   "function"     "hpp"        "ztmaster"      "devices"       "adjusted"              "rp"               "files"         "missing"   
[19,] "receive"        "repeat"     "repeat"       "magiquest"  "documentation" "ledbuiltin"    "nec"                   "renamed"          "hpp"           "parity"    
[20,] "license"        "compatible" "errors"       "print"      "esp"           "ledoff"        "delaymicroseconds"     "error"            "magiquest"     "revert"    
> 