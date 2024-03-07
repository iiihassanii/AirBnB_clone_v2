#!/usr/bin/python3
"""Fabric script that generates a
.tgz archive from the contents of the web_static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Fabric script that generates a
    .tgz archive from the contents of the web_static"""

    # Create versions directory if it doesn't exist
    local("mkdir -p versions")

    # Get the current time
    now = datetime.now()

    # Create the archive name
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )

    try:
        # Archive the web_static directory
        local("tar -czvf versions/{} web_static".format(archive_name))

        # Return the path to the archive
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
