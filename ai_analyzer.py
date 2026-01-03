import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


REPORT_PATH = 'reports/log_report.txt'
MODEL_NAME = 'gemini-2.5-flash'

load_dotenv()

def read_incident_report(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Report file not found: {path}")
    with open(path, 'r') as file:
        return file.read()

def build_chain():

    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        temperature=0.1,
        max_output_tokens=120,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )


    prompt = ChatPromptTemplate.from_messages([
        ("system", "Act as a senior DevOps engineer specializing in log analysis and system reliability."),
        ("user", (
            """Analyze the incident report below.

                Rules (STRICT):
                - Output MAX 6 bullet points total
                - Each bullet ≤ 12 words
                - No paragraphs
                - No explanations
                - No storytelling
                - No markdown headers
                - No emojis
                - Be factual and direct

                Required bullets:
                1. What happened, When, In which tineframe
                2. Primary root cause
                3. Secondary cause (if any)
                4. Affected services
                5. Immediate fix
                6. Long-term prevention"""
        ))
    ])


    chain = prompt | llm | StrOutputParser()
    return chain

def analyze_logs_with_gemini(report_path=REPORT_PATH):
    report_content = read_incident_report(report_path)
    chain = build_chain()
    analysis = chain.invoke({"report": report_content})
    return analysis

# def main():
#     try:
#         print("Starting log analysis...")
#         analysis = analyze_logs_with_gemini()
#         print("\nAI Analysis of Log Report:\n")
#         print("-" * 30)
#         print(analysis)
#     except Exception as e:
#         print(f"Error during AI analysis: {e}")

# if __name__ == "__main__":
#     main()