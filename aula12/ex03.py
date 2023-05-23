def bissexto(ano):
    if ano % 100 == 0 and ano > 400:
        if ano % 400 == 0: return 1
        return 0
    if ano % 4 == 0: return 1
    return 0