from . import home


@home.route("/")
def index():
    return "index"

@home.route("/register/", methods=["GET", "POST"])
def register():
    return 'this is register'