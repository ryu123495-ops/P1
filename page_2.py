import streamlit as st
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def get_weather(location : str) -> str :
  "특정 지역의 날씨 정보 반환"
  return f"{location} 날씨가 맑습니다"

tavily_tool = TavilySearch(
    max_results=5,
    topic="general",
    # include_answer=False,
    # include_raw_content=False,
    # include_images=False,
    # include_image_descriptions=False,
    # search_depth="basic",
    # time_range="day",
    # include_domains=None,
    # exclude_domains=None
)

model = init_chat_model("gpt-5.5")

if "agent" not in st.session_state :
    st.session_state.agent = create_agent(model, tools = [get_weather, tavily_tool], checkpointer=InMemorySaver())

if "messages" not in st.session_state :
    st.session_state.messages = []

st.title("우리 회사 챗봇")

prompt = st.chat_input("무엇이든 물어보세요")
if prompt:
    # response = model.invoke(prompt)

    response = st.session_state.agent.invoke(
        {"messages" : [HumanMessage(prompt)]},
        {"configurable" : {"thread_id" : "1"}}
    )
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    st.session_state.messages.append({"role" : "ai", "content" : response['messages'][-1].content})

for message in st.session_state.messages :
    with st.chat_message(message['role']) :
        st.write(message['content'])