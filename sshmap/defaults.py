#Copyright (c) 2012 Yahoo! Inc. All rights reserved.
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. See accompanying LICENSE file.
"""
Default Values for sshmap
"""
__author__ = 'dhubbard'
import os

# Defaults
JOB_MAX = 100
# noinspection PyBroadException
try:
    for line in open('/proc/%d/limits' % os.getpid(), 'r').readlines():
        if line.startswith('Max processes'):
            JOB_MAX = int(line.strip().split()[2]) / 4
except:
    pass

# Return code values
RUN_OK = 0
RUN_FAIL_AUTH = 1
RUN_FAIL_TIMEOUT = 2
RUN_FAIL_CONNECT = 3
RUN_FAIL_SSH = 4
RUN_SUDO_PROMPT = 5
RUN_FAIL_UNKNOWN = 6
RUN_FAIL_NOPASSWORD = 7
RUN_FAIL_BADPASSWORD = 8

# Text return codes
RUN_CODES = ['Ok', 'Authentication Error', 'Timeout', 'SSH Connection Failed',
             'SSH Failure',
             'Sudo did not send a password prompt', 'Connection refused',
             'Sudo password required',
             'Invalid sudo password']

# Configuration file field descriptions
conf_desc = {
    "username": "IRC Server username",
    "password": "IRC Server password",
    "channel": "sshmap",
}

# Configuration file defaults
conf_defaults = {
    "address": "chat.freenode.net",
    "port": "6667",
    "use_ssl": False,
}