"""Execute Interface related command"""

# Python
import logging
import time
import re

# Unicon
from unicon.core.errors import SubCommandFailure
from unicon.eal.dialogs import Statement, Dialog
from unicon.eal.expect import Spawn, TimeoutError


log = logging.getLogger(__name__)

def execute_test_idprom_fake_insert(device, interface):
    """ 
        Args:
            device ('obj'): device to use  
            interface ('str'): Interface for which we are doing SFP Fake-insert
        Returns:
            Return the test command execution output
        Raises:
            SubCommandFailure
    """
    cmd = "test idprom interface {test_intf} fake-insert".format(test_intf=interface)

    try:
        out = device.execute(cmd)
    except SubCommandFailure:
        raise SubCommandFailure('Failed to perform SFP OIR Fake-insert')
    return out

def execute_test_idprom_fake_remove(device, interface):
    """   
        Args:
            device ('obj'): device to use  
            interface ('str'): Interface for which we are doing SFP Fake-remove
        Returns:
            Return the test command execution output
        Raises:
            SubCommandFailure
    """
    cmd = "test idprom interface {test_intf} fake-remove".format(test_intf=interface)

    try:
        out = device.execute(cmd)
    except SubCommandFailure:
        raise SubCommandFailure('Failed to perform SFP OIR Fake-remove')
    return out
    
def execute_test_crash(device,num,timeout=500,connect_timeout=400):
    """   
        Args:
            device ('obj'): device to use 
            num ('str'): number of the crash type to be executed.
            timeout('integer',optional): Delay for the device to boot.
            connect_timeout ('int, optional'): Time to wait before sending the prompt
                                            (when pattern "Press RETURN to get 
                                            started" matches)
        Returns:
            None
        Raises:
            SubCommandFailure
    """
    def send_crashnum(spawn):        
        spawn.sendline('%s'%num)
        
    def slow_sendline(spawn):
        log.info('inside  slow_sendline')
        time.sleep(connect_timeout)
        spawn.sendline('')
        spawn.sendline('enable')
        spawn.sendline('')
        
   
    dialog = Dialog ([
        Statement(pattern = r"WARNING\:.*\?\s*" ,
                  action = "sendline(C)",
                  args = None,
                  loop_continue = True,
                  continue_timer = False),
        Statement(pattern = r"^.*Type the number for the selected crash\:.*\?\s*",
                  action = send_crashnum,
                  args = None,
                  loop_continue = True,
                  continue_timer = False),
        Statement(pattern = r".*Press RETURN to get started.*",
                  action = slow_sendline,
                  args = None,
                  loop_continue = False,
                  continue_timer = False)
        ])     
    log.info(f"Perform test crash {num} on {device.name}")  
    cmd  = f"test crash"
    try:
        output = device.execute(cmd, reply=dialog, timeout=timeout)
        log.info(f"{cmd} is successful")
    except Exception as e:
        log.error(f"Error while executing {cmd} : {e}")
        return False  

def execute_test_platform_hardware_fantray(device, switch_mode, switch_number):
    """ 
        Args:
            device ('obj'): device to use  
            switch_mode ('str'): switch mode on/off
	    switch_number ('int'): switch number 1/2
    """
    cmd= f"test platform hardware chassis fantray service-mode {switch_mode} switch {switch_number}"
    try:
        out=device.execute(cmd)
    except Exception as err:
        log.error("Error while executing {cmd} : err")
    return out

def execute_test_cable_diagnostics_tdr_interface(device, interface):
    """ Executes test cable-diagnostics tdr interface
        Args:
            device ('obj'): device to use  
            interface ('str'): Interface on which TDR test is to performed
        Returns:
            output ('str'): Device output
	"""
    cmd = f"test cable-diagnostics tdr interface {interface}"
    try:
        output = device.execute(cmd)
    except Exception as err:
        log.error(f"Error while executing {cmd}. Error:\n{err}")
    return output
    
def execute_test_fru_fake_insert(device, mode):
    """ 
        Args:
            device ('obj'): device to use 
            mode ('str'): mode active/standby
        Returns:
            Return the test command execution output
        Raises:
            SubCommandFailure
    """
    cmd = f"test platform software fed switch {mode} fru fake-insert"
    try:
        out = device.execute(cmd)
    except SubCommandFailure as e:
        raise SubCommandFailure(f'Failed to perform FRU Fake-insert. Error:\n{e}')
    return out