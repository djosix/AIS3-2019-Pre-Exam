FROM node:10-alpine
ADD server /www
WORKDIR /www
RUN cd /www && npm install
CMD [ "npm", "start" ]
