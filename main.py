
import time

import webapp2
from google.appengine.ext import ndb


class Book(ndb.Model):
    name = ndb.StringProperty()


class CreateHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name', 'gae_{}'.format(time.time()))
        book_key = Book(name=name).put()
        self.response.write(book_key)


class ListHandler(webapp2.RequestHandler):
    def get(self):
        books = Book.query().fetch()
        out = ''
        for b in books:
            out += '<p>{}</p>'.format(b)
        self.response.write(out)


app = webapp2.WSGIApplication([
    ('/', ListHandler),
    ('/create', CreateHandler),

], debug=True)
