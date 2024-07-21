import streamlit as st
import pandas as pd

class TodoPage:
  def setup(self):
    if "todos" not in st.session_state:
      st.session_state.todos = pd.DataFrame([])
    def add_todo():
      st.session_state.todos = pd.concat([st.session_state.todos, pd.DataFrame([{"DONE": False, "TODO": "TODO"}])])
    self.add_todo = add_todo

  def components(self):
    st.title("TODOリスト")
    st.button("Add Task", on_click=self.add_todo)
    st.session_state.todos = st.data_editor(
      st.session_state.todos, 
      hide_index=True, 
      width=500, 
      column_config={
        "DONE": {"type": "checkbox"},
        "TODO": {"type": "text"}
      }
    )

page = TodoPage()
page.setup()
page.components()



#streamlit run hello.py