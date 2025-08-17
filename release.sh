#!/bin/bash

pyinstaller -D -w -i "icon.ico" --name "FreeDuck" main.py

# copy the project dependencies
cp *.py dist/FreeDuck/_internal
cp -r ui dist/FreeDuck/_internal

# make sure the exe is working
# then use innosetup to create an installer