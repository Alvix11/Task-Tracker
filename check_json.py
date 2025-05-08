import os
import json

def verify_create_json(file_path):
    if not os.path.exists(file_path):
        return False # Return false if the json file does not exist
    else:
        return True # Returns true if the json file exists

def read_json(file_path):
    '''Function to read json files'''
    with open(file_path, "r") as file:
        datas = json.load(file)
    return datas
