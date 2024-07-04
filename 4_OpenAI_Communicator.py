import gradio as gr
import openai

dialogue = []
savetime = 2
n = 0

def get_response(dialogue):
    openai.api_key = "金鑰"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=dialogue
    )
    return response.choices[0].message['content'].strip() 

def chat(ask):
    global dialogue, n
    n += 1
    dialogue.append({"role": "user", "content": ask})  # 存放提問資料
    reply = get_response(dialogue)
    dialogue.append({"role": "assistant", "content": reply})  # 存放回覆資料
    if len(dialogue) > savetime * 2:
        dialogue = dialogue[-savetime*2:]
    return n, reply

iface = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(label="你想說的話"),
    outputs=[gr.Textbox(label="回覆次數"), gr.Textbox(label="回覆的話")],
    title="OpenAI連續對話器"
)

if __name__ == "__main__":
    iface.queue()
    iface.launch()