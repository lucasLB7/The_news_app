class Article:
    def __init__(self,author,title,description,url,url_image):
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.url_image=url_image




class Source:
    def __init__(self,id,source_name,source_desc,source_url):
        self.id=id
        self.description=source_desc
        self.name = source_name
        self.source_url=source_url
