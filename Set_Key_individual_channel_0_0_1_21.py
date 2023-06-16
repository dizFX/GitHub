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


# Set Key Class

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
                    bone_qw.keyframe_insert(data_path="rotation_quaternion", index=0)
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
                bone_qw.keyframe_insert(data_path="rotation_quaternion", index=0)

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
                    bone_qx.keyframe_insert(data_path="rotation_quaternion", index=1)
            print('QUATERNION only')

        #Euler only X
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for bone_ex in bpy.context.selected_pose_bones:
                print(bone_ex.rotation_mode)
                if bone_ex.rotation_mode!='QUATERNION':
                    bone_ex.keyframe_insert(data_path="rotation_euler", index=0)
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
                bone_qx.keyframe_insert(data_path="rotation_quaternion", index=1)

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
                    bone_qy.keyframe_insert(data_path="rotation_quaternion", index=2)
            print('QUATERNION only')

        #Euler only Y
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for bone_ey in bpy.context.selected_pose_bones:
                print(bone_ey.rotation_mode)
                if bone_ey.rotation_mode!='QUATERNION':
                    bone_ey.keyframe_insert(data_path="rotation_euler", index=1)
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
                bone_qy.keyframe_insert(data_path="rotation_quaternion", index=2)

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
                    bone_qz.keyframe_insert(data_path="rotation_quaternion", index=3)
            print('QUATERNION only')

        #Euler only Z
        if (QUATERNION==0 and XYZ+XZY+YXZ+YZX+ZXY+ZYX>=1):
            for bone_ez in bpy.context.selected_pose_bones:
                print(bone_ez.rotation_mode)
                if bone_ez.rotation_mode!='QUATERNION':
                    bone_ez.keyframe_insert(data_path="rotation_euler", index=2)
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
                bone_qz.keyframe_insert(data_path="rotation_quaternion", index=3)

        return {'FINISHED'}


# Dynamic menu

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
    self.layout.operator(CustomDrawOperatorRotW.bl_idname, text="Custom Draw Operator Rot W")

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
    self.layout.operator(CustomDrawOperatorRotX.bl_idname, text="Custom Draw Operator Rot X")

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
    self.layout.operator(CustomDrawOperatorRotY.bl_idname, text="Custom Draw Operator Rot Y")

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
    self.layout.operator(CustomDrawOperatorRotZ.bl_idname, text="Custom Draw Operator Rot Z")


# Pie Menu

class PIE_MT_SetKeyPose_Pie_menu(Menu):
    bl_label = "Pie Menu Set Key Pose"
    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator("wm.call_menu_pie", text = "Loc", icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyPoseLoc_Pie_menu"
        pie.operator("wm.call_menu_pie", text = "Scale", icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyPoseScale_Pie_menu"
        pie.operator("wm.call_menu_pie", text = "Rot", icon = "RIGHTARROW_THIN").name="PIE_MT_SetKeyPoseRot_Pie_menu"

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


# Pie Menu Button

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


# Panel

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


# All Classes and Function for Register

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
    POSE_PT_SetKeyICh_Panel,
]

menu_funcs = [
    menu_func_rot_w,
    menu_func_rot_x,
    menu_func_rot_y,
    menu_func_rot_z,
]


# All Register

# Register and add to the object menu (required to also use F3 search "Custom Draw Operator" for quick access).
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
