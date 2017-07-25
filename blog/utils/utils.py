secret = 'idinahui'

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val):
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val):
        return val

def make_salt(length=5):
    return ''.join(random.choice(letters) for x in xrange(length))

def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)

def valid_pw(name, password, h):
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

def users_key(group='default'):
    return db.Key.from_path('users', group)

# @classmethod
# def by_id(cls, uid):
#     return cls.get_by_id(uid, parent=users_key())
#
# @classmethod
# def by_name(cls, name):
#     u = cls.all().filter('name =', name).get()
#     return u
#
# @classmethod
# def register(cls, name, pw, email=None):
#     pw_hash = make_pw_hash(name, pw)
#     return cls(parent=users_key(),
#                 name=name,
#                 pw_hash=pw_hash,
#                 email=email)
#
# @classmethod
# def login(cls, name, pw):
#     u = cls.by_name(name)
#     if u and valid_pw(name, pw, u.pw_hash):
#         return u

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

def valid_username(username):
    return username and USER_RE.match(username)


PASS_RE = re.compile(r"^.{3,20}$")

def valid_password(password):
    return password and PASS_RE.match(password)


EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def valid_email(email):
    return not email or EMAIL_RE.match(email)

def blog_key(name='default'):
    return db.Key.from_path('blogs', name)

# @property
# def comments(self):
#     return Comment.all().filter("post = ", str(self.key().id()))