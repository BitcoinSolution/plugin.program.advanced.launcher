"""
    Plugin for Launching programs
"""

# -*- coding: UTF-8 -*-
# main imports
import sys
import os

# plugin constants
__plugin__ = "X-Gaming Addon"
__author__ = "Xeno-Gaming"
__url__ = "https://github.com/BitcoinSolution/plugin.program.advanced.launcher"
__git_url__ = "https://github.com/BitcoinSolution/plugin.program.advanced.launcher"
__credits__ = "Xeno-Gaming"
__version__ = "1.0.1"

if ( __name__ == "__main__" ):
    import resources.lib.launcher_plugin as plugin
    plugin.Main()
