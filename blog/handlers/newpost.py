class NewPost(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            return self.redirect('/login')

        subject = self.request.get('subject')
        content = self.request.get('content')
        author = self.user.name

        if subject and content:
            p = Post(parent=blog_key(), subject=subject, author=author,
                     content=content, likes=0, liked_by=[])
            p.put()
            self.redirect('/blog/%s' % str(p.key().id()))
        else:
            error = "Please add a valid subject or content!"
            self.render("newpost.html", subject=subject, error=error,
                        content=content)