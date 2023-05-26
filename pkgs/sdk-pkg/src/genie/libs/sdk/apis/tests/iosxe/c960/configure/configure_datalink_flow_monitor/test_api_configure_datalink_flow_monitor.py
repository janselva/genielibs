import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.c960.configure import configure_datalink_flow_monitor


class TestConfigureDatalinkFlowMonitor(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          stack3-nyquist-1:
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
        self.device = self.testbed.devices['stack3-nyquist-1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_configure_datalink_flow_monitor(self):
        result = configure_datalink_flow_monitor(self.device, 'Gi3/0/2', 'm2in1', 'input')
        expected_output = None
        self.assertEqual(result, expected_output)
