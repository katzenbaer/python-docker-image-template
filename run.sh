docker run -d --env-file env.list --mount type=bind,source="$(pwd)"/assets,target=/app/assets python-docker-image-name
