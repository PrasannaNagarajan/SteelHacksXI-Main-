import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

import os

medical_term = ""
age = 81

# Use your API key here, or retrieve it from an environment variable
genai.configure(api_key="AIzaSyCdnsUoCEkiSwiWvLGNGh1bMN1LetTtfNA")

# creating model with system instructions
med_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction = "You are a tool made to provide medical information to patients during a consultation with a physician. You will be given a word and you will give accurate medical information to the patient. If the word can be used in a medical context, discuss it professionally"
    f"You are to explain in words a {age} year old can understand. You are to categorize words into the following categories:\n"
    "Disease/Injury\nOperation\nTreatment\nDrug\nAnatomical Term\nNone\n"
    "If your word is a Disease/Injury, output in the following format:\n<T>Disease</T><NM>Provided Name of Disease/Injury</NM><SY>List of Symptoms separated by a comma and no spaces</SY><CS>A list of causes separated by a comma with no spaces</CS><TR>A list of treatments separated by a comma with no spaces</TR>"
    "If your word is a Operation, output in the following format:\n<T>Operation</T><NM>Provided name of operation</NM><PRE>Pre operation information</PRE><OP>Operation information</OP><POS>Post operation information</POS><RT>Average recovery time</RT>"
    "If your word is a Treatment, output in the following format:\n<T>Treatment</T><NM>Provided name of treatment</NM><TRI>Treatment information</TRI><TRD>Duration of treatment</TRD>"
    "If your word is a Drug, output in the following format:\n<T>Drug<T><GNM>Generic drug name</GNM><TNM>Trade drug name</TNM><US>Use of the drug</US><SDE>Side effects of the drug</SDE>"
    "If your word is an Anatomical Body Part, output in the following format:\n<T>Anatomical Term</T><NM>Given name of anatomical term</NM><BP>Common name for anatomical term and it’s location</BP><UBP>The use of the body part</BP>"
    "If your word does not fall into any of the other categories, output in the following format:\n<T>None</T>"
    f"Keep your responses as short and informative as possible.\n",
)

while(True):
    medical_term = input("Enter medical term or q to quit:\n")
    if(medical_term == "q"):
        break

    response = med_model.generate_content(
        medical_term,
        safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,},
    )
    print(response.text)
    
