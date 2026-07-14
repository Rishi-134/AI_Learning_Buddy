import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CyberSage AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CyberSage AI - AI Learning Buddy")
st.write(
    "An AI-powered learning assistant for Cybersecurity and Artificial Intelligence."
)

# -----------------------------
# Configure Gemini
# -----------------------------
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel("gemini-2.5-flash")
except Exception:
    st.error("Gemini API Key not found. Please configure it in Streamlit Secrets.")
    st.stop()

# -----------------------------
# Session State
# -----------------------------
if "response" not in st.session_state:
    st.session_state.response = ""

# -----------------------------
# User Input
# -----------------------------
topic = st.text_input("Enter Topic")

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Topic",
        "Real-Life Example",
        "Generate Quiz",
        "Evaluate Learner Answer",
        "Full Learning Session"
    ]
)

learner_answer = ""

if activity == "Evaluate Learner Answer":
    learner_answer = st.text_area(
        "Paste Learner's Answer"
    )

# -----------------------------
# Generate Button
# -----------------------------
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        if activity == "Explain Topic":

            prompt = f"""
You are an expert instructor.

Explain the topic "{topic}" to a complete beginner using simple language.

Define the concept.

Explain why it is important.

Describe how it works step by step.

List its key components.

Mention common applications.

End with:

• Short Summary

• Three Important Points to Remember.
"""

        elif activity == "Real-Life Example":

            prompt = f"""
Provide one realistic real-world example that demonstrates "{topic}".

Explain:

Scenario

How the concept is applied

Benefits

Why it is useful

Lessons learned.
"""

        elif activity == "Generate Quiz":

            prompt = f"""
Create a quiz on "{topic}".

Generate:

4 Multiple Choice Questions

3 True/False Questions

3 Short Answer Questions

After the questions provide:

Correct Answers

Brief Explanation for each answer.
"""

        elif activity == "Evaluate Learner Answer":

            prompt = f"""
You are an experienced instructor.

Evaluate the learner's answer.

Topic:

{topic}

Learner Answer:

{learner_answer}

Assess:

Correctness

Accuracy

Completeness

Clarity

Give score out of 10.

Strengths

Mistakes

Suggestions

Model Answer
"""

        else:

            prompt = f"""
You are CyberSage AI,
an expert mentor for Cybersecurity and Artificial Intelligence.

Teach the learner about

"{topic}"

Follow this sequence.

1. Introduce topic.

2. Explain fundamentals.

3. Give one real-life example.

4. Explain important concepts.

5. Ask interactive questions.

6. Give practical exercises.

7. Evaluate learner responses.

8. Generate quiz with answers.

9. Recommend learning resources.

10. End with summary and key takeaways.

Use beginner-friendly language.
"""

        try:

            with st.spinner("Generating..."):

                response = model.generate_content(prompt)

                st.session_state.response = response.text

        except Exception as e:

            st.error(e)

# -----------------------------
# Output
# -----------------------------
if st.session_state.response:

    st.markdown("## Response")

    st.markdown(st.session_state.response)

# -----------------------------
# Clear Button
# -----------------------------
if st.button("Clear Output"):

    st.session_state.response = ""

    st.rerun()

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Created by Rishi | CyberSage AI Learning Buddy")
