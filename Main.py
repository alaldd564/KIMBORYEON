import streamlit as st

# age = st.slider("How old are you?")
# st.write("I'm",age,"year")

st.set_page_config(
    page_title="Main",
    page_icon="👋",
)
""

st.title("시험에 도전한 여러분을 환영합니다 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """""
    문제는 총 2문제로 구성되어 있으며 주관식입니다.
    **👈 왼쪽 상단에 exam에서 문제를 풀고 solution에서 정답과 풀이를 확인해보세요(이때 정답인 문제는 풀이가 뜨지 않습니다)
    이후 score에서 점수를 확인하고 나가시면 됩니다. 
    문제풀이 시간은 총 3분동안 진행되면 문제를 먼저 끝내신 응시자분들은 조용히 퇴실해주시길 부탁드립니다.

"""
)