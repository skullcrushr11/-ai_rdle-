
#subset_position --> [green,yellow,grey]
hidden_word='penis'
def checker(stri):
    positional_info=dict()
    subset_postition=[True,True,True]

    l=list(hidden_word)
    k=list(stri)
    for i in range(5):
        if l[i]==k[i]:
            subset_postition[0]=True
            subset_postition[1]=False
            subset_postition[2]=False
        elif k[i] in l:
            subset_postition[0]=False
            subset_postition[1]=True
            subset_postition[2]=False
        else:
            subset_postition[0]=False
            subset_postition[1]=False
            subset_postition[2]=True
        positional_info[i]=subset_postition
        subset_postition=[True,True,True]
    return positional_info
print(checker('crane'))
