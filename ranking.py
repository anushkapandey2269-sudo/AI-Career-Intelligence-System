def rank_resumes(resume_list):
    results = []

    for name, text, score in resume_list:
        results.append((name, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results