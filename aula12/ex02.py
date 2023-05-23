def primo(n):
    if n < 2: return False
    for i in range(2,n):
        if not n % i: return False
    return True