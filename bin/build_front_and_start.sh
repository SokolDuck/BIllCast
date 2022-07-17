#!/bin/bash

cd frontend
npm install
npm run build_prod
rm -rf node_modules
cd ..
cd backend
./bin/start.sh
