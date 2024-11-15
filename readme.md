Flask App with Google Authentication
====================================

This is an example [flask](https://flask.palletsprojects.com/en/stable/) application that demonstrates implementing Google authentication using [google_auth_oauthlib](https://pypi.org/project/google-auth-oauthlib/).

This app doesn't "do" much on it's own, but it can be a useful resource to learn how Google authentication works.

Usage
-----

In order to run the application, you'll first need to generate a `client_secret.json` file from the [Google Cloud Console](https://console.cloud.google.com). Place this file alongside files from this repository and then run:

```sh
python3 install -r requirements.txt
OAUTHLIB_INSECURE_TRANSPORT=1 python3 -m flask --app=main.py run --port=80
```

If this command completes successfully, you should have a web application running at http://localhost that allows logging in via Google.
