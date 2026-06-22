import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_answer(context, question):

    prompt = f"""
You are an expert PDF Document Analysis Assistant.

Answer the user's question using ONLY the provided document context.

Context:
{context}

Question:
{question}

Instructions:
- Use markdown formatting.
- Use emojis.
- Use proper headings.
- Use bullet points.
- Highlight important information.
- Do not hallucinate.
- If the answer is not present in the document, say:
  "❌ This information is not available in the uploaded document."

Format:

# 📌 Summary

- Point 1
- Point 2

# 🔍 Key Points

- Point 1
- Point 2

# ⚠️ Important Information

- Point 1
- Point 2

# 📖 Detailed Explanation

Detailed explanation here.

Answer:
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"❌ Gemini Error: {str(e)}"