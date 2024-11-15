"""Example flask web app with Google authentication"""

from flask import Flask, session, abort, redirect, request
from google_auth_oauthlib.flow import Flow

app = Flask("app")
# Be sure to use your own pseudorandom secret
app.secret_key = "NtkWyoBfY8wCjqh7"

# Initialze oauthlib Flow
# https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html
flow = Flow.from_client_secrets_file(
    client_secrets_file="client_secret.json",
    scopes=["https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost/callback",
)


@app.route("/login")
def login():
    """Redirect to authorization URL

    We store a key for this URL in the user session to verify after the flow completes
    """

    authorization_url, _ = flow.authorization_url()
    return redirect(authorization_url)


@app.route("/callback")
def callback():
    """OAuth callback to complete login"""

    flow.fetch_token(authorization_response=request.url)
    auth_session = flow.authorized_session()
    userinfo = auth_session.get("https://www.googleapis.com/userinfo/v2/me").json()
    session["email"] = userinfo["email"]
    return redirect("/")


@app.route("/logout")
def logout():
    """Clears user session"""

    session.clear()
    return redirect("/")


@app.route("/")
def index():
    """Root page allowing login/logout

    Displays user email if logged in
    """

    if "email" in session:
        return f"Logged in as {session['email']}<a href='/logout'><button>Logout</button></a>"

    return "Hello World <a href='/login'><button>Login</button></a>"


def require_login(function):
    """Decorator to abort if we are not logged in"""

    def wrapper():
        if "email" not in session:
            return abort(401)
        return function()

    return wrapper


@app.route("/private")
@require_login
def private():
    """A private route requiring login using decorator"""

    return "Private endpoint requiring login"
