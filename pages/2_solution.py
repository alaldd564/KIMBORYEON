import streamlit as st

st.set_page_config(page_title="solution")

st.markdown("# solution")
st.sidebar.header("solution")
st.write("문제 풀이")



# 입력값을 st.session_state에서 가져오기
answer1 = st.session_state.get('answer1', '')
answer2 = st.session_state.get('answer2', '')
text1 = st.session_state.get('text1', '')
text2 = st.session_state.get('text2', '')

# 정답 정의: text1과 text2에서 가져오기
correct_answer1 = text1
correct_answer2 = text2

# 입력값과 정답 비교 및 결과 표시
if answer1 != correct_answer1:
    st.write("1 + 1 =의 정답은 창문입니다. 왜냐하면 창문 모양이기 때문입니다.")

if answer2 != correct_answer2:
    st.write("6 + 3 =의 정답은 빌딩입니다. 왜냐하면 63빌딩이 매우 유명하기 때문입니다.")
