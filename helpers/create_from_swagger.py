# Read JSON schema, create new python dataclass file

# BUILT-IN
import json
from typing import Literal, Optional
from os import listdir, getenv
from os.path import isfile
from textwrap import dedent



# EXTERNAL

# INTERNAL
from HaloPSA import Halo
import HaloPSA.responses as responses

# CODE

# Setup
HALO_TENANT:str = getenv('HALO_TENANT')
HALO_ID:str = getenv('HALO_CLIENT_ID')
HALO_SECRET:str = getenv('HALO_SECRET')
halo = Halo(tenant=HALO_TENANT, clientid=HALO_ID, secret=HALO_SECRET)

#TODO replace \t with 4 spaces to avoid issues
#TODO add new dataclasses to the __init__ file

# Folders
swagger_file = "helpers/halo_swagger.json"
dataclass_rules_file = "helpers/dataclass_rules.json"
method_rules_file = "helpers/method_rules.json"
dataclass_folder = "HaloPSA/responses"


with open(swagger_file, 'r') as jsonfile:
    json_data = json.loads(jsonfile.read())
    
# Schemas are here
halo_schema = json_data["components"]["schemas"]
halo_methods = json_data["paths"]

with open(dataclass_rules_file, 'r') as jsonfile:
    schemas_to_import = json.loads(jsonfile.read())
    
with open(dataclass_rules_file, 'r') as jsonfile:
    method_rules = json.loads(jsonfile.read())



#TODO move this to a file or something
dataclass_template_str = """# BUILT-IN
import collections
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any
import inspect

# EXTERNAL

#INTERNAL

#CODE
"""



#TODO add a "only create if it doesnt exist" option
child_schema_types = Literal["ignore", "create", "dont_create"] 

def create_dataclass(dataclass_rules:dict, child_schema:child_schema_types="ignore", create_list:bool=False, replace_existing:bool=False, sort:bool=False):
    """Create response dataclasses. To create, the import_rules must atlease contain the schema name as an item. Everything else

    Args:
        dataclass_rules (dict): Importing rules. #TODO allow file path to be provided here instead
        child_schema (child_schema_types, optional): How to handle child schemas. Defaults to "ignore".
        create_list (bool, optional): NO idea what this was for. Defaults to False.
        replace_existing (bool, optional): Replace existing response files. Note that this will NOT check the contents of the file, just whether it exists. Defaults to False.
        sort (bool, optional): Sort the properties alphabetically. Defaults to False (leave original order).

    child_schema_types:
        ignore: Will make the datatype a list
        create: Will create the child dataclass
        dont_create: Will assume the dataclass has already been created.

    Raises:
        ValueError: _description_
        ValueError: _description_
    """
    #TODO complete docstring
    #TODO create a common/shared dataclass file
    #TODO store a list of existing dataclasses that the system can reference to avoid creating them multiple times 
    # is no class name is sent, schema name will be used
    
    # For a 
    for schema, data in dataclass_rules.items(): #TODO rename data to something else
        schema_name:str =  schema
        property_rules:dict= data["property_rules"]
        
        if halo_schema[schema_name]['type'] != "object":
            raise ValueError(f"Unexpected schema type {halo_schema[schema_name]['type']}")
        
        if "class_name" in data.keys() and  data['class_name'] != "":
            class_name:str = data['class_name']
        else:
            class_name = schema_name
        
        # Skip existing responses
        if not replace_existing:
            existing_dataclasses = listdir(dataclass_folder)
            if class_name in existing_dataclasses and isfile(f"{dataclass_folder}/{class_name}.py"):
                continue
        
        dataclass_script = open(f"{dataclass_folder}/{class_name}.py" , "w")
        dataclass_str = dataclass_template_str # Reset
        dataclass_str += f"@dataclass\nclass {class_name}: #/components/schemas/{schema_name}\n"
        
        # This is the data from halo
        schema_properties = halo_schema[schema_name]["properties"]
        
        # Add additional properties to schema properties 
        if 'additional_properties' in data:
            schema_properties.update({k:v for k,v in data['additional_properties'].items()})
        
        # These two lists will contain each item/object/property. Optional properties 
        dataclass_properties:list = []
        optional_dataclass_properties: list = [] # These have to go below items that dont have anything set
        post_init_rules:list = []
        
        # Sort the properties A-Z. Looks nicer but might be confusing
        if sort:
            schema_properties = dict(sorted(schema_properties.items()))
        for prop_name, prop_info in schema_properties.items():
            #TODO make the variable names consistent 
            proptype = prop_info['type'] if 'type' in prop_info.keys() else None
            propformat = prop_info['format'] if 'format' in prop_info.keys() else None # Store property format
            nullable:bool = prop_info['nullable'] if 'nullable' in prop_info.keys() else False
            
            if prop_name in property_rules.keys(): # Check if additional things need to be done
                rules: dict | None = property_rules[prop_name]
            
            else:
                rules = None
                
            prop_str = f"{prop_name}:" # This will be added to the list
            
            # List handling
            if proptype in ["array", "list"]:
                prop_str += " list"
                
                # FIXME Handling child schema creation (currently doesn't work)
                if child_schema != 'ignore':
                    child_schema_name:str = prop_info["items"]["$ref"].split("/")[-1] # Grab the last item
                    prop_str +=f"[{child_schema_name}]"

                    if child_schema == 'create':
                        #create_dataclass(child_schema_name)
                        pass
            
            #TODO remove this? I have no idea what this is for, I cannot find a single line that hits this 
            elif proptype == None and "$ref" in prop_info:
                prop_str += " list"
            
            elif proptype == 'boolean':
                prop_str += " bool"
            
            elif proptype == 'string':
                # Datetime format handling
                if propformat and propformat == "date-time":
                    prop_str += " datetime"
                    if rules and "format" in rules:
                        # Handle multiple datetime formats for a single item
                        if  isinstance(rules["format"], list): 
                            post_init_rules.append(dedent(f"""\
                            if self.{prop_name}:
                            \tformats = ['{"','".join(rules["format"])}']
                            \tfor frmt in formats:
                            \t\ttry:
                            \t\t\tself.{prop_name} = datetime.strptime(self.{prop_name}, frmt)
                            \t\t\tbreak
                            \t\texcept Exception as e:
                            \t\t\tcontinue
                            \telse:
                            \t\traise ValueError("{prop_name} date format is invalid")"""))
                            
                        else:        
                            post_init_rules.append(f"if self.{prop_name}:\n\tself.{prop_name} = datetime.strptime(self.{prop_name}, \"{rules['format']}\")") # Create rule
                    else:
                        #TODO maybe this should always be added to datetime fields?
                        post_init_rules.append(f"if self.{prop_name}:\n\tself.{prop_name} = datetime.fromisoformat(self.{prop_name})") # If no specific date string is provided, then use a generic one
                        
                else:
                    prop_str += " str"
            
            elif proptype in ["integer", "int"]: 
                if propformat and propformat == "int32":
                    prop_str += " int"
                else:
                    print(f"WARN: {prop_name} has unhandled int type: {propformat}. Defaulting to int")
                    prop_str += " int"
                    
            elif proptype in ["number"]: 
                if propformat and propformat == "double":
                    prop_str += " float"
                else:
                    print(f"WARN: {prop_name} has unhandled number type: {propformat}. Defaulting to int")
                    prop_str += " int" #TODO see if there are other types
            else:
                print(f"ERROR: {prop_name} did not match any types. Type is: {proptype}")
                raise ValueError("see console, this is for debug")
                continue # Dont add variables that dont have a type, warn instead
            
            # Add none as a valid type
            if nullable: 
                prop_str += " | None"
            
            if rules:
                # Optional keys (this is going to replace "default: none")
                if "default" in rules.keys():
                    if rules['default'] == None and not nullable:
                        prop_str += " | None"
                    
                    prop_str += f" = field(default={rules['default']})"
                    optional_dataclass_properties.append(prop_str)
                    continue # Avoid double adding
                
                elif "optional" in rules.keys() and rules["optional"]:
                    #TODO this is kind of a dumb workaround, should clean this up.
                    if " | None" not in prop_str:
                        prop_str += " | None"
                    prop_str += f" = field(default=None)"
                    optional_dataclass_properties.append(prop_str)
                    continue # Avoid double adding
                    
            dataclass_properties.append(prop_str)
                    
        for prop in dataclass_properties:
            dataclass_str += f"\t{prop}\n" #TODO I bet there is a nicer way
        
        for prop in optional_dataclass_properties:
            dataclass_str += f"\t{prop}\n"

        if len(post_init_rules) > 0:
            dataclass_str += "\n" # Add a bit of space between the methods and variables
            dataclass_str += "\tdef __post_init__(self):\n"
            for rule in post_init_rules:
                for line in rule.split("\n"): # This will ensure the proper tab level is kept
                    dataclass_str += f"\t\t{line}\n"
        
        # Allow creation from dictionary FIXME this is for debugging
        dataclass_str += dedent("""\
        # Debug method for creating items from dictionary - This comment is required or dedent dedents everything
        \t@classmethod
        \tdef from_dict(cls, dictionary:dict):
        \t\treturn cls(**{
        \t\t\tk: v for k, v in dictionary.items()
        \t\t\tif k in inspect.signature(cls).parameters
        \t\t})""")

        dataclass_script.write(dataclass_str)
        dataclass_script.close()

create_dataclass(schemas_to_import, replace_existing=True)

# What should be imported (THIS IS AN EXAMPLE, NOT USED)
# # Property Rules # #
# For fields that need more formatting
# format: can contain a datetime formatting string, or a list of datetime formatting strings
# default: set the default field value (helpful when things aren't always passed/provided by the data source)
# optional (bool): whether the field is always returned
# comment: Purely for readability or adding additional context #TODO add these as code comments
# Example item
"""
"<Name of Schema>": { 
    "class_name": "<Dataclass Name>",
    "property_rules": {
        <field name>: {
        "format": <list or str of datetime format>,
        "default": <Default field value>,
        "optional": <bool>
        "comment": <Comment string, purely for ease of use for now>    
        }
    },
    "additional_properties": {
        <field name>: {
        "format": <list or str of datetime format>,
        "comment": <Comment string, purely for ease of use for now>
        }
    }
}
"""
# TODO items added via additional rules do not check the default field, which causes issues. Workaround is to add the item to both additional properties and property rules

# This will create methods for an endpoint
def create_methods(method_rules:dict):
    pass
    

pass
# Mark fields as optional from a list
def set_optional_properties(properties:list, schema_name:str, import_rules_file:str="helpers/import_rules.json"):
    with open(import_rules_file, 'r') as jsonfile:
        import_rules = json.loads(jsonfile.read())
        
    # I think opening this here will block it from being modified
    with open(import_rules_file, 'w') as jsonfile:
        if schema_name not in import_rules.keys():
            raise ValueError(f"{schema_name} does not exist in the file")
        
        rules_to_modify = import_rules[schema_name]
        property_rules = rules_to_modify["property_rules"]
        for prop in properties:
            if prop in property_rules.keys():
                property_rules[prop]["optional"] = True
            
            else:
                property_rules[prop] = {
                    "optional": True
                }

        # Put the data back
        jsonfile.writelines(json.dumps(import_rules))

# Paste your exception string in and let the script do the rest
def list_from_exception(schema_name:str, exception:Optional[Exception]=None, import_rules_file:str="helpers/import_rules.json"):
    #TODO this might not always start with "TypeError"
    if exception:
        #TODO use regex for this r"arguments?:"
        if "arguments:" in exception.args[0]:
            properties_str = exception.args[0].split("arguments:")[1]
        else:
            properties_str = exception.args[0].split("argument:")[1]
            
        
    # No exception was provided, so get it via input
    else:
        raw_exception = input("Paste your entire error string starting with 'TypeError':")
        if not raw_exception.lstrip().startswith("TypeError"):
            raise ValueError("Invalid exception string")
        
        
        properties_str = raw_exception.split("arguments:")[1]
    
    
    # Remove `"`, `'`, ` ` and then split it up
    properties = properties_str.replace("'","").replace("\"","").replace(" ", "").split(",")
    set_optional_properties(properties=properties, schema_name=schema_name, import_rules_file=import_rules_file)
    



# THIS IS A LAZY WORKAROUND
def single_ticket_test(ticket_id:int, includedetails:bool=True, includelastaction:bool=True, ticketidonly:bool=False):
    single_ticket = halo.Tickets.get(id=ticket_id, includedetails=includedetails, includelastaction=includelastaction, ticketidonly=ticketidonly)
    try:
        dataclass_ticket = responses.Ticket.from_dict(single_ticket)
        return True
    except Exception as e:
        return e

# Keep trying to fix it
while True:
    result = single_ticket_test(29955, includedetails=False, includelastaction=False)
    input("Try to fix again?")
    if result != True: #TODO this is jank
        list_from_exception(schema_name="Faults", exception=result)
        #pass
        #create_dataclass(schemas_to_import, replace_existing=True)
    else:
        break
    