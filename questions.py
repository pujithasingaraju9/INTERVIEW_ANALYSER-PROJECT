import random

# Question bank (role-based)
questions_db = {
    "backend_developer": [
        "What is an API?",
        "Explain REST architecture.",
        "What is database normalization?",
        "Difference between SQL and NoSQL?",
        "What is indexing in databases?",
        "Explain CRUD operations.",
        "What is middleware in backend?",
        "What is authentication vs authorization?",
        "Explain HTTP methods (GET, POST, PUT, DELETE).",
        "What is a server?"
    ],

    "software_engineer": [
        "What is OOP?",
        "Explain inheritance.",
        "What is polymorphism?",
        "What is encapsulation?",
        "What is a data structure?",
        "Difference between stack and queue?",
        "What is recursion?",
        "What is time complexity?",
        "Explain Big-O notation.",
        "What is debugging?"
    ],

    "hr": [
        "Tell me about yourself.",
        "What are your strengths?",
        "What are your weaknesses?",
        "Why should we hire you?",
        "Where do you see yourself in 5 years?",
        "Describe a challenge you faced.",
        "How do you handle stress?",
        "Why do you want this job?",
        "What motivates you?",
        "Describe your teamwork experience."
    ]
}

def get_questions(role):
    return questions_db.get(role, [])

def get_random_question(role):
    questions = get_questions(role)
    if questions:
        return random.choice(questions)
    return "No questions available for this role."