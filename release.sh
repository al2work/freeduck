#!/bin/bash

# pyinstaller -D -w -i "icon.ico" main.py

pyinstaller --onefile --windowed --name "FreeDuck" --icon "icon.ico" main.py

# --onefile: Bundles everything into a single executable file (e.g., your_script_name.exe on Windows). If omitted, PyInstaller creates a directory containing the executable and its dependencies.
# --name "YourAppName": Specifies the name for the output executable and the generated .spec file.
# --windowed or --noconsole: Creates a GUI application without a console window. This is useful for applications with a graphical user interface.
# --add-data "source_path;destination_path": Includes additional data files (e.g., images, configuration files) in the bundle. The destination_path is relative to the root of the bundled application.
# --icon "icon.ico": Specifies a custom icon for the executable.