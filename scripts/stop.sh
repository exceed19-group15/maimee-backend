#!/bin/bash
echo Mee server
kill -9 $(ps aux | grep uvicorn | awk '{print $2}')
