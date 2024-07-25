
import streamlit as st

with st.echo():
    st.title('오늘 하루')

    st.subheader('----------------------------------------------')

    st.subheader('날씨')
    st.write('천둥 비 ')
    st.write('우리집 최강 강아지가 엄청 무서워함')
             
    st.subheader('cds 과제하기')
    st.write('3차시까지')

    st.button("할 일 완료", type="primary")
    if st.button("할 일 미완료"):
        st.write("게으른 녀석")
    else:
        st.write("넌 최고야 멋져")

    #python -m streamlit run bb.py