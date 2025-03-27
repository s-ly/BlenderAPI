import bpy

def process_object():
    # Проверка выделенных объектов
    if not bpy.context.selected_objects:
        print("Нет выделенных объектов")
        return False
    
    original_obj = bpy.context.active_object
    
    # Проверка типа объекта
    if original_obj.type != 'MESH':
        print("Выделенный объект не является мешем")
        return False

    # 1. Копирование объекта
    bpy.ops.object.duplicate()
    duplicated_obj = bpy.context.active_object
    
    # 2. Clear parent with keep transformation (исправленная часть)
    if duplicated_obj.parent:
        # Сохраняем текущий выбор
        prev_selection = bpy.context.selected_objects
        prev_active = bpy.context.active_object
        
        # Выделяем только дублированный объект
        bpy.ops.object.select_all(action='DESELECT')
        duplicated_obj.select_set(True)
        bpy.context.view_layer.objects.active = duplicated_obj
        
        # Выполняем очистку родителя
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        
        # Восстанавливаем выбор
        for obj in prev_selection:
            obj.select_set(True)
        bpy.context.view_layer.objects.active = prev_active
    
    # 3. Apply Armature modifier as Shape Key
    armature_mod = None
    for mod in duplicated_obj.modifiers:
        if mod.type == 'ARMATURE':
            armature_mod = mod
            break
    
    if armature_mod:
        if not duplicated_obj.data.shape_keys:
            basis = duplicated_obj.shape_key_add(name='Basis')
        
        try:
            # Применяем модификатор как форму
            bpy.ops.object.modifier_apply_as_shapekey(
                modifier=armature_mod.name, 
                keep_modifier=False
            )
            print("Арматура применена как Shape Key")
        except Exception as e:
            print(f"Ошибка: {str(e)}")
            return False
    else:
        print("Не найден Armature модификатор")
        return False
    
    return True

if __name__ == "__main__":
    process_object()