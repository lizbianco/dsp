# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:41:47 2016

@author: EBianco
"""

from datetime import datetime


def solve(d1, d2, f):
    print(datetime.strptime(d2, f) - datetime.strptime(d1, f))

'#5a'
date_start_a = '01-02-2013'
date_stop_a = '07-28-2015'
form_a = '%m-%d-%Y'

solve(date_start_a, date_stop_a, form_a)


'#5b'
date_start_b = '12312013'
date_stop_b = '05282015'
form_b = '%m%d%Y'

solve(date_start_b, date_stop_b, form_b)


'#5c'
date_start_c = '15-Jan-1994'
date_stop_c = '14-Jul-2015'
form_c = '%d-%b-%Y'

solve(date_start_c, date_stop_c, form_c)









