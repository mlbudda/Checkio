# Between Markers
def between_markers(text, begin, end):
    if begin in text and end in text:
        return text[text.find(begin) + len(begin):text.find(end)]
    elif begin in text:
        return text[text.find(begin) + len(begin):]
    elif end in text:
        return text[:text.find(end)]
    else:
        return text

# Running some tests...
print(between_markers('What is >apple<', '>', '<') == "apple", "One sym")
print(between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML")
print(between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened')
print(between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close')
print(between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all')
print(between_markers('No <hi>', '>', '<') == '', 'Wrong direction')