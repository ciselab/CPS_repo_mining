# Stop and remove the previous docker container
CHECK_CONTAINERS=$(docker container ls | grep 'cps-repo-mining-container')
if [ -n "$CHECK_CONTAINERS" ]; then
  echo "Stopping and removing existing container..."
  docker stop cps-repo-mining-container > /dev/null
  docker rm cps-repo-mining-container > /dev/null
fi

# Make results dir if it is needed
if [ ! -d "results" ];then
    mkdir results
fi

# Mount projects directory for local repo analysis
EXTRA_MOUNT=""
if [ -n "$1" ]; then
    if [ -d "$1" ]; then
        # The input argument should be an absolute path 
        EXTRA_MOUNT="--mount type=bind,source=$1,target=/home/user/repo-mining/projects"
    fi
fi

# Run a new docker container.
docker run -dit --name cps-repo-mining-container \
--mount type=bind,source="$(pwd)/results",target=/home/user/repo-mining/results \
$EXTRA_MOUNT \
cps-repo-mining
