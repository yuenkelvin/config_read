from ciscoconfparse import CiscoConfParse
from ciscoconfparse.ccp_util import IPv4Obj
import re
import glob
import sys 


#directory
CONFIG_DIR = '/root/ASW_config/*'

#regular expression
RE_HOSTNAME = re.compile(r'hostname\s(\S+)')
RE_INTF_PARENT = re.compile(r'interface\s(\S+)')
RE_INTF_CHILDSPEC = re.compile(r'^\sip\saddress')
RE_ITF_ADDR = re.compile(r'ip\saddress\s(\S+\s+\S+)')
RE_ITF_DES = re.compile(r'description\s(.*)$')
RE_ITF_SHUT = re.compile(r'^\s(shutdown)')
RE_ITF_ACL_IN = re.compile(r'ip\saccess-group\s(.*)\sin$')
RE_ITF_ACL_OUT = re.compile(r'ip\saccess-group\s(.*)\sout$')

pdirectory = glob.glob(CONFIG_DIR)

#code

#print first row
print( \
'hostname,\
interface,\
description, \
ip_addr, \
network, \
prefix_length, \
shutdown, \
acl_in, \
acl_out')

for pfile in pdirectory:

  parse = CiscoConfParse(pfile)
 
  #variable
  hostname = parse.re_match_iter_typed(RE_HOSTNAME)

  for obj in parse.find_objects_w_child(parentspec=RE_INTF_PARENT, childspec=RE_INTF_CHILDSPEC):

  #print('Config test: {} '.format(obj.text))
  
  #intf = obj.re_match_iter_typed(RE_INTF_PARENT)
    try: 
      ip_addr = obj.re_match_iter_typed(RE_ITF_ADDR,result_type=IPv4Obj)
      itf_des = obj.re_match_iter_typed(RE_ITF_DES)
      itf_acl_in = obj.re_match_iter_typed(RE_ITF_ACL_IN)
      itf_acl_out =  obj.re_match_iter_typed(RE_ITF_ACL_OUT)
      itf_shut = obj.re_match_iter_typed(RE_ITF_SHUT) 
      if itf_shut: 
        itf_shut = 'shutdown'
      else: 
        itf_shut = ''
      
    except:
      print('unable to match ip address in file:{}'.format(pfile) ) 


    print('{}, {}, {}, {}, {}, {}, {}, {}, {}'.format(\
hostname, \
obj.text[10:], \
itf_des, \
ip_addr.ip, \
ip_addr.network, \
ip_addr.prefixlen, \
itf_shut, \
itf_acl_in, \
itf_acl_out ))


