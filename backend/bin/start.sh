#!/bin/bash

cd $APP_MODULE_PATH
uvicorn $APP_MODULE:$APP_NAME --host 0.0.0.0 --port $PORT
