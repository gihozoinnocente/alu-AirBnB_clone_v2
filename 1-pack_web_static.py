#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack"""
from datetime import datetime
from fabric.api import *

import os

def do_pack():
   local('sudo mkdir -p versions')
   t =datetime.now()
   time_str=t.strftime('%Y%m%d%H%M%S')
   local(f'sudo tar -cvzf versions/web_static_{t_str}.tgz web_static')
   f_path = f"versions/web_static_{t_str}.tgz"
   f_size = os.path.getsize(f_path)
   print(f"web_static packed: {f_path} {f_size}Bytes")