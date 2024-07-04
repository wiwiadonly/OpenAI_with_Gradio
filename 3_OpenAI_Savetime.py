import openai

dialogue=[]
savetime=2

def get_response(dialogue):
  openai.api_key = "金鑰"
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=dialogue

  )
  return response.choices[0].message['content'].strip() 


def chat(ask):
  global dialogue
  dialogue.append({"role": "user", "content": ask}) #存放提問資料
  reply = get_response(dialogue)
  dialogue.append({"role": "assistant", "content": reply}) #存放回覆資料
  while len(dialogue)>savetime*2:
    dialogue.pop(0)
  return reply 


if __name__=="__main__":
  n=0
  while(1):
    n+=1
    ask=input('你想問什麼？')
    if ask=='q':
      break
    answer=chat(ask)
    print(f'----------第{n}次回覆:{answer}----------')
    print(f'回覆內容:{answer}')
    print(f'串列內容:{dialogue}')