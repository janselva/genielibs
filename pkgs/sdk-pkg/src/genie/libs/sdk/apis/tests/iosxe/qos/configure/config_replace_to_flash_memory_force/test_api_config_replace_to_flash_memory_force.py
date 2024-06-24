import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.qos.configure import config_replace_to_flash_memory_force


class TestConfigReplaceToFlashMemoryForce(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          NGSVL:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: c9500
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['NGSVL']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_config_replace_to_flash_memory_force(self):
        result = config_replace_to_flash_memory_force(self.device, 'stby-bootflash', 60)
        expected_output = None
        self.assertEqual(result, expected_output)
