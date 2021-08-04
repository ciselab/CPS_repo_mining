# Stop and remove the previous docker container
docker stop cps-repo-mining-container
docker rm cps-repo-mining-container

# Make results dir if it is needed
if [ ! -d "results" ];then
    mkdir results
fi

# Mount projects directory for local repo analysis
extra_mount=""
if [ -n $1 ]; then
    if [ -d "$1" ]; then
        # The input argument should be an absolute path 
        extra_mount="--mount type=bind,source=$1,target=/home/user/repo-mining/projects"
    fi
fi

# Run a new docker container.
docker run -dit --name cps-repo-mining-container \
--mount type=bind,source="$(pwd)/results",target=/home/user/repo-mining/results \
$(echo $extra_mount) \
cps-repo-mining
