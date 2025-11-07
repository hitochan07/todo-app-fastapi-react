# 前提条件：Docker Desktopがインストールされていること

### フォルダ構成
todo-app/
├── backend/
│   ├── app/
│   │    ├──__pychache__/
│   │    │   └── main.cpython-312.pyc
│   │    └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── db/
│   └── init.sql
│
├── frontend/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   │   └── react.svg
│   │   ├── App.css
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── main.tsx
│   ├── Dockerfile
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   ├── tsconfig.app.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   └── vite.config.ts
│
├── docker-compose.yml
└── README.md

### 🚀 起動手順
1. frontendに関連するモジュールをインストールする
`$ cd frontend`
`$ npm install`

2. コンテナをbuildする
`$ docker compose build`

3. コンテナを立ち上げる
`$ docker compose up`

4. 以下にアクセスし、画面が表示されるか確認する
# frontend
http://localhost:5173
# backend
http://localhost:8000


### コンテナにログインするコマンド
`$ docker container exec -it todo-frontend bash`