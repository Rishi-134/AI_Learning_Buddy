import streamlit as st

st.set_page_config(page_title="CyberSage AI", page_icon="🛡️")

st.title("🛡️ CyberSage AI - Learning Buddy")
st.write("Learn Cybersecurity in a simple and interactive way!")

topic = st.text_input("Enter a cybersecurity topic:", "Phishing")

if "show_content" not in st.session_state:
    st.session_state.show_content = False

if st.button("Teach Me"):
    st.session_state.show_content = True

if st.session_state.show_content:

    st.header(f"📚 Topic: {topic}")

    st.subheader("Definition")
    st.write(
        f"{topic} is a cybersecurity concept. It is important because it helps protect systems, data, and users from cyber threats."
    )

    st.subheader("Real-Life Example")
    st.write(
        "Example: You receive an email pretending to be from your bank asking you to click a link and enter your password. This is a common phishing attack."
    )

    st.subheader("Quick Quiz")

    answer = st.radio(
        "Which of the following is the safest action?",
        [
            "Click every email link",
            "Share your password",
            "Verify the sender and URL before clicking",
            "Ignore software updates",
        ],
    )

    if st.button("Check Answer"):
        if answer == "Verify the sender and URL before clicking":
            st.success("✅ Correct! Great job.")
        else:
            st.error("❌ Incorrect. The safest practice is to verify the sender and URL before clicking links.")

st.markdown("---")
st.caption("Created by Rishi | AI Learning Buddy Assignment")
