# Email Classification with the Gemini API

This project uses the Gemini API (Google Generative AI) to classify emails into different stages of the recruitment process, 
such as "Applied", "Interview", "Assessment", etc. The script reads a CSV file containing email bodies and labels each email with the most appropriate classification.

## Functionality

The script performs the following steps:

1. **Loads a CSV file** containing emails.
2. **Uses the Gemini API** to classify each email into a recruitment stage.
3. **Saves the labeled emails** to a new CSV file.

### Recruitment Stages

Emails will be classified into one of the following stages:

- Applied
- Interview
- Assessment/Test
- Review
- Offer
- Rejected

Prerequisites
Before running the script, you'll need to install the project dependencies and configure the Gemini API key.

Dependencies
To install the required dependencies, you'll need Python 3.6 or higher and use pip.

Clone the repository or download the files.
In the terminal, navigate to the project directory.
Install the dependencies using the following command:
pip install -r requirements.txt

Configuring the Gemini API
Before using the Gemini API, you need to obtain an API key.
Create a Google Cloud account and enable access to the Gemini API.
Generate an API key and replace 'YOUR_API_KEY_HERE' in the code with your actual key.
genai.configure(api_key='YOUR_API_KEY_HERE')  # <-- Replace with your API key


