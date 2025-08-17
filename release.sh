#!/bin/bash

pyinstaller -D -w -i "icon.ico" main.py

# clean
# rm -fr dist/ build/ *.spec