# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Hell is other people's code.

bl_info = {
    "name" : "Interface Filter",
    "author" : "Asher",
    "description" : "Want to hide panels? With this add-on, you can hide any panel with a poll function. Theoretically.",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "Runtime method patching is always a recipe for hacky weirdness. Use at your own risk.",
    "category" : "UI"
}

import bpy
import types
from functools import wraps
from . import auto_load
from . import addonprefs
from . import operators

# Declaring this globally. Not sure why, but I have to.
panel = None


# Yoinked from: https://medium.com/@mgarod/dynamically-add-a-method-to-a-class-in-python-c49204b85bd6 
def add_method(cls):
    def decorator(func):
        @wraps(func)
        def wrapper(cls, context): 
            return func(cls, context) 

        cls.poll = types.MethodType(wrapper, cls)

        return func 
    return decorator


def nuke(cls, context):
    return False


auto_load.init()

def register():
    auto_load.register()

    # preferences = bpy.context.preferences
    # addon_prefs = preferences.addons[__package__].preferences

    # for item in addon_prefs.panels:
    #     if item.hide:
    #         global panel
    #         panel = None
    #         command = "panel = " + item.name
    #         exec(command)
    #         print(command)

    #         @add_method(panel)
    #         def poll(cls, context):
    #             return False

def unregister():
    auto_load.unregister()
