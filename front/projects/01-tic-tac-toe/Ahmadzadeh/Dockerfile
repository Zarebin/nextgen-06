#stage1: node
FROM node:12.22.9  AS builder
WORKDIR /workspace/tic-tac-toe-app
COPY * ./
RUN npm install
RUN npm run build

#stage2: nginx
FROM nginx:alpine
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /workspace/tic-tac-toe-app/dist ./
COPY --from=builder /workspace/tic-tac-toe-app/nginx.conf ./etc/nginx
EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]