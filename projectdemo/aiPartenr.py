import streamlit as st
import os   #系统模块，用于管理环境变量
from openai import OpenAI   #用于调用OpenAI API
from openai.types.chat import ChatCompletion, ChatCompletionChunk
import datetime
import json


print("重新执行该文件")

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),  #获取环境变量中的API密钥
    base_url="https://api.deepseek.com" )        #OpenAI API的地址

#系统提示词
system_message="""你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色
                  规则：
                     1．每次只回 1 条消息
                     2．禁止任何场景或状态描述性文字
                     3．匹配用户的语言
                     4．回复简短，像微信聊天一样
                     5．有需要的话可以用❤️🌸等 emoji 表情
                     6．用符合伴侣性格的方式对话
                     7．回复的内容，要充分体现伴侣的性格特征
                  伴侣性格：
                        ‑ %s
                   你必须严格遵守上述规则来回复用户。"""

#初始化聊天信息
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
#初始化昵称
if "partner_name" not in st.session_state:
    st.session_state.partner_name = "小甜甜"
#初始化伴侣性格
if "partner_character" not in st.session_state:
    st.session_state.partner_character = "活泼开朗的东北姑娘"
#初始化会话的标识
if "session_id" not in st.session_state:
    st.session_state.session_id = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#保存会话
def save_session():
    session_data = {
        "chat_history": st.session_state.chat_history,
        "partner_name": st.session_state.partner_name,
        "partner_character": st.session_state.partner_character,
        "session_id": st.session_state.session_id
    }
    with open(f"resourse/session_data_{st.session_state.session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

#从文件夹中获取会话列表
def load_sessions():
    sessions = []
    for file in os.listdir("resourse"):
        if file.startswith("session_data_") and file.endswith(".json"):
            sessions.append(file[13:-5])
    return sessions

#加载会话
def load_conference(session):
    with open(f"resourse/session_data_{session}.json", "r", encoding="utf-8") as f:
        session_data = json.load(f)
    st.session_state.chat_history = session_data["chat_history"]
    st.session_state.partner_name = session_data["partner_name"]
    st.session_state.partner_character = session_data["partner_character"]
    st.session_state.session_id = session_data["session_id"]

#删除会话
def delete_conference(session):
    os.remove(f"resourse/session_data_{session}.json")
    if session == st.session_state.session_id:
        st.session_state.chat_history = []
        st.session_state.partner_name = "小甜甜"
        st.session_state.partner_character = "活泼开朗的东北姑娘"
        st.session_state.session_id = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#展示页面
#设置一个标题
st.title("AI 智能伴侣")

#展示聊天历史
for message in st.session_state.chat_history:
    st.chat_message(message["role"]).write(message["content"])

# 置页面的配置项
st.set_page_config (
  page_title="AI 智能伴侣",
  page_icon="🤖",
  # 布局
  layout="wide",
  # 控制的是侧边栏的状态
  initial_sidebar_state="expanded",
  menu_items={}
)

#with:上下文管理器，代码块里的代码会在上下文管理器中执行
with st.sidebar:
    #AI控制面板
    st.subheader("AI控制面板")
    #新建会话
    if st.button("新建会话",width="stretch"):
        if st.session_state.chat_history:
            st.session_state.chat_history = []
            st.session_state.partner_name = "小甜甜"
            st.session_state.partner_character = "活泼开朗的东北姑娘"
            st.session_state.session_id = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            save_session()
            # 重新运行该文件:在网页的每一次交互都会重新运行该文件，所以它会先加载旧数据，因此需要重新运行该文件以加载新数据
            st.rerun()

    #会话历史
    st.text("会话历史")
    sessions = load_sessions()
    for session in sessions:
        col1,col2=st.columns([4,1])
        with col1:    #设置key，一个上下文中，key不能重复
            if st.button(session,width="stretch",key=f"load_{session}",type="primary" if session==st.session_state.session_id else "secondary"):
                load_conference(session)
                st.rerun()
        with col2:
            if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):
                delete_conference(session)
                st.rerun()
    st.subheader("伴侣信息")
    # 添加一个输入框，用于输入伴侣名称
    partner_name = st.text_input("伴侣名称", placeholder="请输入伴侣名称", value=st.session_state.partner_name)
    if partner_name:
        st.session_state.partner_name = partner_name
    # 添加一个输入框，用于输入伴侣性格
    partner_character = st.text_area("伴侣性格", placeholder="请输入伴侣性格", value=st.session_state.partner_character)
    if partner_character:
        st.session_state.partner_character = partner_character

#消息输入框
message = st.chat_input("请输入你的问题：")
if message:
    #将用户信息写入聊天窗口
    st.chat_message("user").write(message)
    print("用户输入：", message)
    #将用户信息写入聊天历史
    st.session_state.chat_history.append({"role": "user", "content": message})
    response = client.chat.completions.create(  # 调用OpenAI API的chat.completions.create方法
        model="deepseek-v4-pro",  # 使用deepseek-v4-pro模型
        messages=[
            {"role": "system", "content":  system_message % (st.session_state.partner_name, st.session_state.partner_character) },  #系统消息
             *st.session_state.chat_history
            ]  ,
        stream=True
    )
   #非流式输出
   # print("AI输出：", response.choices[0].message.content)
   # 将AI信息写入聊天窗口
   # st.chat_message("assistant").write(response.choices[0].message.content)

    #流式输出
    response_message=st.empty()

    full_response=""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content=chunk.choices[0].delta .content
            full_response+=content
            with response_message:
                st.chat_message("assistant").write(full_response)

       #将AI信息写入聊天历史
    st.session_state.chat_history.append({"role": "assistant", "content": full_response})
    save_session()
    st.rerun()

