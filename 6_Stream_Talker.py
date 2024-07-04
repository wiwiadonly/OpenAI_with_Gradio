import openai

dialogue = []
savetime = 2
openai.api_key = "金鑰"

def get_response(dialogue):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=dialogue,
        stream=True
    )
    for chunk in response:
        if "choices" in chunk and chunk.choices[0].delta and "content" in chunk.choices[0].delta:
            yield chunk.choices[0].delta.content

def chat(ask):
    global dialogue
    dialogue.append({"role": "user", "content": ask})  # 存放提問資料
    full_reply = ""
    for answer in get_response(dialogue):
        full_reply += answer
        print(answer, end="")
    dialogue.append({"role": "assistant", "content": full_reply})  # 存放回覆資料
    while len(dialogue) > savetime * 2:
        dialogue.pop(0)
    return full_reply

if __name__ == "__main__":
    n = 0
    while True:
        n += 1
        ask = input('你想問什麼？')
        if ask == 'q':
            break
        answer = chat(ask)
        print(f'\n----------第{n}次回覆----------')
        print(f'回覆內容:{answer}')
        print(f'串列內容:{dialogue}')