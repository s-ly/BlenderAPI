import bpy

# Оператор, выполняющий действие
class HelloWorldOperator(bpy.types.Operator):
    bl_idname = "wm.hello_world"
    bl_label = "Say Hello"

    def execute(self, context):
        print("Hello World")
        return {'FINISHED'}

# Панель в интерфейсе
class HelloWorldPanel(bpy.types.Panel):
    bl_label = "Hello World Panel"
    bl_idname = "OBJECT_PT_hello_world"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Demo Panel"

    def draw(self, context):
        layout = self.layout
        layout.operator(HelloWorldOperator.bl_idname, text="Click Me!")

# Регистрация классов
def register():
    bpy.utils.register_class(HelloWorldOperator)
    bpy.utils.register_class(HelloWorldPanel)

def unregister():
    bpy.utils.unregister_class(HelloWorldOperator)
    bpy.utils.unregister_class(HelloWorldPanel)

if __name__ == "__main__":
    register()
