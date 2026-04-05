import streamlit as st
from backend.questions import get_questions
from backend.analyzer import analyze_answer
from backend.scorer import calculate_score
from backend.feedback import generate_feedback

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Interview Analyzer", page_icon="🎤", layout="centered")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .stTextArea textarea {
        border-radius: 10px;
    }
    .card {
        background-color: #1c1f26;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown("<h1 style='text-align: center;'>🎤 Interview Performance Analyzer</h1>", unsafe_allow_html=True)

# ------------------ ROLE SELECT ------------------
role = st.selectbox("Select Job Role", ["backend_developer", "software_engineer", "hr"])

# ------------------ SESSION STATE ------------------
if "questions" not in st.session_state:
    st.session_state.questions = []
    st.session_state.q_index = 0
    st.session_state.scores = []

# ------------------ START BUTTON ------------------
if st.button("🚀 Start Interview"):
    st.session_state.questions = get_questions(role)
    st.session_state.q_index = 0
    st.session_state.scores = []

# ------------------ SHOW QUESTIONS ------------------
if st.session_state.questions:
    total_q = len(st.session_state.questions)
    current_index = st.session_state.q_index
    current_q = st.session_state.questions[current_index]

    # Progress bar
    progress = (current_index + 1) / total_q
    st.progress(progress)

    # Question Card
    st.markdown(f"""
        <div class="card">
            <h3>Question {current_index + 1} of {total_q}</h3>
            <p>{current_q}</p>
        </div>
    """, unsafe_allow_html=True)

    # Answer box
    answer = st.text_area("✍️ Your Answer")

    if st.button("✅ Submit Answer"):
        ideal_answer = "This is a sample ideal answer for evaluation"

        similarity = analyze_answer(answer, ideal_answer)
        result = calculate_score(similarity)
        feedback = generate_feedback(result)

        st.session_state.scores.append(similarity)

        # Result Card
        st.markdown(f"""
            <div class="card">
                <h4>📊 Result: {result}</h4>
                <p>Similarity Score: {round(similarity, 2)}</p>
                <p>💡 Feedback: {feedback}</p>
            </div>
        """, unsafe_allow_html=True)

        # Next question
        if current_index < total_q - 1:
            if st.button("➡️ Next Question"):
                st.session_state.q_index += 1
        else:
            st.success("🎉 Interview Completed!")

            avg_score = sum(st.session_state.scores) / len(st.session_state.scores)

            st.markdown(f"""
                <div class="card">
                    <h3>📈 Final Report</h3>
                    <p>Average Score: {round(avg_score, 2)}</p>
                </div>
            """, unsafe_allow_html=True)

            if avg_score > 0.7:
                st.success("🔥 Excellent Performance!")
            elif avg_score > 0.4:
                st.info("👍 Good Performance!")
            else:
                st.error("⚠️ Needs Improvement!")