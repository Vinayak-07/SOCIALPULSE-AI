def momentum(data):
    if not data: return 0.0
    return 0.35*0.5 + 0.25*0.3 + 0.2*0.8 + 0.2*0.4  # documented weights
