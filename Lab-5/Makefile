STATES := app tests
REPO := legarda/lab4

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@docker run --rm -it --name tests --net=appnet $(REPO):tests

docker-push:
	@docker push $(REPO):app
	@docker push $(REPO):tests

docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force

docker-delete:
	@docker rmi --force $$(docker images -q)
