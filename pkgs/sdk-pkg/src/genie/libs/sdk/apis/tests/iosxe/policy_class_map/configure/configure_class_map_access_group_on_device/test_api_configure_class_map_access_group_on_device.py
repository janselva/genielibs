import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.policy_class_map.configure import configure_class_map_access_group_on_device


class TestConfigureClassMapAccessGroupOnDevice(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          Raitt:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['Raitt']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_class_map_access_group_on_device(self):
        result = configure_class_map_access_group_on_device(self.device, 'cm-acl100', '100')
        expected_output = None
        self.assertEqual(result, expected_output)
