import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.fips.configure import configure_crypto_isakmp_policy


class TestConfigureCryptoIsakmpPolicy(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          9300stack:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: cat9k
            type: router
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['9300stack']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_crypto_isakmp_policy(self):
        result = configure_crypto_isakmp_policy(self.device, '1', 'aes', 'sha', 'pre-share', '14', '86400')
        expected_output = None
        self.assertEqual(result, expected_output)
