# !/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback
from Employee import *
from Position import *
from Table import *

class Salary:
    def __init__(self):
        self.employees_info = Employee().get_all_db_data()
        self.positions_info = Position().get_all_db_data()
        self.table_info = Table().get_all_db_data()

    
