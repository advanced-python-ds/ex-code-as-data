.PHONY: download-data

download-data: day3_tiktok/followers.csv day3_tiktok/likes.csv day3_tiktok/sentiments.csv

day3_tiktok/followers.csv:
	aws s3 cp s3://code-as-data/followers.csv day3_tiktok/ --request-payer=requester

day3_tiktok/likes.csv:
	aws s3 cp s3://code-as-data/likes.csv day3_tiktok/ --request-payer=requester

day3_tiktok/sentiments.csv:
	aws s3 cp s3://code-as-data/sentiments.csv day3_tiktok/ --request-payer=requester
