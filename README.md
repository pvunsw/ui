# UI - Readme

This to contain instructions a non-developer end user could use to get this running. 

# LICENCE

Decide on later. 

# Dev setup.

## Install dependencies.
The order may matter.
* Python XY
* Microsoft .NET Framework 4.5
* Labview 2013 64bit (or later)
* NI-DAQmx (make sure it's > 14.5)
* Git.

## Set up a simulated device for testing.
![How to setup a simulated device](/doc/configuring_test_device.gif)

Then run main.py

# Workflow

We'll use "master" for the current state of development, but new features should be taken to new branches then merged to master when working.

There will also be a branch "releasable" which is a branch which a user should be able to pull a tar-ball from, read the Readme, and get working with. So in this sense, "master" will be more for keeping up with the current state of development. 

