# Stop and remove the previous docker container
CHECK_CONTAINERS=$(docker container ls | grep 'cps-repo-mining-container')
if [ -n "$CHECK_CONTAINERS" ]; then
  echo "Stopping and removing existing container..."
  docker stop cps-repo-mining-container > /dev/null
  docker rm cps-repo-mining-container > /dev/null
fi

# Remove previous docker image
CHECK_IMAGES=$(docker images | grep 'cps-repo-mining')
if [ -n "$CHECK_IMAGES" ]; then
  docker rmi 'cps-repo-mining'
fi

# Build the new image from Dockerfile.CPS-repo-mining
docker image build -t cps-repo-mining \
$(pwd) -f Dockerfile.CPS-repo-mining
