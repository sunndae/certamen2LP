FROM node:18

WORKDIR /app

COPY ./certamen2_react/package*.json ./certamen2_react/package-lock.json* ./

RUN npm install 

COPY . .

CMD ["npm", "start"]


