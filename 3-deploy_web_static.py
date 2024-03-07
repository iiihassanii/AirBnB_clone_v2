#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy:"""
from fabric.api import put, run, local
from fabric.api import env
from datetime import datetime
from os import path
archive_path = None


env.hosts = ['54.90.18.3', '100.26.232.118']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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

        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(foldername))

        # Remove old symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create new symbolic link
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(foldername))

        return True
    except Exception as e:
        return False


def deploy():
    """Fabric script (based on the file 2-do_deploy_web_static.py)
    that creates and distributes an archive to your web servers,
    using the function deploy:"""
    global archive_path
    if archive_path is None:
        archive_path = do_pack()
        if archive_path is None:
            return False
    return do_deploy(archive_path)
