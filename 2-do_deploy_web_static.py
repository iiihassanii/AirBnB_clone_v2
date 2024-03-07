#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
hat distributes an archive to your web servers,
using the function do_deploy:"""
from fabric.api import put, run
from fabric.api import env
from datetime import datetime
from os import path

env.hosts = ['54.90.18.3', '100.26.232.118']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distribute an archive to your web servers"""

    try:
        # Upload the archive
        if not path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')

        # Extract archive name
        archive_name = archive_path.split('/')[-1]
        foldername = archive_name.split('.')[0]

        # Create directory
        run("sudo mkdir -p /data/web_static/releases/{}/".format(foldername))

        # Uncompress the archive
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_name, foldername))

        # Delete the uploaded archive
        run("sudo rm /tmp/{}".format(archive_name))

        # Move files to appropriate location
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(foldername, foldername))

        # Remove old symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create new symbolic link
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(foldername))

        print("New version deployed!")
        return True
    except:
        return False
