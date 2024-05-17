#!/usr/bin/python3
""" script that generates a .tgz archive from the
contents of the web_static folder of your
AirBnB Clone repo, using the function do_pack. """
from fabric import task,  run , api
import datetime


@task
def do_pack():
    """ compresses and names the compressed tgz version of the web_satatic folder """
    now = datetime.datetime.now()
    formatted_datetime = now.strftime("%Y%m%d%H%M%S")
    archived_file_name = "web_static_{}".format(formatted_datetime)
    run('mkdir versions')
    status = run(f'tar -cvzf ./versions/{archived_file_name}.tgz /home/nada-zaki/alx/AirBnB_clone_v2/web_static')
    print(status)
