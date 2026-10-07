FROM apache/spark:3.5.7-python3

USER root

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY conf/metrics.properties /opt/spark/conf/metrics.properties

RUN mkdir -p /opt/spark/jobs \
    && chown -R spark:spark /opt/spark/jobs /opt/spark/conf/metrics.properties

WORKDIR /opt/spark/jobs

USER spark
