class Login(BlogHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('welcome')
        else:
            if not username:
                msg = 'Add the user name'
            elif not password:
                msg = 'Add password'
            else:
                msg = 'Invalid login'
            self.render('login.html', error = msg)