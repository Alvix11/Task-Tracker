from utils import actual_date_and_time
from helpers import load_tasks, save_tasks

class TaskManager():

    def task_add(args, file_path):
        '''Function to add new tasks'''

        datas = {}
        id = 1

        # We obtain the current date and time
        present_date = actual_date_and_time()

        data = load_tasks(file_path)

        if data: # We verify that there are already saved tasks to get the last id and increment it.
            id = max(map(int, data.keys())) + 1
            
            # Data to be stored in the json file
            data[str(id)] = {
                "description": str(args.description),
                "status": "todo",
                "createdAt": str(present_date),
                "updateAt": "",
                }
            
            save_tasks(file_path, data)
            print(f"Tarea agregada con el id: {id}")
        else:
            # Data to be stored in the json file
            datas[str(id)] = {
                "description": str(args.description),
                "status": "todo",
                "createdAt": str(present_date),
                "updateAt": "",
            }
            save_tasks(file_path, datas)
            print(f"Tarea creada con el id: {id}")

    def task_update(args, file_path):
        '''Function to update tasks'''
        present_date = actual_date_and_time()

        data = load_tasks(file_path)
        if data:
            if str(args.id) in data: # We verify that the id exists
                data[str(args.id)]["description"] = str(args.description) # Update description
                data[str(args.id)]["updateAt"] = str(present_date) # Update updateAt
                save_tasks(file_path, data)
                print(f"Tarea con el id: {args.id} actualizada") 
            else:
                print(f"La tarea con el id: {args.id} no existe")
        else:
            print("No existen tareas para actualizar, crea una tarea primero con el comando add")

    def task_delete(args, file_path):
        '''Funtion to delete task'''
        data = load_tasks(file_path)

        if data:
            if str(args.id) in data: 
                del data[str(args.id)] # Delete task
                save_tasks(file_path, data) 
                print(f"Tarea con el id: {args.id} eliminada")
            else:
                print(f"La tarea con el id: {args.id} no existe")
        else:
                print("No existen tareas, crea una tarea primero con el comando add")

    def task_mark_in_progress(args, file_path):
        '''Function to mark tasks in progress'''
        present_date = actual_date_and_time()

        data = load_tasks(file_path)

        if data:
            if str(args.id) in data: 
                data[str(args.id)]["status"] = "in-progress"
                data[str(args.id)]["updateAt"] = str(present_date)
                save_tasks(file_path, data)
                print(f"Tarea con el id: {args.id} marcada en progreso")
            else:
                print(f"La tarea con el id: {args.id} no existe")
        else:
            print("No existen tareas, crea una tarea primero con el comando add")

    def task_mark_done(args, file_path):
        '''Function to mark tasks in progress'''
        present_date = actual_date_and_time()

        data = load_tasks(file_path)

        if data:
            if str(args.id) in data:
                data[str(args.id)]["status"] = "done" 
                data[str(args.id)]["updateAt"] = str(present_date)
                save_tasks(file_path, data)
                print(f"Tarea con el id: {args.id} marcada como hecha")
            else:
                print(f"La tarea con el id: {args.id} no existe")
        else:
            print("No existen tareas, crea una tarea primero con el comando add")


    def tasks_list(args, file_path):
        '''Function to list all tasks'''
        data = load_tasks(file_path)

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
                        print(f"\033[94mTask ID:\033[0m {key}")
                        print(f"\033[93m➤ Description:\033[0m {value['description']}")
                        print(f"\033[93m➤ Status:\033[0m {value['status']}")
                        print(f"\033[93m➤ Add:\033[0m {value['createdAt']}")
                        print(f"\033[93m➤ Update:\033[0m {value['updateAt']}")
                        print("─" * 30)
            elif args.status == "todo":
                for key, value in data.items():
                    if value["status"] == args.status:
                        print(f"\033[94mTask ID:\033[0m {key}")
                        print(f"\033[93m➤ Description:\033[0m {value['description']}")
                        print(f"\033[93m➤ Status:\033[0m {value['status']}")
                        print(f"\033[93m➤ Add:\033[0m {value['createdAt']}")
                        print(f"\033[93m➤ Update:\033[0m {value['updateAt']}")
                        print("─" * 30)
                        
            elif args.status == "in-progress":
                for key, value in data.items():
                    if value["status"] == args.status:
                        print(f"\033[94mTask ID:\033[0m {key}")
                        print(f"\033[93m➤ Description:\033[0m {value['description']}")
                        print(f"\033[93m➤ Status:\033[0m {value['status']}")
                        print(f"\033[93m➤ Add:\033[0m {value['createdAt']}")
                        print(f"\033[93m➤ Update:\033[0m {value['updateAt']}")
                        print("─" * 30)
        else:
            print("No existen tareas, crea una tarea primero con el comando add")