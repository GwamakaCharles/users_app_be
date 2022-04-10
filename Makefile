run-dev:
	gunicorn app:app

run:
	gunicorn --config config.py app:app