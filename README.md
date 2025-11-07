# Todo App

FastAPI（backend）・React + Vite（frontend）・PostgreSQL（db）で構成された Todo 管理アプリです。

## 前提条件
- Docker Desktop 4.x 以上（Compose v2 が使えること）
- `git`, `make` など一般的な CLI ツール
- ローカルで個別に動かす場合のみ：Python 3.12 / Node.js 20 + npm 10 以上

## フォルダ構成
```
todo-app/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── test_main.py
│   ├── Dockerfile
│   └── requirements.txt
├── db/
│   └── init.sql
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── Test.tsx
│   │   ├── main.tsx
│   │   └── App.css ほかスタイル関連
│   ├── Dockerfile
│   ├── package.json / package-lock.json
│   ├── tsconfig*.json
│   └── vite.config.ts
├── docker-compose.yml
└── README.md
```

## 環境構築（Docker 利用・推奨）
1. リポジトリをクローンし、プロジェクト直下（`todo-app/`）へ移動する
2. 必要に応じてフロントの依存をホストにも入れておきたい場合は `cd frontend && npm install` を実行（ホットリロードでホストの型補完を効かせたいケース向け）
3. コンテナをビルド  
   ```
   docker compose build
   ```
4. コンテナを起動  
   ```
   docker compose up -d
   ```
5. 動作確認  
   - Frontend: http://localhost:5173  
   - Backend (FastAPI docs): http://localhost:8000/docs  
   - DB: PostgreSQL が `localhost:5433` に公開されています（初期化 SQL は `db/init.sql`）
6. 停止するときは `docker compose down`。ログ確認は `docker compose logs -f <service>` を利用してください。

### コンテナに入る
```
docker compose exec frontend bash
docker compose exec backend bash
docker compose exec db psql -U user -d tododb
```

## ローカル実行（必要な場合のみ）
### Backend
```
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```
cd frontend
npm install
npm run dev -- --host 0.0.0.0 --port 5173
```

## よく使うコマンド
- テスト（Backend）：`cd backend && pytest`（`test_main.py` を想定）
- Lint / Format（Frontend）：`cd frontend && npm run lint`

必要に応じて各サービスの Dockerfile や `docker-compose.yml` を変更し、構成を拡張してください。
