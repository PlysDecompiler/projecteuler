#https://projecteuler.net/problem=54

hands = open('poker.txt', 'r').read().split('\n')
hands = [(h.split(' ')[:5], h.split(' ')[5:]) for h in hands if h != '']

values = '23456789TJQKA'
inds = {v: values.index(v) for v in values}

def is_flush(hand):
    return all(hand[0][1] == hand[i][1] for i in range(1,5)) 

def is_straight(counts):
    longvalues = 'A'+values
    if any(all([(longvalues[i+k] in counts and counts[longvalues[i+k]] == 1) for k in range(5)]) for i in range(len(longvalues)-5)):
        return True
    else:
        return False        

def counts(hand):
    d = {}
    for card in hand:
        val = card[0]
        if val not in d:
            d[val] = 0
        d[val]+=1
    return d

wins = 0

def analyse(allhands):
    global wins
    global flushstring
    for hand in allhands:
        c1, c2 = counts(hand[0]), counts(hand[1])
        f1, f2 = is_flush(hand[0]), is_flush(hand[1])
        s1, s2 = is_straight(c1), is_straight(c2)
        sort1 = sorted(c1.keys(), key = lambda k: inds[k])
        sort2 = sorted(c2.keys(), key = lambda k: inds[k])

        #Straight Flush                    
        if f1 and f2 and s1 and s2:
            if inds[sort1[-2]] > inds[sort2[-2]]:
                wins+=1
                continue
            elif inds[sort1[-2]] < inds[sort2[-2]]: 
                continue
        #Quadruples
        for k in values[::-1]:
            if k in c1 and c1[k] == 4:
                wins+=1
                break
            elif k in c2 and c2[k] == 4:
                break
        else:
            #Full Houses
            for k in values[::-1]:
                if k in c1 and c1[k] == 3:
                    if 2 in c1.values():
                        wins+=1
                        break
                elif k in c2 and c2[k] == 3:
                    if 2 in c2.values():
                        break
            else:
                #flushes
                if f1 and not f2:
                    wins+=1
                    continue
                elif f2 and not f1:
                    continue
                elif f1 and f2:
                    for highest in range(1,6):
                        if inds[sort1[-highest]] > inds[sort2[-highest]]:
                            wins+=1
                            break
                        elif inds[sort1[-highest]] < inds[sort2[-highest]]:
                            break
                else:
                    #straights
                    if s1 and not s2:
                        wins+=1
                        continue
                    elif s2 and not s1:
                        continue
                    elif s1 and s2:
                        if inds[sort1[-2]] > inds[sort2[-2]]:
                            wins+=1
                            continue
                        elif inds[sort1[-2]] < inds[sort2[-2]]:
                            continue
                    #triplets
                    for k in values[::-1]:
                        if k in c1 and c1[k] == 3:
                            wins+=1
                            break
                        elif k in c2 and c2[k] == 3:
                            break
                    else:
                        dbls1 = [so for so in sort1 if c1[so] == 2]
                        unique1 = [so for so in sort1 if c1[so] == 1]
                        dbls2 = [so for so in sort2 if c2[so] == 2]
                        unique2 = [so for so in sort2 if c2[so] == 1]

                        if len(dbls1) and len(dbls2):
                            #one or two pairs
                            if len(dbls1) > len(dbls2):
                                wins+=1
                                continue
                            elif len(dbls1) < len(dbls2):
                                continue
                            else:
                                if len(dbls1) == 2:
                                    #two pairs
                                    if inds[dbls1[-1]] > inds[dbls2[-1]]:
                                        wins+=1
                                        continue
                                    elif inds[dbls1[-1]] < inds[dbls2[-1]]:
                                        continue
                                    else:
                                        if inds[dbls1[-2]] > inds[dbls2[-2]]:
                                            wins+=1
                                            continue
                                        elif inds[dbls1[-2]] < inds[dbls2[-2]]:
                                            continue
                                        else:
                                            if inds[unique1[-1]] > inds[unique2[-1]]:
                                                wins+=1
                                                continue
                                            elif inds[unique1[-1]] < inds[unique2[-1]]:
                                                continue
                                elif len(dbls1) == 1:
                                    #one pair
                                    if inds[dbls1[-1]] > inds[dbls2[-1]]:
                                        wins+=1
                                        continue
                                    elif inds[dbls1[-1]] < inds[dbls2[-1]]:
                                        continue
                                    else:
                                        for y in range(1,4):
                                            if inds[unique1[-y]] > inds[unique2[-y]]:
                                                wins+=1
                                                break
                                            elif inds[unique1[-y]] < inds[unique2[-y]]:
                                                break
                        elif len(dbls1):
                            wins+=1
                            continue
                        elif len(dbls2):
                            continue
                        else:
                            #check highest card
                            for j in range(1,6):
                                if inds[unique1[-j]] > inds[unique2[-j]]:
                                    wins+=1
                                    break
                                elif inds[unique1[-j]] < inds[unique2[-j]]:
                                    break

analyse(hands)
print wins

#solution: 376
#There is definitely room to improve the algorithms and also to detect a draw and also to deal with the game-mode of Texas Hold'em
