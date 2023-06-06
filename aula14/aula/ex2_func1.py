def sera_primo(n):
    if n in [0,1]:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True