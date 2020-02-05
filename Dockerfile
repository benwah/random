FROM buildpack-deps:buster

# docker run --rm -i -t 4c7b93a3cd2e bash

RUN useradd -U -m -s /bin/bash benchy
RUN apt-get update && apt-get install -y --no-install-recommends \
                wget sudo curl software-properties-common
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN sudo apt-get -y --no-install-recommends install nodejs ruby ruby-dev python3.7 python3.7-dev python3.7-venv

USER benchy
WORKDIR /home/benchy
COPY --chown=benchy:benchy . /home/benchy

RUN python3 -m venv pyenv
RUN pyenv/bin/pip3 install wheel
RUN pyenv/bin/pip3 install -r requirements.txt

ENV PATH="/home/benchy/.gem/ruby/2.5.0/bin:${PATH}"
ENV GEM_HOME="/home/benchy/.gem/ruby/2.5.0"

RUN gem install --user-install bundler:1.17.3
RUN bundler
