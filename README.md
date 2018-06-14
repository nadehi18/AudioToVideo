# record
Record is a small program made in Python to record from the command line.
It also optionally opens a GUI window that allows the user to save the file and exit.


    usage: record.py [-h] [-n] [-u] [-d DIRECTORY] [-m MINUTES] [-s SECONDS]
                     FILENAME

    positional arguments:
      FILENAME              The name of the file

    optional arguments:
      -h, --help            show this help message and exit
      -n, --nogui           Runs the program without opening the GUI
      -u, --usedate         Adds the date to the filename
      -d DIRECTORY, --directory DIRECTORY
                            Directory to save the file in
      -m MINUTES, --minutes MINUTES
                            Length of time to record in minutes
      -s SECONDS, --seconds SECONDS
                            Length of time to record in seconds





#Dependencies:

**pyaudio**

**tkinter**

#To Do:

- [x] Reconfigure argument handling
- [x] Document code
- [ ] Add more arguments and options
