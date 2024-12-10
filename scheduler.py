import schedule
import time
from threading import Event

stop_event = Event()  # Для остановки цикла

def start_scheduler():
    schedule.every(10).seconds.do(lambda: print("Reminder!"))

    while not stop_event.is_set():
        schedule.run_pending()
        time.sleep(1)

def stop_scheduler():
    stop_event.set()
