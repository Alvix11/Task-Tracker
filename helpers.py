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
        print(f"An error occurred: {e}")
        return False
    
def display_tasks(tasks):
    '''Function to display tasks'''
    for key, value in tasks.items():
        # We display the tasks with customized formatting with colors (ANSI Escape Codes)
        print(f"\033[94mTask ID:\033[0m {key}")
        print(f"\033[93m➤ Description:\033[0m {value['description']}")
        print(f"\033[93m➤ Status:\033[0m {value['status']}")
        print(f"\033[93m➤ Add:\033[0m {value['createdAt']}")
        print(f"\033[93m➤ Update:\033[0m {value['updateAt']}")
        print("─" * 30)

def is_text(args):
    '''Function to verify that the task passed by the user is not blank or numbers.'''
    desc = str(args.description).strip()
    if not desc:
        print('Enter a valid task, no blanks')
        return False
    try:
        float(desc)
        print('Enter a valid task, not numbers')
        return False
    except ValueError:
        return True