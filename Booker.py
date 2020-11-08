from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from datetime import datetime, timedelta

class Booker:
    def __init__(self, calendar_id):
        self.calendar = self.getCalendar(calendar_id)

    def getCalendar(self, calendar_id):
        calendar = GoogleCalendar(calendar_id, './credentials.json') # room 6164
        return calendar

    def addEvent(self, user='Goard Lab'):
        [start, end] = self.getTimes()
        event = Event(
            user,
            start = start,
            end = end)
        self.calendar.add_event(event) # add the event
        print('Event created for ' + user + ' from ' + start.strftime('%A, %H:%M') + ' to ' + end.strftime('%A, %H:%M') + '!') # tell me when i can go
    
    def getTimes(self, duration=15):
        start = datetime.now()
        while True:
            end = start + timedelta(minutes=duration)
            events = list(self.calendar.get_events(time_min = start, time_max = end)) # find events in the time
            if len(events) == 0: # break the loop
                break
            else:
                start = events[-1].end # get the end time of the latest event and set to new start time
        return start, end

if __name__ == '__main__':
    book = Booker()
    book.addEvent()
