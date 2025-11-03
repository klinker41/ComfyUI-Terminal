import subprocess

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_typ = AnyType("*")

class CommandExecNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "script": ("STRING", {
                    "multiline": True,
                    "default": "echo Hello World"
                }),
            },
            "optional": {
                "a": (any_typ, ),
                "b": (any_typ, ),
                "c": (any_typ, ),
                "d": (any_typ, ),
                "e": (any_typ, ),
                "f": (any_typ, ),
                "g": (any_typ, ),
                "h": (any_typ, ),
                "i": (any_typ, ),
                "j": (any_typ, ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run_command"
    CATEGORY = "Custom/Utility"

    def run_command(self, script, a=None, b=None, c=None, d=None, e=None, f=None, g=None, h=None, i=None, j=None):
        import subprocess
        
        variable_declarations = []
        if a is not None:
            variable_declarations.append(f"a='{a}'")
        if b is not None:
            variable_declarations.append(f"b='{b}'")
        if c is not None:
            variable_declarations.append(f"c='{c}'")
        if d is not None:
            variable_declarations.append(f"d='{d}'")
        if e is not None:
            variable_declarations.append(f"e='{e}'")
        if f is not None:
            variable_declarations.append(f"f='{f}'")
        if g is not None:
            variable_declarations.append(f"g='{g}'")
        if h is not None:
            variable_declarations.append(f"h='{h}'")
        if i is not None:
            variable_declarations.append(f"i='{i}'")
        if j is not None:
            variable_declarations.append(f"j='{j}'")

        # Create the final script
        complete_script = "\n".join(variable_declarations) + "\n" + script
        try:
            result = subprocess.check_output(
                complete_script, shell=True, stderr=subprocess.STDOUT, universal_newlines=True
            )
        except subprocess.CalledProcessError as e:
            result = f"[ERROR] Code {e.returncode}:\n{e.output}"
        return (result,)


# Registro do node no ComfyUI
NODE_CLASS_MAPPINGS = {
    "CommandExecNode": CommandExecNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CommandExecNode": "Terminal"
}
