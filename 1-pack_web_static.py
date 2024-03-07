#!/usr/bin/python3
"""Fabric script that generates a
.tgz archive from the contents of the web_static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Fabric script that generates a
    .tgz archive from the contents of the web_static"""

    # Create versions
    local("mkdir -p versions")

    # archive name web_static_<year><month><day><hour><minute><second>.tgz
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second
    )

    try:
        local("tar -czvf versions/{} web_static".format(now))
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None
