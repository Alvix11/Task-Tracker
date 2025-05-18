# Task Tracker CLI

A command-line application to easily manage your daily tasks.

## Requirements

- Python 3.7 or higher

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```
2. (Optional) Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

## Usage

Run the application from the terminal:

```bash
python main.py <command> [arguments]
```

### Available Commands

- **add**  
  Add a new task.
  ```bash
  python main.py add "Task description"
  ```

- **update**  
  Edit the description of an existing task.
  ```bash
  python main.py update <id> "New description"
  ```

- **delete**  
  Delete a task by its ID.
  ```bash
  python main.py delete <id>
  ```

- **mark-in-progress**  
  Mark a task as "in progress".
  ```bash
  python main.py mark-in-progress <id>
  ```

- **mark-done**  
  Mark a task as "done".
  ```bash
  python main.py mark-done <id>
  ```

- **list**  
  List all tasks or filter by status (`todo`, `in-progress`, `done`).
  ```bash
  python main.py list
  python main.py list done
  python main.py list todo
  python main.py list in-progress
  ```

## Examples

Add a task:
```bash
python main.py add "Wash the dishes"
```

List all tasks:
```bash
python main.py list
```

Mark a task as done:
```bash
python main.py mark-done 2
```

Delete a task:
```bash
python main.py delete 3
```

## Notes

- Tasks are stored in the `tasks.json` file in the project directory.
- For help with commands, you can use:
  ```bash
  python main.py --help
  ```

---

Contributions and suggestions are welcome!