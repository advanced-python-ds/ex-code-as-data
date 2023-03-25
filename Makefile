.PHONY: exercise1

exercise1: exercise1/followers.csv exercise1/likes.csv exercise1/sentiments.csv

exercise1/followers.csv:
	aws s3 cp s3://code-as-data/followers.csv exercise1/ --request-payer=requester

exercise1/likes.csv:
	aws s3 cp s3://code-as-data/likes.csv exercise1/ --request-payer=requester

exercise1/sentiments.csv:
	aws s3 cp s3://code-as-data/sentiments.csv exercise1/ --request-payer=requester
