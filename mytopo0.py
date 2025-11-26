"""
Custom Topology:
+--------+       +--------+
| client |-------| server |
+--------+       +--------+
"""

from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        # Add hosts without pre-assigned IPs
        client = self.addHost('client', ip=None)
        server = self.addHost('server', ip=None)

        # Add a link between them
        self.addLink(client, server)


# Register the topology so Mininet can recognize it
topos = {'mytopo': (lambda: MyTopo())}