import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6JAD_bkCcLtLz9AHxOqetQnoq7wwGxt7mN44wrSNHujTw")

for model in genai.list_models():
    print(model.name)