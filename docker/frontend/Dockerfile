FROM node:latest

WORKDIR /app

COPY ../../weather_map/frontend/package.json ./
COPY ../../weather_map/frontend/package-lock.json ./
RUN npm install

COPY ../../weather_map/frontend/ ./
RUN npm run build

EXPOSE 3000