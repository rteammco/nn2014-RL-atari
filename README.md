CS 394N - Final Project
==========

Final project for CS394N (Neural Networks) - Fall 2014. Reinforcement Learning using ALE (the Atari Learning Environment).

Notice
----------
This project is currently configured to only work on UTCS machines.

Installation
----------
The "install_everything" script does not work yet, but the commented pseudocode serves as a list of steps to install the project.

Libraries
----------
The only library used by this code is the modified ALE library with object detection (which in turn requires SDL).

Makefile
----------
Again, only configured to work on the UTCS machines at this time as it requires dependencies on that system. The makefile will automatically link all libraries, so you don't need to export any paths at runtime. All paths are absolute, so the executable should run anywhere on the system. The only parts that may require updating are the top three values: `SRC_FILES` and `ALE_DIR`.

Source Code
----------
All original source code is in `src/main.cpp` and the `python` directory. The file `python/test.py` provides an example of how to use the `ALEInterface` Python object to communicate with the C++ code which acts as a wrapper for the ALE emulator.

Running the Executable
----------
Everything will be compiled into an executable called `proj`. Do not run this file! Use the python `ALEInterface` object to communicate with it (see `python/test.py`).
