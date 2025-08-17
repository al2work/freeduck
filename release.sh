#!/bin/bash

pyinstaller -D -w -i "icon.ico" freeduck.py

# clean
# rm -fr dist/ build/ *.spec