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


For more information raad [this comment](https://github.com/turtlebot/turtlebot/blob/f2d46b705722b61948313e3f2ec167dcaeeb3359/turtlebot_node/nodes/turtlebot_node.py#L388).