# MaterialX export for Substance Painter

This plugin adds support for simple MaterialX support for Substance Painter.
It currently only support arnold and Metallic/Roughness workflows

## Prerequisites
* Substance Painter
* Python in path (currently only tested with python 2.7)
* MaterialX installed for the python interpreter in path (only tested with 1.36)

## Installation
Install the plugin using the deploy.bat script
A correctly installed plugin should look something like this in the Painter documents directory:
```
plugins
└───materialx-export
    │   ExportTools.js
    │   main.qml
    │   MaterialXExport.qml
    │   Style.qml
    │   tool-bar.qml
    │
    └───python
        │   materialx_export.py
        │   write_sample.py
        │
        └───matxtools
                matxtools.py
                __init__.py
```

## Running
A correctly installed plugin will show up as a button in painter. 

To export:
* Click the plugin button
* Type in/browse for the location and file you want to export the textures. 
The expected input is the MaterialX file to write, the textures for it will be written in the same
directory as the MaterialX file
* Click the export button

When the path is setup you can easily reexport the textures by clicking export again
  