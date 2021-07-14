from app.httpserver import app as httpserver
from app.dnsserver import resolver, logger
from dnslib.server import DNSServer

if __name__ == '__main__':
    print("Starting services...")
    dnsserver = DNSServer(resolver, port=8053, address="127.0.0.1", logger=logger, tcp=True)
    dnsserver.start_thread()
    print("dns up")
    httpserver.run(debug=False, use_reloader=False, host='127.0.0.1', port=8080)
    print("http up")
