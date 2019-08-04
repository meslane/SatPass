Running this program returns data on radio pass times for all tracked satellites using the N2YO API

Running the noncomplied .py file requires the instillation of the pytz and tzlocal libraries for converting 
the UTC date format to that of the user's local time. As the compiled file only runs based on python bytecode, 
no library instillation is required, only a Python 3 install. 

In order to run this script, one must create a unique API key on N2YO by visiting 
https://www.n2yo.com/login/edit/ and generating a key. Note that you must have an account to do this.
Upon generation, copy your key into a file named key.txt and store it in the same directory as SatPass. 
It will be used by the program to access the API

To add a satellite to the tracker, simply input its NORAD ID on a new line in the "tracked_satellites" file,
and the script will automatically include its pass details if the ID is valid

Location setting are stored in the location.txt file and are formatted as follows:

LINE 1: latitude of observer 
LINE 2: longitude of observer
LINE 3: altitude of observer (typically this can just be set to 0)
LINE 4: minimum visible altitude for a pass to be considered (recommend setting this around 10-20 degrees) 
