import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.pki.configure import configure_pki_import


class TestConfigurePkiImport(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          fugazi:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: iosxe
            type: iosxe
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['fugazi']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_pki_import(self):
        result = configure_pki_import(self.device, 'test1', 'pkcs12', 'bootflash:', 'self.p12', None, 'cisco123', None, None, None, None, 'no', False, False, False, None, 'yes')
        expected_output = None
        self.assertEqual(result, expected_output)
