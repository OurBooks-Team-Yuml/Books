#!/bin/bash
set -x
awslocal s3 mb s3://books
awslocal s3 mb s3://authors
