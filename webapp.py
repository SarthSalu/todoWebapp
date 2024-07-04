import streamlit as st
import functions


def add_todo():
    todo_ = st.session_state['new_todo']
    todos.append(todo_+"\n")
    functions.write_todos(todos)
    st.session_state.new_todo = ""


if "new_todo" not in st.session_state:
    st.session_state.new_todo = ""

st.title("My To-Do App")
st.subheader("This is a todo app")
todos = functions.get_todos()
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add a new task...", on_change=add_todo, key='new_todo')
