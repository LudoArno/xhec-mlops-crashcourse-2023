prefect_setup:
	poetry run prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
	poetry run prefect server start --host 127.0.0.1

prefect_reset:
	poetry run prefect server database reset