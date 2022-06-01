import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.vpdn.configure import unconfigure_vpdn_group


class TestUnconfigureVpdnGroup(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = """
        devices:
          BB_C8500-12X4QC:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: iosxe
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['BB_C8500-12X4QC']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_vpdn_group(self):
        result = unconfigure_vpdn_group(self.device, '11')
        expected_output = None
        self.assertEqual(result, expected_output)