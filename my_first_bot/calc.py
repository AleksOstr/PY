import math

allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

def evaluate(expression: str):
    code = compile(expression, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"The use of '{name}' is not allowed")
    return str(eval(code, {"__builtins__": {}}, allowed_names))