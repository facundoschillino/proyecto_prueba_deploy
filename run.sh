# exit on error
set -o errexit

# Entrar al directorio del manage.py (en tu caso es la raíz, así que no hace falta cd)
# cd /opt/render/project/src   # en Render normalmente ya estás ahí

# Levantar gunicorn apuntando directo a tu wsgi
gunicorn sitio.wsgi:application --bind 0.0.0.0:$PORT

