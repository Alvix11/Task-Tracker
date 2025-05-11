import argparse

class Parser():

    FILE_PATH = "tasks.json" # File name json

    def parser_settings():

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

        # Subcommand mark-in-progress
        add_parser = subparser.add_parser("mark-in-progress", help="Mark a task as in progress")
        add_parser.add_argument("id", type=int, help="Task id")

        # Subcommand mark-done
        add_parser = subparser.add_parser("mark-done", help="Mark a task as done")
        add_parser.add_argument("id", type=int, help="Task id")

        # Subcommand list all tasks
        add_parser = subparser.add_parser("list", help="List all task")
        add_parser.add_argument(
                                "status", 
                                nargs="?", 
                                choices=["done", "todo", "in-progress"],
                                default=None, 
                                help="Filter tasks"
                                )


        # The arguments provided by the user from the command line are parsed.
        return parser.parse_args()           
        