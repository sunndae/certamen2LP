FROM node:18

WORKDIR /app

COPY ./react/package*.json ./

RUN npm install 

COPY . .

# Comando para ejecutar la aplicación
CMD ["npm", "start"]


