#!bin/bash
source setenv.sh
psql "host=b04fa70e-33f5-4118-b5b0-033a7529e5cc.bkvfv1ld0bj2bdbncbeg.databases.appdomain.cloud port=30099 dbname=ibmclouddb user=$USERNAME sslmode=verify-full"
