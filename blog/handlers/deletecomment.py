class DeleteComment(BlogHandler):
    def get(self, post_id, comment_id):
        comment = Comment.get_by_id(int(comment_id), parent=self.user.key())
        if comment:
            comment.delete()
            self.redirect('/blog/%s' % str(post_id))
        else:
            self.write('Something went wrong.')