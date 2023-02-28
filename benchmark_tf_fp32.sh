#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )" || exit
script_path="${PWD}"

LD_PRELOAD="${script_path}"/libjemalloc.so.2.5.1 python deepfm.py --steps 3000 --no_eval --tf --parquet_dataset false --data_location /root/data/ > "${script_path}"/deepfm.log 2>&1

python log_process.py --log "${script_path}"/deepfm.log