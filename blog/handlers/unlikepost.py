class UnlikePost(BlogHandler):
    def get(self, post_id):
        if not self.user:
            self.redirect('/login')
        else:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)
            author = post.author
            is_user = self.user.name

            if author == is_user and is_user in post.liked_by:
                self.redirect('/unlike')
            else:
                post.likes -= 1
                post.liked_by.remove(is_user)
                post.put()
                self.redirect('/blog')
# wait for datastore to be updated before refreshing page
        temp = db.get(key)