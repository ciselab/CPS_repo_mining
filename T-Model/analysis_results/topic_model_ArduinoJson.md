|Word 	 		| 	Topic		|
|---------------|---------------|
|memory			|	10, 13, 19	|

memory	18 commits
e20c47c57ba0222e1cb66fa0d113b185513d6bff DynamicJsonDocument reallocates memory pool is it's too small
1d942cdf41d4957546088c1e93b97cf04664bd03 Use singly-linked list to reduce memory usage
04e8acd844cd8e8bd22beccf1294407357ef0181 Store offset between slots to reduce memory usage
720e6548c73040b7d80bbc0c5af96d4d6d99b152 Replacing a value now releases the memory
cf149940ed37b7454bec0fa492d26a19e1a82d17 Moved JsonBuffer to Memory/
3f96e070ce9315ce1c75b8a65afe90f1a11471b8 Reduced memory consumption by not duplicating spaces and comments
5a4d993f7d0429789f960988d973a3b5bc79db59 Fixed memory alignment, which made ESP8266 crash (issue #104)
601b51890f64e021f8b4f7c5ac0027820f983fa5 Fixed segmentation fault in  when memory allocation fails (issue #92)
2524a00a9661fcf2a1ad3affea4d1742226fa2e3 Fixed segmentation fault in `DynamicJsonBuffer` when memory allocation fails (issue #92)
5236de1433f96ea1930e6fbf53008e8b9b54024c Added memory usage
006fc1314153ee833696a7e7122aae9c8ae1e6bd Example: change the type of the json string from char* to char[] because it cause issue in memory protected environments.


      Topic 1                Topic 2         Topic 3       Topic 4       Topic 5          Topic 6                   Topic 7          Topic 8                  Topic 9              
 [1,] "issue"                "warnings"      "removed"     "fixes"       "closes"         "renamed"                 "issue"          "tests"                  "issue"              
 [2,] "updated"              "visual"        "comments"    "moved"       "support"        "array"                   "coverage"       "jsonvalue"              "values"             
 [3,] "script"               "studio"        "change"      "refactoring" "arduino"        "table"                   "string"         "issue"                  "missing"            
 [4,] "change"               "project"       "replaced"    "minor"       "jsondocument"   "tests"                   "implementation" "strings"                "removed"            
 [5,] "fixes"                "donators"      "json"        "changed"     "error"          "print"                   "clangtidy"      "nested"                 "char"               
 [6,] "tests"                "replaced"      "travis"      "travis"      "removed"        "nested"                  "clang"          "copyright"              "readme"             
 [7,] "publish"              "parse"         "jsonvariant" "progress"    "jsonvariant"    "hash"                    "moved"          "vscode"                 "simplified"         
 [8,] "log"                  "created"       "arduino"     "template"    "nesting"        "bool"                    "badge"          "operators"              "input"              
 [9,] "hash"                 "gcc"           "jsonstring"  "parameter"   "files"          "updated"                 "changed"        "jsonvariant"            "links"              
[10,] "remove"               "coverage"      "copyright"   "char"        "clangtidy"      "private"                 "writing"        "indentedprintdecorator" "gcc"                
[11,] "ambiguous"            "supported"     "support"     "github"      "memorypool"     "mergeparserandgenerator" "refactoring"    "mingw"                  "string"             
[12,] "changelogmd"          "reading"       "progmem"     "settings"    "invalid"        "adds"                    "publish"        "features"               "compiler"           
[13,] "deserializationerror" "jsonvalue"     "issues"      "namespace"   "protected"      "failing"                 "script"         "renamed"                "error"              
[14,] "cmake"                "mode"          "enable"      "method"      "jsonhttpclient" "subscript"               "include"        "pool"                   "function"           
[15,] "operators"            "platformio"    "jsonbuffer"  "types"       "gcc"            "classes"                 "array"          "return"                 "size"               
[16,] "true"                 "appveyoryml"   "constant"    "compiler"    "issue"          "files"                   "muted"          "match"                  "float"              
[17,] "update"               "uninitialized" "refactoring" "script"      "script"         "cpplint"                 "undefined"      "expected"               "fuzzing"            
[18,] "check"                "removed"       "aptget"      "arduinoh"    "coverage"       "casting"                 "arduinojson"    "volatile"               "jsonobject"         
[19,] "closes"               "extracted"     "messagepack" "arm"         "library"        "operator"                "epic"           "store"                  "comments"           
[20,] "copyarray"            "custom"        "const"       "memberproxy" "false"          "remove"                  "linkedstring"   "merged"                 "dynamicjsondocument"

      Topic 10          Topic 11            Topic 12         Topic 13            Topic 14     Topic 15          Topic 16       Topic 17            Topic 18        Topic 19    
 [1,] "version"         "size"              "warning"        "issue"             "version"    "fixes"           "list"         "class"             "updated"       "string"    
 [2,] "return"          "reduced"           "gcc"            "removed"           "simplified" "string"          "donators"     "jsonarray"         "error"         "closes"    
 [3,] "beta"            "bytes"             "version"        "travis"            "array"      "changelog"       "fixes"        "extracted"         "char"          "issue"     
 [4,] "arduino"         "usage"             "moved"          "renamed"           "updated"    "type"            "jsonvalue"    "jsonobject"        "master"        "support"   
 [5,] "jsonobject"      "esp"               "removed"        "library"           "generator"  "object"          "default"      "strings"           "objects"       "removed"   
 [6,] "renamed"         "removing"          "renamed"        "string"            "error"      "updated"         "operator"     "base"              "readmemd"      "memory"    
 [7,] "memory"          "travis"            "request"        "stringbuilder"     "float"      "token"           "changed"      "values"            "adapters"      "char"      
 [8,] "double"          "og"                "link"           "invalid"           "issue"      "jsonobjectbase"  "compilation"  "dynamicjsonbuffer" "create"        "array"     
 [9,] "json"            "private"           "executable"     "deprecated"        "copyarray"  "studio"          "link"         "common"            "merged"        "return"    
[10,] "stored"          "compiled"          "cpp"            "dynamicjsonbuffer" "single"     "terminator"      "static"       "namespace"         "documentation" "tests"     
[11,] "update"          "saves"             "const"          "jsondocument"      "clang"      "changed"         "jsondocument" "restored"          "serialize"     "custom"    
[12,] "increased"       "errors"            "closes"         "memory"            "builds"     "clang"           "readme"       "methods"           "matching"      "jsonarray" 
[13,] "deserializejson" "stack"             "jsonvariantist" "jsonstring"        "implicit"   "deserializejson" "closes"       "implementation"    "replaced"      "platformio"
[14,] "jsonarray"       "dynamicjsonbuffer" "unit"           "examples"          "gcc"        "split"           "extracted"    "scripts"           "particle"      "readme"    
[15,] "coverage"        "virtual"           "mode"           "wsignconversion"   "spaces"     "converted"       "duplicate"    "true"              "improved"      "error"     
[16,] "strings"         "jsonvalue"         "platformio"     "script"            "wandbox"    "operator"        "master"       "arrays"            "integration"   "arduino"   
[17,] "default"         "version"           "readme"         "replace"           "badge"      "compiler"        "extracting"   "parse"             "highlighting"  "defined"   
[18,] "getmember"       "string"            "ignore"         "object"            "platformio" "filter"          "overloaded"   "jsonparserbase"    "ide"           "strings"   
[19,] "floats"          "adding"            "avoid"          "copyright"         "catch"      "platformio"      "unused"       "fails"             "syntax"        "digits"    
[20,] "check"           "increase"          "default"        "disabled"          "sponsors"   "support"         "arduino"      "pool"              "readme"        "arrays"    

      Topic 20           
 [1,] "travis"           
 [2,] "tests"            
 [3,] "improved"         
 [4,] "files"            
 [5,] "object"           
 [6,] "error"            
 [7,] "capacity"         
 [8,] "serialization"    
 [9,] "remove"           
[10,] "avoid"            
[11,] "function"         
[12,] "cmake"            
[13,] "jsonarrayiterator"
[14,] "update"           
[15,] "spaces"           
[16,] "cmakeliststxt"    
[17,] "jsonvariant"      
[18,] "copied"           
[19,] "compilation"      
[20,] "macro"            
> 