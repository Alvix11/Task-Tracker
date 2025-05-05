import argparse
from task_functions import task_add, task_update, task_delete

FILE_PATH = "tasks.json" # File name json

# A parser is created to receive positional arguments.
parser = argparse.ArgumentParser(description="Task Tracker") 
subparser = parser.add_subparsers(dest="command", help="Available subcommands")

# Subcommand add
add_parser = subparser.add_parser("add", help="Add a new task")
add_parser.add_argument("description", type=str, help="Task description")

# Subcommand update
add_parser = subparser.add_parser("update", help="Edit a task")
add_parser.add_argument("id", type=int, help="Task id")
add_parser.add_argument("description", type=str, help="Update description")

# Subcommand delete
add_parser = subparser.add_parser("delete", help="Task delete")
add_parser.add_argument("id", type=int, help="Task id")

# The arguments provided by the user from the command line are parsed.
args = parser.parse_args()           
        
def main():  
    '''Here you will control the flow of the CLI application.'''
    if args.command == "add":
        task_add(args, FILE_PATH)
    elif args.command == "update":
        task_update(args, FILE_PATH)
    elif args.command == "delete":
        task_delete(args, FILE_PATH)

if __name__ == "__main__":
    '''Run the application'''
    main()