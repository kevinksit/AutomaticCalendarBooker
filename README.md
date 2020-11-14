# AutomaticCalendarBooker
This simple set of scripts is useful for easily booking different users onto a shared calendar using a keypad.

## Prerequisites
This package requires gcsa (for accessing the Google Calendar API) and pickle (for saving the registry).

```bash
pip install gcsa
pip install pickle
```

## Set up
To set this up, we first need to get access to the Google Calendar API and download a credentials file that the script can use.  
1. Click [here](https://developers.google.com/calendar/quickstart/python) and enable the Google Calendar API and download the resulting file (.json). I recommend renaming it to `credentials.json` for simplicity, and place it in the main folder.
2. Log onto the account that has access to the Calendar you wish to book on and get the Calendar ID ([instructions](https://docs.simplecalendar.io/find-google-calendar-id/)).
3. In `CalendarManager.py`, replace the input argument to `Booker` with your calendar ID from step 2, formatted as a string.

## Usage
When booking a time, the manager will book the next available 15 minute slot on the calendar you specified in the set up. It will automatically avoid double booking on the same calendar, and shift your slot to the next available. At the end, it will also provide a confirmation message of the booked time slot.

### First run instructions
1. Open up your preferred terminal
2. Navigate to where you have `CalendarManager.py` stored.
3. Run the script `python CalendarManager.py`
4. On the first run, a browser window will open and prompt you to login to an account which has access to your calendar, and save `token.pickle`.
5. Because a "user registry" does not exist, a `registry.pickle` will automatically be created to hold usernames and the corresponding keys. `registry.pickle` is just a Python dictionary that's saved

### General usage instructions
1. Run `python CalendarManager.py`
2. Press any number key on the keyboard (NumPad recommended).
3. If that user exists, it will automatically book to the calendar specified earlier. If not, it will prompt you to enter a "username" which is used as the name of the event to be booked onto the calendar.
Note: You can enter a blank username to cancel registration.

### Editing registry
1. Run `python CalendarManager.py`
2. Press `e` on the keyboard to enter "edit mode"
3. Follow the onscreen instructions to edit or remove users from the registry.

Developed by KS
