import os

def verify_create_json(file_path):
    if not os.path.exists(file_path):
        return False # Return false if the json file does not exist
    else:
        return True # Returns true if the json file exists