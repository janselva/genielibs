"""Common verification functions for OSPF3"""

# Python
import logging

# Genie
from genie.utils.timeout import Timeout
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.utils import Dq

# pyATS
from genie.utils import Dq

log = logging.getLogger(__name__)


def verify_ospf3_interface_type(device,
                                interface,
                                interface_type,
                                max_time=60,
                                check_interval=10):
    """ Verifies ospf3 interface type

        Args:
            device ('obj'): device to use
            interface ('str'): Interface to use
            interface_type ('str'): Interface type
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check

        Returns:
            True/False

        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        out = None
        try:
            out = device.parse('show ospf3 interface extensive')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        #{'ospf-interface': [{'interface-name': 'ge-0/0/1.0'}]}
        for ospf_interface in out.q.get_values('ospf3-interface'):

            #{'interface-name': 'ge-0/0/1.0'}
            intf = ospf_interface.get('interface-name', None)

            #{'interface-type': 'LAN'}
            intf_type = ospf_interface.get('interface-type', None)
            if intf == interface and intf_type == interface_type:
                return True

        timeout.sleep()

    return False


def verify_ospf3_neighbor_state(device,
                                expected_state,
                                interface,
                                max_time=60,
                                check_interval=10):
    """ Verifies state of ospf neighbor

        Args:
            device ('obj'): device to use
            expected_state ('str'): OSPF adjacency state that is expected
            interface ('str'): Name of interface
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check

        Returns:
            True/False

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            output = device.parse('show ospf3 neighbor')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        #{'ospf-neighbor-information': {'ospf-neighbor': [{}]}}
        neighbors = output.q.get_values('ospf3-neighbor')
        for neighbor in neighbors:
            #'interface-name': 'ge-0/0/0.0'
            #'ospf-neighbor-state': 'Full'
            if neighbor.get('interface-name',[]) == interface and \
               neighbor.get('ospf-neighbor-state',[]).lower() == expected_state.lower():
                return True

        timeout.sleep()

    return False


def verify_no_ospf3_neigbor_output(device,
                                   extensive=False,
                                   max_time=60,
                                   check_interval=10):
    """ Verifies if ospf3 neighbor doesn't exists

        Args:
            device ('obj'): device to use
            extensive ('bool'): If ospf command is extensive
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check

        Returns:
            True/False

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():

        if extensive:
            try:
                output = device.parse('show ospf3 neighbor extensive')
            except SchemaEmptyParserError:
                timeout.sleep()
                continue

        else:
            try:
                output = device.parse('show ospf3 neighbor')
            except SchemaEmptyParserError:
                timeout.sleep()
                continue

        if output:
            return False

        timeout.sleep()

    return True


def verify_ospf3_neighbor_number(device,
                                 expected_interface=None,
                                 expected_number=None,
                                 expected_state=None,
                                 max_time=60,
                                 check_interval=10):
    """ Verifies the number of ospf3 neighbors that meets the criteria

        Args:
            device ('obj'): device to use
            expected_interface ('str'): Interface to use
            expected_number ('str'): State occurrence
            expected_state ('str'): Interface state
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check

        Returns:
            
            Boolean

        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            out = device.parse("show ospf3 neighbor")
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # {
        # "ospf3-neighbor-information": {
        #     "ospf3-neighbor": [
        #         {
        #             "interface-name": "ge-0/0/0.0",
        #             "ospf-neighbor-state": "Full",
        #         },

        count = 0
        for neighbor in out.q.get_values('ospf3-neighbor'):
            # check variables

            interface_name = neighbor.get('interface-name', None)
            if expected_interface and expected_interface != interface_name:
                continue

            neighbor_state = neighbor.get('ospf-neighbor-state', None)
            if expected_state and expected_state.lower(
            ) != neighbor_state.lower():
                continue

            # if all variables exist, count plus 1
            count += 1

        if count == expected_number:
            return True

        timeout.sleep()

    return False


def verify_ospf3_interface(device,
                           expected_interface=None,
                           expected_interface_type=None,
                           expected_state=None,
                           extensive=True,
                           max_time=60,
                           check_interval=10,
                           expected_hello_interval=None):
    """ Verifies ospf3 interface exists with criteria

        Args:
            device ('obj'): device to use
            expected_interface ('str'): Interface to use
            expected_interface_type ('str'): Interface type
            expected_state ('str'): Interface state
            extensive ('boolean'): Flag for extensive command
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check
            expected_hello_interval ('str'): Expected hello interval

        Returns:
            Boolean

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        out = None

        try:
            if extensive:
                out = device.parse('show ospf3 interface extensive')
            else:
                out = device.parse('show ospf3 interface')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # {
        # "ospf3-interface-information": {
        #     "ospf3-interface": [
        #         {
        #             "interface-name": "ge-0/0/0.0",
        #             "interface-type": "P2P",
        #             "ospf-interface-state": "PtToPt",
        #             "hello-interval": "100",
        #         },

        for ospf_interface in out.q.get_values('ospf3-interface'):

            intf = ospf_interface.get('interface-name', None)
            if expected_interface and expected_interface != intf:
                continue

            intf_type = ospf_interface.get('interface-type', None)
            if expected_interface_type and expected_interface_type != intf_type:
                continue

            intf_state = ospf_interface.get('ospf-interface-state', None)
            if expected_state and expected_state != intf_state:
                continue

            intf_hello_interval = ospf_interface.get('hello-interval', None)
            if expected_hello_interval and str(expected_hello_interval) != intf_hello_interval:
                continue

            return True
        timeout.sleep()
    return False


def verify_ospfv3_spf_delay(device,
                           expected_spf_delay=None,
                           max_time=60,
                           check_interval=10):
    """ Verify SPF delay

        Args:
            device('obj'): device to use
            expected_spf_delay('float'): SPF delay time    
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check

        Returns:  
            Boolean       
        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)

    # show commands: "show ospf overview"
    while timeout.iterate():
        try:
            output = device.parse('show ospf3 overview')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        spf_delay = output.q.get_values('ospf-spf-delay', None)
        if spf_delay:
            spf_delay = float(spf_delay[0])


        if spf_delay == expected_spf_delay:
            return True

        timeout.sleep()
    return False
def verify_ospf3_metric(device,
                        interface,
                        metric,
                        max_time=60,
                        check_interval=10):
    """Verify the OSPF3 metric

    Args:
        device (obj): Device object
        interface (str): Interface name
        metric (str): OSPF3 metric
    Returns:
        True/False
    Raises:
        N/A
    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        out = None
        try:
            out = device.parse('show ospf3 interface extensive')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Example dictionary

        # "ospf3-interface": [
        #         {
        #             "interface-cost": "5",
        #             "interface-name": "ge-0/0/0.0",
        #         },

        ospf3_interface_list = out.q.get_values('ospf3-interface')

        for ospf3_interface_dict in ospf3_interface_list:

            #{'interface-name': 'ge-0/0/1.0'}
            interface_ = ospf3_interface_dict.get('interface-name')

            #{'interface-cost': '5'}
            metric_ = ospf3_interface_dict.get('interface-cost')

            if interface_.lower() == interface.lower() and str(metric_) == str(
                    metric):
                return True
    return False

def verify_ospf3_neighbors_found(device, extensive=False,
    max_time=90, check_interval=10, expected_interface=None, instance=None):
    """ Verifies ospf3 neighbors values exists

        Args:
            device ('obj'): device to use
            extensive ('str'): If to check with extensive command
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check
            expected_interface ('str'): Interface to check for
            instance ('str'): Instance to check for

        Returns:
            True/False

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        out = None
        try:
            if instance:
                out = device.parse('show ospf3 neighbor instance {instance}'.format(
                    instance=instance
                ))
            elif extensive:
                out = device.parse('show ospf3 neighbor extensive')
            else:
                out = device.parse('show ospf3 neighbor')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        ospf3_neighbors = out.q.get_values('ospf3-neighbor')

        if expected_interface:
            if len([
                neighbor for neighbor in ospf3_neighbors if neighbor.get('interface-name') == expected_interface
                ]) > 0:
                return True
            else:
                timeout.sleep()
                continue

        if len(ospf3_neighbors) > 0:
            return True
        timeout.sleep()
    return False

def verify_ospfv3_neighbors_not_found(device, extensive=False,
    max_time=90, check_interval=10, expected_interface=None):
    """ Verifies ospfv3 neighbors values exists

        Args:
            device ('obj'): device to use
            extensive ('str'): If to check with extensive command. Defaults to False
            max_time ('int'): Maximum time to keep checking. Defaults to 90
            check_interval ('int'): How often to check. Defaults to 10
            expected_interface ('str'): Interface to check for. Defaults to None

        Returns:
            True/False

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        out = None
        try:
            if extensive:
                out = device.parse('show ospf3 neighbor extensive')
            else:
                out = device.parse('show ospf3 neighbor')
        except SchemaEmptyParserError:
            return True

        ospf3_neighbors = out.q.get_values('ospf3-neighbor')

        if expected_interface:
            if len([
                neighbor for neighbor in ospf3_neighbors \
                    if neighbor.get('interface-name') == expected_interface
                ]) == 0:
                return True
            else:
                timeout.sleep()
                continue

        if len(ospf3_neighbors) == 0:
            return True
        timeout.sleep()
    return False


def verify_ospf3_overview(device, router_id, max_time=90, check_interval=10):
    """ Verifies ospf3 overview values

        Args:
            device ('obj'): device to use
            router_id ('str'): Router ID
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check

        Returns:
            True/False

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        out = None
        try:
            out = device.parse('show ospf3 overview')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        router_id_ = out.q.contains_key_value('ospf-router-id',
                                              router_id,
                                              value_regex=True)
        if router_id_:
            return True
        timeout.sleep()
    return False


def verify_ospfv3_interface_in_database(device,
                                       expected_interface,
                                       expected_interface_type=None,
                                       expected_metric=None,
                                       adv_router=False,
                                       expect_output=True,
                                       max_time=60,
                                       check_interval=10):
    """ Verifies ospf interface exists with criteria

        Args:
            device ('obj'): device to use
            expected_interface ('str'): Interface to use
            expected_interface_type ('str'): Interface type
            expected_metric ('str'): Metric of Interface
            adv_router ('bool'): Whether to look for address in adversiting router
            expect_output ('str'): Flag, either expecting output or no output
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check

        Returns:
            Boolean

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        try:
            out = device.parse('show ospf3 database extensive')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        #'ospf3-database': [{
        #    'lsa-type':
        #        'Router',
        #        'lsa-id':
        #            '0.0.0.0',
        #        'advertising-router':
        #            '1.1.1.1'
        #            }
        #        ]

        for ospf3_database in Dq(out).get_values('ospf3-database'):

            if not adv_router:
                #'lsa-type': 'Router'
                lsa_type = ospf3_database.get('lsa-type', None)
                lsa_type = lsa_type.lower() if lsa_type else lsa_type
                if expected_interface_type.lower() != lsa_type:
                    continue

                #'type-value': '2'
                if str(expected_metric) != ospf3_database.get('ospf3-external-lsa', {}).get('type-value',None):
                    continue

                #'ospf3-prefix': ['2001::1/128']
                current_prefix = ospf3_database.get('ospf3-external-lsa', {}).get('ospf3-prefix',None)
                if expected_interface != current_prefix:
                    continue
            else:
                prefix_ips = ospf3_database.get('ospf3-intra-area-prefix-lsa',{}).get('ospf3-prefix',{})
                if expected_interface not in prefix_ips:
                    continue

            return True
        timeout.sleep()
    return False

def verify_ospf3_database_prefix(device,
                                 expected_prefix,
                                 max_time=60,
                                 check_interval=10):
    """API for verifying ospf3 prefix exists in database

    Args:
        device (obj): device object
        expected_prefix (string): prefix being searched for
        max_time (int, optional): maximum timeoute time. Defaults to 60.
        check_interval (int, optional): check interval. Defaults to 10.

    Returns:
        True/False

    Raises:
        N/A
    """

    # 'ospf3-database':{
    #     'ospf3-inter-area-prefix-lsa':
    #             'FFFF::FF/128'
    #   }

    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        try:
            out = device.parse('show ospf3 database extensive')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        for ospf3_database in Dq(out).get_values('ospf3-database'):
            prefix_ = Dq(ospf3_database).get_values('ospf3-prefix', 0)
            if not isinstance(prefix_, list):
                if prefix_.startswith(expected_prefix):
                    return True
        timeout.sleep()
    return False

def verify_show_ospf3_database_lsa_types(device,
                                         expected_types,
                                         max_time=60,
                                         check_interval=10):
    """Verify 'show ospf3 database' lsa-types contains expected_types

    Args:
        device ('obj'): device to use
        expected_types ('str'): types to verify
        max_time ('int'): Maximum time to keep checking
        check_interval ('int'): How often to check

    Raise: None

    Returns: Boolean

    """
    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        out = None
        try:
            out = device.parse('show ospf3 database')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
    
        found_types = out.q.get_values("lsa-type")

        verified = set(found_types).issuperset(set(expected_types))

        if verified:
            return True
        else:
            timeout.sleep()
            continue

    return False
