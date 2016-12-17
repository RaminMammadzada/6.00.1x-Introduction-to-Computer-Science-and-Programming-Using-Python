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
    
