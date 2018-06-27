
poo:
	pip-compile --upgrade --output-file ./requirements.txt ./requirements.in

shit:
	pip install -r ./requirements.txt

dumpster:
	docker build -t crapper:local . && docker run -it --rm -p 8080:80 crapper:local


