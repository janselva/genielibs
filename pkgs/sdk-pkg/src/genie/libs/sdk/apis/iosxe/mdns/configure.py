"""Configure mdns functions on device """

# Python
import logging

# Unicon
from unicon.core.errors import SubCommandFailure

# Genie
from genie.harness.utils import connect_device
log = logging.getLogger(__name__)

def configure_mdns(
    device,
    service_definition_name=None,
    service_list=None,
    direction=None,
    policy_name=None,
    service_list_msg_type=None,
    direction_msg_type=None,
    message_type=None,
    service_list_filter=None,
    direction_filter_type=None,
    filter_name=None,
    policy_name1=None
):
    """ Configure mDNS (Multicast Domain Name System) services on agent and service peer
    
        mdns-sd gateway
        mdns-sd service-definition custom10
          service-type _airplay._tcp.local
          service-type _raop._tcp.local
          service-type _ipp._tcp.local
          service-type _afpovertcp._tcp.local
          service-type _nfs._tcp.local
          service-type _ssh._tcp.local
          service-type _dpap._tcp.local
          service-type _daap._tcp.local
          service-type _ichat._tcp.local
          service-type _presence._tcp.local
          service-type _http._tcp.local
          service-type _ipps._tcp.local
          service-type _printer._tcp.local
          service-type _smb._tcp.local
          service-type _ftp._tcp.local
        mdns-sd service-list service_list31 IN
        match custom10
        mdns-sd service-list service_list32 OUT
        match custom10
        mdns-sd service-list service_list33 OUT
        match custom10
        mdns-sd service-list service_list34 IN
        match custom10
        mdns-sd service-policy Policy41
          service-list service_list31 IN
        mdns-sd service-policy Policy42
          service-list service_list32 OUT
          service-list service_list33 OUT
          service-list service_list34 IN
        mdns-sd service-list service_list55 IN
        match custom10 message-type query
        mdns-sd service-list service_list66 OUT
        match custom10 location-filter filter8
        mdns-sd service-policy Policy43
          service-list service_list55 IN
          service-list service_list66 OUT
        end
                
    Args:
        device ('obj'): device to configure
        service definition ('str', optional): service definition name. Default value is None
        service_list ('list', optional): list with all services. Default value is None
        direction ('str', optional): direction. Default value is None
        policy_name ('dict', optional): dict with all Policy names and directions. Default value is None
        service_list_msg_type ('str', optional): creating service list for msg type. Default value is None
        direction_msg_type ('str', optional): creating direction for msg type. Default value is None
        message_type ('str', optional): Message type. Default value is None
        service_list_filter ('str', optional): creating service list for filter type. Default value is None
        direction_filter_type ('str', optional): creating direction for filter type. Default value is None
        filter_name ('str', optional): Filter name. Default value is None
        policy_name1 ('dict', optional): creating new dict for adding new service list for msg and filter types. Default value is None
        
        dict = {'Policy41': ['service_list31', 'IN'],
                'Policy42': ['service_list32',
                             'OUT',
                             'service_list33',
                             'OUT',
                             'service_list34',
                             'IN']}
        
        dict = {'Policy43': ['service_list55', 'IN', 
                             'service_list66', 
                             'OUT']}

  Returns:
      None

  Raises:
      SubCommandFailure
    """
    log.debug("Configuring mdns on globally")    
    try:
        config = ["mdns-sd gateway"]        
        if service_definition_name != None:
            config.extend([
                "mdns-sd service-definition {srvc_def_name}".format(srvc_def_name=service_definition_name),
                "service-type _airplay._tcp.local",
                "service-type _raop._tcp.local",
                "service-type _ipp._tcp.local",
                "service-type _afpovertcp._tcp.local",
                "service-type _nfs._tcp.local",
                "service-type _ssh._tcp.local",
                "service-type _dpap._tcp.local",
                "service-type _daap._tcp.local",
                "service-type _ichat._tcp.local",
                "service-type _presence._tcp.local",
                "service-type _http._tcp.local",
                "service-type _ipps._tcp.local",
                "service-type _printer._tcp.local",
                "service-type _smb._tcp.local",
                "service-type _ftp._tcp.local"
            ]) 
        # Following if block is used for creating multiple service list with direction and definition name       
        if isinstance(service_list,list):
            for i in range(len(service_list)):
                config.extend([
                    "mdns-sd service-list {srvc_list_name} {direction}".format(
                        srvc_list_name=service_list[i],
                        direction=direction[i]),
                    "match {srvc_def_name}".format(
                        srvc_def_name=service_definition_name)
                ])
        # Following else block is used for creating only one service list with direction and definition name                   
        else:
            config.extend([
                "mdns-sd service-list {srvc_list_name} {direction}".format(
                    srvc_list_name=service_list,
                    direction=direction),
                "match {srvc_def_name}".format(
                    srvc_def_name=service_definition_name)
            ])                          
        # Following if block is used for creating multiple service policies with service lists attaching them
        if policy_name != None:
            for policy,dirctn in policy_name.items():
                config.extend(["mdns-sd service-policy {policy_name}".format(policy_name=policy)])
                count=0
                # Following for loop is used for attaching multiple service lists to one policy
                for plcy in range(len(dirctn)//2):
                    config.extend(["service-list {srvc_list_name} {direction}".format(
                        srvc_list_name=dirctn[count], 
                        direction=dirctn[count+1])
                    ])
                    count=count+2 
        # Following if block is used for creating service list with message                       
        if service_list_msg_type != None:        
            config.extend([
                "mdns-sd service-list {srvc_lst_msg_type} {dirctn_msg_type}".format(
                    srvc_lst_msg_type=service_list_msg_type, 
                    dirctn_msg_type=direction_msg_type),
                "match {srvc_def_name} message-type {msg_type}".format(
                    srvc_def_name=service_definition_name,
                    msg_type=message_type)
            ])                                
        # Following if block is used for creating service list with filter                                                
        if service_list_filter != None:        
            config.extend([
                "mdns-sd service-list {srvc_lst_filter} {dirctn_filter_type}".format(
                    srvc_lst_filter=service_list_filter, 
                    dirctn_filter_type=direction_filter_type),
                "match {srvc_def_name} location-filter {filter_name}".format(
                    srvc_def_name=service_definition_name,
                    filter_name=filter_name)
            ])                      
        # Following if block is used for again creating new service policy for adding new service list (msg and filter) to paricular policy             
        if policy_name1 != None:
            for policy,dirctn in policy_name1.items():
                config.extend(["mdns-sd service-policy {policy_name1}".format(policy_name1=policy)])
                count=0 
                for plcy in range(len(dirctn)//2):
                    config.extend(["service-list {srvc_list_name} {direction}".format(
                        srvc_list_name=dirctn[count], 
                        direction=dirctn[count+1])
                    ])
                    count=count+2                                          
        device.configure(config)
        
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure mdns. Error:\n{error}".format(error=e)
        )

def unconfigure_mdns_config(
    device,
    policy_name=None,
    service_list=None,
    direction=None,
    service_definition_name=None,
    service_list_filter=None,
    direction_filter_type=None,
    filter_name=None,
    service_list_msg_type=None,
    direction_msg_type=None
):
    """ Unconfigure mDNS (Multicast Domain Name System) services on agent and service peer

        Args:
            device ('obj'): device to configure
            policy_name ('list', optional): dict with all Policy names and directions. Default value is None
            service_list ('list', optional): list with all services. Default value is None
            direction ('str', optional): direction. Default value is None
            service definition ('str', optional): service definition name. Default value is None
            service_list_filter ('str', optional): creating service list for filter type. Default value is None
            direction_filter_type ('str', optional): creating direction for filter type. Default value is None
            filter_name ('str', optional): filter name. Default value is None
            service_list_msg_type ('str', optional): creating service list for msg type. Default value is None
            direction_msg_type ('str', optional): creating direction for msg type. Default value is None

        Returns:
            N/A
        Raises:
            SubCommandFailure: Failed executing configure commands
    """
    log.debug("Removing mdns configurations on globally")
    
    try:       
        config = ["no mdns-sd gateway"]
        
        # Following if block is used for removing multiple service policies and single policy
        if isinstance(policy_name,list):
            for policy in range(len(policy_name)):
                config.extend(["no mdns-sd service-policy {policy_name}".format(policy_name=policy_name[policy])])
        else:
            config.extend(["no mdns-sd service-policy {policy_name}".format(policy_name=policy_name)])                
        # Following if block is used for removing multiple service lists and single service list
        if isinstance(service_list,list):
            for service in range(len(service_list)):
                config.extend(["no mdns-sd service-list {srvc_list_name} {direction}".format(
                    srvc_list_name=service_list[service],
                    direction=direction[service])
                ])
        else:
            config.extend(["no mdns-sd service-list {srvc_list_name} {direction}".format(
                srvc_list_name=service_list,
                direction=direction)
            ])        
        # Following if block is used for removing service lists and filter               
        if service_list_filter != None:        
            config.extend([
                "no mdns-sd service-list {srvc_lst_filter} {dirctn_filter_type}".format(
                    srvc_lst_filter=service_list_filter, 
                    dirctn_filter_type=direction_filter_type),
                "no mdns-sd location-filter {filter_name}".format(
                    filter_name=filter_name)
            ])               
        # Following if block is used for removing service lists and messages
        if service_list_msg_type != None:                
            config.extend(["no mdns-sd service-list {srvc_lst_msg_type} {dirctn_msg_type}".format(
                srvc_lst_msg_type=service_list_msg_type, 
                dirctn_msg_type=direction_msg_type)
            ])
        # Below config used removing service definition      
        config.extend (["no mdns-sd service-definition {srvc_def_name}".format(
            srvc_def_name=service_definition_name)
        ])        
        device.configure(config)
        
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not remove mdns configure. Error:\n{error}".format(error=e)
        )
                       
def configure_vlan_agent(device, vlan, policy, active_query_timer, transport_way, vlan_src_intf=None):

    """ Configures vlan on mDNS(Multicast Domain Name System) agent

        Args:
            device (`obj`): Device object
            vlan ('int'): Vlan ID
            policy ('str'): Policy name
            active_query_timer ('int'): Active Query timer value
            transport_way ('str'): Transport way (ipv4,ipv6 or both, which need to allow)
            vlan_src_intf('int', optional): Source interface vlan. Default value is None

        Returns:
            N/A
        Raises:
            SubCommandFailure: Failed executing configure commands
    """
    log.debug("Configuring vlan on agent globally")

    try:
        config = [
            "vlan configuration {vlan_id}".format(vlan_id=vlan),
            "mdns-sd gateway",
            "service-policy {policy}".format(policy=policy),
            "active-query timer {active_query_timer}".format(
                active_query_timer=active_query_timer),
        ]
        if vlan_src_intf != None:        
            config.extend([
                "source-interface vlan {vlan_src_intf}".format(
                    vlan_src_intf=vlan_src_intf),
                "service-inst-suffix {vlan_src_intf}".format(
                    vlan_src_intf=vlan_src_intf)
            ])
        config.extend(["transport {ipv4_ipv6_both}".format(ipv4_ipv6_both=transport_way)])        
        device.configure(config)
                
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure Vlan. Error:\n{error}".format(error=e)
        )
        
def unconfigure_mdns_vlan(device, vlan):

    """ Removing mdns-sd gateway from vlan configuartion (mDNS-Multicast Domain Name System)

        Args:
            device (`obj`): Device object
            vlan ('int'): Vlan ID value
        Returns:
            None
        Raises:
            SubCommandFailure
    """
    log.debug("Removing vlan configs on mDNS globally")

    try:
        device.configure([
            "vlan configuration {vlan_id}".format(vlan_id=vlan),
            "no mdns-sd gateway"
        ])        
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not remove vlan configs from mDNS. Error:\n{error}".format(error=e)
        )

def configure_vlan_sp(device, vlan, policy, active_query_timer, src_vlan, ip_address, transport_way):

    """ Configures vlan on SP(service peer)

        Args:
            device (`obj`): Device object
            vlan ('int'): Vlan ID
            policy ('str'): Policy name
            active_query_timer ('int'): Active Query timer value
            src_vlan ('int'): Source interface vlan id
            ip_address ('str'): Ip address (ipv4 or ipv6)
            transport_way ('str'): Transport way (ipv4,ipv6 or both, which need to allow)

        Returns:
            None
        Raises:
            SubCommandFailure
    """
    log.debug("Configuring vlan on sp globally")

    try:
        device.configure([
            "vlan configuration {vlan_id}".format(vlan_id=vlan),
            "mdns-sd gateway",
            "service-policy {policy}".format(policy=policy),
            "active-query timer {active_query_timer}".format(
                active_query_timer=active_query_timer),
            "source-interface vlan {src_vlan}".format(src_vlan=src_vlan),
            "sdg-agent {ip_address}".format(ip_address=ip_address),
            "transport {ipv4_ipv6_both}".format(ipv4_ipv6_both=transport_way)
        ])
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure Vlan. Error:\n{error}".format(error=e)
        )

def configure_mdns_location_filter(device, location_filter, location_group, vlan, role):

    """ Configures location filter details on vlan

        Args:
            device ('obj'): device to use
            location_filter ('str'): location filter name
            location_group ('str'): location group name 
            vlan ('int'): Vlan id 
            role ('str'): Role name
        Returns:
            None
        Raises:
            SubCommandFailure
    """
    log.debug(
            "Configuring location filter {loc_filter} details "
            "on {vlan_id}".format(loc_filter=location_filter, vlan_id=vlan)
            )
    try:
        device.configure([
            "mdns-sd location-filter {loc_filter}".format(
                loc_filter=location_filter),
            "match location-group {loc_grp} vlan {vlan_id} role {role_name}".format(
                loc_grp=location_group,
                vlan_id=vlan,role_name=role)
        ])
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure mdns-sd with location-filter"
            "{loc_filter} on vlan {vlan_id}, Error: {error}".format(
                loc_filter=location_filter, vlan_id=vlan, error=e
            )
        )
        
def configure_mdns_location_group(device, location_group, vlan, interface):

    """ Configures location group details on interface

        Args:
            device ('obj'): device to use
            location_group ('int'): location group name
            vlan ('int'): Vlan id value 
            interface ('list'): list of interfaces to configure
        Returns:
            None
        Raises:
            SubCommandFailure
    """
    log.debug(
            "Configuring location group {loc_grp} details "
            "on {intf}".format(loc_grp=location_group, intf=interface)
            )
    try:
        config = [
            "mdns-sd location-group {loc_grp} vlan {vlan_id}".format(
                loc_grp=location_group,vlan_id=vlan)
        ]
        if isinstance(interface,list):
            for interf in interface:
                config.extend([
                    "interface {intf}".format(intf=interf)
                ])
        else:
            config.extend(["interface {intf}".format(intf=interface)])  
                      
        device.configure(config)    
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure mdns-sd with location-group"
            "{loc_grp} interface {interface}, Error: {error}".format(
                loc_grp=location_group, interface=interface, error=e
            )
        )

def unconfigure_mdns_location_group(device, location_group, vlan):

    """ Removing location group details on interface

        Args:
            device ('obj'): device to use
            location_group ('int'): location group name
            vlan ('int'): Vlan id value 
        
        Returns:
            None
        Raises:
            SubCommandFailure
    """
    log.debug("Removing location group details")
    try:
        config = [
            "no mdns-sd location-group {loc_grp} vlan {vlan_id}".format(
                loc_grp=location_group,
                vlan_id=vlan)
        ]        
        device.configure(config)
                
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not remove loation-group configs on device. Error:\n{error}".format(error=e)
        )

def configure_mdns_sd_agent(device, timer=None, count=None):

    """ Configures mDNS(Multicast Domain Name System) agent

        Args:
            device (`obj`): Device object
            timer ('int', optional): Timer value. Default value is None
            count ('int', optional): Count value. Default value is None 

        Returns:
            None
        Raises:
            SubCommandFailure
    """
    log.debug("Configuring mdns_sd_agent on globally")

    try:
        config = [
            "mdns-sd gateway",
            "mode sdg-agent"
        ]
        if timer != None and count != None:        
            config.extend([
                "service-announcement-timer periodicity {timer_val}".format(
                    timer_val=timer),
                "service-announcement-count {count_val}".format(
                    count_val=count),
                "service-query-timer periodicity {timer_val}".format(
                    timer_val=timer),
                "service-query-count {count_val}".format(
                    count_val=count)
            ])
        device.configure(config)        
                            
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure mdns_sd_agent. Error:\n{error}".format(error=e)
        )

def configure_mdns_sd_service_peer(device, vlan, ip_addr, response_timer=None, timer=None, count=None, value=None):

    """ Configures mDNS(Multicast Domain Name System) service peer

        Args:
            device (`obj`): Device object
            vlan ('int'): Vlan value
            ip_addr ('str'): ipv4,ipv6 address
            response_timer ('int', optional): active response timer. Default value is None
            timer ('int', optional): Timer value. Default value is None 
            count ('int', optional): Count value. Default value is None 
            value ('int', optional): rate limit value . Default value is None

        Returns:
            None
        Raises:
            SubCommandFailure
    """
    log.debug("Configuring mdns_sd_service_peer on globally")

    try:
        config = [
            "mdns-sd gateway",
            "mode service-peer",
            "source-interface vlan {vlan_id}".format(vlan_id=vlan),
            "sdg-agent {ipv4_ipv6}".format(ipv4_ipv6=ip_addr)
                ]
        if response_timer != None:        
            config.extend(["active-response-timer {resp_timer}".format(resp_timer=response_timer)])
        if timer != None and count != None:        
            config.extend([      
                "service-announcement-timer periodicity {timer_val}".format(
                    timer_val=timer),
                "service-announcement-count {count_val}".format(
                    count_val=count),
                "service-query-timer periodicity {timer_val}".format(
                    timer_val=timer),
                "service-query-count {count_val}".format(
                    count_val=count)
            ])
        if value != None:        
            config.extend(["rate-limit {value}".format(value=value)])
            
        device.configure(config)
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure mdns_sd_service_peer. Error:\n{error}".format(error=e)
        )

def configure_mdns_trust(device, interface):

    """ Configures location filter details on vlan

        Args:
            device ('obj'): device to use
            interface ('str'): interface
        Returns:
            None
        Raises:
            SubCommandFailure
    """
    log.debug("Configuring mdns-trust on interface")
    try:
        device.configure([
            "interface {intf}".format(intf=interface),
            "mdns-sd trust",
        ])
    except SubCommandFailure as e:
        raise SubCommandFailure(
            "Could not configure mdns_trust. Error:\n{error}".format(error=e)
        )
        
def configure_mdns_service_definition(device, name, srvc_type):

    """ Configure mDNS(Multicast Domain Name System) service definition 
        Args:
            device ('obj'): device to use
            name ('str')
            srvc_type ('list'):
          
        Returns:
            None
        Raises:
            SubCommandFailure: Failed configuring mdns service-definition
    """
    log.debug("Configuring mdns service defintion with  name={},srvc_type={}".format(name,srvc_type))

    try:
        for type in srvc_type:
            device.configure([
                "mdns-sd service-definition {}".format(name),
                "service-type  {} ".format(type)              
            ])
              
    except SubCommandFailure:
        raise SubCommandFailure(
            "Could not configure mdns service-definition {name}".format(
                name=name
            )
        )