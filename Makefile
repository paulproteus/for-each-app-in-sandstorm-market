all: index.json

index.json:
	wget https://app-index.sandstorm.io/apps/index.json
