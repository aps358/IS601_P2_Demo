FROM python:3.8-buster
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN adduser -D myuser
RUN apk add --no-cache g++ musl-dev linux-headers
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install --user -r requirements.txt