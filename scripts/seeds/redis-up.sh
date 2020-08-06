#!/bin/bash

cd
cd redis-5.0.8/src/
./redis-server --port 6379 --slaveof 127.0.0.1 6376

