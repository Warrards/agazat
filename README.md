# Hálózat
telnet 193.41.10.1
conf t
ISP(config)#ip dhcp ex 193.41.20.1 193.41.20.20
ISP(config)#
ISP(config)#ip dhcp pool User_Voip
ISP(dhcp-config)#net 193.41.20.0 255.255.255.0
ISP(dhcp-config)#def 193.41.20.1
ISP(dhcp-config)#dns 70.70.70.10
ISP(dhcp-config)#domain isp.hu
ISP(dhcp-config)#option 150 ip 70.70.80.20
ISP(dhcp-config)#exit
ISP(config)#exit
telnet 70.70.80.20
VTYtitok
ena
enaTitok
conf t
CMS(config)#banner motd "Illetektelneknek a belepes tilos!"
CMS(config)#ip route 0.0.0.0 0.0.0.0 70.70.80.1

CMS(config)#user admin pri 15 sec admin
CMS(config)#ip domain-n isp.hu
CMS(config)#crypto key gene rsa 
1024 bit

CMS(config)#line vty 0 4
CMS(config-line)#login local
CMS(config-line)#transport input ssh
CMS(config-line)#exit
CMS(config)#do wr