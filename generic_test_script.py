

#!/usr/bin/env python3

# NEW PYTHON SCRIPTS
# TESTING PHASE

# RInChI Project
# BENJAMIN HAMMOND 2014


import logging
import sqlite3

from rinchi_tools import rinchi_lib, v02_convert

# Define a handle for the RInChI class within the C++ library
rinchi_handle = rinchi_lib.RInChI()

select_command = "SELECT rowid, {}, {} FROM rinchis02".format("rinchi","rauxinfo")
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def populate_list(db_filename, s_command):
    db = sqlite3.connect(db_filename)
    cursornew = db.cursor()
    logging.info("populating")
    for row in cursornew.execute(s_command):
        data_to_add = []
        try:
            the_rinchi = v02_convert.convert_rinchi(row[1])
            data_to_add.append(the_rinchi)
            data_to_add.append(v02_convert.convert_rauxinfo(row[2]))
            data_to_add.append(rinchi_handle.rinchikey_from_rinchi(the_rinchi, "L"))
            data_to_add.append(rinchi_handle.rinchikey_from_rinchi(the_rinchi, "S"))
            data_to_add.append(rinchi_handle.rinchikey_from_rinchi(the_rinchi, "W"))
        except:
            logging.info(row[1])
            logging.info(row[2])
            logging.info(data_to_add)
    db.close()


populate_list("rinchi.db",select_command)