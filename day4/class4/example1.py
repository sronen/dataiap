dataiap_home = '../../dataiap/'

import sys
sys.path.append(dataiap_home+'resources/util/')
from email_util import *

walker = EmailWalker(dataiap_home+'datasets/emails/lay-k')
for email_dict in walker:
    print email_dict['subject']