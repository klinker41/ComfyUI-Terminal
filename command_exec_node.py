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
                "command": ("STRING", {
                    "multiline": True,
                    "default": "echo Hello World"
                }),
            },
            "optional": {
                "a": (any, ),
                "b": (any, ),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run_command"
    CATEGORY = "Custom/Utility"

    def run_command(self, command, a=None, b=None):
        import subprocess
        
        variable_declarations = []
        if a is not None:
            variable_declarations.append(f"a='{a}'")
        if b is not None:
            variable_declarations.append(f"b='{b}'")

        # Create the final script
        complete_script = "\n".join(variable_declarations) + "\n" + bash_script
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
