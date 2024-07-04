
FILEPATH = "todo.txt"


def get_todos(filepath = FILEPATH):
    """
    gets the list of tasks from the text file
    """
    with open(filepath, 'r') as file_local:
        the_list = file_local.readlines()
    return the_list


def write_todos(todos, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)
