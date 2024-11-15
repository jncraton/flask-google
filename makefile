all: run-dev

run-dev:
	OAUTHLIB_INSECURE_TRANSPORT=1 python3 -m flask --app=main.py run --port=80

clean:
	rm -rf __pycache__
