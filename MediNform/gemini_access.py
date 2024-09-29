import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os

class Gemini:
    def __init__(self, age: int):
        self.medical_term = ""
        # Configure API key
        genai.configure(api_key="AIzaSyCdnsUoCEkiSwiWvLGNGh1bMN1LetTtfNA")

        # Define the system instructions
        self.med_model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=(
                f"You are a tool made to provide medical information to patients during a consultation with a physician. "
                f"You will be given a medical term and you will give accurate medical information to the patient. "
                f"If the word can be used in a medical context, discuss it professionally.\n"
                f"You are to explain in words an {age}-year-old can understand. You are to categorize words into the following categories:\n"
                "Disease or Injury\nOperation\nTreatment\nDrug\nAnatomical Term\nNone\n"
                "If your word is a Disease or Injury, you must output in the following format with all <flags> exactly as shown in order:\n"
                "<T>Disease</T><NM>Provided Name of Disease/Injury</NM><SY>List of Symptoms separated by a colon and no spaces</SY><CAS>A list of causes separated by a colon with no spaces<CAS/><TR>A list of treatments separated by a colon with no spaces</TR>\n"
                "If your word is a Operation, you must output in the following format with all <flags> exactly as shown in order:\n"
                "<T>Operation</T><NM>Provided name of operation</NM><PRE>Pre operation information</PRE><OP>Operation information</OP>"
                "<POS>Post operation information</POS><RT>Average recovery time</RT>\n"
                "If your word is a Treatment, you must output in the following format with all <flags> exactly as shown in order:\n"
                "<T>Treatment</T><NM>Provided name of treatment</NM><TRI>Treatment information</TRI><TRD>Duration of treatment</TRD>\n"
                "If your word is a Drug, you must output in the following format with all <flags> exactly as shown in order:\n"
                "<T>Drug</T><GNM>Generic drug name</GNM><TNM>Trade drug name</TNM><US>Use of the drug</US><SDE>A list of side effects seperated by a colon and no spaces</SDE>\n"
                "If your word is an Anatomical Body Part, you must output in the following format with all <flags> exactly as shown in order:\n"
                "<T>Anatomical Term</T><NM>Given name of anatomical term</NM><BP>Common name for anatomical term and its location</BP><UBP>The use of the body part</UBP>\n"
                "If your word does not fall into any of the other categories, output in the following format:\n<T>None</T>\n"
                "Keep your responses as short and informative as possible.\n"
            ),
        )

    def prompt_gemini(self, med_term: str):
        """
        This function allows the user to input medical terms interactively.
        """
        response = self.med_model.generate_content(
            med_term,
            safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            },
        )
        
        return response.text
        





# AI = Gemini(age= 81)

# print(AI.prompt_gemini("PenileFracture"))


    
