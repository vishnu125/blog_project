import uuid
import datetime
from src.posts import Post
from src.database import Database
class Blog(object):
    def __init__(self,author,description,title,id=None):
      self.author=author
      self.description=description
      self.title=title
      self.id=uuid.uuid4().hex if id is None else id

    def new_post(self):
        title=input('Enter post title ')
        content=input('Enter new post ')
        date =input('Enter post date or leave blank for today:(ddmmyyyy)')
        if date=='':
            date=datetime.datetime.utcnow()
        else:
            date=datetime.datetime.strptime(date,'%d%m%Y')
        post= Post(blog_id=self.id,title=title,author=self.author,content=content,
                   created_date=date)
        post.save_to_mongo()


    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',data=self.json())

    def json(self):
        return { 'author':self.author,
                 'title':self.title,
                 'description':self.description,
                 'id':self.id}

    @classmethod
    def from_mongo(cls,id):
        blog_data= Database.find_one(collection='blogs', query={'id': id})
        return cls(author=blog_data['author'],
                   description=blog_data['description'],
                   title=blog_data['title'],
                   id=blog_data['id'])