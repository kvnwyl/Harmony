# Harmony

>Automation. Perfection.

Harmony is a customisable tool for running through a set of python scripts (called plugins) sequentially.

# Usage

Running the `Harmony.py` will automatically run through all plugins located in the plugins directory.

## Creating a Plugin

To create a plugin, create a new directory in the `plugins` directory with the name of the plugin. Within this folder, create your main class as the name of your plugin in the `.py` format.

To fully utilise the capabilities of a plugin, your class should inherit from the `Plugin` class.

Additionally, if additional configuration items are required for the plugin, a JSON configuration file can be included under the condition that it follows the convention `nameofplugin_config.json`.

# Origin

Originally developed to assist in automating custom builds, the tool was extended to support any amount of plugins, making the tool incredible extensible.

# Notes

Due to the way that Harmony executes scripts, it can be seen as very unsafe and therefore caution is advised when creating plugins.