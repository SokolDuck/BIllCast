#!/bin/bash

cd $APP_MODULE_PATH
uvicorn $APP_MODULE:$APP_NAME --reload --host $HOST --port $PORT
