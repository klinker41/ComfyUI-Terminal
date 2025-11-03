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
        import os
        
        env = os.environ.copy()
    
        variables = {
            'a': a, 'b': b, 'c': c, 'd': d, 'e': e,
            'f': f, 'g': g, 'h': h, 'i': i, 'j': j
        }
        
        for name, value in variables.items():
            if value is not None:
                env[name] = str(value)
                
        try:
            result = subprocess.check_output(
                script, shell=True, stderr=subprocess.STDOUT, text=True, env=env
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
