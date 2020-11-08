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
1. Click [here](www.google.com) and enable the Google Calendar API and download the resulting file (.json). I recommend renaming it to `credentials.json` for simplicity, and place it in the main folder.
2. Log onto the account that has access to the Calendar you wish to book on and get the Calendar ID ([instructions](https://docs.simplecalendar.io/find-google-calendar-id/)).
3. In `CalendarManager.py`, replace the input argument to `Booker` with your calendar ID from step 2, formatted as a string.
4. On first run, a browser window will open and prompt you to login to the account that has access to the calendar, and create a `token.pickle`.

## Usage