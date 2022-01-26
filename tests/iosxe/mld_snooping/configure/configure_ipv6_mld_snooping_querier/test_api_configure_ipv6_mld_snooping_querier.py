import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.mld_snooping.configure import configure_ipv6_mld_snooping_querier


class TestConfigureIpv6MldSnoopingQuerier(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          Cat9300_VTEP1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9300
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Cat9300_VTEP1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_ipv6_mld_snooping_querier(self):
        result = configure_ipv6_mld_snooping_querier(self.device)
        expected_output = None
        self.assertEqual(result, expected_output)
