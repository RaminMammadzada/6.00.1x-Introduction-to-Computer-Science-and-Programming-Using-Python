def avr(grades, weights):
    assert not len(grades)==0, 'no grades data'
    newgr=[convertLetterGrade(elt)for elt in grades]
    return dotProduct(newgr,weights)/len(newgr)
    
