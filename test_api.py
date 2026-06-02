import google.generativeai as genai

genai.configure(
    api_key="AQ.Ab8RN6JAD_bkCcLtLz9AHxOqetQnoq7wwGxt7mN44wrSNHujTw"
)

models = genai.list_models()

for model in models:
    print(model.name)