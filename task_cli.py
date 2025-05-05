import argparse
from task_functions import task_add

FILE_PATH = "tasks.json" # File name json

# A parser is created to receive positional arguments.
parser = argparse.ArgumentParser(description="Task Tracker")
# An optional “--add” argument is defined that allows the user to add a new task from the command line.
parser.add_argument("--add", type=str, help="Agregar una tarea nueva")

# The arguments provided by the user from the command line are parsed.
args = parser.parse_args()           
        
def main():  
    '''Here you will control the flow of the CLI application.'''
    if args.add:
        task_add(args, FILE_PATH)

if __name__ == "__main__":
    '''Run the application'''
    main()