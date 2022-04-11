# The gunicorn server will look for the file app.py and run it.
run-dev:
	gunicorn app:app

run:
	gunicorn --config config.py app:app