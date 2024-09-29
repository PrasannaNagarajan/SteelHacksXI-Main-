# MedInform
MediNform is a software powered by Google Gemini AI that can help bridge the information gap between medical physicians and patients.


## Description

MediNform leverages speech-to-text technology to capture live doctor-patient interactions, delivering real-time feedback and relevant information tailored to each consultation. Utilizing Google's Gemini AI, MediNform identifies diseases, injuries, medications, procedures, and treatments, offering patients additional context and support. This functionality is designed to ease the anxiety of patients who may feel overwhelmed by their medical situations.

In addition to providing reassurance, MediNform serves as an essential accessibility tool for individuals with communication challenges, such as anxiety, hearing loss and muteness. The platform adjusts its explanations based on the patient’s age, ensuring that younger patients receive simplified, easy-to-understand information, while older patients benefit from more detailed, technical descriptions. This adaptability promotes a better understanding of health issues, fostering a more comfortable and informed experience for all patients.

While just a demo, our team hopes MediNform can spark innovation in the way we approch medical consultations. We hope this demo can showcase how the power of AI can be used to help patients communicate with healthcare professionals. Being sick is stressful enough, so we want to put a focus on taking some of that stress away.

## Getting Started
To run this program:
### Windows
Run the MediNform executable file
### Other OS
Ensure you have the following python libraries installed by using ``pip install``:
- ``pyqt6``
- ``speech_recognition``
- ``google-generativeai``

Once certain all of these libraries are installed, you can run the file directly from the ``doctor.py`` file after copying the repository to your machine.

## Using the MediNform Demo
To use the MediNform, follow the steps listed in Getting Started section of the README. Then, once you run the program, you will be greeted with a "Doctor Window". This is the view the doctor will have on their computers. It contains a text box to take notes, a start transcript button, a stop transcript button, and an input for age and name. You must input the age before pressing start transcript.

Upon entering a valid age and starting the transcript, a brief initialization period will begin before a "Patient Window" will pop up. This window will showcase the patients view, which would be displayed using a tablet or other smart device. The right side of the window will contain a running list of medical terms that the patient can then click on. Once the patient clicks on a term, the terms description will display on the left side of the screen.

Once the doctor is done with their consultation, they will press the stop transcript button, which will end the AI key terms tool. The physician can then start the transcript with a new patient, or close the "Doctor Window" to end the program


## Authors
Hunter Foster
Email: 
@huf5

Michael Puthumana
Email: mip132@pitt.edu
@mputh

Prasanna Nagarajan
Email: prn37@pitt.edu
@PrasannaNagarajan

Theophilos Zervos
Email: tnz3@pitt.edu
@TheoZervos

## License
This project is licensed under the GNU General Public License v3.0 - see License.md file for details

## AI Use Notice
ChatGPT was used to aid in the creation of MediNform for help with GUI development and for understanding of certain imports

## Medical Library Notice
Access to the ``medical_wordlist.txt`` file possible through:
- https://github.com/CodeSante/medical-wordlist.git
