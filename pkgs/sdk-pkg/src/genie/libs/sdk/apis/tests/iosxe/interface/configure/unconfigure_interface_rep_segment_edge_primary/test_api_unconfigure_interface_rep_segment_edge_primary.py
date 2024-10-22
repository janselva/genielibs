import os
import unittest
from pyats.topology import loader
from genie.libs.sdk.apis.iosxe.interface.configure import unconfigure_interface_rep_segment_edge_primary


class TestUnconfigureInterfaceRepSegmentEdgePrimary(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        testbed = f"""
        devices:
          IR_DBS_IE3400_1:
            connections:
              defaults:
                class: unicon.Unicon
              a:
                command: mock_device_cli --os iosxe --mock_data_dir {os.path.dirname(__file__)}/mock_data --state connect
                protocol: unknown
            os: iosxe
            platform: switch
            type: switch
        """
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['IR_DBS_IE3400_1']
        self.device.connect(
            learn_hostname=True,
            init_config_commands=[],
            init_exec_commands=[]
        )

    def test_unconfigure_interface_rep_segment_edge_primary(self):
        result = unconfigure_interface_rep_segment_edge_primary(self.device, 'GigabitEthernet1/1', '1')
        expected_output = None
        self.assertEqual(result, expected_output)
