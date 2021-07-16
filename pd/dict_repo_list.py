#!/usr/bin/env python
"""
Tests for the search_current.py script.
"""
import os
import pathlib

""" If the location of the local repositories are on a different location, change this here. """
location_github = os.path.join(pathlib.Path.home(), "Documents", "GitHub")

""" It is possible to manually set the location to a different path. """
# noinspection SpellCheckingInspection
projects = {
	"aira": None,
	"AirSim": None,
	"android_app_manager": None,
	"android_camera_driver": None,
	"android_sensors_driver": None,
	"apollo": None,
	"Arduino": None,
	"arduino-esp32": None,
	"Arduino-IRremote": None,
	"ArduinoJson": None,
	"ardumower": None,
	"ardupilot": None,
	"BeamNGpy": None,
	"carla": None,
	"CoppeliaSimLib": None,
	"cylon": None,
	"dronekit-android": None,
	"dronekit-python": None,
	"DronePilot": None,
	"DroneSym": None,
	"dustcloud": None,
	"GAAS": None,
	"gobot": None,
	"grbl": None,
	"johnny-five": None,
	"librervac-cordlib": None,
	"mavlink": None,
	"node-ar-drone": None,
	"openpilot": None,
	"PiMower": None,
	"PX4-Autopilot": None,
	"pypilot": None,
	"qgroundcontrol": None,
	"rfid": None,
	"robonomics": None,
	"robonomics-js": None,
	"robonomics_contracts": None,
	"stofzuigerrobot": None,
	"turtlebot": None,
	"turtlebot3": None,
	"Valetudo": None,
	"WebODM": None,
}


def build_repo_dict(type_remote: bool = False) -> dict:
	"""
	Can return either the local or remote repositories.
	If the local repository dictionary key has no value, the value is build-up.
	Assumed is the location of the GitHub path, set previously with variable location_github.

	Returns:
		projects: Dictionary of local repositories build up.

	"""
	if type_remote:
		return remote
	else:
		for project in projects:
			if projects[project] is None:
				projects[project] = os.path.join(location_github, project)
	return projects


""" Remote repositories """
# noinspection SpellCheckingInspection
remote = {
	"aira": "https://github.com/airalab/aira",
	"AirSim": "https://github.com/microsoft/AirSim",
	"android_app_manager": "https://github.com/ros-android/android_app_manager",
	"android_camera_driver": "https://github.com/ros-android/android_camera_driver",
	"android_sensors_driver": "https://github.com/ros-android/android_sensors_driver",
	"apollo": "https://github.com/ApolloAuto/apollo",
	"Arduino": "https://github.com/esp8266/Arduino",
	"arduino-esp32": "https://github.com/espressif/arduino-esp32",
	"Arduino-IRremote": "https://github.com/z3t0/Arduino-IRremote",
	"ArduinoJson": "https://github.com/bblanchon/ArduinoJson",
	"ardumower": "https://github.com/Ardumower/ardumower",
	"ardupilot": "https://github.com/ArduPilot/ardupilot",
	"BeamNGpy": "https://github.com/BeamNG/BeamNGpy.git",
	"carla": "https://github.com/carla-simulator/carla",
	"CoppeliaSimLib": "https://github.com/CoppeliaRobotics/CoppeliaSimLib",
	"cylon": "https://github.com/hybridgroup/cylon",
	"dronekit-android": "https://github.com/dronekit/dronekit-android",
	"dronekit-python": "https://github.com/dronekit/dronekit-python",
	"DronePilot": "https://github.com/alduxvm/DronePilot",
	"DroneSym": "https://github.com/scorelab/DroneSym",
	"dustcloud": "https://github.com/dgiese/dustcloud",
	"GAAS": "https://github.com/generalized-intelligence/GAAS",
	"gobot": "https://github.com/hybridgroup/gobot",
	"grbl": "https://github.com/gnea/grbl",
	"johnny-five": "https://github.com/rwaldron/johnny-five",
	"librervac-cordlib": "https://github.com/LibreRVAC/librervac-cordlib",
	"mavlink": "https://github.com/mavlink/mavlink",
	"node-ar-drone": "https://github.com/felixge/node-ar-drone",
	"openpilot": "https://github.com/commaai/openpilot",
	"PiMower": "https://github.com/rohmer/PiMower",
	"PX4-Autopilot": "https://github.com/PX4/Firmware",
	"pypilot": "https://github.com/pypilot/pypilot",
	"qgroundcontrol": "https://github.com/mavlink/qgroundcontrol",
	"rfid": "https://github.com/miguelbalboa/rfid",
	"robonomics": "https://github.com/airalab/robonomics",
	"robonomics-js": "https://github.com/airalab/robonomics-js",
	"robonomics_contracts": "https://github.com/airalab/robonomics_contracts",
	"stofzuigerrobot": "https://github.com/alvitawa/stofzuigerrobot",
	"turtlebot": "https://github.com/turtlebot/turtlebot",
	"turtlebot3": "https://github.com/ROBOTIS-GIT/turtlebot3",
	"Valetudo": "https://github.com/Hypfer/Valetudo",
	"WebODM": "https://github.com/OpenDroneMap/WebODM",
}
