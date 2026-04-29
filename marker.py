import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

assessment_number = "91479"

student_work = """
Velocity is the rate of change of displacement over time.
To find the velocity at t=3, I differentiate s(t) = 4t^2 + 2t
s'(t) = 8t + 2
At t=3: v = 8(3) + 2 = 26 m/s
"""

prompt = f"""
You are an NCEA marker for New Zealand high school assessments.

Assessment number: {assessment_number}
NCEA Level 2 Physics - Mechanics

Student work:
{student_work}

Please do the following:
1. Give the student a grade: Excellence, Merit, Achieved, or Not Achieved
2. Explain exactly which parts of their work earned that grade
3. Write short feedback the teacher can give the student

Format your response with these exact sections:
GRADE:
EVIDENCE:
FEEDBACK:
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)