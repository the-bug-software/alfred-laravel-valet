#!/usr/bin/env python
# -*- codirectoryng: utf-8 -*-
# Author: Robert-Cristian Chiribuc <robert.chiribuc@thebug.ro>

import sys
import os
import json

from workflow import Workflow, ICON_WEB, ICON_WARNING


def read_valet_config():
    valet_config = os.path.expanduser("~/") + '.config/valet/'

    with open(valet_config + 'config.json', 'r') as f:
        data = json.load(f)

    return data


def main(wf):
    query = None  # Ensure `query` is initialised

    # Set `query` if a value was passed (it may be an empty string)
    if len(wf.args):
        query = wf.args[0]

    # Get Valet config data
    valet = read_valet_config()

    # Check if Valet paths are defined
    if not valet['paths']:
        wf.add_item('No Valet paths found', icon=ICON_WARNING)

    projects = []
    for path in valet['paths']:
        for directory in os.listdir(path):
            if os.path.isdir(os.path.join(path, directory)):
                projects.append(directory)

    # If `query` is `None` or an empty string, all items are returned
    projects = wf.filter(query, projects)

    for project in projects:
        wf.add_item(project, project + '.' + valet['tld'], arg='http://' + project + '.' + valet['tld'], uid=project,
                    valid=True, icon=ICON_WEB)

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
