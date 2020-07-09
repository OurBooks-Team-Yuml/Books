#!/bin/bash
set -x
awslocal s3 mb s3://books
awslocal s3 mb s3://authors
awslocal s3api put-bucket-acl --bucket books --acl public-read
awslocal s3api put-bucket-acl --bucket authors --acl public-read
