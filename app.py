import streamlit as st
import google.generativeai as genai

# ------------------ Gemini API ------------------
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------ Page ------------------
st.set_page_config(page_title="CyberSage AI", page_icon="🛡️")

st.title("🛡️ CyberSage AI - Learning Buddy")
st.write("Learn Cybersecurity and AI concepts using Gemini AI!")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Topic",
        "Real-Life Example",
        "Generate Quiz",
        "Evaluate Learner Answer",
        "Full Learning Session"
    ]
)

# Store output
if "response" not in st.session_state:
    st.session_state.response = ""

learner_answer = ""

if option == "Evaluate Learner Answer":
    learner_answer = st.text_area("Paste the learner's answer here")

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        if option == "Explain Topic":

            prompt = f"""
You are an expert instructor. Explain the topic "{topic}" to a complete beginner using simple language.

Define the concept.

Explain why it is important.

Describe how it works step by step.

List its key components.

Mention common applications.

End with a short summary and three important points to remember.
"""

        elif option == "Real-Life Example":

            prompt = f"""
Provide one realistic real-world example that demonstrates "{topic}".

Explain the scenario.

How the concept is applied.

Why it is useful.

Benefits it provides.

Lessons the learner should take away.
"""

        elif option == "Generate Quiz":

            prompt = f"""
Create a quiz on "{topic}" consisting of 10 questions.

Include:

• Multiple Choice Questions

• True/False Questions

• Short Answer Questions

After all questions provide correct answers with brief explanations.
"""

        elif option == "Evaluate Learner Answer":

            prompt = f"""
You are an experienced instructor.

Evaluate the learner's answer about "{topic}".

Learner's Answer:

{learner_answer}

Assess:

Correctness

Accuracy

Completeness

Clarity

Give a score out of 10.

Identify strengths.

Explain mistakes.

Provide suggestions for improvement.

Finally provide a model answer.
"""

        else:

            prompt = f"""
You are CyberSage AI, an expert mentor for cybersecurity and artificial intelligence.

Teach the learner about "{topic}" from beginner to advanced level.

Follow this sequence:

1. Introduce the topic.

2. Explain the fundamentals in simple language.

3. Provide one real-life example.

4. Explain important concepts step by step.

5. Ask interactive questions.

6. Give practical exercises.

7. Evaluate learner responses.

8. Generate a short quiz with answers.

9. Recommend learning resources.

10. End with summary and key takeaways.

Use simple language and encourage the learner throughout.
"""

        response = model.generate_content(prompt)

        st.session_state.response = response.text

# Display output
if st.session_state.response:
    st.markdown(st.session_state.response)

st.markdown("---")
st.caption("Created by Rishi | CyberSage AI Learning Buddy")
