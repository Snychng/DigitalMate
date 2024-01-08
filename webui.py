import gradio as gr

# 定义与GPT模型交互的函数
def gpt_response(input_text, onload_checkbox, slider):
    # 实际应用中应从GPT模型获取响应
    return "这是GPT的响应示例。"

# 创建GPT API接口展示框和用户输入框
# 在这个例子中，我们直接使用了gpt_response函数作为Gradio接口的fn参数

# 定义布局
with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# 予成AI数字人")
    with gr.Row():
        gr.Image(value="./static/pic/pic2.jpg", label="Image Demo")
    with gr.Row():
        input_text = gr.Textbox(label="输入您的问题", placeholder="请输入您的问题", lines=2)
        output_text = gr.Textbox(label="GPT的响应", lines=4)
        # input_text.change(fn=gpt_response, inputs=input_text, outputs=output_text)
    with gr.Row():
        submit_button = gr.Button("提交")  # 创建提交按钮
        stop_button = gr.Button("停止", variant="secondary")  # 创建停止按钮
    with gr.Row():
        gr.Interface(
            fn=gpt_response,
            inputs=["text", "checkbox", gr.Slider(0, 100)],
            outputs=["text", "number"],
        )

# 运行界面，指定端口为 8888
demo.launch(server_port=8888)