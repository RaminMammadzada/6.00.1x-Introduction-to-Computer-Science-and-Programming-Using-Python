'''
def isWordIn(word,text):
    import string
    text=text.split(' ')
    row=0
    for each_word in text:
            for punct in list(string.punctuation):
                each_word=each_word.replace(punct, ' ')
            text[row]=each_word
            row+=1
    print text
    print word
isWordIn('soft','"Soft!" he exclaimed as he threw the football.')
'''

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.Guid=guid
        self.Title=title
        self.Subject=subject
        self.Summary=summary
        self.Link=link
        
    def getGuid(self):
        return self.Guid
    
    def getTitle(self):
        return self.Title
    
    def getSubject(self):
        return self.Subject
    
    def getSummary(self):
        return self.Summary
    
    def getLink(self):
        return self.Link
    def __str__(self):
        print self.Summary