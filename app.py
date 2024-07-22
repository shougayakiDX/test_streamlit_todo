import streamlit as st
import pandas as pd

class TodoList: #todoリストのページを管理するためのクラスを定義
  def setup(self): #初期設定を行う、↓st.session_stateでセッション状態を管理
    if "todos" not in st.session_state:
      st.session_state.todos = pd.DataFrame([]) #行・列型の表形式のデータ構造
    def add_todo():
      st.session_state.todos = pd.concat([st.session_state.todos, pd.DataFrame([{"DONE": False, "TODO": "TODO", "DUEDATE": "DUEDATE"}])]) #concat()で既存のリストに新たな要素を追加
    self.add_todo = add_todo

  def components(self): #todoリストのUIを構築し、画面に反映させる
    st.title("TODOリスト")
    st.button("Add TASK", on_click=self.add_todo) #ボタンをクリックするとadd_todo()関数が呼び出される
    st.session_state.todos = st.data_editor(
      st.session_state.todos, 
      hide_index=True,
      width=1000, 
      column_config={
        "DONE": {"type": "checkbox"},
        "TASK": {"type": "text"},
        "DUEDATE": {"type": "text"},
      }
    )

page = TodoList()
page.setup()
page.components()



#streamlit run hello.py