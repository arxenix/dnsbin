import os
import json
from uuid import uuid4
from flask import Flask, jsonify
from .redis import redis
# this is the http server for the dnsbin service, e.g. dns.hc.lc
app = Flask(__name__)

BIN_TTL = int(os.getenvb("BIN_TTL")) # bin ttl seconds

@app.route('/api/<bin>/queries')
def get_queries(bin):
    bin_key = f"bins.{bin}"
    # get all list elements except first (which is "init")
    queries = redis.lrange(bin_key, 1, -1)
    queries = [json.loads(q) for q in queries]
    return jsonify({'queries': queries})

@app.route('/api/create')
def create_bin():
    bin_key = f"bins.{uuid4()}"
    p = redis.pipeline()
    p.lpush(bin_key, "init")
    p.expire(bin_key, BIN_TTL)
    p.execute()
    return jsonify({'bin': bin_key})