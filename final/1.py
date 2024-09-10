#!/usr/bin/python

"""
This script creates the network environment for Lab5:
- Starts all routers, switches and hosts
- You need to choose either Topo1 or Topo2
- XTerm window launched for all devices.
"""
# Needed to check for display status 
import inspect
import os

# Needed to patch Mininet's isShellBuiltin module
import sys

# Run commands when you exit the python script
import atexit

# patch isShellBuiltin (suggested by MiniNExT's authors)
import mininet.util

sys.modules['mininet.util'] = mininet.util

# Loads the default controller for the switches

from mininet.node import Controller

# Needed to set logging level and show useful information during script execution.
from mininet.log import setLogLevel, info

# To launch xterm for each node
from mininet.term import cleanUpScreens, makeTerms # for supporting copy/paste

# Provides the mininet> prompt
from mininet.cli import CLI

# Primary constructor for the virtual environment.
from mininet.net import Mininet

# We import the TC-enabled link
from mininet.link import Intf, TCIntf, TCLink


# Variable initialization
net = None
hosts = None


def run():
    " Creates the virtual environment, by starting the network and configuring debug information "
    info(' Creating an instance of Lab5 network topology\n')
    global net
    global hosts
   
    net = Mininet(intf=TCIntf)
    
    info('\n Adding Controller\n')
    net.addController( 'c0' )
    
    info('\n** Adding Hosts\n')
    r1 = net.addHost('r1', ip='x.x.x.x', hostname='r1')
    
    
    
    
  
    info('\n** Adding Switches\n')
    # Adding switches to the network
    sw1 = net.addSwitch('sw1')
    sw2 = net.addSwitch('sw2')
    
    info('\n** Creating Links \n')
    link_r1sw1 = net.addLink( r1, sw1, intfName1='r1-eth0')
    link_r1sw2 = net.addLink( r1, sw2, intfName1='r1-eth1')
    
    
    
    
    
    
    info('\n** Modifying Link Parameters \n')
    """
        Default parameters for links:
        bw = None,
     delay = None,
     jitter = None,
     loss = None,
     disable_gro = True,
     speedup = 0,
     use_hfsc = False,
     use_tbf = False,
     latency_ms = None,
     enable_ecn = False,
     enable_red = False,
     max_queue_size = None 
    """
    link_r1sw2.intf1.config( bw=3)
    
    net.start()

    info( '*** Configuring hosts\n' )
    info(' Executing custom commands\n')
    output = net.nameToNode.keys
    r1.cmd('ifconfig r1-eth1 x.x.x.x netmask x.x.x.x')

    
    
    
    
    
    
  #Enable Xterm window for every host
    info(' Enabling xterm for hosts only\n')
    # We check if the display is available
    hosts = [ r1, h1, h2, h3, h4 ]
    if 'DISPLAY' not in os.environ:
        error( "Error starting terms: Cannot connect to display\n" )
        return
    # Remove previous (and possible non-used) socat X11 tunnels
    cleanUpScreens()
    # Mininet's function to create Xterms in hosts
    makeTerms( hosts, 'host' )

  # Enable the mininet> prompt 
    info('** Running CLI\n')
    CLI(net)

    info( '*** Closing the terminals on the hosts\n' )
    r1.cmd("killall xterm")
    
    
    
    
    
    

    # This command stops the simulation
    net.stop()
    cleanUpScreens()

if name == 'main':
    # Set the log level on terminal
    setLogLevel('info')
    
    # Execute the script
    run()