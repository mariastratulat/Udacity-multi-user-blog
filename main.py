import os

import jinja2
import webapp2

import random
import hashlib
import hmac
from string import letters

from google.appengine.ext import db

# from blog.handlers import blogfront
# from blog.handlers import *
# from models import *




template_dir = os.path.join(os.path.dirname(__file__), 'blog/templates')
jinja_env = jinja2.Environment(autoescape = True,
                               loader = jinja2.FileSystemLoader(template_dir))


app = webapp2.WSGIApplication({('/?', BlogFront),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/blog/([0-9]+)/deletepost', DeletePost),
                               ('/signup', Register),
                               ('/welcome', Welcome),
                               ('/blog/([0-9]+)/edit', EditPost),
                               ('/blog/([0-9]+)/like', LikePost),
                               ('/blog/([0-9]+)/unlike', UnlikePost),
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/blog/([0-9]+)/newcomment', NewComment),
                               ('/blog/([0-9]+)/editcomment/([0-9]+)',
                                EditComment),
                               ('/blog/([0-9]+)/deletecomment/([0-9]+)',
                                DeleteComment),
                               },
                              debug=True)