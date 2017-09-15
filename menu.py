from src.database import Database
from src.blog import Blog

class Menu():

    def __init__(self):
        self.user=input('Enter author name ')
        self.user_blog=None
        if self._user_has_account():
            print ('welcome back {}'.format(self.user))
        else:
            self._prompt_user_for_account()


    def _user_has_account(self):
        blog= Database.find_one(collection='blogs',query={'author':self.user})
        if blog is not None:
            self.user_blog=Blog.from_mongo(id=blog['id'])
            return True
        else:
            return False


    def _prompt_user_for_account(self):
        title=input('Enter a blog title')
        description=input('Enter a blog description')
        blog=Blog(author=self.user,title=title,description=description)
        blog.save_to_mongo()
        self.user_blog=blog

    def run_menu(self):
        read_or_write=input('Do you want to read (R) or write (W) ')
        if read_or_write=='R':
            self._list_blogs()
            self._view_blogs()
        elif read_or_write=='W':
            self.user_blog.new_post()
        else:
            print('Thanks for logging')

    def _list_blogs(self):
        list_blog=Database.find(collection='blogs',query={})
        for b in list_blog:
         print ('id:{} ,title: {},author:{}'.format(b['id'],b['title'],b['author']))

    def _view_blogs(self):
       blog_to_see= input ('Enter the id of blog you want to see')
       blog=Blog.from_mongo(blog_to_see)
       posts=blog.get_post()
       for post in posts:
           print ('created_date:{},title:{}\n\n{}'.format(post['created_date'],post['title'],post['content']))
