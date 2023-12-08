from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key='enter your key here',
)

request = input("Enter your request\ntype end to stop\n")

while request.lower != "end":
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request,
            }
        ],
        model="gpt-3.5-turbo",
    )
    # generated_text = chat_completion.choices
    # print(generated_text)

    print(chat_completion.choices[0].message.content)
    
    request = input("Enter your request\ntype end to stop\n")


print("Thank you for using my project")