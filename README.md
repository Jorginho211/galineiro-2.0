# Galineiro-2.0

## Requisitos
Paquetes que deben estar instalados dentro do sistema:

* python3
* python3-venv
* python3-pip
* fswebcam

## Creación do entorno e instalación de dependencias

* Crear un entorno virtual de python
```shell
$ python3 -m venv {projectPath}/env/
```

* Inicializacion do entorno virtual de python
```
$ source {projectPath}/env/bin/activate
```

* Instalar as dependencias
```shell
$ pip3 install -r requirements.txt
```

## Configuración das variables de entorno

* Crear unha copia do archivo de exemplo
```shell
$ cp .env.example .env
```

* Editar as variables de entorno segundo interese

## Inicialización do proxecto (Opción 1)

```shell
$ python3 run.py
```

## Inicializacion do proxecto con Gunicorn e Nginx (Opción 2)

### Requisitos:
* nginx
* make

### Inicialización do proxecto co servidor de contido Gunicorn
Inicializar proxecto con Gunicorn, indicando a ip desde a que se vai a servir o contido (0.0.0.0, permite desde calquera)

```shell
$ gunicorn -b {{HOST_IP}}:5000 -w 1 -p gunicorn.pid wsgi:app

ej: gunicorn -b 127.0.0.1:5000 -w 1 -p gunicorn.pid wsgi:app
```

### Configuración de nginx
Modificación do arquivo nginx/galineiro.conf para engadir o certificado, nome do server e o porto

```
    listen       443 ssl;
    server_name  localhost;

    ssl_certificate /etc/nginx/certs/server.crt;
    ssl_certificate_key /etc/nginx/certs/server.key;
```

Copiar o arquivo nginx/galineiro.conf a sites-available
```shell
# cp nginx/galineiro.conf /etc/nginx/sites-available/
```

Facer un enlace simbolico en sites-enabled
```shell
# ln -s /etc/nginx/sites-available/galineiro.conf /etc/nginx/sites-enabled/
```

Inicializar o servidor nginx
```shell
# nginx
```

Copiar o script de arranque init a /etc/init.d/ e cambiar permisos
```shell
# cp scripts/galineiro20 /etc/init.d/
# chmod 775 /etc/init.d/galineiro20
```

Iniciar galineiro
```shell
# /etc/init.d/galineiro20 start
```

Poñer o script de inicio por defecto no arranque
```shell
# update-rc.d galineiro20 defaults
```

## Vagrant (Opción 3)
### Requisitos
* Virtualbox
* Vagrant

### Configuración
Configurar o arquivo nginx/galineiro.conf (ver opción 2)

Executar o seguinte comando para inicializar a VM con vagrant
```shell
$ vagrant up
```

Entrar na VM por ssh co seguinte comando
```shell
$ vagrant ssh
```

Inicializar o proxecto
```shell
$ cd /vagrant/
$ make start
```