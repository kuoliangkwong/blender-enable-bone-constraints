bl_info = {
    "name": "Enable Bone Constraints",
    "author": "KKL",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "Pose Mode > Right Click > Pose Context Menu",
    "description": "Show/hide bone constraints for selected pose bones",    
    "category": "Pose"}

import bpy
from bpy.types import Menu

# EBC aka Enable Bone Constraint

class EBC_operator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Enable Bone Constraints"
    enum_items = (('SHOW','Show','True'),('HIDE','Hide','False'))
    myprop = bpy.props.EnumProperty(items=enum_items)

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        enum_items_dict = {id: name for id, name, desc in self.enum_items}
        showStr = next(desc for id, name, desc in self.enum_items if id == self.myprop)
        show = showStr.lower() == "true"
        for poseBone in bpy.context.selected_pose_bones:
            for constraint in poseBone.constraints:
                constraint.mute = not show
        return {'FINISHED'}
        
def menu_func(self, context):
    layout = self.layout
    layout.separator()
    layout.operator_menu_enum(EBC_operator.bl_idname, "myprop", text=EBC_operator.bl_label)

classes = (
    EBC_operator,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_pose_context_menu.append(menu_func)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_pose_context_menu.append(menu_func)

if __name__ == "__main__":
    register()
