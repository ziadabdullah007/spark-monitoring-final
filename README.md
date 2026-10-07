# Spark Job Monitoring with Docker

## Architecture

Spark Master + Spark Worker
        |
        | Spark metrics
        v
    Prometheus <----- cAdvisor <----- Docker containers
        |
        v
      Grafana

## Start everything

```bash
docker compose up -d --build
```

## Check containers

```bash
docker compose ps
```

## Run the Spark job

```bash
docker compose --profile job run --rm spark-submit
```

The submit container executes spark-submit against:

spark://spark-master:7077

## URLs

Spark Master:
http://localhost:8080

Spark Worker:
http://localhost:8081

cAdvisor:
http://localhost:8082

Prometheus:
http://localhost:9090

Grafana:
http://localhost:3000

Grafana login:
admin / admin

## Prometheus

Open:

http://localhost:9090/targets

cAdvisor should be UP.

Spark Master and Spark Worker should also be checked.

## Grafana

The Prometheus datasource is provisioned automatically.

Dashboard:
Spark Job Monitoring Dashboard

Panels:
1. Running Jobs
2. Completed Jobs
3. Failed Jobs
4. CPU Usage
5. Executors
6. Memory Usage

## Stop

```bash
docker compose down
```
