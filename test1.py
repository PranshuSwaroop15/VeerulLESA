# api_key="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"

import os
import openai

import gradio as gr
openai.api_key = "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"


# print(openai.Model.list())

# ans=openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Say this is a test",
#   max_tokens=7,
#   temperature=0
# )

# print(ans)
# start_sequence="\nAI:"

# restart_sequence="\nHuman:"

start = "Your are a AI Search Engine, answer the following query with a witty answer and include validated facts only."

def generate(prompt):
    start_sequence = "{}.{}".format(start,prompt)
    completions = openai.Completion.create(
      model="text-davinci-003",
      prompt=start_sequence,
      temperature=0.1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0.51,
      presence_penalty=0.5,
      #stream = False,
      #echo = True
    )
          
    
    message = completions.choices[0].text
    # print(f"AI Response : {message}")
    return message

# generate("How many days are there in a week")

# while True:
    
#     query=input("Ask a Question to AI\n")

#     generate(query)


def chatgpt_clone(input,history):
    
    history=history or []

    s=list(sum(history,()))

    s.append(input)

    inp=''.join(s)

    output=generate(inp)
    history.append((input,output))
    return history,history

    

block=gr.Blocks()

with block:
    gr.Markdown("""<h1><center>Alfred AI Assistant</center></h1>""")
    chatbot=gr.Chatbot()
    message=gr.Textbox(placeholder=start)

    state=gr.State()
    submit=gr.Button("Send")
    submit.click(chatgpt_clone,inputs=[message,state],outputs=[chatbot,state])


block.launch(debug=True)


