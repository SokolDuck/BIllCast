FROM node:16-alpine3.15

WORKDIR /app

COPY package*.json /app/

RUN apk add --no-cache --virtual .gyp \
        python3 \
        make \
        g++ \
    && npm install \
    && apk del .gyp

COPY ./ /app/

ENV VUE_APP_ENV=development

EXPOSE 8081

CMD ["npm", "run", "serve"]
