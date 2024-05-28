
<h2 align="center"> Django Template</h2>

<p align="center">
  
  <a>
    <img src="https://img.shields.io/github/languages/top/brian-emarquez/django-template?color=green">
  </a>

  <a href="https://github.com/brian-emarquez/django-template/stargazers">
    <img src="https://img.shields.io/github/stars/BrianMarquez3/Learning-Microsoft-SQL-SERVER.svg?style=flat" alt="Stars">
  </a>

  <a href="https://github.com/brian-emarquez/django-template/network">
    <img src="https://img.shields.io/github/forks/brian-emarquez/django-template.svg?style=flat" alt="Forks">

  </a>
    <img src="https://img.shields.io/github/v/tag/brian-emarquez/django-template?color=green&label=Version&logo=django">
  </a>
  
  <a>
    <img src="https://img.shields.io/github/languages/code-size/brian-emarquez/django-template">
  </a>
    
  <a href="https://github.com/brian-emarquez/django-template/network">
    <img src="https://img.shields.io/badge/Plataform-Windows-green">
  </a><br>
 
  <img src="https://img.shields.io/github/last-commit/brian-emarquez/django-template?color=darkgreen&style=for-the-badge">

  <img src="https://img.shields.io/github/languages/count/brian-emarquez/django-template?style=for-the-badge">
  
</p>
  
<table align="center">
  <tr>
    <td align="center" style="padding=0;width=50%;">
      <img align="center" style="padding=0;" src="./assets/django.png" />
    </td>
  </tr>
</table>

---

_Tutorial para crear un Proyecto_

[Tutorial Crear Proyecto Django](https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-20-04-es)

- Crear un entorno virtual

```bash
mkdir django-apps
cd django-apps
```
_env_

```bash
virtualenv env
```

_Activar entorno_

```bash
. env/bin/activate
```

_Intalar Django(version)_

```bash
pip install django
django-admin --version
```

_Ajustar la configuración del firewall_

```bash
sudo ufw allow 8000
```

## Iniciar el proyecto

```bash
django-admin startproject testsite
cd testsite
ls
```

```bash
cd testsite/
```

## Crear super usuario

```bash
python manage.py createsuperuser
```

- Acceder a la app web de Django

```bash
cd ~/django-apps/testsite/
python manage.py runserver 0.0.0.0:8000
```

<table align="center">
  <tr>
    <td align="center" style="padding=0;width=50%;">
      <img align="center" style="padding=0;" src="./assets/django-3-testsite.png" />
    </td>
  </tr>
</table>


## Django Admin


```bash
http://your_server_ip:8000/admin/
```


<table align="center">
  <tr>
    <td align="center" style="padding=0;width=50%;">
      <img align="center" style="padding=0;" src="./assets/django-admin-login.png" />
    </td>
  </tr>
</table>

- Requirements

[https://pip.pypa.io/en/stable/cli/pip_freeze/]


_Desactivar_

```bash
deactivate
```

## (Ubuntu) Linux Permisos

_privilegios linux_
```bash
sudo chmod -R 777 file
```

_IP linux_
```bash
ifconfig
```

## Postgres Linux


_Coomando inicializacion_

```bash
service postgresql start
service postgresql status
service postgresql stop
```



## Django with Postgres Nginx andmGunicorn

_Tutorial_

Github Tutorial - [Django, Postgres, Nginx y Gunicorn](https://github.com/brian-emarquez/Django-with-Postgres-Nginx-and-Gunicorn)

## Python-Django

_Tutorial_

Github Python-Django - [https://github.com/brian-emarquez/Python-Django)