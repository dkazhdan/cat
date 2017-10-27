: ${1?"Usage: $0 Please pass your API_KEY as an argument"}

echo "API_KEY=$1">.env

docker-compose up -d
