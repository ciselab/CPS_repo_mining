#!/usr/bin/env python
"""
Creating a graph from results
"""
import re
import matplotlib.pyplot as plt
import time
import pathlib
import os


def create_graph(data: dict, data_title: str, sub_dir: str):
    """
    Create a bar graph with the input received.

    Args:
        data: Data to create the graph with.
        data_title: Title for the graph.
        sub_dir: Subdirectory to store the graph in.
    """
    plt.cla()
    plt.title(data_title)
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()), rotation=90)

    current = str(time.time())
    result_current = re.match('[0-9]+', current)
    format_current = result_current[0]

    location = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results", sub_dir)
    if not os.path.exists(os.path.abspath(location)):
        os.makedirs(location)

    new_title = data_title.replace(" ", "_")
    file_name = str(format_current + "_" + new_title)

    """Adjustments"""
    plt.tight_layout()

    """ Save plot """
    save_location = os.path.join(location, file_name)
    plt.savefig(save_location)
