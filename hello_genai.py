import google.generativeai as genai
import os


genai.configure(api_key=os.environ["GEMINI_API"])
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Crie uma história sobre um computador mágico")


with open("curriculo-joao-silva.txt") as file:
    curriculum = file.read()

response = model.generate_content(
    f"Deixar o meu currículo mais resumido e assertivo:{curriculum}")

print(response.text)