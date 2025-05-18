from utils import actual_date_and_time
from helpers import load_tasks, save_tasks, display_tasks, is_text
from settings import FILE_PATH

class TaskManager:

    file_path = FILE_PATH

    def task_add(self, args):
        '''Function to add new tasks'''
        datas = {} # Dictionary to be used if the file does not exist
        id = 1 # Id to be used if no tasks are created
        present_date = actual_date_and_time() # We obtain the current date and time

        data = load_tasks(self.file_path)

        if data: # We verify that there are already saved tasks to get the last id and increment it.
            id = max(map(int, data.keys())) + 1
            
            if is_text(args):
                # Data to be stored in the json file
                data[str(id)] = {
                    "description": str(args.description),
                    "status": "todo",
                    "createdAt": str(present_date),
                    "updateAt": "",
                }
                save_tasks(self.file_path, data)
                print(f"Task added with id: {id}")
        else:
            if is_text(args):
                # Data to be stored in the json file
                datas[str(id)] = {
                    "description": str(args.description),
                    "status": "todo",
                    "createdAt": str(present_date),
                    "updateAt": "",
                }
                save_tasks(self.file_path, datas)
                print(f"Task created with id: {id}")

    def task_update(self, args):
        '''Function to update tasks'''
        present_date = actual_date_and_time()

        data = load_tasks(self.file_path)
        if data:
            if str(args.id) in data: # We verify that the id exists
                if is_text(args):
                    data[str(args.id)]["description"] = str(args.description) # Update description
                    data[str(args.id)]["updateAt"] = str(present_date) # Update updateAt
                    save_tasks(self.file_path, data)
                    print(f"Task with id: {args.id} updated") 
            else:
                print(f"Task with id: {args.id} does not exist")
        else:
            print("There are no tasks to update, create a task first with the command add")

    def task_delete(self, args):
        '''Funtion to delete task'''
        data = load_tasks(self.file_path)

        if data:
            if str(args.id) in data: 
                del data[str(args.id)] # Delete task
                save_tasks(self.file_path, data) 
                print(f"Task with the id: {args.id} removed")
            else:
                print(f"Task with id: {args.id} does not exist")
        else:
            print("There are no tasks, create a task first with the add command")

    def task_mark_in_progress(self, args):
        '''Function to mark tasks in progress'''
        present_date = actual_date_and_time()

        data = load_tasks(self.file_path)

        if data:
            if str(args.id) in data: 
                data[str(args.id)]["status"] = "in-progress"
                data[str(args.id)]["updateAt"] = str(present_date)
                save_tasks(self.file_path, data)
                print(f"Task with id: {args.id} flagged in progress")
            else:
                print(f"Task with id: {args.id} does not exist")
        else:
            print("There are no tasks, create a task first with the add command")

    def task_mark_done(self, args):
        '''Function to mark tasks in progress'''
        present_date = actual_date_and_time()

        data = load_tasks(self.file_path)

        if data:
            if str(args.id) in data:
                data[str(args.id)]["status"] = "done" 
                data[str(args.id)]["updateAt"] = str(present_date)
                save_tasks(self.file_path, data)
                print(f"Task with id: {args.id} marked as done")
            else:
                print(f"Task with id: {args.id} does not exist")
        else:
            print("There are no tasks, create a task first with the add command")

    def tasks_list(self, args):
        '''Function to list all tasks'''
        data = load_tasks(self.file_path)
        if data:
            if args.status:
                filtered = {k: v for k, v in data.items() if v["status"] == args.status}
            else:
                filtered = data
            display_tasks(filtered)
        else:
            print("There are no tasks, create a task first with the add command")