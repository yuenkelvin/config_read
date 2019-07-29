from ciscoconfparse import CiscoConfParse
from ciscoconfparse.ccp_util import IPv4Obj
import re
import glob
import sys 


#directory
CONFIG_DIR = '/root/ASW_config/*'

#regular expression
RE_HOSTNAME = re.compile(r'hostname\s(\S+)')
RE_ADDR = re.compile(r'ip\saddress\s(\S+\s+\S+)')
RE_INTF_PARENT = re.compile(r'interface\s(\S+)')
RE_INTF_CHILDSPEC = re.compile(r'^\sip\saddress')

pdirectory = glob.glob(CONFIG_DIR)

#code

#print first row
print('hostname, interface,ip_addr,network,prefix_length')

for pfile in pdirectory:

  parse = CiscoConfParse(pfile)

  hostname = parse.re_match_iter_typed(RE_HOSTNAME)

  for obj in parse.find_objects_w_child(parentspec=RE_INTF_PARENT, childspec=RE_INTF_CHILDSPEC):

  #print('Config test: {} '.format(obj.text))
  
  #intf = obj.re_match_iter_typed(RE_INTF_PARENT)
    try: 
      ip_addr = obj.re_match_iter_typed(RE_ADDR,result_type=IPv4Obj)
    except:
      print('unable to match ip address in file:{}'.format(pfile) ) 


    print('{}, {}, {}, {}, {}'.format(hostname, obj.text[10:],ip_addr.ip, ip_addr.network, ip_addr.prefixlen ))

