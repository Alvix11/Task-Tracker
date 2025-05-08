from utils import actual_date_and_time
from check_json import verify_create_json, read_json
import json

class TaskManager():

    def task_add(args, file_path):
        '''Function to add new tasks'''

        # Dictionary to correctly store data in the json file
        data = {}

        # We obtain the current date and time
        present_date = actual_date_and_time()

        if verify_create_json(file_path): # Verify that the json file exists
            datas = read_json(file_path)# We load the stored data

            if datas: # We verify that there are already saved tasks to get the last id and increment it.
                id = max(map(int, datas.keys())) + 1
            else:
                # Main id used if json file does not exist
                id = 1

            # Data to be stored in the json file
            datas[str(id)] = {
                    "description": str(args.description),
                    "status": "todo",
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
                "description": str(args.description),
                "status": "todo",
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

    def task_update(args, file_path):
        '''Function to update tasks'''

        # We obtain the current date and time
        present_date = actual_date_and_time()

        if verify_create_json(file_path): # Verify that the json file exists
            with open(file_path, "r") as file:
                data = json.load(file) # We load the stored data

                if data: # We verify that the json file has tasks to be updated

                    if str(args.id) in data: # We verify that the id exists

                        data[str(args.id)]["description"] = str(args.description) # Update description
                        data[str(args.id)]["updateAt"] = str(present_date) # Update updateAt

                        with open(file_path, "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False) # Update the json file
                            print(f"Tarea con el id: {args.id} actualizada")
                    else:
                        print(f"La tarea con el id: {args.id} no existe")
                else:
                    print("No existen tareas, crea una tarea primero con el comando add")

        else:
            print("No existe el archivo de tarea, asi que no puedes actualizar")

    def task_delete(args, file_path):
        '''Funtion to delete task'''

        if verify_create_json(file_path): # Verify that the json file exists
            with open(file_path, "r") as file:
                data = json.load(file) # We load the stored data

                if data:
                    if str(args.id) in data: # We verify that the id exists
                        del data[str(args.id)] # Delete task

                        with open(file_path, "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False) # Update the json file
                            print(f"Tarea con el id: {args.id} eliminada")
                    else:
                        print(f"La tarea con el id: {args.id} no existe")
                else:
                    print("No existen tareas, crea una tarea primero con el comando add")
        else:
            print("No existe el archivo de tarea, asi que no puedes eliminar")

    def task_mark_in_progress(args, file_path):
        '''Function to mark tasks in progress'''

        # We obtain the current date and time, and give it a better format.
        present_date = actual_date_and_time()

        if verify_create_json(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)

                if data:
                    if str(args.id) in data: # We verify that the id exists
                        data[str(args.id)]["status"] = "in-progress" # Update status
                        data[str(args.id)]["updateAt"] = str(present_date) # Update updateAt

                        with open(file_path, "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False) # Update the json file
                            print(f"Tarea con el id: {args.id} marcada en progreso")
                    else:
                        print(f"La tarea con el id: {args.id} no existe")
                else:
                    print("No existen tareas, crea una tarea primero con el comando add")
        else:
            print("No existe el archivo de tareas")

    def task_mark_done(args, file_path):
        '''Function to mark tasks in progress'''

        # We obtain the current date and time, and give it a better format.
        present_date = actual_date_and_time()

        if verify_create_json(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)

                if data:
                    if str(args.id) in data:
                        data[str(args.id)]["status"] = "done" # Update status
                        data[str(args.id)]["updateAt"] = str(present_date) # Update updateAt

                        with open(file_path, "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False) # Update the json file
                            print(f"Tarea con el id: {args.id} marcada como hecha")
                    else:
                        print(f"La tarea con el id: {args.id} no existe")
                else:
                    print("No existen tareas, crea una tarea primero con el comando add")
        else:
            print("No existe el archivo de tareas")


    def task_list_all(args, file_path):
        '''Function to list all tasks'''
        if verify_create_json(file_path): # Verify that the json file exists
            with open(file_path, "r") as file:
                data = json.load(file) # We load the stored data

                if data:
                    if args.status == None:
                        for key, value in data.items():
                            # We display the tasks with customized formatting with colors (ANSI Escape Codes)
                            print(f"\033[94mTask ID:\033[0m {key}")
                            print(f"\033[93m➤ Description:\033[0m {value['description']}")
                            print(f"\033[93m➤ Status:\033[0m {value['status']}")
                            print(f"\033[93m➤ Add:\033[0m {value['createdAt']}")
                            print(f"\033[93m➤ Update:\033[0m {value['updateAt']}")
                            print("─" * 30)
                    elif args.status == "done":
                        for key, value in data.items():
                            if value["status"] == args.status:
                                # We display the tasks with customized formatting with colors (ANSI Escape Codes)
                                print(f"\033[94mTask ID:\033[0m {key}")
                                print(f"\033[93m➤ Description:\033[0m {value['description']}")
                                print(f"\033[93m➤ Status:\033[0m {value['status']}")
                                print(f"\033[93m➤ Add:\033[0m {value['createdAt']}")
                                print(f"\033[93m➤ Update:\033[0m {value['updateAt']}")
                                print("─" * 30)
                    elif args.status == "todo":
                        for key, value in data.items():
                            if value["status"] == args.status:
                                # We display the tasks with customized formatting with colors (ANSI Escape Codes)
                                print(f"\033[94mTask ID:\033[0m {key}")
                                print(f"\033[93m➤ Description:\033[0m {value['description']}")
                                print(f"\033[93m➤ Status:\033[0m {value['status']}")
                                print(f"\033[93m➤ Add:\033[0m {value['createdAt']}")
                                print(f"\033[93m➤ Update:\033[0m {value['updateAt']}")
                                print("─" * 30)
                    elif args.status == "in-progress":
                        for key, value in data.items():
                            if value["status"] == args.status:
                                # We display the tasks with customized formatting with colors (ANSI Escape Codes)
                                print(f"\033[94mTask ID:\033[0m {key}")
                                print(f"\033[93m➤ Description:\033[0m {value['description']}")
                                print(f"\033[93m➤ Status:\033[0m {value['status']}")
                                print(f"\033[93m➤ Add:\033[0m {value['createdAt']}")
                                print(f"\033[93m➤ Update:\033[0m {value['updateAt']}")
                                print("─" * 30)
                else:
                    print("No existen tareas, crea una tarea primero con el comando add")
        else:
            print("No existe el archivo de tarea, asi que no tienes tareas para listar")
