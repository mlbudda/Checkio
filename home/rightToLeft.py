# Right to Left
def left_join(phrases: tuple) -> str:
    new = ''
    for i in phrases:
        changed = str(i)
        new = new + changed.replace('right', 'left') + ','
    return new[:-1]

# Running some tests...
print(left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left")
print(left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left")
print(left_join(("brightness wright",)) == "bleftness wleft", "One phrase")
print(left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace")