# Between Markers (simplified)

def between_markers(text, begin, end):
    a = text.find(begin) + 1
    b = text.find(end)
    return text[a:b]

# Running some tests...
print(between_markers('What is >apple<', '>', '<') == "apple")
print(between_markers('What is [apple]', '[', ']') == "apple")
print(between_markers('What is ><', '>', '<') == "")
print(between_markers('>apple<', '>', '<') == "apple")
