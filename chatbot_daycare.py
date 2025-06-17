# download model on ollama.com
# ollama run llama3.2
# pip install ollama
# ollama pull llama 3.2

import ollama

def chat_with_HappyKids():
    print("Start chatting with Happy Kids Daycare. 'exit' command to exit")
    
    # give context to the bot, provide basic information needed to answer user enquiries.
    context = 'you are the manager of the daycare. You must provide uprecise and accurate responses. Here are some details about the daycare: daycare is open from Monday through Friday from 8am to 5.30pm. Daycare has openings available for part-time and full-time day. Kids must be at least 2 years old and not older than 5years old. Kids have to be potty trained. Food and snacks are provided. We can provide tours to enquiring parents, tours are available tuesdays at 6pm. Respond to user queries accordingly. Here is the first query '

    while True:
        user_input = input("Parent: ")
        
        if user_input.lower() == "exit":
            break
        
        stream = ollama.chat(
            model="llama3.2",
            messages=[{"role": "user", "content": context+user_input}],
            stream=True
        )
        
        print("Happy Kids Daycare: ", end="")
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
        print ('\n')
            
chat_with_HappyKids()