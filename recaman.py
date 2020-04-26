def calculate_racaman(stepps):
    placestaken = []
    hopdistance = 0
    i = 0
    while (hopdistance < stepps):
        placestaken.append(i)
        hopdistance += 1
        nexti = i - hopdistance
        if ((nexti < 0) or (nexti in placestaken)):
            nexti = i + hopdistance
        i = nexti
    return placestaken