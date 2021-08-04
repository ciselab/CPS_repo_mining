# Remove previous docker image 
docker rmi $(docker images | grep 'cps-repo-mining')

# Build the new image from Dockerfile.CPS-repo-mining
docker image build -t cps-repo-mining \
--build-arg USER_ID=$(id -u) \
--build-arg GROUP_ID=$(id -g) \
$(pwd) -f Dockerfile.CPS-repo-mining
