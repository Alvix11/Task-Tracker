from task_functions import TaskManager
from settings import Parser

args = Parser.parser_settings()
file_path = Parser.FILE_PATH

def main():  
    '''Here you will control the flow of the CLI application.'''
    if args.command == "add":
        TaskManager.task_add(args, file_path)
    elif args.command == "update":
        TaskManager.task_update(args, file_path)
    elif args.command == "delete":
        TaskManager.task_delete(args, file_path)
    elif args.command == "mark-in-progress":
        TaskManager.task_mark_in_progress(args, file_path)
    elif args.command  == "mark-done":
        TaskManager.task_mark_done(args, file_path)
    elif args.command == "list":
        TaskManager.tasks_list(args, file_path)
            

if __name__ == "__main__":
    '''Run the application'''
    main()