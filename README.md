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
The libraries used by this code are the modified ALE library with object detection and RL-glue. The code provides a demo of using both.

Makefile
----------
Again, only configured to work on the UTCS machines at this time as it requires dependencies on that system. The makefile will automatically link all libraries, so you don't need to export any paths at runtime. All paths are absolute, so the executable should run anywhere on the system. The only parts that may require updating are the top three values: `SRC_FILES`, `ALE_DIR`, and `RLGLUE_DIR`.

Source Code
----------
All original source code is in `src/main.cpp`. The other two files are necessary for RL-glue to compile, and need to be customized when using RL-glue.

Running the Executable
----------
Everything will be compiled into an executable called `proj`. To run it, you need to specify a game (ROM file). For example,

`./proj space_invaders`

Do not include the ".bin" part of the ROM (this is done automatically). ROMs are expected to be saved in a folder called `roms` in the ALE library's directory.

The current code just runs random actions for 10 games on whatever ROM you load.
