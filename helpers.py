from utils import verify_create_json, read_json, write_json

def load_tasks(file_path):
    '''Function to load tasks'''
    if verify_create_json(file_path): # We verify that the json file exists
        data = read_json(file_path) # Read json file
        if data:
            return data
        return {}

def save_tasks(file_path, data):
    '''Function to save tasks'''
    try:
        write_json(file_path, data)
        return True
    except Exception as e:
        print(f"Ocurrio un error: {e}")
        return False