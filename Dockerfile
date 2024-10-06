FROM python:3.9 AS builder

WORKDIR /usr/src/app

# Crear un entorno virtual
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Instalar dependencias de Python
RUN pip install --upgrade pip
COPY . .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Test runner
FROM python:3.9 AS test_runner

# Copiar el código fuente y el entorno virtual
WORKDIR /usr/src/app
COPY --from=builder /venv /venv
COPY --from=builder /usr/src/app/tests tests
COPY --from=builder /usr/src/app /usr/src/app

ENV PATH="/venv/bin:$PATH"
ENV PYTHONPATH=/usr/src/app/src

# Instalar pytest para ejecutar las pruebas
RUN pip install pytest

# Ejecutar pytest
RUN pytest tests

# Final stage for the service
FROM python:3.9 AS service
WORKDIR /usr/src/app
COPY --from=test_runner /venv /venv
COPY --from=builder /usr/src/app /usr/src/app
ENV PATH="/venv/bin:$PATH"
ENV PYTHONPATH=/usr/src/app/src 

# Ejecutar el servidor Uvicorn
CMD ["uvicorn", "openapi_server.main:app", "--host", "0.0.0.0", "--port", "8080"]
