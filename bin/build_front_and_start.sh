#!/bin/bash

cd frontend
npm install
npm run build_prod
rm -rf node_modules
cd ..
cd cd backend
uvicorn $APP_MODULE:$APP_NAME --host=0.0.0.0 --port=${PORT:-5000}
