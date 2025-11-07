# ARM Mac対応の安定構成
FROM --platform=linux/arm64 node:20-bullseye

WORKDIR /app

COPY package*.json ./

# rollup関連は旧安定版をインストール。npmのバグを回避するため。(Apple Silicon + Docker (Linux/ARM) 環境だと、間違ったプラットフォーム用のバイナリをインストールしてしまう
RUN npm install --no-optional && \
    npm install rollup@4.5.0 --save-dev && \
    npm cache clean --force

COPY . .

CMD ["npx", "vite", "--host", "0.0.0.0", "--port", "5173"]
