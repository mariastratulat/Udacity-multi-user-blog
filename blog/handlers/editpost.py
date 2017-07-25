class EditPost(BlogHandler):
    def get(self, post_id):
        if not self.user:
            self.redirect('/login')
        else:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            author = post.author
            is_user = self.user.name

            if author == is_user:
                key = db.Key.from_path('Post', int(post_id), parent=blog_key())
                post = db.get(key)
                error = ""
                self.render("editpost.html", subject=post.subject,
                            content=post.content, error=error)
            else:
                self.write("Please add a valid subject and content!")

    def post(self, post_id):
        if not self.user:
            self.redirect('/login')
        else:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            author = post.author
            is_user = self.user.name

            if post and author == is_user:
                post.subject = self.request.get('subject')
                post.content = self.request.get('content')
                post.put()
            self.redirect('/blog/%s' % str(post.key().id()))