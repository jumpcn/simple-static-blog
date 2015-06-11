import markdown2

class Post:
    
    def __init__(self, s):
        self.origin = s
        self.strMD = markdown2.markdown(self.origin, extras=["fenced-code-blocks"])

    def get_markdown(self):
        return self.strMD


