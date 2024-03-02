
demo='''
“Well, I do not mind coming to hear what cock-and-bull story you have trumped up” muttered Saurin, turning away.
'''
demo.split()
dict={}
for i in demo:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
