#!/bin/bash

uvicorn $APP_MODULE:$APP_NAME --reload --host 0.0.0.0 --port 8080
