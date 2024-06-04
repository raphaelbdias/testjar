import ollama
from weather import url, weatherdata


weatherdata = weatherdata(url)

response = ollama.chat(model='testjar', messages=[
  {
    'role': 'user',
    'content': f'Respond the following in a prapgraph. Current weather data {weatherdata}',
  },
])
print(response['message']['content'])