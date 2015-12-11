# ***Establish SSH session for remote execution and output of network device configurations***#

# Import modules

import getpass
import paramiko
import time
import sys


def disable_paging(disable_page):
    """Disable paging on a Cisco router
    :param disable_page:
    """

    disable_page.send("terminal length 0\n")
    time.sleep(1)

    # Clear the buffer on the screen
    output_disable_paging = disable_page.recv(1000)

    return output_disable_paging


if __name__ == '__main__':
    # Define variables

    # Prompt users for IP, username, and admin of remote switch/router
    ip = raw_input("Please enter the IP address:")
    username = raw_input("Please enter username of network device:")
    # password= input("Please enter password of network device:")
    password = raw_input("Please enter password of network device:")

    # Create SSH Object
    remote_conn_pre = paramiko.SSHClient()

    # Add untrusted host
    remote_conn_pre.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())

    # Initiate SSH session
    remote_conn_pre.connect(ip, username=username, password=password,
                            look_for_keys=False, allow_agent=False)
    print ("SSH connection established to %s" % ip)

    # Use invoke_shell to establish an 'interactive session'
    remote_conn = remote_conn_pre.invoke_shell()
    print ("Interactive SSH session established")

    # Strip the initial router prompt
    output = remote_conn.recv(1000)

    # See what we have
    print (output)

    # Flush the output buffer
    sys.stdout.flush()

    # Turn off paging
    disable_paging(remote_conn)

    # Prompt for user exec password
    
   # remote_conn.send("enable terminal")
   # password = getpass.getpass("Please enter enable terminal password of network device:")

    # Send show commands and output individual files for the 'running-config', 'startup-config', and 'show version'#

    # Send running-config command
    
    remote_conn.send("show running-config\r\n")

    # Wait for the command to complete
    time.sleep(2)

    # Read all output returned
    output = remote_conn.recv(65534)

    print (output)

    # Flush the buffer
    sys.stdout.flush()

    # Output running-config to txt file
    with open('running-config.txt', 'wb') as f_out:
        f_out.write(output)

    print ('running-config')

    # Send startup-config command
    
    remote_conn.send("show startup-config\r\n")

    # Wait for the command to complete
    time.sleep(2)

    # Read all output returned
    output = remote_conn.recv(65534)

    print (output)

    # Flush the buffer
    sys.stdout.flush()

    # Output startup-config to txt file
    with open('startup-config.txt', 'wb') as f_out:
        f_out.write(output)

    print ('startup-config')

    # Send show version command
    
    remote_conn.send("show version\r\n")

    # Wait for the command to complete
    time.sleep(2)

    # Read all output returned
    output = remote_conn.recv(65534)

    print (output)

    # Flush the buffer
    sys.stdout.flush()

    # Output running-config to txt file
    with open('show-version.txt', 'wb') as f_out:
        f_out.write(output)

    print ('show version')

    # *** Run show commands to be returned to a single text file ***#

    # Send "show run | incl enable secret" command
    
    remote_conn.send("show run | incl enable secret\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show startup-config" command
    
    remote_conn.send("show startup-config\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show run | beg banner"
    
    remote_conn.send("show run | beg banner\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl incl tcp small-servers" command
    
    remote_conn.send("show run | incl tcp-small-servers\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl udp-small-servers" command
    
    remote_conn.send("show run | incl udp-small-servers\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Output show run command to text file
    with open('output.txt', 'wb') as f_out:
        f_out.write(output)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl service pad" command
    
    remote_conn.send("show run | incl service pad\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl service tcp" command
    
    remote_conn.send("show run | incl service tcp\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl finger" command
    
    remote_conn.send("show run | incl finger\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl http secure" command
    
    remote_conn.send("show run | incl http secure\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)
    sys.stdout.flush()

    # Send "show run | incl boot network" command
    
    remote_conn.send("show run | incl boot network\r\n")

    # Wait for the command to complete
    time.sleep(2)

    # Output show run command to text file
    with open('output.txt', 'wb') as f_out:
        f_out.write(output)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl service config" command
    
    remote_conn.send("show run | incl service config\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show ntp associations" command
    
    remote_conn.send("show ntp associations\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show vlan-switch" command
    
    remote_conn.send("show vlan-switch\r\n")

    # Wait for the command to complete
    time.sleep(2)

    # Output show run command to text file
    with open('output.txt', 'wb') as f_out:
        f_out.write(output)

    print (output)

    sys.stdout.flush()

    # Send "show interfaces trunk" command
    
    remote_conn.send("show interfaces trunk\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show interfaces" command
    
    remote_conn.send("show interfaces\r\n")

    # Wait for the command to complete
    time.sleep(2)

    # Output show run command to text file
    with open('output.txt', 'wb') as f_out:
        f_out.write(output)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl logging" command
    
    remote_conn.send("show run | incl logging\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show run | beg vty 0" command
    
    remote_conn.send("show run | beg vty 0\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show line con 0 | begin Timeout" command
    
    remote_conn.send("show line con 0 | begin Timeout\r\n")

    # Wait for the command to complete
    time.sleep(2)

    with open('output.txt', 'wb') as f_out:
        f_out.write(output)

    print (output)

    sys.stdout.flush()

    # Send "show ip ssh" command
    
    remote_conn.send("show ip ssh\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show snmp" command
    
    remote_conn.send("show snmp\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show snmp community" command
    
    remote_conn.send("show snmp community\r\n")

    # Wait for the command to complete
    time.sleep(2)

    # Output show run command to text file
    with open('output.txt', 'wb') as f_out:
        f_out.write(output)

    print (output)

    sys.stdout.flush()
    
    remote_conn.send("show access-lists\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show run | incl dot1x" command
    
    remote_conn.send("show run | incl dot1x\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show port-security" command
    
    remote_conn.send("show run | incl dot1x\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show interface pruning" command
    
    remote_conn.send("show interface pruning\r\n")

    # Wait for the command to complete
    time.sleep(2)

    print (output)

    sys.stdout.flush()

    # Send "show snmp group" command
    
    remote_conn.send("show snmp group\r\n")

    # Wait for the command to complete
    time.sleep(2)

    output = remote_conn.recv(65534)
    print (output)
    sys.stdout.flush()

    # Output show run command to text file
    with open('output.txt', 'wb') as f_out:
        f_out.write(output)

    print ('output')

    sys.stdout.flush()

    # End SSH session
    # close (f_out)
    print ("Script finished, closing SSH connection")
    remote_conn.close()
