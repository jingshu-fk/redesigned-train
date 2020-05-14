#!/bin/sh

export LANG="zh_CN.UTF-8"
ps -ef | grep fileprocess | grep -v grep | awk '{print $2}' | xargs kill

sleep 10

nohup java -jar fileprocess-0.0.1-SNAPSHOT.jar > /dev/null &