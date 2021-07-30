#!/usr/bin/env python
"""
Test dict of the remote repositories,
test dict of local repositories.
"""

# noinspection SpellCheckingInspection
projects = {
    "carla": {"local": None, "remote": "https://github.com/carla-simulator/carla"},
    "AirSim": {"local": None, "remote": "https://github.com/microsoft/AirSim"},
    "BeamNGpy": {"local": None, "remote": "https://github.com/BeamNG/BeamNGpy.git"},
}

remote_result = {
    "carla": "https://github.com/carla-simulator/carla",
    "AirSim": "https://github.com/microsoft/AirSim",
    "BeamNGpy": "https://github.com/BeamNG/BeamNGpy.git",
}


local_results = {
    "carla": None,
    "AirSim": None,
    "BeamNGpy": None,
}