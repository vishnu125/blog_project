from src.database import Database
import uuid
import datetime
class Post:
    def __init__(self,blog_id,title,content,author,created_date=datetime.datetime.utcnow(),id=None):
        self.blog_id=blog_id
        self.title=title
        self.content=content
        self.author=author
        self.created_date=created_date
        self.id=uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
         Database.insert(collection='posts',data=self.json())


    def json(self):
        return {'blog_id' :self.blog_id,
                'title':self.title,
                'content':self.content,
                'author':self.author,
                'id':self.id,
                'created_date':self.created_date
        }

    @classmethod
    def from_mongo(cls,id):
       post_data= Database.find_one(collection='posts',query={'id':id})
       return cls(blog_id=post_data['blog_id'],
                  title=post_data['title'],
                  content = post_data['content'],
                  author=post_data['author'],
                  created_date=post_data['created_date'])

    @staticmethod
    def from_blog(blog_id):
      return  ([ x for x in Database.find(collection='posts', query={'blog_id':blog_id})])
