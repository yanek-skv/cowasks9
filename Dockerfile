FROM python
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y cowsay nano
RUN echo PATH=$PATH:/usr/games >> ~/.bashrc
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]
