FROM node:18-alpine as builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN npm run build

FROM nginx:1.23-alpine
RUN mkdir /app
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
COPY nginx/nginx.conf /etc/nginx/nginx.conf