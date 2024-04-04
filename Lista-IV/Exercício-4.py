textinput = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''
print("Original:", textinput)

textinput = textinput.lower().strip(".,:;?!").split()
print("Edited:", textinput)
textout = []

for word in textinput:
    if word.startswith(('p', 'y', 't', 'h')) or word.endswith(('p', 'y', 't', 'h')):
        textout.append(word)

textout = list(set(textout))

print("Words that start or end with one of the letters of python:", textout)