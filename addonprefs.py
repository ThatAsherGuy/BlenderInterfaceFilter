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
import os
import rna_keymap_ui

# So the general idea here is to generate a list of panel names, along with a show/hide flag.
# Since Blender doesn't have a StringVector property, we're using a collection of property groups.
# This hacky dictionary is stored here in the add-on properties, so we can iterate through it on startup.
# Theoretically. Still need to figure out the un-hiding part.

class FilterPanel(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(name="Test Property", default="Unknown")
    hide: bpy.props.BoolProperty(name="Test Property", default=True)


class UIF_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    panels: bpy.props.CollectionProperty(
        type=FilterPanel,
        name="Filtered Panels",
        description="A list of panels which will be forcibly disabled via method patching")

    def draw(self, context):
        layout = self.layout

        column = layout.column(align=True)

        for panel in self.panels:
            row = column.row()
            row.label(text=panel.name)