from pystray import Icon, Menu, MenuItem
from PIL import Image

def create_tray(scheduler_stop_callback):
    icon_image = Image.open("assets/icon2.png")

    def on_quit(icon, item):
        print("Exiting the program")
        scheduler_stop_callback()  # Останавливаем планировщик
        icon.stop()

    menu = Menu(
        MenuItem("Quit", on_quit)
    )
    tray_icon = Icon("Exercise Reminder", icon_image, menu=menu)
    tray_icon.run()
