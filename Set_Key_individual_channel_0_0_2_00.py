bl_info = {
    'name': "Set_Key_I_Ch",
    'author': "dizFX, Konstantin Coufal, Andrey Maslennikov",
    'version': (0, 0, 1),
    'blender': (3, 5, 1),
    'description': "Set Key individual channal",
    "location": "View3D > N Panel",
    "category": "Tools",
}

import bpy
from random import randint
from bpy.types import (
    Operator,
    Panel,
    PropertyGroup,
    Object,
    Menu
    )
from bpy.utils import register_class, unregister_class


# Pose Mode or Object Mode

def set_bone_pose_mode():
    mode_armature = bpy.context.active_object.mode
    if mode_armature == 'POSE':
        return 0
    else:
        return 1

def set_bone_object_mode():
    mode_object = bpy.context.active_object.mode
    if mode_object == 'OBJECT':
        return 0
    else:
        return 1


# Set Key Class Pose

class SetKeyIChPoseLocationX(Operator):
    """Set Key Pose Location X"""
    bl_idname = "pose.set_key_location_x"
    bl_label = "lX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone in bpy.context.selected_pose_bones:
            bone.keyframe_insert(data_path="location", index=0)

        return {'FINISHED'}

class SetKeyIChPoseLocationY(Operator):
    """Set Key Pose Location Y"""
    bl_idname = "pose.set_key_location_y"
    bl_label = "lY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone in bpy.context.selected_pose_bones:
            bone.keyframe_insert(data_path="location", index=1)

        return {'FINISHED'}

class SetKeyIChPoseLocationZ(Operator):
    """Set Key Pose Location Y"""
    bl_idname = "pose.set_key_location_z"
    bl_label = "lZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone in bpy.context.selected_pose_bones:
            bone.keyframe_insert(data_path="location", index=2)

        return {'FINISHED'}

class SetKeyIChPoseScaleX(Operator):
    """Set Key Pose Scale X"""
    bl_idname = "pose.set_key_scale_x"
    bl_label = "sX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone in bpy.context.selected_pose_bones:
            bone.keyframe_insert(data_path="scale", index=0)

        return {'FINISHED'}

class SetKeyIChPoseScaleY(Operator):
    """Set Key Pose Scale Y"""
    bl_idname = "pose.set_key_scale_y"
    bl_label = "sY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone in bpy.context.selected_pose_bones:
            bone.keyframe_insert(data_path="scale", index=1)

        return {'FINISHED'}

class SetKeyIChPoseScaleZ(Operator):
    """Set Key Pose Scale Y"""
    bl_idname = "pose.set_key_scale_z"
    bl_label = "sZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone in bpy.context.selected_pose_bones:
            bone.keyframe_insert(data_path="scale", index=2)

        return {'FINISHED'}

class SetKeyIChPoseRotationW(Operator):
    """Set Key Pose Rotation W"""
    bl_idname = "pose.set_key_rotation_w"
    bl_label = "rW"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        XYZ = 0
        XZY = 0
        YXZ = 0
        YZX = 0
        ZXY = 0
        ZYX = 0
        QUATERNION = 0

        for bone in bpy.context.selected_pose_bones:
            mode = bone.rotation_mode

            if mode=='XYZ':
                XYZ = 1
            if mode=='XZY':
                XZY = 1
            if mode=='YXZ':
                YXZ = 1
            if mode=='YZX':
                YZX = 1
            if mode=='ZXY':
                ZXY = 1
            if mode=='ZYX':
                ZYX = 1
            if mode=='QUATERNION':
                QUATERNION = 1

        #Quaternion only W
        if (QUATERNION==1
            and XYZ==0
            and XZY==0
            and YXZ==0
            and YZX==0
            and ZXY==0
            and ZYX==0):
            for bone_qw in bpy.context.selected_pose_bones:
                print(bone_qw.rotation_mode)
                if bone_qw.rotation_mode=='QUATERNION':
                    bone_qw.keyframe_insert(data_path="rotation_quaternion",
                                            index=0)
            print('QUATERNION only')

        #Euler only W
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for bone_ew in bpy.context.selected_pose_bones:
                print(bone_ew.rotation_mode)
                if bone_ew.rotation_mode!='QUATERNION':
                    print('Euler only')
            print('Euler only No W')

        #Quaternion and Euler W
        if (QUATERNION==1 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            bpy.ops.object.custom_draw_rot_w('INVOKE_DEFAULT')
            print('Quaternion and Euler')

        return {'FINISHED'}

class SetKeyIChPoseRotationEulerW(Operator):
    """Set Key Pose Rotation Euler W"""
    bl_idname = "pose.set_key_rotation_euler_w"
    bl_label = "Rot Euler No W"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone_ew in bpy.context.selected_pose_bones:
            print(bone_ew.rotation_mode)
            if bone_ew.rotation_mode!='QUATERNION':
                print('Euler only')

        return {'FINISHED'}

class SetKeyIChPoseRotationQuaternionW(Operator):
    """Set Key Pose Rotation Quaternion W"""
    bl_idname = "pose.set_key_rotation_quaternion_w"
    bl_label = "Rot Quat W"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone_qw in bpy.context.selected_pose_bones:
            print(bone_qw.rotation_mode)
            if bone_qw.rotation_mode=='QUATERNION':
                bone_qw.keyframe_insert(data_path="rotation_quaternion",
                                        index=0)

        return {'FINISHED'}

class SetKeyIChPoseRotationX(Operator):
    """Set Key Pose Rotation X"""
    bl_idname = "pose.set_key_rotation_x"
    bl_label = "rX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        XYZ = 0
        XZY = 0
        YXZ = 0
        YZX = 0
        ZXY = 0
        ZYX = 0
        QUATERNION = 0

        for bone in bpy.context.selected_pose_bones:
            mode = bone.rotation_mode

            if mode=='XYZ':
                XYZ = 1
            if mode=='XZY':
                XZY = 1
            if mode=='YXZ':
                YXZ = 1
            if mode=='YZX':
                YZX = 1
            if mode=='ZXY':
                ZXY = 1
            if mode=='ZYX':
                ZYX = 1
            if mode=='QUATERNION':
                QUATERNION = 1

        #Quaternion only X
        if (QUATERNION==1
            and XYZ==0
            and XZY==0
            and YXZ==0
            and YZX==0
            and ZXY==0
            and ZYX==0):
            for bone_qx in bpy.context.selected_pose_bones:
                print(bone_qx.rotation_mode)
                if bone_qx.rotation_mode=='QUATERNION':
                    bone_qx.keyframe_insert(data_path="rotation_quaternion",
                                            index=1)
            print('QUATERNION only')

        #Euler only X
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for bone_ex in bpy.context.selected_pose_bones:
                print(bone_ex.rotation_mode)
                if bone_ex.rotation_mode!='QUATERNION':
                    bone_ex.keyframe_insert(data_path="rotation_euler",
                                            index=0)
            print('Euler only')

        #Quaternion and Euler X
        if (QUATERNION==1 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            bpy.ops.object.custom_draw_rot_x('INVOKE_DEFAULT')
            print('Quaternion and Euler')

        return {'FINISHED'}

class SetKeyIChPoseRotationEulerX(Operator):
    """Set Key Pose Rotation Euler X"""
    bl_idname = "pose.set_key_rotation_euler_x"
    bl_label = "Rot Euler X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone_ex in bpy.context.selected_pose_bones:
            print(bone_ex.rotation_mode)
            if bone_ex.rotation_mode!='QUATERNION':
                bone_ex.keyframe_insert(data_path="rotation_euler", index=0)

        return {'FINISHED'}

class SetKeyIChPoseRotationQuaternionX(Operator):
    """Set Key Pose Rotation Quaternion X"""
    bl_idname = "pose.set_key_rotation_quaternion_x"
    bl_label = "Rot Quat X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone_qx in bpy.context.selected_pose_bones:
            print(bone_qx.rotation_mode)
            if bone_qx.rotation_mode=='QUATERNION':
                bone_qx.keyframe_insert(data_path="rotation_quaternion",
                                        index=1)

        return {'FINISHED'}

class SetKeyIChPoseRotationY(Operator):
    """Set Key Pose Rotation Y"""
    bl_idname = "pose.set_key_rotation_y"
    bl_label = "rY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        XYZ = 0
        XZY = 0
        YXZ = 0
        YZX = 0
        ZXY = 0
        ZYX = 0
        QUATERNION = 0

        for bone in bpy.context.selected_pose_bones:
            mode = bone.rotation_mode

            if mode=='XYZ':
                XYZ = 1
            if mode=='XZY':
                XZY = 1
            if mode=='YXZ':
                YXZ = 1
            if mode=='YZX':
                YZX = 1
            if mode=='ZXY':
                ZXY = 1
            if mode=='ZYX':
                ZYX = 1
            if mode=='QUATERNION':
                QUATERNION = 1

        #Quaternion only Y
        if (QUATERNION==1
            and XYZ==0
            and XZY==0
            and YXZ==0
            and YZX==0
            and ZXY==0
            and ZYX==0):
            for bone_qy in bpy.context.selected_pose_bones:
                print(bone_qy.rotation_mode)
                if bone_qy.rotation_mode=='QUATERNION':
                    bone_qy.keyframe_insert(data_path="rotation_quaternion",
                                            index=2)
            print('QUATERNION only')

        #Euler only Y
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for bone_ey in bpy.context.selected_pose_bones:
                print(bone_ey.rotation_mode)
                if bone_ey.rotation_mode!='QUATERNION':
                    bone_ey.keyframe_insert(data_path="rotation_euler",
                                            index=1)
            print('Euler only')

        #Quaternion and Euler Y
        if (QUATERNION==1 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            bpy.ops.object.custom_draw_rot_y('INVOKE_DEFAULT')
            print('Quaternion and Euler')

        return {'FINISHED'}

class SetKeyIChPoseRotationEulerY(Operator):
    """Set Key Pose Rotation Euler Y"""
    bl_idname = "pose.set_key_rotation_euler_y"
    bl_label = "Rot Euler Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone_ey in bpy.context.selected_pose_bones:
            print(bone_ey.rotation_mode)
            if bone_ey.rotation_mode!='QUATERNION':
                bone_ey.keyframe_insert(data_path="rotation_euler", index=1)

        return {'FINISHED'}

class SetKeyIChPoseRotationQuaternionY(Operator):
    """Set Key Pose Rotation Quaternion Y"""
    bl_idname = "pose.set_key_rotation_quaternion_y"
    bl_label = "Rot Quat Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone_qy in bpy.context.selected_pose_bones:
            print(bone_qy.rotation_mode)
            if bone_qy.rotation_mode=='QUATERNION':
                bone_qy.keyframe_insert(data_path="rotation_quaternion",
                                        index=2)

        return {'FINISHED'}

class SetKeyIChPoseRotationZ(Operator):
    """Set Key Pose Rotation Z"""
    bl_idname = "pose.set_key_rotation_z"
    bl_label = "rZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        XYZ = 0
        XZY = 0
        YXZ = 0
        YZX = 0
        ZXY = 0
        ZYX = 0
        QUATERNION = 0

        for bone in bpy.context.selected_pose_bones:
            mode = bone.rotation_mode

            if mode=='XYZ':
                XYZ = 1
            if mode=='XZY':
                XZY = 1
            if mode=='YXZ':
                YXZ = 1
            if mode=='YZX':
                YZX = 1
            if mode=='ZXY':
                ZXY = 1
            if mode=='ZYX':
                ZYX = 1
            if mode=='QUATERNION':
                QUATERNION = 1

        #Quaternion only Z
        if (QUATERNION==1
            and XYZ==0
            and XZY==0
            and YXZ==0
            and YZX==0
            and ZXY==0
            and ZYX==0):
            for bone_qz in bpy.context.selected_pose_bones:
                print(bone_qz.rotation_mode)
                if bone_qz.rotation_mode=='QUATERNION':
                    bone_qz.keyframe_insert(data_path="rotation_quaternion",
                                            index=3)
            print('QUATERNION only')

        #Euler only Z
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for bone_ez in bpy.context.selected_pose_bones:
                print(bone_ez.rotation_mode)
                if bone_ez.rotation_mode!='QUATERNION':
                    bone_ez.keyframe_insert(data_path="rotation_euler",
                                            index=2)
            print('Euler only')

        #Quaternion and Euler Z
        if (QUATERNION==1 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            bpy.ops.object.custom_draw_rot_z('INVOKE_DEFAULT')
            print('Quaternion and Euler')

        return {'FINISHED'}

class SetKeyIChPoseRotationEulerZ(Operator):
    """Set Key Pose Rotation Euler Z"""
    bl_idname = "pose.set_key_rotation_euler_z"
    bl_label = "Rot Euler Z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone_ez in bpy.context.selected_pose_bones:
            print(bone_ez.rotation_mode)
            if bone_ez.rotation_mode!='QUATERNION':
                bone_ez.keyframe_insert(data_path="rotation_euler", index=2)

        return {'FINISHED'}

class SetKeyIChPoseRotationQuaternionZ(Operator):
    """Set Key Pose Rotation Quaternion Z"""
    bl_idname = "pose.set_key_rotation_quaternion_z"
    bl_label = "Rot Quat Z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for bone_qz in bpy.context.selected_pose_bones:
            print(bone_qz.rotation_mode)
            if bone_qz.rotation_mode=='QUATERNION':
                bone_qz.keyframe_insert(data_path="rotation_quaternion",
                                        index=3)

        return {'FINISHED'}


# Dynamic menu Pose

class CustomDrawOperatorRotW(Operator):
    bl_idname = "object.custom_draw_rot_w"
    bl_label = "Quaternion and Euler are highlighted. W"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("OperatorRotW", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Choose where to place the keys! W")

        row = col.row()
        spl = row.split(align = False)
        spl.operator("pose.set_key_rotation_quaternion_w")

        layout = self.layout
        col = layout.column()
        col.label(text="Or click ok. Without setting the keys. W")

# Dynamic menu W.
def menu_func_rot_w(self, context):
    self.layout.operator(CustomDrawOperatorRotW.bl_idname,
                         text="Custom Draw Operator Rot W")

class CustomDrawOperatorRotX(Operator):
    bl_idname = "object.custom_draw_rot_x"
    bl_label = "Quaternion and Euler are highlighted. X"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("OperatorRotX", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Choose where to place the keys! X")

        row = col.row()
        spl = row.split(align = False)
        spl.operator("pose.set_key_rotation_euler_x")
        spl.operator("pose.set_key_rotation_quaternion_x")

        layout = self.layout
        col = layout.column()
        col.label(text="Or click ok. Without setting the keys. X")

# Dynamic menu X.
def menu_func_rot_x(self, context):
    self.layout.operator(CustomDrawOperatorRotX.bl_idname,
                         text="Custom Draw Operator Rot X")

class CustomDrawOperatorRotY(Operator):
    bl_idname = "object.custom_draw_rot_y"
    bl_label = "Quaternion and Euler are highlighted. Y"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("OperatorRotY", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Choose where to place the keys! Y")

        row = col.row()
        spl = row.split(align = False)
        spl.operator("pose.set_key_rotation_euler_y")
        spl.operator("pose.set_key_rotation_quaternion_y")

        layout = self.layout
        col = layout.column()
        col.label(text="Or click ok. Without setting the keys. Y")

# Dynamic menu Y.
def menu_func_rot_y(self, context):
    self.layout.operator(CustomDrawOperatorRotY.bl_idname,
                         text="Custom Draw Operator Rot Y")

class CustomDrawOperatorRotZ(Operator):
    bl_idname = "object.custom_draw_rot_z"
    bl_label = "Quaternion and Euler are highlighted. Z"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("OperatorRotX", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Choose where to place the keys! Z")

        row = col.row()
        spl = row.split(align = False)
        spl.operator("pose.set_key_rotation_euler_z")
        spl.operator("pose.set_key_rotation_quaternion_z")

        layout = self.layout
        col = layout.column()
        col.label(text="Or click ok. Without setting the keys. Z")

# Dynamic menu Z.
def menu_func_rot_z(self, context):
    self.layout.operator(CustomDrawOperatorRotZ.bl_idname,
                         text="Custom Draw Operator Rot Z")


# Pie Menu Pose

class PIE_MT_SetKeyPose_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Pose"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("wm.call_menu_pie", text = "Loc",
                     icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyPoseLoc_Pie_menu"
        pie.operator("wm.call_menu_pie", text = "Scale",
                     icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyPoseScale_Pie_menu"
        pie.operator("wm.call_menu_pie", text = "Rot",
                     icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyPoseRot_Pie_menu"

class PIE_MT_SetKeyPoseLoc_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Pose Loc"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("pose.set_key_location_x", text = "X loc")
        pie.operator("pose.set_key_location_z", text = "Z loc")
        pie.operator("pose.set_key_location_y", text = "Y loc")

class PIE_MT_SetKeyPoseRot_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Pose Rotation"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("pose.set_key_rotation_x", text = "X rot")
        pie.operator("pose.set_key_rotation_z", text = "Z rot")
        pie.operator("pose.set_key_rotation_y", text = "Y rot")
        pie.operator("pose.set_key_rotation_w", text = "W rot")

class PIE_MT_SetKeyPoseScale_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Pose Scale"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("pose.set_key_scale_x", text = "X sca")
        pie.operator("pose.set_key_scale_z", text = "Z sca")
        pie.operator("pose.set_key_scale_y", text = "Y sca")


# Pie Menu Button Pose

class PieMenuButtonPose(Operator):
    """Pie Menu Button Pose"""
    bl_idname = "pose.pie_pose_all"
    bl_label = "Pie_Pose_All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="PIE_MT_SetKeyPose_Pie_menu")

        return {'FINISHED'}

class PieMenuButtonPoseLocXYZ(Operator):
    """Pie Menu Button Pose Loc XYZ"""
    bl_idname = "pose.pie_pose_loc_xyz"
    bl_label = "L_Pie_XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="PIE_MT_SetKeyPoseLoc_Pie_menu")

        return {'FINISHED'}

class PieMenuButtonPoseRotXYZ(Operator):
    """Pie Menu Button Pose Rot XYZ"""
    bl_idname = "pose.pie_pose_rot_xyz"
    bl_label = "R_Pie_XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="PIE_MT_SetKeyPoseRot_Pie_menu")

        return {'FINISHED'}

class PieMenuButtonPoseScaleXYZ(Operator):
    """Pie Menu Button Pose Scale XYZ"""
    bl_idname = "pose.pie_pose_scale_xyz"
    bl_label = "S_Pie_XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="PIE_MT_SetKeyPoseScale_Pie_menu")

        return {'FINISHED'}


# Set Key Class Object

class SetKeyIChObjectLocationX(Operator):
    """Set Key Object Location X"""
    bl_idname = "object.set_key_object_location_x"
    bl_label = "lX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_lx in bpy.context.selected_objects:
            obj_lx.keyframe_insert(data_path="location", index=0)

        return {'FINISHED'}

class SetKeyIChObjectLocationY(Operator):
    """Set Key Object Location Y"""
    bl_idname = "object.set_key_object_location_y"
    bl_label = "lY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_ly in bpy.context.selected_objects:
            obj_ly.keyframe_insert(data_path="location", index=1)

        return {'FINISHED'}

class SetKeyIChObjectLocationZ(Operator):
    """Set Key Object Location Y"""
    bl_idname = "object.set_key_object_location_z"
    bl_label = "lZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_lz in bpy.context.selected_objects:
            obj_lz.keyframe_insert(data_path="location", index=2)

        return {'FINISHED'}

class SetKeyIChObjectScaleX(Operator):
    """Set Key Object Scale X"""
    bl_idname = "object.set_key_object_scale_x"
    bl_label = "sX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_sx in bpy.context.selected_objects:
            obj_sx.keyframe_insert(data_path="scale", index=0)

        return {'FINISHED'}

class SetKeyIChObjectScaleY(Operator):
    """Set Key Object Scale Y"""
    bl_idname = "object.set_key_object_scale_y"
    bl_label = "sY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_sy in bpy.context.selected_objects:
            obj_sy.keyframe_insert(data_path="scale", index=1)

        return {'FINISHED'}

class SetKeyIChObjectScaleZ(Operator):
    """Set Key Object Scale Y"""
    bl_idname = "object.set_key_object_scale_z"
    bl_label = "sZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_sz in bpy.context.selected_objects:
            obj_sz.keyframe_insert(data_path="scale", index=2)

        return {'FINISHED'}

class SetKeyIChObjectRotationW(Operator):
    """Set Key Object Rotation W"""
    bl_idname = "object.set_key_object_rotation_w"
    bl_label = "rW"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        XYZ = 0
        XZY = 0
        YXZ = 0
        YZX = 0
        ZXY = 0
        ZYX = 0
        QUATERNION = 0

        for obj in bpy.context.selected_objects:
            mode_obj = obj.rotation_mode

            if mode_obj=='XYZ':
                XYZ = 1
            if mode_obj=='XZY':
                XZY = 1
            if mode_obj=='YXZ':
                YXZ = 1
            if mode_obj=='YZX':
                YZX = 1
            if mode_obj=='ZXY':
                ZXY = 1
            if mode_obj=='ZYX':
                ZYX = 1
            if mode_obj=='QUATERNION':
                QUATERNION = 1

        #Quaternion only W
        if (QUATERNION==1
            and XYZ==0
            and XZY==0
            and YXZ==0
            and YZX==0
            and ZXY==0
            and ZYX==0):
            for obj_qw in bpy.context.selected_objects:
                print(obj_qw.rotation_mode)
                if obj_qw.rotation_mode=='QUATERNION':
                    obj_qw.keyframe_insert(data_path="rotation_quaternion",
                                            index=0)
            print('QUATERNION only Object')

        #Euler only W
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for obj_ew in bpy.context.selected_objects:
                print(obj_ew.rotation_mode)
                if obj_ew.rotation_mode!='QUATERNION':
                    print('Euler only Object')
            print('Euler only No W Object')

        #Quaternion and Euler W
        if (QUATERNION==1 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            bpy.ops.object.custom_draw_object_rot_w('INVOKE_DEFAULT')
            print('Quaternion and Euler Object')

        return {'FINISHED'}

class SetKeyIChObjectRotationEulerW(Operator):
    """Set Key Object Rotation Euler W"""
    bl_idname = "object.set_key_objecr_rotation_euler_w"
    bl_label = "Rot Euler No W"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_ew in bpy.context.selected_objects:
            print(obj_ew.rotation_mode)
            if obj_ew.rotation_mode!='QUATERNION':
                print('Euler only Object')

        return {'FINISHED'}

class SetKeyIChObjectRotationQuaternionW(Operator):
    """Set Key Object Rotation Quaternion W"""
    bl_idname = "object.set_key_object_rotation_quaternion_w"
    bl_label = "Rot Quat W"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_qw in bpy.context.selected_objects:
            print(obj_qw.rotation_mode)
            if obj_qw.rotation_mode=='QUATERNION':
                obj_qw.keyframe_insert(data_path="rotation_quaternion",
                                        index=0)

        return {'FINISHED'}

class SetKeyIChObjectRotationX(Operator):
    """Set Key Object Rotation X"""
    bl_idname = "object.set_key_object_rotation_x"
    bl_label = "rX"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        XYZ = 0
        XZY = 0
        YXZ = 0
        YZX = 0
        ZXY = 0
        ZYX = 0
        QUATERNION = 0

        for obj in bpy.context.selected_objects:
            mode_obj = obj.rotation_mode

            if mode_obj=='XYZ':
                XYZ = 1
            if mode_obj=='XZY':
                XZY = 1
            if mode_obj=='YXZ':
                YXZ = 1
            if mode_obj=='YZX':
                YZX = 1
            if mode_obj=='ZXY':
                ZXY = 1
            if mode_obj=='ZYX':
                ZYX = 1
            if mode_obj=='QUATERNION':
                QUATERNION = 1

        #Quaternion only X
        if (QUATERNION==1
            and XYZ==0
            and XZY==0
            and YXZ==0
            and YZX==0
            and ZXY==0
            and ZYX==0):
            for obj_qx in bpy.context.selected_objects:
                print(obj_qx.rotation_mode)
                if obj_qx.rotation_mode=='QUATERNION':
                    obj_qx.keyframe_insert(data_path="rotation_quaternion",
                                           index=1)
            print('QUATERNION only Object')

        #Euler only X
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for obj_ex in bpy.context.selected_objects:
                print(obj_ex.rotation_mode)
                if obj_ex.rotation_mode!='QUATERNION':
                    obj_ex.keyframe_insert(data_path="rotation_euler", index=0)
            print('Euler only Object')

        #Quaternion and Euler X
        if (QUATERNION==1 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            bpy.ops.object.custom_draw_object_rot_x('INVOKE_DEFAULT')
            print('Quaternion and Euler Object')

        return {'FINISHED'}

class SetKeyIChObjectRotationEulerX(Operator):
    """Set Key Object Rotation Euler X"""
    bl_idname = "object.set_key_object_rotation_euler_x"
    bl_label = "Rot Euler X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_ex in bpy.context.selected_objects:
            print(obj_ex.rotation_mode)
            if obj_ex.rotation_mode!='QUATERNION':
                obj_ex.keyframe_insert(data_path="rotation_euler", index=0)

        return {'FINISHED'}

class SetKeyIChObjectRotationQuaternionX(Operator):
    """Set Key Object Rotation Quaternion X"""
    bl_idname = "object.set_key_object_rotation_quaternion_x"
    bl_label = "Rot Quat X"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_qx in bpy.context.selected_objects:
            print(obj_qx.rotation_mode)
            if obj_qx.rotation_mode=='QUATERNION':
                obj_qx.keyframe_insert(data_path="rotation_quaternion",
                                       index=1)

        return {'FINISHED'}

class SetKeyIChObjectRotationY(Operator):
    """Set Key Object Rotation Y"""
    bl_idname = "object.set_key_object_rotation_y"
    bl_label = "rY"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        XYZ = 0
        XZY = 0
        YXZ = 0
        YZX = 0
        ZXY = 0
        ZYX = 0
        QUATERNION = 0

        for obj in bpy.context.selected_objects:
            mode_obj = obj.rotation_mode

            if mode_obj=='XYZ':
                XYZ = 1
            if mode_obj=='XZY':
                XZY = 1
            if mode_obj=='YXZ':
                YXZ = 1
            if mode_obj=='YZX':
                YZX = 1
            if mode_obj=='ZXY':
                ZXY = 1
            if mode_obj=='ZYX':
                ZYX = 1
            if mode_obj=='QUATERNION':
                QUATERNION = 1

        #Quaternion only Y
        if (QUATERNION==1
            and XYZ==0
            and XZY==0
            and YXZ==0
            and YZX==0
            and ZXY==0
            and ZYX==0):
            for obj_qy in bpy.context.selected_objects:
                print(obj_qy.rotation_mode)
                if obj_qy.rotation_mode=='QUATERNION':
                    obj_qy.keyframe_insert(data_path="rotation_quaternion",
                                           index=2)
            print('QUATERNION only Object')

        #Euler only Y
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for obj_ey in bpy.context.selected_objects:
                print(obj_ey.rotation_mode)
                if obj_ey.rotation_mode!='QUATERNION':
                    obj_ey.keyframe_insert(data_path="rotation_euler", index=1)
            print('Euler only Object')

        #Quaternion and Euler Y
        if (QUATERNION==1 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            bpy.ops.object.custom_draw_object_rot_y('INVOKE_DEFAULT')
            print('Quaternion and Euler Object')

        return {'FINISHED'}

class SetKeyIChObjectRotationEulerY(Operator):
    """Set Key Object Rotation Euler Y"""
    bl_idname = "object.set_key_object_rotation_euler_y"
    bl_label = "Rot Euler Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_ey in bpy.context.selected_objects:
            print(obj_ey.rotation_mode)
            if obj_ey.rotation_mode!='QUATERNION':
                obj_ey.keyframe_insert(data_path="rotation_euler", index=1)

        return {'FINISHED'}

class SetKeyIChObjectRotationQuaternionY(Operator):
    """Set Key Object Rotation Quaternion Y"""
    bl_idname = "object.set_key_object_rotation_quaternion_y"
    bl_label = "Rot Quat Y"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_qy in bpy.context.selected_objects:
            print(obj_qy.rotation_mode)
            if obj_qy.rotation_mode=='QUATERNION':
                obj_qy.keyframe_insert(data_path="rotation_quaternion",
                                       index=2)

        return {'FINISHED'}

class SetKeyIChObjectRotationZ(Operator):
    """Set Key Object Rotation Z"""
    bl_idname = "object.set_key_object_rotation_z"
    bl_label = "rZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        XYZ = 0
        XZY = 0
        YXZ = 0
        YZX = 0
        ZXY = 0
        ZYX = 0
        QUATERNION = 0

        for obj in bpy.context.selected_objects:
            mode_obj = obj.rotation_mode

            if mode_obj=='XYZ':
                XYZ = 1
            if mode_obj=='XZY':
                XZY = 1
            if mode_obj=='YXZ':
                YXZ = 1
            if mode_obj=='YZX':
                YZX = 1
            if mode_obj=='ZXY':
                ZXY = 1
            if mode_obj=='ZYX':
                ZYX = 1
            if mode_obj=='QUATERNION':
                QUATERNION = 1

        #Quaternion only Z
        if (QUATERNION==1
            and XYZ==0
            and XZY==0
            and YXZ==0
            and YZX==0
            and ZXY==0
            and ZYX==0):
            for obj_qz in bpy.context.selected_objects:
                print(obj_qz.rotation_mode)
                if obj_qz.rotation_mode=='QUATERNION':
                    obj_qz.keyframe_insert(data_path="rotation_quaternion",
                                           index=3)
            print('QUATERNION only Object')

        #Euler only Z
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for obj_ez in bpy.context.selected_objects:
                print(obj_ez.rotation_mode)
                if obj_ez.rotation_mode!='QUATERNION':
                    obj_ez.keyframe_insert(data_path="rotation_euler",
                                           index=2)
            print('Euler only Object')

        #Quaternion and Euler Z
        if (QUATERNION==1 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            bpy.ops.object.custom_draw_object_rot_z('INVOKE_DEFAULT')
            print('Quaternion and Euler Object')

        return {'FINISHED'}

class SetKeyIChObjectRotationEulerZ(Operator):
    """Set Key Object Rotation Euler Z"""
    bl_idname = "object.set_key_object_rotation_euler_z"
    bl_label = "Rot Euler Z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_ez in bpy.context.selected_objects:
            print(obj_ez.rotation_mode)
            if obj_ez.rotation_mode!='QUATERNION':
                obj_ez.keyframe_insert(data_path="rotation_euler", index=2)

        return {'FINISHED'}

class SetKeyIChObjectRotationQuaternionZ(Operator):
    """Set Key Object Rotation Quaternion Z"""
    bl_idname = "object.set_key_object_rotation_quaternion_z"
    bl_label = "Rot Quat Z"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        for obj_qz in bpy.context.selected_objects:
            print(obj_qz.rotation_mode)
            if obj_qz.rotation_mode=='QUATERNION':
                obj_qz.keyframe_insert(data_path="rotation_quaternion",
                                       index=3)

        return {'FINISHED'}


# Dynamic menu Object

class CustomDrawOperatorObjectRotW(Operator):
    bl_idname = "object.custom_draw_object_rot_w"
    bl_label = "Quaternion and Euler are highlighted. W"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("OperatorObjectRotW", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Choose where to place the keys! W")

        row = col.row()
        spl = row.split(align = False)
        spl.operator("object.set_key_object_rotation_quaternion_w")

        layout = self.layout
        col = layout.column()
        col.label(text="Or click ok. Without setting the keys. W")

# Dynamic menu W.
def menu_func_object_rot_w(self, context):
    self.layout.operator(CustomDrawOperatorObjectRotW.bl_idname,
                         text="Custom Draw Operator Object Rot W")

class CustomDrawOperatorObjectRotX(Operator):
    bl_idname = "object.custom_draw_object_rot_x"
    bl_label = "Quaternion and Euler are highlighted. X"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("OperatorObjectRotX", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Choose where to place the keys! X")

        row = col.row()
        spl = row.split(align = False)
        spl.operator("object.set_key_object_rotation_euler_x")
        spl.operator("object.set_key_object_rotation_quaternion_x")

        layout = self.layout
        col = layout.column()
        col.label(text="Or click ok. Without setting the keys. X")

# Dynamic menu X.
def menu_func_object_rot_x(self, context):
    self.layout.operator(CustomDrawOperatorObjectRotX.bl_idname,
                         text="Custom Draw Operator Object Rot X")

class CustomDrawOperatorObjectRotY(Operator):
    bl_idname = "object.custom_draw_object_rot_y"
    bl_label = "Quaternion and Euler are highlighted. Y"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("OperatorObjectRotY", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Choose where to place the keys! Y")

        row = col.row()
        spl = row.split(align = False)
        spl.operator("object.set_key_object_rotation_euler_y")
        spl.operator("object.set_key_object_rotation_quaternion_y")

        layout = self.layout
        col = layout.column()
        col.label(text="Or click ok. Without setting the keys. Y")

# Dynamic menu Y.
def menu_func_object_rot_y(self, context):
    self.layout.operator(CustomDrawOperatorObjectRotY.bl_idname,
                         text="Custom Draw Operator Object Rot Y")

class CustomDrawOperatorObjectRotZ(Operator):
    bl_idname = "object.custom_draw_object_rot_z"
    bl_label = "Quaternion and Euler are highlighted. Z"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print("OperatorObjectRotX", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.label(text="Choose where to place the keys! Z")

        row = col.row()
        spl = row.split(align = False)
        spl.operator("object.set_key_object_rotation_euler_z")
        spl.operator("object.set_key_object_rotation_quaternion_z")

        layout = self.layout
        col = layout.column()
        col.label(text="Or click ok. Without setting the keys. Z")

# Dynamic menu Z.
def menu_func_object_rot_z(self, context):
    self.layout.operator(CustomDrawOperatorObjectRotZ.bl_idname,
                         text="Custom Draw Operator Object Rot Z")



# Pie Menu Object

class PIE_MT_SetKeyObject_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Object"
    def draw(self, context):
        layout = self.layout
        pie_obj = layout.menu_pie()

        pie_obj.operator("wm.call_menu_pie", text = "Loc",
                         icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyObjectLoc_Pie_menu"
        pie_obj.operator("wm.call_menu_pie", text = "Scale",
                         icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyObjectScale_Pie_menu"
        pie_obj.operator("wm.call_menu_pie", text = "Rot",
                         icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyObjectRot_Pie_menu"

class PIE_MT_SetKeyObjectLoc_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Object Loc"
    def draw(self, context):
        layout = self.layout
        pie_obj = layout.menu_pie()

        pie_obj.operator("object.set_key_object_location_x", text = "X loc")
        pie_obj.operator("object.set_key_object_location_z", text = "Z loc")
        pie_obj.operator("object.set_key_object_location_y", text = "Y loc")

class PIE_MT_SetKeyObjectRot_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Object Rotation"
    def draw(self, context):
        layout = self.layout
        pie_obj = layout.menu_pie()

        pie_obj.operator("object.set_key_object_rotation_x", text = "X rot")
        pie_obj.operator("object.set_key_object_rotation_z", text = "Z rot")
        pie_obj.operator("object.set_key_object_rotation_y", text = "Y rot")
        pie_obj.operator("object.set_key_object_rotation_w", text = "W rot")

class PIE_MT_SetKeyObjectScale_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Object Scale"
    def draw(self, context):
        layout = self.layout
        pie_obj = layout.menu_pie()

        pie_obj.operator("object.set_key_object_scale_x", text = "X sca")
        pie_obj.operator("object.set_key_object_scale_z", text = "Z sca")
        pie_obj.operator("object.set_key_object_scale_y", text = "Y sca")


# Pie Menu Button Object

class PieMenuButtonObject(Operator):
    """Pie Menu Button Object"""
    bl_idname = "object.pie_object_all"
    bl_label = "Pie_Object_All"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="PIE_MT_SetKeyObject_Pie_menu")

        return {'FINISHED'}

class PieMenuButtonObjectLocXYZ(Operator):
    """Pie Menu Button Object XYZ"""
    bl_idname = "object.pie_object_loc_xyz"
    bl_label = "L_Pie_XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="PIE_MT_SetKeyObjectLoc_Pie_menu")

        return {'FINISHED'}

class PieMenuButtonObjectRotXYZ(Operator):
    """Pie Menu Button Object Rot XYZ"""
    bl_idname = "object.pie_object_rot_xyz"
    bl_label = "R_Pie_XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="PIE_MT_SetKeyObjectRot_Pie_menu")

        return {'FINISHED'}

class PieMenuButtonObjectScaleXYZ(Operator):
    """Pie Menu Button Object Scale XYZ"""
    bl_idname = "object.pie_object_scale_xyz"
    bl_label = "S_Pie_XYZ"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        bpy.ops.wm.call_menu_pie(name="PIE_MT_SetKeyObjectScale_Pie_menu")

        return {'FINISHED'}

# Panel All

class POSE_PT_SetKeyICh_Panel(Panel):
    bl_label = "Set Key Individual Channel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SetKeyICh"

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.enabled = not set_bone_pose_mode()
        col.label(text="Pose Mode")
        box = col.box()
        box.label(text="Pie Memu")
        spl = box.split(align = False)
        spl.operator("pose.pie_pose_all")
        spl = box.split(align = False)
        spl.operator("pose.pie_pose_loc_xyz")
        spl.operator("pose.pie_pose_rot_xyz")
        spl.operator("pose.pie_pose_scale_xyz")
        box = col.box()
        box.label(text="Location XYZ")
        spl = box.split(align = False)
        spl.operator("pose.set_key_location_x")
        spl.operator("pose.set_key_location_y")
        spl.operator("pose.set_key_location_z")
        box = col.box()
        box.label(text="Rotation WXYZ")
        spl = box.split(align = False)
        spl.operator("pose.set_key_rotation_w")
        spl.operator("pose.set_key_rotation_x")
        spl.operator("pose.set_key_rotation_y")
        spl.operator("pose.set_key_rotation_z")
        box = col.box()
        box.label(text="Scale XYZ")
        spl = box.split(align = False)
        spl.operator("pose.set_key_scale_x")
        spl.operator("pose.set_key_scale_y")
        spl.operator("pose.set_key_scale_z")

        col = layout.column()
        col.enabled = not set_bone_object_mode()
        col.label(text="Object Mode")
        box = col.box()
        box.label(text="Pie Memu")
        spl = box.split(align = False)
        spl.operator("object.pie_object_all")
        spl = box.split(align = False)
        spl.operator("object.pie_object_loc_xyz")
        spl.operator("object.pie_object_rot_xyz")
        spl.operator("object.pie_object_scale_xyz")
        box = col.box()
        box.label(text="Location XYZ")
        spl = box.split(align = False)
        spl.operator("object.set_key_object_location_x")
        spl.operator("object.set_key_object_location_y")
        spl.operator("object.set_key_object_location_z")
        box = col.box()
        box.label(text="Rotation WXYZ")
        spl = box.split(align = False)
        spl.operator("object.set_key_object_rotation_w")
        spl.operator("object.set_key_object_rotation_x")
        spl.operator("object.set_key_object_rotation_y")
        spl.operator("object.set_key_object_rotation_z")
        box = col.box()
        box.label(text="Scale XYZ")
        spl = box.split(align = False)
        spl.operator("object.set_key_object_scale_x")
        spl.operator("object.set_key_object_scale_y")
        spl.operator("object.set_key_object_scale_z")


# Classes and Function for Register All

classes = [
    SetKeyIChPoseLocationX,
    SetKeyIChPoseLocationY,
    SetKeyIChPoseLocationZ,
    SetKeyIChPoseScaleX,
    SetKeyIChPoseScaleY,
    SetKeyIChPoseScaleZ,
    SetKeyIChPoseRotationW,
    SetKeyIChPoseRotationEulerW,
    SetKeyIChPoseRotationQuaternionW,
    SetKeyIChPoseRotationX,
    SetKeyIChPoseRotationEulerX,
    SetKeyIChPoseRotationQuaternionX,
    SetKeyIChPoseRotationY,
    SetKeyIChPoseRotationEulerY,
    SetKeyIChPoseRotationQuaternionY,
    SetKeyIChPoseRotationZ,
    SetKeyIChPoseRotationEulerZ,
    SetKeyIChPoseRotationQuaternionZ,
    CustomDrawOperatorRotW,
    CustomDrawOperatorRotX,
    CustomDrawOperatorRotY,
    CustomDrawOperatorRotZ,
    PIE_MT_SetKeyPose_Pie_menu,
    PIE_MT_SetKeyPoseLoc_Pie_menu,
    PIE_MT_SetKeyPoseRot_Pie_menu,
    PIE_MT_SetKeyPoseScale_Pie_menu,
    PieMenuButtonPose,
    PieMenuButtonPoseLocXYZ,
    PieMenuButtonPoseRotXYZ,
    PieMenuButtonPoseScaleXYZ,
    SetKeyIChObjectLocationX,
    SetKeyIChObjectLocationY,
    SetKeyIChObjectLocationZ,
    SetKeyIChObjectScaleX,
    SetKeyIChObjectScaleY,
    SetKeyIChObjectScaleZ,
    SetKeyIChObjectRotationW,
    SetKeyIChObjectRotationEulerW,
    SetKeyIChObjectRotationQuaternionW,
    SetKeyIChObjectRotationX,
    SetKeyIChObjectRotationEulerX,
    SetKeyIChObjectRotationQuaternionX,
    SetKeyIChObjectRotationY,
    SetKeyIChObjectRotationEulerY,
    SetKeyIChObjectRotationQuaternionY,
    SetKeyIChObjectRotationZ,
    SetKeyIChObjectRotationEulerZ,
    SetKeyIChObjectRotationQuaternionZ,
    CustomDrawOperatorObjectRotW,
    CustomDrawOperatorObjectRotX,
    CustomDrawOperatorObjectRotY,
    CustomDrawOperatorObjectRotZ,
    PIE_MT_SetKeyObject_Pie_menu,
    PIE_MT_SetKeyObjectLoc_Pie_menu,
    PIE_MT_SetKeyObjectRot_Pie_menu,
    PIE_MT_SetKeyObjectScale_Pie_menu,
    PieMenuButtonObject,
    PieMenuButtonObjectLocXYZ,
    PieMenuButtonObjectRotXYZ,
    PieMenuButtonObjectScaleXYZ,
    POSE_PT_SetKeyICh_Panel,
]

menu_funcs = [
    menu_func_rot_w,
    menu_func_rot_x,
    menu_func_rot_y,
    menu_func_rot_z,
    menu_func_object_rot_w,
    menu_func_object_rot_x,
    menu_func_object_rot_y,
    menu_func_object_rot_z,
]


# Register All

# Register and add to the object menu (required to also use F3 search
# "Custom Draw Operator" for quick access).

for fun in menu_funcs:
    bpy.types.VIEW3D_MT_object.append(fun)

def register():
    for cl in classes:
        register_class(cl)

def unrerister():
    for cl in reversed(classes):
        unregister_class(cl)

if __name__ == '__main__':
    register()
