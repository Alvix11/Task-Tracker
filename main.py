from task_functions import TaskManager
from settings import get_parser

args = get_parser()

def main(): 
    '''Run the application''' 
    manager = TaskManager()

    # Here you will control the flow of the CLI application.
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
    else:
        print("Command not recognized. Use --help to see the options.")   

if __name__ == "__main__":
    main()