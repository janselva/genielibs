import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.interface.get import get_running_config_section_dict


class TestGetRunningConfigSectionDict(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          R1_xe:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: iosxe
            type: CSR1000v
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['R1_xe']
        self.device.connect()

    def test_get_running_config_section_dict(self):
        result = get_running_config_section_dict(self.device)
        expected_output = {'Building configuration...': {},
 'Current configuration : 12259 bytes': {},
 'boot-end-marker': {},
 'boot-start-marker': {},
 'cdp run': {},
 'control-plane': {},
 'crypto pki certificate chain TP-self-signed-2655316104': {'certificate self-signed 01': {'quit': {}}},
 'crypto pki trustpoint TP-self-signed-2655316104': {'enrollment selfsigned': {},
                                                     'revocation-check none': {},
                                                     'rsakeypair TP-self-signed-2655316104': {},
                                                     'subject-name cn=IOS-Self-Signed-Certificate-2655316104': {}},
 'diagnostic bootup level minimal': {},
 'enable secret 5 $1$ufBe$ebDG13UD9/PqK.NsPBqOo.': {},
 'end': {},
 'hostname R1_xe': {},
 'interface GigabitEthernet1': {'ip address 172.16.1.211 255.255.255.0': {},
                                'negotiation auto': {},
                                'no mop enabled': {},
                                'no mop sysid': {},
                                'vrf forwarding Mgmt-intf': {}},
 'interface GigabitEthernet2': {'cdp enable': {},
                                'negotiation auto': {},
                                'no ip address': {},
                                'no mop enabled': {},
                                'no mop sysid': {}},
 'interface GigabitEthernet2.110': {'encapsulation dot1Q 110': {},
                                    'ip address 10.12.110.1 255.255.255.0': {},
                                    'ip ospf 1 area 0': {},
                                    'ip pim sparse-mode': {},
                                    'ipv6 address 2001:10:12:110::1/64': {},
                                    'ipv6 ospf 1 area 0': {},
                                    'mpls ip': {}},
 'interface GigabitEthernet2.115': {'encapsulation dot1Q 115': {},
                                    'ip address 10.12.115.1 255.255.255.0': {},
                                    'ip igmp join-group 239.1.1.1': {},
                                    'ip igmp join-group 239.1.1.2': {},
                                    'ip igmp static-group 239.1.1.3': {},
                                    'ip igmp static-group 239.1.1.4': {},
                                    'ip router isis test': {},
                                    'ipv6 address 2001:10:12:115::1/64': {},
                                    'ipv6 mld join-group FF1E:ABCD:DEF1:1111::1': {},
                                    'ipv6 mld join-group FF1E:ABCD:DEF1:1111::2': {},
                                    'ipv6 mld static-group FF1E:ABCD:DEF1:1111::3': {},
                                    'ipv6 mld static-group FF1E:ABCD:DEF1:1111::4': {},
                                    'ipv6 router isis test': {}},
 'interface GigabitEthernet2.120': {'encapsulation dot1Q 120': {},
                                    'ip address 10.12.120.1 255.255.255.0': {},
                                    'ipv6 address 2001:10:12:120::1/64': {},
                                    'ipv6 rip ripng enable': {}},
 'interface GigabitEthernet2.390': {'encapsulation dot1Q 390': {},
                                    'ip address 10.12.90.1 255.255.255.0': {},
                                    'ipv6 address 2001:10:12:90::1/64': {},
                                    'vrf forwarding VRF1': {}},
 'interface GigabitEthernet2.410': {'encapsulation dot1Q 410': {},
                                    'ip address 10.12.110.1 255.255.255.0': {},
                                    'ip ospf 2 area 0': {},
                                    'ip pim sparse-mode': {},
                                    'ipv6 address 2001:10:12:110::1/64': {},
                                    'ipv6 enable': {},
                                    'mpls ip': {},
                                    'vrf forwarding VRF1': {}},
 'interface GigabitEthernet2.415': {'encapsulation dot1Q 415': {},
                                    'ip address 10.12.115.1 255.255.255.0': {},
                                    'ip igmp join-group 239.1.1.1': {},
                                    'ip igmp join-group 239.1.1.2': {},
                                    'ip igmp static-group 239.1.1.3': {},
                                    'ip igmp static-group 239.1.1.4': {},
                                    'ip router isis test1': {},
                                    'ipv6 address 2001:10:12:115::1/64': {},
                                    'ipv6 mld join-group FF1E:ABCD:DEF1:1111::1': {},
                                    'ipv6 mld join-group FF1E:ABCD:DEF1:1111::2': {},
                                    'ipv6 mld static-group FF1E:ABCD:DEF1:1111::3': {},
                                    'ipv6 mld static-group FF1E:ABCD:DEF1:1111::4': {},
                                    'ipv6 router isis test1': {},
                                    'vrf forwarding VRF1': {}},
 'interface GigabitEthernet2.420': {'encapsulation dot1Q 420': {},
                                    'ip address 10.12.120.1 255.255.255.0': {},
                                    'ipv6 address 2001:10:12:120::1/64': {},
                                    'ipv6 rip ripng enable': {},
                                    'vrf forwarding VRF1': {}},
 'interface GigabitEthernet2.90': {'encapsulation dot1Q 90': {},
                                   'ip address 10.12.90.1 255.255.255.0': {},
                                   'ipv6 address 2001:10:12:90::1/64': {}},
 'interface GigabitEthernet3': {'cdp enable': {},
                                'negotiation auto': {},
                                'no ip address': {},
                                'no mop enabled': {},
                                'no mop sysid': {}},
 'interface GigabitEthernet3.110': {'encapsulation dot1Q 110': {},
                                    'ip address 10.13.110.1 255.255.255.0': {},
                                    'ip ospf 1 area 0': {},
                                    'ip pim sparse-mode': {},
                                    'ipv6 address 2001:10:13:110::1/64': {},
                                    'ipv6 ospf 1 area 0': {},
                                    'mpls ip': {}},
 'interface GigabitEthernet3.115': {'encapsulation dot1Q 115': {},
                                    'ip address 10.13.115.1 255.255.255.0': {},
                                    'ip router isis test': {},
                                    'ipv6 address 2001:10:13:115::1/64': {},
                                    'ipv6 router isis test': {}},
 'interface GigabitEthernet3.120': {'encapsulation dot1Q 120': {},
                                    'ip address 10.13.120.1 255.255.255.0': {},
                                    'ipv6 address 2001:10:13:120::1/64': {},
                                    'ipv6 rip ripng enable': {}},
 'interface GigabitEthernet3.390': {'encapsulation dot1Q 390': {},
                                    'ip address 10.13.90.1 255.255.255.0': {},
                                    'ipv6 address 2001:10:13:90::1/64': {},
                                    'vrf forwarding VRF1': {}},
 'interface GigabitEthernet3.410': {'encapsulation dot1Q 410': {},
                                    'ip address 10.13.110.1 255.255.255.0': {},
                                    'ip ospf 2 area 0': {},
                                    'ip pim sparse-mode': {},
                                    'ipv6 address 2001:10:13:110::1/64': {},
                                    'mpls ip': {},
                                    'vrf forwarding VRF1': {}},
 'interface GigabitEthernet3.415': {'encapsulation dot1Q 415': {},
                                    'ip address 10.13.115.1 255.255.255.0': {},
                                    'ip router isis test1': {},
                                    'ipv6 address 2001:10:13:115::1/64': {},
                                    'ipv6 router isis test1': {},
                                    'vrf forwarding VRF1': {}},
 'interface GigabitEthernet3.420': {'encapsulation dot1Q 420': {},
                                    'ip address 10.13.120.1 255.255.255.0': {},
                                    'ipv6 address 2001:10:13:120::1/64': {},
                                    'ipv6 rip ripng enable': {},
                                    'vrf forwarding VRF1': {}},
 'interface GigabitEthernet3.90': {'encapsulation dot1Q 90': {},
                                   'ip address 10.13.90.1 255.255.255.0': {},
                                   'ipv6 address 2001:10:13:90::1/64': {}},
 'interface GigabitEthernet4': {'cdp enable': {},
                                'channel-group 12 mode active': {},
                                'negotiation auto': {},
                                'no ip address': {},
                                'no mop enabled': {},
                                'no mop sysid': {}},
 'interface GigabitEthernet5': {'cdp enable': {},
                                'channel-group 12 mode active': {},
                                'negotiation auto': {},
                                'no ip address': {},
                                'no mop enabled': {},
                                'no mop sysid': {}},
 'interface GigabitEthernet6': {'cdp enable': {},
                                'channel-group 13 mode active': {},
                                'negotiation auto': {},
                                'no ip address': {},
                                'no mop enabled': {},
                                'no mop sysid': {}},
 'interface GigabitEthernet7': {'cdp enable': {},
                                'channel-group 13 mode active': {},
                                'negotiation auto': {},
                                'no ip address': {},
                                'no mop enabled': {},
                                'no mop sysid': {}},
 'interface Loopback0': {'ip address 1.1.1.1 255.255.255.255': {},
                         'ip ospf 1 area 0': {},
                         'ip pim sparse-mode': {},
                         'ipv6 address 2001:1:1:1::1/128': {},
                         'ipv6 ospf 1 area 0': {},
                         'ipv6 rip ripng enable': {}},
 'interface Loopback300': {'ip address 1.1.1.1 255.255.255.255': {},
                           'ip ospf 2 area 0': {},
                           'ip pim sparse-mode': {},
                           'ipv6 address 2001:1:1:1::1/128': {},
                           'ipv6 rip ripng enable': {},
                           'vrf forwarding VRF1': {}},
 'interface Port-channel12': {'no ip address': {},
                              'no mop enabled': {},
                              'no mop sysid': {},
                              'no negotiation auto': {}},
 'interface Port-channel13': {'no ip address': {},
                              'no mop enabled': {},
                              'no mop sysid': {},
                              'no negotiation auto': {}},
 'ip access-list extended acl_name': {'permit ip any any': {}},
 'ip access-list extended ipv4_acl': {'permit tcp any any eq 22': {},
                                      'permit tcp any any eq 443': {},
                                      'permit tcp any any eq www': {}},
 'ip access-list extended ipv4_ext': {},
 'ip access-list extended test22': {'deny   ip any any': {},
                                    'permit tcp 192.168.1.0 0.0.0.255 host 1.1.1.1 established log': {},
                                    'permit tcp host 2.2.2.2 eq www telnet 443 any precedence network ttl eq 255': {}},
 'ip admission watch-list expiry-time 0': {},
 'ip domain name cisco.com': {},
 'ip forward-protocol nd': {},
 'ip http authentication local': {},
 'ip http client source-interface GigabitEthernet1': {},
 'ip http secure-server': {},
 'ip msdp cache-sa-state': {},
 'ip msdp peer 2.2.2.2 connect-source Loopback0': {},
 'ip msdp peer 3.3.3.3 connect-source Loopback0': {},
 'ip msdp vrf VRF1 cache-sa-state': {},
 'ip msdp vrf VRF1 peer 2.2.2.2 connect-source Loopback300': {},
 'ip msdp vrf VRF1 peer 3.3.3.3 connect-source Loopback300': {},
 'ip multicast-routing distributed': {},
 'ip multicast-routing vrf VRF1 distributed': {},
 'ip pim bsr-candidate Loopback0 0': {},
 'ip pim rp-address 2.2.2.2': {},
 'ip pim rp-candidate Loopback0': {},
 'ip pim send-rp-announce Loopback0 scope 32': {},
 'ip pim send-rp-discovery Loopback0 scope 32': {},
 'ip pim vrf VRF1 bsr-candidate Loopback300 0': {},
 'ip pim vrf VRF1 rp-address 2.2.2.2': {},
 'ip pim vrf VRF1 rp-candidate Loopback300': {},
 'ip pim vrf VRF1 send-rp-announce Loopback300 scope 32': {},
 'ip pim vrf VRF1 send-rp-discovery Loopback300 scope 32': {},
 'ip prefix-list test seq 10 permit 35.0.0.0/8 le 16': {},
 'ip prefix-list test seq 15 permit 36.0.0.0/8 le 16': {},
 'ip prefix-list test seq 20 permit 37.0.0.0/8 ge 24': {},
 'ip prefix-list test seq 25 permit 38.0.0.0/8 ge 16 le 24': {},
 'ip prefix-list test seq 5 permit 35.0.0.0/8': {},
 'ip sla 1': {'frequency 10': {}, 'udp-echo 239.1.1.1 65000': {}},
 'ip sla 2': {'frequency 10': {},
              'udp-echo 239.1.1.1 65000': {},
              'vrf VRF1': {}},
 'ip sla 3': {'frequency 10': {}, 'udp-echo 239.2.2.1 65000': {}},
 'ip sla 4': {'frequency 10': {},
              'udp-echo 239.2.2.1 65000': {},
              'vrf VRF1': {}},
 'ip sla 5': {'frequency 10': {}, 'udp-echo 239.3.3.1 65000': {}},
 'ip sla 6': {'frequency 10': {},
              'udp-echo 239.3.3.1 65000': {},
              'vrf VRF1': {}},
 'ip sla schedule 1 life forever start-time now': {},
 'ip sla schedule 2 life forever start-time now': {},
 'ip sla schedule 3 life forever start-time now': {},
 'ip sla schedule 4 life forever start-time now': {},
 'ip sla schedule 5 life forever start-time now': {},
 'ip sla schedule 6 life forever start-time now': {},
 'ip ssh version 2': {},
 'ipv6 access-list ipv6_acl': {'permit ipv6 any any log': {},
                               'permit ipv6 host 2001::1 host 2001:1::2': {},
                               'permit tcp any eq www 8443 host 2001:2::2': {}},
 'ipv6 multicast-routing': {},
 'ipv6 multicast-routing vrf VRF1': {},
 'ipv6 pim bsr candidate bsr 2001:1:1:1::1': {},
 'ipv6 pim bsr candidate rp 2001:1:1:1::1': {},
 'ipv6 pim rp-address 2001:2:2:2::2': {},
 'ipv6 pim vrf VRF1 bsr candidate bsr 2001:1:1:1::1': {},
 'ipv6 pim vrf VRF1 bsr candidate rp 2001:1:1:1::1': {},
 'ipv6 pim vrf VRF1 rp-address 2001:2:2:2::2': {},
 'ipv6 prefix-list test6 seq 10 permit 2001:DB8:2::/64 ge 65': {},
 'ipv6 prefix-list test6 seq 15 permit 2001:DB8:3::/64 le 128': {},
 'ipv6 prefix-list test6 seq 20 permit 2001:DB8:4::/64 ge 65 le 98': {},
 'ipv6 prefix-list test6 seq 5 permit 2001:DB8:1::/64': {},
 'ipv6 rip vrf-mode enable': {},
 'ipv6 router rip ripng': {'address-family ipv6 vrf VRF1': {},
                           'exit-address-family': {}},
 'ipv6 unicast-routing': {},
 'license udi pid CSR1000V sn 90T3DC8EFSV': {},
 'line con 0': {'exec-timeout 0 0': {}, 'login local': {}, 'stopbits 1': {}},
 'line vty 0 4': {'login local': {}, 'transport input telnet ssh': {}},
 'lldp run': {},
 'mac access-list extended mac_acl': {'deny   host 0000.0000.0000 host 0000.0000.0000 msdos': {},
                                      'deny   host 0000.0000.0000 host 0000.0000.0000 vlan 10': {},
                                      'permit host 0000.0000.0000 host 0000.0000.0000': {},
                                      'permit host aaaa.aaaa.aaaa host bbbb.bbbb.bbbb aarp': {}},
 'multilink bundle-name authenticated': {},
 'no aaa new-model': {},
 'no ip http server': {},
 'no license smart enable': {},
 'no logging console': {},
 'no platform punt-keepalive disable-kernel-core': {},
 'platform console serial': {},
 'platform qfp utilization monitor load 80': {},
 'redundancy': {},
 'router bgp 65000': {'address-family ipv4': {'neighbor 2.2.2.2 activate': {},
                                              'neighbor 3.3.3.3 activate': {},
                                              'network 1.1.1.1 mask 255.255.255.255': {}},
                      'address-family ipv4 vrf VRF1': {'neighbor 2.2.2.2 activate': {},
                                                       'neighbor 2.2.2.2 remote-as 65000': {},
                                                       'neighbor 2.2.2.2 update-source Loopback300': {},
                                                       'neighbor 3.3.3.3 activate': {},
                                                       'neighbor 3.3.3.3 remote-as 65000': {},
                                                       'neighbor 3.3.3.3 update-source Loopback300': {},
                                                       'network 1.1.1.1 mask 255.255.255.255': {}},
                      'address-family ipv6': {'neighbor 2001:2:2:2::2 activate': {},
                                              'neighbor 2001:3:3:3::3 activate': {},
                                              'network 2001:1:1:1::1/128': {}},
                      'address-family ipv6 vrf VRF1': {'neighbor 2001:2:2:2::2 activate': {},
                                                       'neighbor 2001:2:2:2::2 remote-as 65000': {},
                                                       'neighbor 2001:2:2:2::2 update-source Loopback300': {},
                                                       'neighbor 2001:3:3:3::3 activate': {},
                                                       'neighbor 2001:3:3:3::3 remote-as 65000': {},
                                                       'neighbor 2001:3:3:3::3 update-source Loopback300': {},
                                                       'network 2001:1:1:1::1/128': {}},
                      'bgp log-neighbor-changes': {},
                      'bgp router-id 1.1.1.1': {},
                      'exit-address-family': {},
                      'neighbor 2.2.2.2 remote-as 65000': {},
                      'neighbor 2.2.2.2 update-source Loopback0': {},
                      'neighbor 2001:2:2:2::2 remote-as 65000': {},
                      'neighbor 2001:2:2:2::2 update-source Loopback0': {},
                      'neighbor 2001:3:3:3::3 remote-as 65000': {},
                      'neighbor 2001:3:3:3::3 update-source Loopback0': {},
                      'neighbor 3.3.3.3 remote-as 65000': {},
                      'neighbor 3.3.3.3 update-source Loopback0': {},
                      'no bgp default ipv4-unicast': {}},
 'router eigrp test': {'address-family ipv4 unicast autonomous-system 100': {'exit-af-topology': {},
                                                                             'network 1.1.1.1 0.0.0.0': {},
                                                                             'network 10.12.90.0 0.0.0.255': {},
                                                                             'network 10.13.90.0 0.0.0.255': {},
                                                                             'topology base': {}},
                       'address-family ipv4 unicast vrf VRF1 autonomous-system 100': {'exit-af-topology': {},
                                                                                      'network 1.1.1.1 0.0.0.0': {},
                                                                                      'network 10.12.90.0 0.0.0.255': {},
                                                                                      'network 10.13.90.0 0.0.0.255': {},
                                                                                      'topology base': {}},
                       'address-family ipv6 unicast autonomous-system 100': {'exit-af-topology': {},
                                                                             'topology base': {}},
                       'exit-address-family': {}},
 'router eigrp tet': {'address-family ipv6 unicast vrf VRF1 autonomous-system 100': {'exit-af-topology': {},
                                                                                     'topology base': {}},
                      'exit-address-family': {}},
 'router isis test': {'address-family ipv6': {'multi-topology': {}},
                      'exit-address-family': {},
                      'metric-style wide': {},
                      'net 49.0001.1111.1111.1111.00': {}},
 'router isis test1': {'address-family ipv6': {'multi-topology': {}},
                       'exit-address-family': {},
                       'metric-style wide': {},
                       'net 49.0001.1111.1111.1111.00': {},
                       'vrf VRF1': {}},
 'router ospf 1': {'router-id 1.1.1.1': {}},
 'router ospf 2 vrf VRF1': {'router-id 11.11.11.11': {}},
 'router ospfv3 1': {'address-family ipv6 unicast': {},
                     'exit-address-family': {}},
 'router rip': {'address-family ipv4 vrf VRF1': {'network 1.0.0.0': {},
                                                 'network 10.0.0.0': {},
                                                 'no auto-summary': {}},
                'exit-address-family': {},
                'network 1.0.0.0': {},
                'network 10.0.0.0': {},
                'version 2': {}},
 'service config': {},
 'service timestamps debug datetime msec': {},
 'service timestamps log datetime msec': {},
 'spanning-tree extend system-id': {},
 'subscriber templating': {},
 'username admin password 0 Cisc0123': {},
 'username cisco privilege 15 secret 5 $1$zmuJ$N4opUnBFwW7eNn5hfKj550': {},
 'version 16.9': {},
 'vrf definition Mgmt-intf': {'address-family ipv4': {},
                              'address-family ipv6': {},
                              'exit-address-family': {}},
 'vrf definition VRF1': {'address-family ipv4': {},
                         'address-family ipv6': {},
                         'exit-address-family': {},
                         'rd 65000:1': {}}}
        self.assertEqual(result, expected_output)