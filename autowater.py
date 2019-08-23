import time
import piplates.RELAYplate as plate

plate.relayON(0,3)
plate.relayON(0,7)
time.sleep(10)
plate.relayOFF(0,3)
plate.relayON(0,4)
time.sleep(7)
plate.relayOFF(0,7)
plate.relayOFF(0,4)