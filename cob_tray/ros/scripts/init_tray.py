#!/usr/bin/python
 

import roslib

roslib.load_manifest('cob_script_server')

import rospy


from simple_script_server import script
 

class InitTray(script):

        def Initialize(self):

               self.sss.init("tray")

 
if __name__ == "__main__":

        SCRIPT = InitTray()

        SCRIPT.Start()
