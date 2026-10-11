def verify(assignments):
    if not assignments:
        return False
    return all(a.score >= 0.45 for a in assignments)
