import streamlit as st

st.set_page_config(page_title="score")

st.markdown("# score")
st.sidebar.header("score")
st.write("문제의 점수를 계산합니다.")

# 세션 상태에서 사용자 입력과 정답 가져오기

answer1 = st.session_state.get('answer1', '')
answer2 = st.session_state.get('answer2', '')
text1 = st.session_state.get('text1', '')
text2 = st.session_state.get('text2', '')

# 정답 정의
correct_answer1 = text1
correct_answer2 = text2

# 문제 맞춘 수 계산
correct_count = 0
if answer1 == correct_answer1:
    correct_count += 1
if answer2 == correct_answer2:
    correct_count += 1

# 점수 및 메시지 결정
if correct_count == 2:
    score_message = "당신은 100점 입니다. 쩌는군요"
elif correct_count == 1:
    score_message = "당신은 50점 입니다. 노력이 필요해요"
else:
    score_message = "당신은 0점입니다. 이 멍청한 녀석"

# 결과 메시지 출력
st.write(score_message)
