function ?= "topconf"

AWS_PROFILE ?= default
aws=aws --profile=$(AWS_PROFILE)
AWS_S3_BUCKET ?= topconf-code
AWS_DYNAMO_TABLE ?= anton-DynamoTable-11NPIBCQJ5R3J

default: init install package

init:
	virtualenv .venv

deploy: install package
	$(aws) s3 cp *.zip s3://$(AWS_S3_BUCKET)
	$(aws) s3 cp cloudformation.yaml s3://$(AWS_S3_BUCKET)
#	$(aws) lambda update-function-code --function-name="$(function)" --zip-file=fileb://lambda.zip --publish
.PHONY: deploy


install: init
	. .venv/bin/activate && pip install -r requirements.txt -t lib --upgrade | true

test:
	python test_main.py

clear:
	rm -rf lib/
	rm -rf .venv
	rm -f lambda.zip

package:
	zip -9 -r lambda.zip . -x@.zipignore

import:
	python import.py data/data.csv $(AWS_DYNAMO_TABLE)
.PHONY: import