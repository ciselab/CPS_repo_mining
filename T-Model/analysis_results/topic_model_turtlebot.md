# turtlebot

## Result

time (1)
f04a2af6e2cd2d443435938745bb459e8304a8c3 tuning kinect time offset and disabling registration for cpu savings

## Words/Topics

|Word 	 		| 	Topic		|
|---------------|---------------|
|unstable		|	2			|
|avoid			|	10, 13, 20	|
|time			|	19			|
|battery		|	1, 6, 17	|


unstable	6 commits
One commit could be interesting:
d4bf791e460604c95c6e40b18b1c92cb00f95597 unstable no longer makes sense.
Vague commit message. 

avoid	7 commits
91e6b345f1ab4df4fa593ecd95305f56e6a831f6 update publisher queue_size to avoid warning in indigo
d62c0f544ce6b46d23b8e1c93e9b91efa722160c update publisher queue_size to avoid warning in indigo

time	3 commits
Could be interesting
928306ba94acbfcc4e0ee61c7c8e432561b0824f Issue #102: Battery info fixed for new laptops. Also I have changed the default path where to look for the BAT0 files, as the current one was deprecated long time ago
f04a2af6e2cd2d443435938745bb459e8304a8c3 tuning kinect time offset and disabling registration for cpu savings
-> interesting
f04a2af6e2cd2d443435938745bb459e8304a8c3 tuning kinect time offset and disabling registration for cpu savings

battery	16 commits
928306ba94acbfcc4e0ee61c7c8e432561b0824f Issue #102: Battery info fixed for new laptops. Also I have changed the default path where to look for the BAT0 files, as the current one was deprecated long time ago
bdf3080e8a0c14d1be0bd82a93c049fa826f5d9e Making laptop battery script work with the new /sys filesystem organization.
dd70a283906c3a4fdc9b10dcb669014000059878 environment variable for battery settings - move to a proper configurable solution later, #16.
7581608ddd51a0c3d770566edd431a4255322823 bugfix the laptop battery check.


      Topic 1         Topic 2           Topic 3      Topic 4           Topic 5               Topic 6                Topic 7         Topic 8                Topic 9       Topic 10   
 [1,] "launch"        "adding"          "updates"    "create"          "dependency"          "default"              "create"        "missing"              "updating"    "app"      
 [2,] "robot"         "teleop"          "xacro"      "gazebo"          "removed"             "fixing"               "dependency"    "files"                "turtlebot"   "manager"  
 [3,] "cmdvelmux"     "base"            "remove"     "kinect"          "request"             "closes"               "issue"         "apps"                 "changelog"   "android"  
 [4,] "setting"       "removing"        "launch"     "names"           "laptop"              "interactions"         "merging"       "adds"                 "rosinstall"  "launcher" 
 [5,] "fixing"        "renaming"        "minimal"    "teleop"          "rosinstall"          "depend"               "release"       "update"               "stackxml"    "replace"  
 [6,] "topic"         "turtlebot"       "update"     "publisher"       "dsensor"             "patch"                "environment"   "fixes"                "xtion"       "updated"  
 [7,] "separate"      "android"         "ready"      "rosinstaller"    "kinect"              "changelog"            "links"         "eclipse"              "parameter"   "include"  
 [8,] "battery"       "asus"            "driver"     "parameters"      "turtlebotnode"       "files"                "xacro"         "kobuki"               "wiki"        "remove"   
 [9,] "ps"            "updated"         "robot"      "turtlebotteleop" "optional"            "turtlebotdescription" "linuxhardware" "project"              "kobuki"      "simple"   
[10,] "laptop"        "fuerte"          "appmanager" "camera"          "plates"              "asus"                 "app"           "base"                 "mobile"      "diff"     
[11,] "directory"     "unstable"        "issue"      "indigo"          "android"             "turtlebot"            "moved"         "mesh"                 "diagnostics" "avoid"    
[12,] "false"         "patch"           "stacks"     "base"            "poles"               "script"               "pro"           "android"              "nodelet"     "eclipse"  
[13,] "replace"       "tag"             "velocity"   "fixes"           "app"                 "launchers"            "calls"         "request"              "ecl"         "joystick" 
[14,] "repository"    "turtlebotteleop" "bring"      "update"          "models"              "navigation"           "files"         "bringup"              "mesh"        "cleanup"  
[15,] "url"           "unused"          "default"    "adding"          "dependencies"        "gitignore"            "outdated"      "turtlebotdescription" "collada"     "remapping"
[16,] "library"       "url"             "missing"    "scan"            "broken"              "includes"             "node"          "package"              "dynamic"     "list"     
[17,] "prefixes"      "cleanup"         "noisy"      "appmanager"      "turtlebotrosinstall" "battery"              "rule"          "updated"              "debs"        "env"      
[18,] "error"         "configuration"   "option"     "mjpegserver"     "check"               "driver"               "list"          "comments"             "python"      "robot"    
[19,] "minimallaunch" "implement"       "python"     "merging"         "configure"           "version"              "variable"      "folders"              "dae"         "rolled"   
[20,] "renamed"       "warning"         "refactor"   "aptget"          "hexagon"             "issue"                "mass"          "gitignore"            "adds"        "cmdvel"   

      Topic 11                              Topic 12           Topic 13           Topic 14               Topic 15        Topic 16        Topic 17      Topic 18             
 [1,] "httpsgithubcomturtlebotturtlebot"    "urdf"             "remove"           "turtlebot"            "teleop"        "tag"           "adding"      "request"            
 [2,] "master"                              "upstart"          "fuerte"           "package"              "launcher"      "changeset"     "request"     "remove"             
 [3,] "hydrodevel"                          "merging"          "preparing"        "stack"                "urdf"          "turtlebot"     "battery"     "modified"           
 [4,] "indigo"                              "script"           "request"          "adds"                 "dsensor"       "diamondback"   "change"      "opennilaunch"       
 [5,] "closes"                              "turtlebotbringup" "moved"            "rapp"                 "fixing"        "electric"      "create"      "adding"             
 [6,] "node"                                "removes"          "typo"             "interface"            "camera"        "updated"       "adds"        "base"               
 [7,] "model"                               "updated"          "avoid"            "app"                  "list"          "stack"         "apps"        "install"            
 [8,] "missing"                             "ros"              "bringup"          "bugfix"               "arg"           "update"        "groovy"      "rosinstaller"       
 [9,] "request"                             "launcher"         "node"             "ecl"                  "version"       "version"       "rviz"        "parameter"          
[10,] "driver"                              "link"             "dependency"       "ticket"               "kinect"        "launch"        "reconfigure" "support"            
[11,] "openni"                              "default"          "variable"         "network"              "conflict"      "adds"          "asus"        "changelogs"         
[12,] "release"                             "map"              "groovy"           "updating"             "adding"        "rename"        "install"     "create"             
[13,] "description"                         "removing"         "files"            "rep"                  "base"          "safety"        "previous"    "dependency"         
[14,] "inorder"                             "depth"            "concert"          "turtlebotdescription" "dsensorconfig" "linkjoint"     "header"      "kinect"             
[15,] "astra"                               "moving"           "turtlebotbringup" "indigo"               "sync"          "default"       "rqt"         "package"            
[16,] "chirp"                               "request"          "setting"          "map"                  "issue"         "opennilaunch"  "extra"       "repo"               
[17,] "cmdvel"                              "turtlebotteleop"  "error"            "typo"                 "migrate"       "request"       "xtion"       "bitpiratehydrodevel"
[18,] "roomba"                              "adding"           "navigation"       "issue"                "robot"         "files"         "launch"      "module"             
[19,] "httpsgithubcomturtlebotturtlebotgit" "interaction"      "stack"            "rocon"                "app"           "interactions"  "gazebo"      "scripts"            
[20,] "diff"                                "settings"         "kobuki"           "parameter"            "mapping"       "visualisation" "logo"        "moved"              

      Topic 19               Topic 20               
 [1,] "update"               "removing"             
 [2,] "turtlebot"            "capabilities"         
 [3,] "changelog"            "fixes"                
 [4,] "turtlebotrosinstall"  "remove"               
 [5,] "mode"                 "bringup"              
 [6,] "gyro"                 "turtlebotcapabilities"
 [7,] "launchers"            "error"                
 [8,] "updating"             "paired"               
 [9,] "dependency"           "reconfigure"          
[10,] "adding"               "pole"                 
[11,] "replace"              "xacro"                
[12,] "missing"              "avoid"                
[13,] "urdf"                 "files"                
[14,] "turtlebotdescription" "adds"                 
[15,] "joystick"             "joystick"             
[16,] "interaction"          "bugfixes"             
[17,] "change"               "package"              
[18,] "time"                 "real"                 
[19,] "commenting"           "turtlebotirdevel"     
[20,] "switching"            "acceleration"         
