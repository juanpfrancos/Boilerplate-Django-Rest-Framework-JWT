
1. Ejecutar las migraciones y crear un superusuario:

```bash
python manage.py migrate
python manage.py createsuperuser
```

2. Ejecutar el servidor:

```bash
python manage.py runserver
```

Ahora puedes acceder a la documentación de los endpoints en `http://localhost:8000/api/schema/` y probar los endpoints de registro, inicio de sesión y fecha actual.

Para hacer las peticiones a los respectivos endpoints, puedes utilizar herramientas como `curl` o `Postman`. Aquí tienes un ejemplo de cómo hacer una petición de registro con `curl`:

```bash
curl -X POST http://localhost:8000/api/users/ -H "Content-Type: application/json" -d '{"username": "testuser", "email": "test@example.com", "password": "testpassword"}'
```

Para hacer una petición de inicio de sesión, puedes hacer lo siguiente:

```bash
curl -X POST http://localhost:8000/api/login/ -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}'
```

Y para hacer una petición al endpoint protegido que requiere el token, puedes hacer lo siguiente:

```bash
curl -X GET http://localhost:8000/api/current_datetime/ -H "Authorization: Bearer <token>"
```

Recuerda reemplazar `<token>` con el token de acceso que obtuviste al iniciar sesión.
