import argparse

FILE_PATH = "tasks.json" # File name json

def get_parser():
    '''Function to get the user's entries on the console'''

    # A parser is created to receive positional arguments.
    parser = argparse.ArgumentParser(description="Task Tracker") 
    subparser = parser.add_subparsers(dest="command", help="Available subcommands")

    # Subcommand add
    add = subparser.add_parser("add", help="Add a new task")
    add.add_argument("description", type=str, help="Task description")

    # Subcommand update
    update = subparser.add_parser("update", help="Edit a task")
    update.add_argument("id", type=int, help="Task id")
    update.add_argument("description", type=str, help="Update description")

    # Subcommand delete
    delete = subparser.add_parser("delete", help="Task delete")
    delete.add_argument("id", type=int, help="Task id")

    # Subcommand mark-in-progress
    in_progress = subparser.add_parser("mark-in-progress", help="Mark a task as in progress")
    in_progress.add_argument("id", type=int, help="Task id")

    # Subcommand mark-done
    done = subparser.add_parser("mark-done", help="Mark a task as done")
    done.add_argument("id", type=int, help="Task id")

    # Subcommand list all tasks
    list_cmd = subparser.add_parser("list", help="List all task")
    list_cmd.add_argument(
                            "status", 
                            nargs="?", 
                            choices=["done", "todo", "in-progress"],
                            default=None, 
                            help="Filter tasks"
                            )
    
    # Returns user-supplied arguments from the command line
    return parser.parse_args() 