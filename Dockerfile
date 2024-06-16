#Version que voy a usar para el certamen
FROM python:3.10 

# crea una carpeta que se llama app.
WORKDIR /app/

# la carpeta app va a copiar lo que haya aqui.
COPY requirements.txt .

# correré un comando que yo quiera que se ejecute cuando yo haga el build de la imagen
RUN pip install -r requirements.txt