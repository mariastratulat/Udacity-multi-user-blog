class EditComment(BlogHandler):
    def get(self, post_id, comment_id):
        post = Post.get_by_id(int(post_id), parent=blog_key())
        comment = Comment.get_by_id(int(comment_id), parent=self.user.key())
        if comment:
            self.render("editcomment.html", content=post.content,
                        subject=post.subject, comment=comment.comment)
        else:
            self.write('Something went wrong.')

    def post(self, post_id, comment_id):
        if not self.user:
            return self.redirect('/login')

        comment = Comment.get_by_id(int(comment_id), parent=self.user.key())

        if comment and comment.parent().key().id() == self.user.key().id():
            comment.comment = self.request.get('comment')
            comment.put()
        self.redirect('/blog/%s' % str(post_id))