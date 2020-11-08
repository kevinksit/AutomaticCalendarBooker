import msvcrt
from Booker import Booker
from Registry import Registry
from os import system
import time

class CalendarManager:
    def __init__(self):
        self.booker = Booker('ucsb.edu_sj35l06299ha3d7v1a0oarfml8@group.calendar.google.com'); #  this is the calendar_id for Room 6164
        self.registry = Registry()

    def checkInput(self, input_char):
        if self.registry.check(input_char):
            print('Acessing calendar...')
            self.booker.addEvent(self.registry.getUser(input_char)) # this should return the correct name
        else:
            self.registry.add(input_char)

    def main(self):
        while True:
            print('\nPress a number key (or backspace to quit)')
            input_char = msvcrt.getch().decode('ASCII')
            if input_char == '\b': #backspace or esc
                print('Quitting...')
                break
            elif input_char == 'e': # enter edit mode
                self.registry.edit()
            else:
                self.clear()
                self.checkInput(input_char)
            time.sleep(0.5)

    def clear(self):
        _ = system('cls')

if __name__ == '__main__':
    cm = CalendarManager()
    cm.main()
