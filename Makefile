# Exportar variables de entorno do archivo .env
ifneq (,$(wildcard .env))
	include .env
else
	include .env.example
endif
export

install:
	python3 -m venv venv/
	. venv/bin/activate; pip3 install -r requirements.txt

start_dev: venv/
	. venv/bin/activate; python3 run.py

start: venv/
	. venv/bin/activate; gunicorn -b 127.0.0.1:$(GALINEIRO_GUNICORN_PORT) --log-file gunicorn.log -w 1 -p gunicorn.pid wsgi:app

stop: venv/
	kill `cat gunicorn.pid` &> /dev/null

clean: stop
	rm -r venv/ *.pid &> /dev/null