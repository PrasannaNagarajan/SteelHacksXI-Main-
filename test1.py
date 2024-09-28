import google.generativeai as genai
import os


medical_term = "appendectomy"
age = 81

# Use your API key here, or retrieve it from an environment variable
genai.configure(api_key="AIzaSyCdnsUoCEkiSwiWvLGNGh1bMN1LetTtfNA")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(f"Explain to a {age}-year-old about {medical_term}.\n\n"
        f"**Why would someone need it?**\n"
        f"- Explain why {medical_term} might be needed, whether it's for a condition, surgery, or treatment.\n\n"
        
        f"**What happens during the surgery/disease/drug/treatment?**\n"
        f"- If it's a surgery, explain what happens during the operation. If it's a disease, explain how it affects the body. If it's a drug, explain how it works.\n\n"
        
        f"**Recovery time (if applicable):**\n"
        f"- If it involves surgery or treatment, explain the general recovery time. If not, discuss the usual course of treatment or how long the drug takes to work.\n\n"
        
        f"**Important to remember:**\n"
        f"- Highlight any important points about {medical_term}, such as common side effects (for drugs), risks (for surgeries), or daily care routines (for diseases).\n\n"
        
        
        f"put this at the end of every prompt :Remember, your doctor is your best resource for information about your specific situation. Don't hesitate to ask questions!\n\n"
        
        f"put the title as bold for each of the subheadings in the output"
        
        
    )
print(response.text)
