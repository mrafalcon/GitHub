import inspect

def foo():
    # возьми текущий фрейм объект (frame object)
    current_frame = inspect.currentframe()
    # получи фрейм объект, который его вызвал
    caller_frame = current_frame.f_back
    # возьми у вызвавшего фрейма исполняемый в нём объект типа "код" (code object)
    code_obj = caller_frame.f_code
    # и получи его имя
    code_obj_name = code_obj.co_name
    print("Имя вызывающего объекта: ", code_obj_name)
