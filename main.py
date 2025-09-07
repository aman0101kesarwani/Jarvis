import os

import eel

# to tell eel where frontend is
eel.init("www")

# Opens Edge in app mode to display the local web page like a standalone desktop app
os.system('start msedge.exe --app="http://localhost:8000/index.html"')

#TO start this file
eel.start('index.html', mode=None, host='localhost', block=True)

# to ignore the extra files due to envkjarvis folder we create a .gitignore file and set the path of as /nmvkjarvis and save this .gitignore file is First project-Jarvis file
