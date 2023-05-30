FROM node:12.22.9
WORKDIR /workspace/tic-tac-toe-api-app AS builder
COPY * ./
RUN npm install
EXPOSE 3000
CMD [ "node", "board-size-api.js" ]