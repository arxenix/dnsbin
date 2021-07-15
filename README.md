# dnsbin
dead-simple python dnsbin for logging dns queries

- uses redis for storage, bin lifetime defaults to 3600sec
- starts HTTP server on port 8080 and dns server on port 8053
- docker-compose binds these to 80 and 53, respectively


API:
- GET /api/create
  - creates a new bin and returns the bin ID
  - all dns queries to <id>.$HOSTNAME get logged to the bin
  - e.g. `13e04e7f-b896-4541-aab2-faaa9e919fd8.dns.hc.lc`
- GET /api/:id/queries
  - returns all dns queries that the bin has received

TODO:
- host on dns.hc.lc
- add deployment instructions
