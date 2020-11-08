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

import bpy
import types
from functools import wraps

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


class UIF_AddPanelOperator(bpy.types.Operator):
    bl_idname = "object.uif_addpanel"
    bl_label = "UIF Add Panel"

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__package__].preferences

        new_panel = addon_prefs.panels.add()
        new_panel.name = "bpy.types.VIEW3D_PT_view3d_properties"

        new_panel = addon_prefs.panels.add()
        new_panel.name = "bpy.types.VIEW3D_PT_view3d_cursor"

        new_panel = addon_prefs.panels.add()
        new_panel.name = "bpy.types.VIEW3D_PT_meta_panel"

        return {'FINISHED'}



class UIF_HidePanelsOperator(bpy.types.Operator):
    bl_idname = "object.uif_hide_panels"
    bl_label = "UIF Hide Panels"

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__package__].preferences

        for item in addon_prefs.panels:
            global panel
            panel = None
            command = "global panel; panel = " + item.name
            exec(command)

            @add_method(panel)
            def poll(cls, context):
                return False

        return {'FINISHED'}