# Build and run scheduling-policies development enviroment.
#
# By: Lucas de Sousa Rosa <roses.lucas404@gmail.com>
# Created: 2022/09/04 20:21 by @fredgrub

WORKING_DIR = $$(pwd)
CONTAINER_NAME = sched
DEV_IMAGE_NAME = sched-policies

simgrid:
	docker build -f Dockerfile.simgrid -t simgrid-v3_13 .

dev: simgrid
	docker build -f Dockerfile -t ${DEV_IMAGE_NAME} .

build_docker: dev

run:
	docker run -d -it --name ${CONTAINER_NAME} -p 8888:8888 --mount type=bind,source=${WORKING_DIR},target=/home/simgrid/dev ${DEV_IMAGE_NAME}

end:
	docker stop ${CONTAINER_NAME}
	docker rm ${CONTAINER_NAME}