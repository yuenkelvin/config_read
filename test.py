from ciscoconfparse import CiscoConfParse
from ciscoconfparse.ccp_util import IPv4Obj
import re

#directory
parse = CiscoConfParse('/root/config_read/ASW_config/DR_Core_3750G.log')

#regular expression
RE_ADDR = re.compile(r'ip\saddress\s(\S+\s+\S+)')
RE_INTF_PARENT = re.compile(r'interface')
RE_INTF_CHILDSPEC = re.compile(r'^\sip\saddress')

#code
print('interface,ip_addr,network,prefix_length')
for obj in parse.find_objects_w_child(parentspec=RE_INTF_PARENT, childspec=RE_INTF_CHILDSPEC):

  #print('Config test: {} '.format(obj.text))
  
  ip_addr = obj.re_match_iter_typed(RE_ADDR,result_type=IPv4Obj)

  print('{},{},{},{}'.format(obj.text,ip_addr.ip, ip_addr.network, ip_addr.prefixlen ))

