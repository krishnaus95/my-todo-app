FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list
    of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# This is a procedure, so we don't have to return anything


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "function":
    print("Hello from functions")
    print(get_todos())
