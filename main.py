import pystray
from PIL import Image
import reghandle
from functools import partial
from tkinter import messagebox
import sys, os

app_name = 'micTray'

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
    
icon_path = resource_path('microphone-solid.ico')

icon = pystray.Icon(app_name)
image = Image.open(icon_path)
icon.icon = image

def no_action():
  return

def get_status_indicator(*_):
  return 'Current status: ' + reghandle.value

def exit_program():
  icon.stop()
  exit('Exit triggered by user')

menu = pystray.Menu(
  pystray.MenuItem(get_status_indicator, no_action), 
  pystray.MenuItem('Toggle', partial(reghandle.toggle, icon)),
  pystray.MenuItem('Exit', exit_program)
  )

icon.menu = menu
icon.run()