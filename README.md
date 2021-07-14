# dnsbin
dead-simple python dnsbin for logging dns queries

- uses redis for storage, bin lifetime defaults to 3600sec
- starts HTTP server on port 8080 and dns server on port 8053
- docker-compose binds these to 80 and 53, respectively
