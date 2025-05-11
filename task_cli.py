from task_functions import TaskManager
from settings import Parser

args = Parser.parser_settings()

def main():  
    '''Here you will control the flow of the CLI application.'''
    if args.command == "add":
        TaskManager.task_add(args, Parser.FILE_PATH)
    elif args.command == "update":
        TaskManager.task_update(args, Parser.FILE_PATH)
    elif args.command == "delete":
        TaskManager.task_delete(args, Parser.FILE_PATH)
    elif args.command == "mark-in-progress":
        TaskManager.task_mark_in_progress(args, Parser.FILE_PATH)
    elif args.command  == "mark-done":
        TaskManager.task_mark_done(args, Parser.FILE_PATH)
    elif args.command == "list":
        TaskManager.tasks_list(args, Parser.FILE_PATH)
            

if __name__ == "__main__":
    '''Run the application'''
    main()