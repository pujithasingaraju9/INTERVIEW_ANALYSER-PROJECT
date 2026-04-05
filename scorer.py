def calculate_score(score):
    if score > 0.7:
        return "Excellent"
    elif score > 0.4:
        return "Good"
    else:
        return "Needs Improvement"