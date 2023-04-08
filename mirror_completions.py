import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)