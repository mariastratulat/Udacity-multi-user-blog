
class Comment(db.Model):
    comment = db.StringProperty(required=True)
    post = db.StringProperty(required=True)
    author = db.StringProperty(required=True)