import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from groq import Groq

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        assessment_number = request.form["assessment_number"]
        student_work = request.form["student_work"]

        prompt = f"""
You are an NCEA marker for New Zealand high school assessments.

Assessment number: {assessment_number}
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
        result = response.choices[0].message.content

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)