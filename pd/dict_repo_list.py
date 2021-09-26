#!/usr/bin/env python
"""
Data for the test_repository_commits_mining script.
"""
import os
import pathlib

""" If the location of the local repositories are on a different location, change this here. """
location_github = os.path.join(pathlib.Path.home(),"repo-mining", "projects")

"""
It is possible to manually set the location to a different path.

Explanation:
"name_project": {"local": None, "remote": "url"}
change to:
"name_project": {"local": "/right/here", "remote": "url"}

Changing None to your local path, you overwrite the otherwise build-up path.

If set to None, the local path will bu build-up by function build_repo_dict as follows:
local path = location_github + project_name
Where location_github is given in the top of this file.
"""
# noinspection SpellCheckingInspection
projects = {
	"aira": {"local": None, "remote": "https://github.com/airalab/aira"},
	"AirSim": {"local": None, "remote": "https://github.com/microsoft/AirSim"},
	"android_app_manager": {"local": None, "remote": "https://github.com/ros-android/android_app_manager"},
	"android_camera_driver": {"local": None, "remote": "https://github.com/ros-android/android_camera_driver"},
	"android_sensors_driver": {"local": None, "remote": "https://github.com/ros-android/android_sensors_driver"},
	"apollo": {"local": None, "remote": "https://github.com/ApolloAuto/apollo"},
	"Arduino": {"local": None, "remote": "https://github.com/esp8266/Arduino"},
	"arduino-esp32": {"local": None, "remote": "https://github.com/espressif/arduino-esp32"},
	"Arduino-IRremote": {"local": None, "remote": "https://github.com/z3t0/Arduino-IRremote"},
	"ArduinoJson": {"local": None, "remote": "https://github.com/bblanchon/ArduinoJson"},
	"ardumower": {"local": None, "remote": "https://github.com/Ardumower/ardumower"},
	"ardupilot": {"local": None, "remote": "https://github.com/ArduPilot/ardupilot"},
	"BeamNGpy": {"local": None, "remote": "https://github.com/BeamNG/BeamNGpy.git"},
	"carla": {"local": None, "remote": "https://github.com/carla-simulator/carla"},
	"CoppeliaSimLib": {"local": None, "remote": "https://github.com/CoppeliaRobotics/CoppeliaSimLib"},
	"cylon": {"local": None, "remote": "https://github.com/hybridgroup/cylon"},
	"dronekit-android": {"local": None, "remote": "https://github.com/dronekit/dronekit-android"},
	"dronekit-python": {"local": None, "remote": "https://github.com/dronekit/dronekit-python"},
	"DronePilot": {"local": None, "remote": "https://github.com/alduxvm/DronePilot"},
	"DroneSym": {"local": None, "remote": "https://github.com/scorelab/DroneSym"},
	"dustcloud": {"local": None, "remote": "https://github.com/dgiese/dustcloud"},
	"GAAS": {"local": None, "remote": "https://github.com/generalized-intelligence/GAAS"},
	"gobot": {"local": None, "remote": "https://github.com/hybridgroup/gobot"},
	"grbl": {"local": None, "remote": "https://github.com/gnea/grbl"},
	"johnny-five": {"local": None, "remote": "https://github.com/rwaldron/johnny-five"},
	"librervac-cordlib": {"local": None, "remote": "https://github.com/LibreRVAC/librervac-cordlib"},
	"mavlink": {"local": None, "remote": "https://github.com/mavlink/mavlink"},
	"node-ar-drone": {"local": None, "remote": "https://github.com/felixge/node-ar-drone"},
	"openpilot": {"local": None, "remote": "https://github.com/commaai/openpilot"},
	"PiMower": {"local": None, "remote": "https://github.com/rohmer/PiMower"},
	"PX4-Autopilot": {"local": None, "remote": "https://github.com/PX4/Firmware"},
	"pypilot": {"local": None, "remote": "https://github.com/pypilot/pypilot"},
	"qgroundcontrol": {"local": None, "remote": "https://github.com/mavlink/qgroundcontrol"},
	"rfid": {"local": None, "remote": "https://github.com/miguelbalboa/rfid"},
	"robonomics": {"local": None, "remote": "https://github.com/airalab/robonomics"},
	"robonomics-js": {"local": None, "remote": "https://github.com/airalab/robonomics-js"},
	"robonomics_contracts": {"local": None, "remote": "https://github.com/airalab/robonomics_contracts"},
	"stofzuigerrobot": {"local": None, "remote": "https://github.com/alvitawa/stofzuigerrobot"},
	"turtlebot": {"local": None, "remote": "https://github.com/turtlebot/turtlebot"},
	"turtlebot3": {"local": None, "remote": "https://github.com/ROBOTIS-GIT/turtlebot3"},
	"Valetudo": {"local": None, "remote": "https://github.com/Hypfer/Valetudo"},
	"WebODM": {"local": None, "remote": "https://github.com/OpenDroneMap/WebODM"},
}


def build_repo_dict():
	"""
	If the local repository dictionary key has no value, the value is build-up.
	Assumed is the location of the GitHub path, set previously with variable location_github.
	"""
	for project in projects:
		if projects[project]["local"] is None:
			updated_local = os.path.join(location_github, project)
			projects[project].update({"local": updated_local})
