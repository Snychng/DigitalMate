import gradio as gr
import librosa  # 语音数据格式返回
import time
import httpx
import gradio as gr
from openai import OpenAI
import yaml

# 加载config文件
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)

http_client = httpx.Client(
    base_url=f"https://api.openai.com/v1",
    proxies={
        'http://': config['http_proxy'],
        'https://': config['https_proxy']
    }
)

ai_client = OpenAI(
    api_key=config['openai_api_key'],
    http_client=http_client
)

# 定义与OpenAI GPT模型交互的函数
def slow_echo(message, history):
    messages = []
    messages.append({"role": "system", "content": config['gpt_system']})
    # 构建历史消息列表
    for ht in history:
        if ht[1]:            
            messages.append({"role": "user", "content": ht[0]})
            messages.append({"role": "assistant", "content": ht[1]})
    messages.append({"role": "user", "content": message})

    # 请求OpenAI GPT模型生成响应
    response = ai_client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        temperature=0,
        stream=True
    )

    start_time = time.time()
    collected_chunks = []
    collected_messages = []
    try:
        for chunk in response:
            chunk_time = time.time() - start_time
            collected_chunks.append(chunk)
            chunk_message = chunk.choices[0].delta.content
            if chunk_message:
                collected_messages.append(chunk_message)
            print(f"Message received after {chunk_time:.2f} s: {chunk_message}")
            full_reply_content = ''.join(collected_messages)
            yield full_reply_content
    except Exception as e:
        full_reply_content = '意外故障'
        print(f"Error: {e}")
        yield full_reply_content


with open('./static/css/ui.css', 'r') as css_file:
    ui_css = css_file.read()

# 定义布局
with gr.Blocks(theme=gr.themes.Soft(), css=ui_css) as demo:
    with gr.Row():
            gr.Markdown("# <center> 予成")
    with gr.Tab("文本生成对话") as text2text_tab:
        with gr.Row():
            gr.Markdown("## 文本生成对话")
        with gr.Row():
            gr.ChatInterface(slow_echo)
        with gr.Row():
            gr.Markdown("<br> 这是一个基于Gradio的ChatGPT-Webui")
    with gr.Tab("语音生成对话") as text2voice_tab:
        with gr.Row():
            gr.Markdown("## 语音生成对话")

demo.queue()

# 运行界面，指定端口为 8888
demo.launch(server_name='0.0.0.0', server_port=8888)