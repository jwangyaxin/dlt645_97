#!/usr/bin/env python3
##########################Electric Meter Constant#######################
import dlt645
import sys
from test_dlt645 import *

verbose = 1

port_id = '/dev/ttyUSB0'

chn=dlt645.Channel(port_id = port_id, tmo_cnt = 10, wait_for_read = 0.5)

# open the channel
if not chn.open():
    sys.stdout.write('Fail to open %s...exit script!\n\n\n' % port_id)
    sys.exit()

# read meter address
rsp = read_meter_address(chn)

if rsp:
    addr = chn.rx_addr;
    rsp = read_MeterNumber(chn, addr, verbose)