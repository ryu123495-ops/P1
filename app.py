import streamlit as st

page_1 = st.Page("page_1.py", title = "Landing Page")
page_2 = st.Page("page_2.py", title = "Chatbot")
page_3 = st.Page("page_3.py", title = "Login")

pages = st.navigation([page_1, page_2, page_3], position="top")

pages.run()

# st.title("우리 회사 챗봇")

# st.write("채팅을 입력하세요.")

# st.markdown("하이하이요 *환영합니다* 반갑습니다")

# st.badge("성공", icon=":material/check:", color="green")

# import pandas as pd
# from numpy.random import default_rng as rng

# df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["삼성전자", "SK하이닉스", "삼성전기"])

# st.line_chart(df)

# col1, col2, col3 = st.columns(3)
# col1.metric("코스피", "5400", "1.2%")
# col2.metric("코스닥", "680", "-1.2%")
# col3.metric("원달러환율", "1335.4", "0.12%")