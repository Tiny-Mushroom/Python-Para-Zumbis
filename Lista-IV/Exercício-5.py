textinput = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''
print("Original:", textinput)


textinput = textinput.lower().strip(".,:;?!").split()
print("Edited:", textinput)
textout = []


for i in textinput:
    if i.startswith("p"):
        textout = textout.append(i)
    if i.endswith("p"):
        textout = textout.append(i)
    if i.startswith("y"):
        textout = textout.append(i)
    if i.endswith("y"):
        textout = textout.append(i)
    if i.startswith("t"):
        textoutput = textoutput.append(i)
    if i.endswith("t"):
        textoutput = textoutput.append(i)
    if i.startswith("h"):
        textoutput = textoutput.append(i)
    if i.endswith("h"):
        textoutput = textoutput.append(i)
        
        

print("Output:", textout)



print("Words with h:", textoutput)
textoutput = textoutput.clear()

for i in textinput:
    if i.startswith("o"):
        textoutput = textoutput.append(i)
    if i.endswith("o"):
        textoutput = textoutput.append(i)
        
print("Words with o:", textoutput)
textoutput = textoutput.clear()

for i in textinput:
    if i.startswith("n"):
        textoutput = textoutput.append(i)
    if i.endswith("n"):
        textoutput = textoutput.append(i)
        
print("Words with n:", textoutput)
textoutput = textoutput.clear()
