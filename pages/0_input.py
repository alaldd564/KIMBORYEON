import streamlit as st

# text = st.text_input("입력")

# if st.button("Save"):
#     st.session_state.text = text

# #st.session_state는 키와 값으로 나뉨
# #st.session_state.key or
# #st.session_state["key"]
#python -m streamlit run Main.py


# 입력 필드 생성
text1 = st.text_input("입력 1")
text2 = st.text_input("입력 2")

# 저장 버튼 클릭 시
if st.button("Save"):
    # 입력된 값을 session_state에 저장
    st.session_state.text1 = text1
    st.session_state.text2 = text2
    st.write("저장된 값 1:", st.session_state.text1)
    st.write("저장된 값 2:", st.session_state.text2)

# 저장된 값을 화면에 표시 (디버깅 용도)


