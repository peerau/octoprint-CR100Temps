import logging

def catch_head_temperature(comm, line, *args, **kwargs):
  if "Echo:Get Head(0)" in line:
    logging.getLogger("octoprint.plugin." + __name__).info("Bad head temp line encountered, fixing with {line}.")
    real = line.split(' ')[2]
    line = f"ok {real}"
  return line

__plugin_name__ = "CR-100 Temp patch"
__plugin_version__ = "0.1.0"
__plugin_description__ = "A quick gcode changer plugin for OctoPrint"
__plugin_pythoncompat__ = ">=3.7,<4"
