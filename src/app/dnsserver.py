import os
from typing import Optional
from dnslib.server import DNSLogger
from dnslib.dns import DNSRecord, DNSQuestion
from dnslib.label import DNSLabel
from .redis import redis

HOSTNAME = DNSLabel(os.getenvb())

class BinResolver(object):

    def extract_bin_name(self, request: DNSRecord) -> Optional[bytes]:
        if len(request.questions) == 1:
            # we only support single-question queries, like most dns servers
            question: DNSQuestion = request.questions[0]
            label = question.get_qname()
            # make sure the question is of form $bin.$hostname
            if label.matchSuffix(HOSTNAME):
                bin_label = label.stripSuffix(HOSTNAME)
                if len(bin_label.label) >= 1:
                    # in case of $x.$bin.$hostname, extract $bin
                    return bin_label.label[-1]
        return None
    
    # override
    def resolve(self, request: DNSRecord, handler):
        bin_name = self.extract_bin_name(request)
        if bin_name:
            # add to list, if list exists
            redis.lpushx(f"bins.{bin_name}", str(request))

        reply = request.reply()
        #reply.add_answer(*RR.fromZone("abc.def. 60 A 1.2.3.4"))
        return reply
        
resolver = BinResolver()
logger = DNSLogger(prefix=False)
