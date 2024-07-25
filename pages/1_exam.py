import streamlit as st

st.set_page_config(page_title="exam")

st.markdown("# exam")
st.sidebar.header("exam")

# 문제 1
st.write("1 + 1 =")
answer1 = st.text_input("정답 1")

# 문제 2
st.write("6 + 3 =")
answer2 = st.text_input("정답 2")

# 저장 버튼 클릭 시
if st.button("Save Answers"):
    # 값을 session_state에 저장
    st.session_state['answer1'] = answer1
    st.session_state['answer2'] = answer2

    # 저장된 값을 화면에 표시
    st.write("저장된 값 1:", st.session_state['answer1'])
    st.write("저장된 값 2:", st.session_state['answer2'])
