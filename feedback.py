def generate_feedback(result):
    if result == "Excellent":
        return "Great answer!"
    elif result == "Good":
        return "Try to improve clarity."
    else:
        return "Work on fundamentals."