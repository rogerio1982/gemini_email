import pandas as pd
import google.generativeai as genai
import time

# Configure your Gemini API key
genai.configure(api_key='keykeykey')  # <-- Replace with your actual key

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Valid recruitment stage labels
valid_labels = [
    "Applied", "Interview", "Assessment/test",
    "Review", "Offer", "Rejected"
]

# Function to label emails using Gemini
def label_email_with_gemini(email_body):
    if pd.isna(email_body) or len(str(email_body).strip()) < 20:
        return "Unknown"

    prompt = f"""
You are a recruitment assistant. Classify the email below into one of the following recruitment stages:
{', '.join(valid_labels)}.

Email:
\"\"\"
{email_body}
\"\"\"

Respond only with the most appropriate label.
    """
    try:
        response = model.generate_content(prompt)
        label = response.text.strip()
        if label in valid_labels:
            return label
        return "Unknown"
    except Exception as e:
        print("Gemini API error:", e)
        return "Error"

# Load the CSV file
df = pd.read_csv("emails - emails.csv")

# Apply the labeling function
print("🔍 Labeling emails with Gemini...")

df["gemini_label"] = df["body"].apply(label_email_with_gemini)

# Save the labeled data to a new CSV
output_path = "emails_labeled_by_gemini.csv"
df.to_csv(output_path, index=False)

print(f"✅ Labeling complete. File saved as: {output_path}")
