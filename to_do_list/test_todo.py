import todo

def test_create_todo():
    todo.todos = []
    todo.create_todo(todo.todos,
        title = "Make some stuff",
        description = "Stuff needs to be programmed",
        level = "Important")

    assert len(todo.todos) == 1, "Todo was not created!"
    assert todo.todos[0]['title'] == "Make some stuff"
    assert (todo.todos[0]['description'] == "Stuff needs to be programmed")
    assert todo.todos[0]['level'] == "Important"

    print "ok - create_todo"

def test_get_function():
    assert todo.get_function('new') == todo.create_todo
    print "ok - get function new"

def test_get_fields():
    assert (todo.get_fields('new') == ['title', 'description', 'level'])
    print "ok - get fields"

def test_run_command():
    result = todo.run_command(
        'test',
        {'abcd': 'edfg', 'ijkl': 'mnlo'}
    )
    expected = """Command 'test' returned:
    abcd: edfg
    ijkl: mnlo """
    print result
    assert result == expected, \
        result + " != " + expected
    print "ok - run command"

def test_show_todos():
    todo.todos = [
        { 'title' : 'test todo',
          'description' : 'This is a test',
          'level' : 'Important'
          } ]
    result = todo.show_todos(todo.todos)
    lines = result.split("\n")

    first_line = lines[0]
    assert "Item" in first_line
    assert "Title" in first_line
    assert "Description" in first_line
    assert "Level" in first_line

    second_line = lines[1]
    assert "1" in second_line
    assert "test todo" in second_line
    assert "This is a test" in second_line
    assert "Important" in second_line
    print "ok - show_todos"

test_create_todo()
test_get_function()
test_get_fields()
test_run_command()
test_show_todos()
