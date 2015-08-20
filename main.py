import pygame
import time, datetime
import threading

def music():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("music/GoodMorningFreedom.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

class Clock:

    def __init__(self):
        self.alarm_time = None
        self._alarm_thread = None
        self.update_interval = 1
        self.event = threading.Event()

    def run(self):
        while True:
            self.event.wait(self.update_interval)
            if self.event.isSet():
                break
            now = datetime.datetime.now()
            if self._alarm_thread and self._alarm_thread.is_alive():
                alarm_symbol = '+'
            else:
                alarm_symbol = ' '
            print alarm_symbol
            print now

    def set_alarm(self, hour, minute):
        now = datetime.datetime.now()
        alarm = now.replace(hour=int(hour), minute=int(minute))
        delta = int((alarm - now).total_seconds())
        if delta <= 0:
            alarm = alarm.replace(day=alarm.day + 1)
            delta = int((alarm - now).total_seconds())
        if self._alarm_thread:
            self._alarm_thread.cancel()
        self._alarm_thread = threading.Timer(delta, music)
        self._alarm_thread.daemon = True
        self._alarm_thread.start()

clock = Clock()
clock.set_alarm(15, 20)
clock.run()