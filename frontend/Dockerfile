FROM node:18

WORKDIR /app

ADD package.json ./
ADD package-lock.json ./
RUN npm install --frozen-lockfile

ADD . .
RUN npm run build
CMD ["node", ".output/server/index.mjs"]
