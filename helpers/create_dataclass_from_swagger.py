# Read JSON schema, create new python dataclass file

# BUILT-IN
import json
from typing import Literal

# EXTERNAL

# INTERNAL

# CODE

# swagger location
swagger_file = "helpers/halo_swagger.json"
import_rules_file = "helpers/import_rules.json"

with open(swagger_file, 'r') as jsonfile:
    json_data = json.loads(jsonfile.read())
    
with open(import_rules_file, 'r') as jsonfile:
    schemas_to_import = json.loads(jsonfile.read())

# Schemas are here
json_schemas = json_data["components"]["schemas"]

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

child_schema_types = Literal["ignore", "create", "dont_create"] #TODO add a "only create if it doesnt exist" option
# # Child schema options # #
# ignore: will just make it a list
# create: will create an additional schema
# dont_create: will assume it has already been created
def create_dataclass(import_rules:dict, child_schema:child_schema_types="ignore", create_list:bool=False):
    # is no class name is sent, schema name will be used
    for schema, data in import_rules.items():
        schema_name:str =  schema
        property_rules:dict= data["property_rules"]
        
        if json_schemas[schema_name]['type'] != "object":
            raise ValueError(f"Unexpected schema type {json_schemas[schema_name]['type']}")
        
        if "class_name" in data.keys() and  data['class_name'] != "":
            class_name:str = data['class_name']
        else:
            class_name = schema_name
        
        dataclass_script = open(f"HaloPSA/responses/{class_name}.py" , "w")
        dataclass_str = dataclass_template_str # Reset
        
        dataclass_str += f"@dataclass\nclass {class_name}: #/components/schemas/{schema_name}\n"
        
        schema_properties = json_schemas[schema_name]["properties"]
        
        if 'additional_properties' in data: # add additional rules
            schema_properties.update({k:v for k,v in data['additional_properties'].items()})
        dataclass_properties:list = []
        optional_dataclass_properties: list = [] # These have to go below items that dont have anything set
        post_init_rules:list = []
        for prop_name, prop_info in schema_properties.items():
            proptype = prop_info['type'] if 'type' in prop_info.keys() else None #
            propformat = prop_info['format'] if 'format' in prop_info.keys() else None # Store property format
            nullable:bool = prop_info['nullable'] if 'nullable' in prop_info.keys() else False
            
            if prop_name in property_rules.keys(): # Check if additional things need to be done
                rules: dict | None = property_rules[prop_name]
            
            else:
                rules = None
                
            prop_str = f"{prop_name}:" # This will be added to the list
            
            if proptype in ["array", "list"]:
                prop_str += " list"
                if child_schema != 'ignore':
                    child_schema_name:str = prop_info["items"]["$ref"].split("/")[-1] # Grab the last item
                    prop_str +=f"[{child_schema_name}]"
                
                    if child_schema == 'create':
                        #create_dataclass(child_schema_name)
                        pass #TODO fix!
                        
            elif proptype == None and "$ref" in prop_info:
                prop_str += " list"
                
            elif proptype == 'boolean':
                prop_str += " bool"
            
            elif proptype == 'string':
                if propformat and propformat == "date-time":
                    prop_str += " datetime"
                    if rules and "format" in rules:
                        post_init_rules.append(f"if self.{prop_name}:\n\tself.{prop_name} = datetime.strptime(self.{prop_name}, \"{rules['format']}\")") # Create rule
                    else:
                        post_init_rules.append(f"if self.{prop_name}:\n\tself.{prop_name} = datetime.strptime(self.{prop_name}, \"%Y-%m-%dT%H:%M:%S\")") # If no specific date string is provided, then use a generic one
                        
                else:
                    prop_str += " str"
            
            elif proptype in ["integer", "int"]: 
                if propformat and propformat == "int32":
                    prop_str += " int"
                else:
                    print(f"WARN: Unhandled int type: {propformat}")
                    prop_str += " int"
                    
            elif proptype in ["number"]: 
                if propformat and propformat == "double":
                    prop_str += " float"
                else:
                    print(f"WARN: Unhandled number type: {propformat}")
                    prop_str += " int" #TODO see if there are other types
            else:
                print(f"ERROR: {prop_name} did not match any types. Type is: {proptype}")
                raise ValueError("see console, this is for debug")
                continue # Dont add variables that dont have a type, warn instead
            
            if nullable: # Add none as a valid type
                prop_str += " | None"
            
            if rules:
                if "default" in rules.keys():
                    if rules['default'] == None and not nullable:
                        prop_str += " | None"
                    prop_str += f" = field(default={rules['default']})"
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
        
        #TODO this is for debugging
        dataclass_str += """	@classmethod 
        def from_dict(cls, dictionary:dict):
            return cls(**{
                k: v for k, v in dictionary.items() 
                if k in inspect.signature(cls).parameters 
            })"""
        dataclass_script.write(dataclass_str)
        dataclass_script.close()
        pass


create_dataclass(schemas_to_import)

# What should be imported (THIS IS AN EXAMPLE, NOT USED)
# # Property Rules # #
# For fields that need more formatting
# format: can contain a datetime formatting string
# default: set the default field value (helpful when things aren't always passed/provided by the data source)
