import json

# given a json schema enum, return an equivalent python enum
def enum(type_):
    if type_["type"] == "string":
        return f'''{type_["id"]} = Enum("{type_["id"]}", "{" ".join(type_["enum"])}")
{type_["id"]}.__doc__ = """{type_.get("description", "")}"""

'''
    else:
        print(type_)
        1/0

def typemap(typ):
    return {
        "string": "str",
        "integer": "int",
        "number": "float",
        "array": "List",
        "boolean": "bool",
        "any": "Any",
        # if we get here, the spec is for a dict<any, any>
        "object": "dict",
    }[typ]

def handle_properties(properties):
    dependencies = []
    constructor_args = ["self"]
    args = []

    for p in properties:
        if "$ref" in p:
            ref = p["$ref"].split(".")
            if len(ref) > 1:
                dependencies.append(ref[0])
            ptype = f'"{p["$ref"]}"'
        else:
            # TODO: handle array sub-types here
            # TODO: handle enum sub-types above
            ptype = typemap(p["type"])

        if p.get("type") == "object" and "properties" in p:
            # allow objects to pass as long as the spec means
            # dict<any, any> and not a recursive object
            print(p)
            1/0

        if p.get("optional"):
            constructor_args.append(f'{p["name"]}: {ptype}=None')
        else:
            constructor_args.append(f'{p["name"]}: {ptype}')

        if "description" in p:
            args.append(f'# {p["description"]}')

        args.append(f'self.{p["name"]} = {p["name"]}')

    return dependencies, constructor_args, args

def object_(type_):
    if "properties" not in type_:
        return ([], f'class {type_["id"]}: pass\n\n')

    props = sorted(type_["properties"], key=lambda x: x.get("optional", False))
    dependencies, constructor_args, args = handle_properties(props)

    docstring = f'\n    """{type_["description"]}"""' if "description" in type_ else ""

    return (dependencies, f'''class {type_["id"]}:{docstring}
    def __init__({', '.join(constructor_args)}):
        ''' + '\n        '.join(args) + "\n\n")

def array(type_):
    # TODO: convert to ta tuple if there is minitems and maxitems?
    # ex: {'id': 'Quad', 'type': 'array', 'items': {'type': 'number'}, 'minItems': 8, 'maxItems': 8, 'description': 'An array of quad vertices, x immediately followed by y for each point, points clock-wise.', 'experimental': True}
    # should be a Tuple[float, float, float, float, float, float, float, float] ?
    # there's only this one case though, so I'm not going to stress it.
    out = []
    if "type" in type_["items"]:
        eltype = typemap(type_["items"]["type"])
    else:
        eltype = f'"{type_["items"]["$ref"]}"'

    if "description" in type_:
        out.append(f'# {type_["description"]}\n')
    if "description" in type_["items"]:
        out.append(f'# items: {type_["items"]["description"]}')
    out.append(f'{type_["id"]} = List[{eltype}]\n')

    return "".join(out)

def simple(type_):
    out = []
    ttype = typemap(type_["type"])

    if "description" in type_:
        out.append(f'# {type_["description"]}\n')
    out.append(f'{type_["id"]} = {ttype}\n\n')

    return "".join(out)

def command(cmd, domain):
    name = cmd["name"]
    docstr = f'\n    """{cmd["description"]}"""\n' if "description" in cmd else ''

    props = sorted(cmd.get("parameters", []), key=lambda x: x.get("optional", False))
    dependencies, constructor_args, args = handle_properties(props)

    if args:
        argcode = '\n        ' + '\n        '.join(args) + "\n\n"
    else:
        argcode = " pass"

    return f'''class {name}(ChromeCommand):{docstr}
    def __init__({", ".join(constructor_args)}):{argcode}

'''

if __name__=="__main__":
    protocol = json.loads(open("protocol.json", ).read())
    for domain in protocol["domains"]:
        name = domain["domain"]
        types = []
        commands = []
        dependencies = set()
        for type_ in domain.get("types", []):
            if "enum" in type_: types.append(enum(type_))
            elif type_["type"] in ["string", "integer", "number"]:
                types.append(simple(type_))
            elif type_["type"] == "object":
                deps, typeobj = object_(type_)
                dependencies.update(deps)
                types.append(typeobj)
            # TODO array
            elif type_["type"] == "array": types.append(array(type_))
            else: 1/0

        for cmd in domain.get("commands", []):
            commands.append(command(cmd, domain["domain"]))

        mod = open(f"chrome_control/{name}.py", 'w')
        mod.write("""from enum import Enum
from typing import Any, List

from .base import ChromeCommand

""")

        for dep in dependencies:
            mod.write(f'from . import {dep}\n')

        # TODO: objects have to be defined before being referenced fffuuuuu
        #       so if class A has a parameter of type B, type B must appear
        #       in the source file above type A
        mod.write('\n')
        mod.write(''.join(types))

        mod.write(''.join(commands))
