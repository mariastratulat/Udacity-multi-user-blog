class DeletePost(BlogHandler):
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
                post.delete()
                self.render("deletepost.html")
            else:
                self.redirect("/")
