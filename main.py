from task_functions import TaskManager
from settings import get_parser

args = get_parser()

def main():  
    '''Here you will control the flow of the CLI application.'''
    manager = TaskManager()

    if args.command == "add":
        manager.task_add(args)
    elif args.command == "update":
        manager.task_update(args)
    elif args.command == "delete":
        manager.task_delete(args)
    elif args.command == "mark-in-progress":
        manager.task_mark_in_progress(args)
    elif args.command  == "mark-done":
        manager.task_mark_done(args)
    elif args.command == "list":
        manager.tasks_list(args)       

if __name__ == "__main__":
    '''Run the application'''
    main()