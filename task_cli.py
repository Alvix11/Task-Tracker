import argparse
from task_functions import task_add, task_update

FILE_PATH = "tasks.json" # File name json

# A parser is created to receive positional arguments.
parser = argparse.ArgumentParser(description="Task Tracker") 
subparser = parser.add_subparsers(dest="command", help="Subcomandos disponibles")

# Subcommand add
add_parser = subparser.add_parser("add", help="Agrega una nueva tarea")
add_parser.add_argument("description", type=str, help="Descripcion de la tarea")

# Subcommand update
add_parser = subparser.add_parser("update", help="Edita una tarea")
add_parser.add_argument("id", type=int, help="Id de la tarea")
add_parser.add_argument("description", type=str, help="Actualizar descripcion")

# The arguments provided by the user from the command line are parsed.
args = parser.parse_args()           
        
def main():  
    '''Here you will control the flow of the CLI application.'''
    if args.command == "add":
        task_add(args, FILE_PATH)
    elif args.command == "update":
        task_update(args, FILE_PATH)

if __name__ == "__main__":
    '''Run the application'''
    main()