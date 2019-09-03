Running this program returns data on radio pass times for all tracked satellites using the N2YO API

Running the .py file requires the instillation of the pytz and tzlocal libraries for converting the UTC 
date format to that of the user's local time. Both libraries are very lightweight and can be installed
in seconds using pip, or by running the .bat file included in the download if you're on windows, or 
the .bash file if you are on linux. You should only need to do this once 

In order to run this script, one must create a unique API key on N2YO by visiting 
https://www.n2yo.com/login/edit/ and generating a key. Note that you must have an account to do this.
Upon generation, copy your key into a file named key.txt and store it in the same directory as SatPass. 
It will be used by the program to access the API

To add a satellite to the tracker, simply input its NORAD ID on a new line in the "tracked_satellites" file
and the script will automatically include its pass details if the ID is valid

Configuration settings are stored in the configs.txt file and are formatted as follows:

LINE 1: latitude of observer 
LINE 2: longitude of observer
LINE 3: altitude of observer (typically this can just be set to 0)
LINE 4: number of days to look ahead
LINE 5: minimum visible altitude for a pass to be considered (recommend setting this no lower than 20 degrees) 
