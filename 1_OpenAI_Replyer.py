import gradio as gr
import openai

def openaireply(ask):
  openai.api_key = "金鑰"
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "user", "content": ask}
      ]
  )
  return response.choices[0].message['content'].strip() 


def getask(ask):
    reply = openaireply(ask)
    return reply 

iface = gr.Interface(
    fn=getask,
    inputs=gr.Textbox(label="你想說的話"),
    outputs=gr.Textbox(label="回覆的話"),
    title="OpenAI回覆器"
)

if __name__ == "__main__":
    iface.queue()
    iface.launch()