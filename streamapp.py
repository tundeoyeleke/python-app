import streamlit as st

# App title
st.title("To-Do List App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []


new_task = st.text_input("Add a new task", placeholder="Enter your task here...")

if st.button("➕ Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append(new_task)
        st.success(f"Task added: {new_task}")
    else:
        st.warning("Task cannot be empty!")

# Display tasks
st.subheader("Your Tasks:")
if st.session_state.tasks:
    for index, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([8, 2])
        col1.write(f"{index + 1}. {task}")
        if col2.button("❌", key=f"delete_{index}"):
            st.session_state.tasks.pop(index)
            st.experimental_rerun()
else:
    st.info("No tasks added yet!")

