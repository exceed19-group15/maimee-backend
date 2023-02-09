#!/bin/bash
echo MaiMee server
nohup uvicorn main:app --host >.out &
