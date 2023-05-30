FROM node:12.22.9  AS builder
WORKDIR workspace/tic-tac-toe
COPY package*.json ./
COPY webpack.config.js ./ 
RUN npm install
COPY src ./src
RUN npm run build

# stage-2
FROM nginx:alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /workspace/tic-tac-toe/src/index.html ./

COPY --from=builder /workspace/tic-tac-toe/dist ./dist
COPY --from=builder /workspace/tic-tac-toe/src/nginx.conf ./etc/nginx
EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]