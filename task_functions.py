from datetime import datetime
from check_json import verify_create_json
import json

def task_add(args, file_path):
    '''Function to add new tasks'''
    
    # Main id used if json file does not exist
    id = 1

    # Dictionary to correctly store data in the json file
    data = {}

    # We obtain the current date and time, and give it a better format.
    present_date = datetime.now() 
    present_date = present_date.strftime("%A %d de %B, %H:%M")

    if verify_create_json(file_path): # Verify that the json file exists
        with open(file_path, "r") as file:
            datas = json.load(file) # We load the stored data

            if datas: # We verify that there are already saved tasks to get the last id and increment it.
                id = max(map(int, datas.keys())) + 1
            
            # Data to be stored in the json file
            datas[str(id)] = {
                    "description": str(args.add),
                    "status": "to do",
                    "createdAt": str(present_date),
                    "updateAt": "",
                }
            
            with open(file_path, "w", encoding="utf-8") as file:
                # We add the new task with a message indicating its id
                json.dump(datas, file, indent=4, ensure_ascii=False)
                print(f"Tarea agregada con el id: {id}")
    else:
        # Data to be stored in the json file
        data[str(id)] = {
            "description": str(args.add),
            "status": "to do",
            "createdAt": str(present_date),
            "updateAt": "",
        }
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                # Create the json file and add the new task indicating its id
                json.dump(data, file, indent=4, ensure_ascii=False)
                print(f"Tarea creada con el id: {id}")
        except Exception as e:
            print(f"Ocurrio un error {e}")