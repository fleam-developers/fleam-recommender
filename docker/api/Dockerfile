FROM python:3.10.4-bullseye as builder


ENV DOCKERIZE_VERSION v0.6.1

# Update the system
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    build-essential \
    curl \
    # Install dockerize to simplify the running application
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    # Install poetry for the project
    && curl -sSL https://install.python-poetry.org | python3 - \
    # Clean the apt cache
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*


WORKDIR /app

    
