class NewComment(BlogHandler):
    def get(self, post_id):
        if not self.user:
            self.redirect("/login")
        else:
            post = Post.get_by_id(int(post_id), parent=blog_key())
            subject = post.subject
            content = post.content
            self.render("newcomment.html", subject=subject, pkey=post.key(),
                        content=content)

    def post(self, post_id):
        if not self.user:
            return self.redirect('/login')

        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        comment = self.request.get('comment')

        if comment:
            author = self.request.get('author')
            c = Comment(comment=comment, post=post_id, author=author,
                        parent=self.user.key())
            c.put()
            self.redirect('/blog/%s' % str(post_id))
        else:
            error = "Please add a comment!"
            self.render("permalink.html", post=post, content=content, error=error)
