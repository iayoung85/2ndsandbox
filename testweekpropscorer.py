#scores a proposed set of group assignments based on how many times each pairing has been used in the past
def week_prop_scorer(proposedpairs,all_groups):
    score=0
    for n in all_groups:
        if n in proposedpairs or [n[1],n[0]] in proposedpairs:
            score+=1
    return score
test=week_prop_scorer([['e', 'b'], ['a', 'h'], ['f', 'c'], ['g', 'd']],[['a', 'd'], ['c', 'b'], ['a', 'b'], ['d', 'c'], ['a', 'c'], ['b', 'd'], ['b', 'd'], ['a', 'c'], ['b', 'e'], ['a', 'd'], ['c', 'f'], ['d', 'join another group'], ['b', 'f'], ['c', 'g'], ['a', 'e'], ['c', 'd'], ['e', 'g'], ['a', 'f'], ['b', 'h'], ['a', 'b'], ['c', 'e'], ['d', 'f'], ['h', 'g'], ['e', 'd'], ['a', 'g'], ['b', 'c'], ['f', 'h']]
)
print(test)

negtest=week_prop_scorer([['f', 'e'], ['h', 'c'], ['g', 'b'], ['a', 'd']],[['a', 'd'], ['c', 'b'], ['a', 'b'], ['d', 'c'], ['a', 'c'], ['b', 'd'], ['b', 'd'], ['a', 'c'], ['b', 'e'], ['a', 'd'], ['c', 'f'], ['d', 'join another group'], ['b', 'f'], ['c', 'g'], ['a', 'e'], ['c', 'd'], ['e', 'g'], ['a', 'f'], ['b', 'h'], ['a', 'b'], ['c', 'e'], ['d', 'f'], ['h', 'g'], ['e', 'd'], ['a', 'g'], ['b', 'c'], ['f', 'h']]
)
print(negtest)