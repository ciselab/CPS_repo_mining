# turtlebot

remote: https://github.com/turtlebot/turtlebot

## Commit #1 
[b9ab8e2c7e6c8c067c74ed6b7b05f27c09a639f5](https://github.com/turtlebot/turtlebot/commit/b9ab8e2c7e6c8c067c74ed6b7b05f27c09a639f5)

message: Limit joint_states to 10hz for performance.

Antipattern Category: Smith:Is_Everything_OK

keyword: performance


This commit limits the joint state publisher, which publishes the states of the torque controlled joints.
This commit make sure that there is at least 0.1 ms (10 hz) gap between two joint state publishes. This is related to the antipattern intorduced by Smith, Is Everything OK, which is explained as: "This   antipattern   refers   to   repeatedly   checking   the   CPS   platform status, such as the remaining battery life, storage space, etc.". In this case the commit makes sure that the CPS avoid this antipattern in checking the state of the joints.

## Commit #2
[f2d46b705722b61948313e3f2ec167dcaeeb3359](https://github.com/turtlebot/turtlebot/commit/f2d46b705722b61948313e3f2ec167dcaeeb3359)

message: node now fast-fails if USB disconnected and has a --respawnable option to throttle restarting

Antipattern Category: New:Delayed_Sync_With_Physical_Events

keyword: fast


This commit aims to make sure that the driver node fast-fails when the USB device is disconnected. This also ensures that the driver node does not mistakenly detect and reassociate with a newly plugged-in USB device as the previous USB device.


For more information read [this comment](https://github.com/turtlebot/turtlebot/blob/f2d46b705722b61948313e3f2ec167dcaeeb3359/turtlebot_node/nodes/turtlebot_node.py#L388).


## Commit #3
[eadff801651b25ffc7114df7d48bb3be417464a6](https://github.com/turtlebot/turtlebot/commit/eadff801651b25ffc7114df7d48bb3be417464a6)

issue: https://github.com/turtlebot/turtlebot/issues/11

message: trying a lower resolution depth mode to run faster

Antipattern Category: General:Hard-coding

keyword: fast

This commit aims to address an issue that concerns the value of a parameter used for a 3D sensor. The issue reporter suggested changing this value to another value, in which the qualities of the images are lower, to improve the performance of the CPS. 
However, the other developers diagreed with this change and rewinded the setting back in
the [next commit](https://github.com/turtlebot/turtlebot/commit/90fc0a687f1b88cb064be816c71fcac839eefe32#diff-b8c62891ee6719640c4753d924bf5a3a6a5dbc013b030ad0889d0ac91c05132f). The [later commits](https://github.com/turtlebot/turtlebot/commit/552392fcc6ff23e7690e7e6c1e545b959c9b121c#diff-b8c62891ee6719640c4753d924bf5a3a6a5dbc013b030ad0889d0ac91c05132f) allowed the external apps to configure these values.

## Commit #4
[288c08370a41757a4612a5a118b049e40f9b9631]()

## Commit #5
[bf3e001b8d1e91269c61d9b22b969f438545fa3c]()