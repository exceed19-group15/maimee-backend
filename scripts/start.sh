#!/bin/bash
echo MaiMee server
nohup uvicorn main:app --host 0.0.0.0 >.out &
