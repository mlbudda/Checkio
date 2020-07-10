import re
# Stressful Subject
def is_stressful(subj):
    """
        recognize stressful subject
    """
    subj_lower = subj.lower()

    x = re.search('h+e+l+p|h.e.l.p|a+s+a+p|a.s.a.p|u+r+g+e+n+t|u.r.g.e.n.t', subj_lower)

    if x or subj[-3:] == '!!!' or subj.isupper():
        return True
    else:
        return False

# Running some tests..
print(is_stressful("Hi") == False)
print(is_stressful("I neeed HELP") == True)