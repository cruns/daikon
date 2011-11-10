#
#   Copyright [2011] [Patrick Ancillotti]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import ConfigParser
import sys
import os.path

class configuration:

    def __init__(self, arguments):
        self.arguments = arguments


    def config_setup(self):
        self.config_parser = ConfigParser.ConfigParser()

        if not self.config_parser.read(['/etc/daikon/daikon.conf',
                os.path.expanduser('~/.daikon.conf'), 'daikon.conf']):
            sys.stderr.write("ERROR: No config file found!\n")
            sys.exit(1)
        elif not self.config_parser.has_section(self.cluster()):
            sys.stderr.write("ERROR: No cluster section defined for this cluster!\n")
            sys.exit(1)
        else:
            return self.config_parser


    def cluster(self):
        if hasattr(self.arguments, "cluster") and self.arguments.cluster is not None:
            cluster = self.arguments.cluster
        else:
            cluster = 'default'
        return cluster


    def host(self):
        if not self.config_parser.get(self.cluster(), 'host'):
            sys.stderr.write("ERROR: No default host defined!\n")
            sys.exit(1)
        elif hasattr(self.arguments, 'host') and self.arguments.host:
            host = self.arguments.host
        else:
            host = self.config_parser.get(self.cluster(), 'host')
        return host


    def port(self):
        if not self.config_parser.get(self.cluster(), 'port'):
            sys.stderr.write("ERROR: No default port defined!\n")
            sys.exit(1)
        elif hasattr(self.arguments, 'port') and self.arguments.port:
            port = self.arguments.port
        else:
            port = self.config_parser.get(self.cluster(), 'port')
        return port


    def replicas(self):
        if not self.config_parser.get(self.cluster(), 'replicas'):
            sys.stderr.write("ERROR: No default replicas defined!\n")
            sys.exit(1)
        elif hasattr(self.arguments, 'replicas') and self.arguments.replicas:
            replicas = self.arguments.replicas
        else:
            replicas = self.config_parser.get(self.cluster(), 'replicas')
        return replicas


    def shards(self):
        if not self.config_parser.get(self.cluster(), 'shards'):
            sys.stderr.write("ERROR: No default shards defined!\n")
            sys.exit(1)
        elif hasattr(self.arguments, 'shards') and self.arguments.shards:
            shards = self.arguments.shards
        else:
            shards = self.config_parser.get(self.cluster(), 'shards')
        return shards
