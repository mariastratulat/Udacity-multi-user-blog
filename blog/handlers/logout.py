class Logout(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/login')