import os

def notify(text):
	os.system('zenity --notification --text="' + text + '"')
