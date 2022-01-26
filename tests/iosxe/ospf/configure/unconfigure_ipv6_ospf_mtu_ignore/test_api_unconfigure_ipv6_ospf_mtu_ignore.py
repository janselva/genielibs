import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.ospf.configure import unconfigure_ipv6_ospf_mtu_ignore


class TestUnconfigureIpv6OspfMtuIgnore(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Intrepid-DUT-1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: C9600
            type: C9600
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Intrepid-DUT-1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_ipv6_ospf_mtu_ignore(self):
        result = unconfigure_ipv6_ospf_mtu_ignore(device=self.device, interface='Vlan3000')
        expected_output = None
        self.assertEqual(result, expected_output)
