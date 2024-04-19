#Script to manage restart in a MITgcm+BFM simulation
# PL 22.IX.2022
import argparse
def argument():
    parser = argparse.ArgumentParser(description = '''
    Script to manage restart in a MITgcm+BFM simulation
    It sets automatically start and end times, and restarts
    at the end of the simulation.
    ''',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(   '--iteration', '-it',
                                type = int,
                                required = True,
                                help = ''' interation index'''

                                )
    parser.add_argument(   '--start_date', '-sd',
                                type = str,
                                required = False,
                                default="20060101-000000",
                                help = ''' starting date'''

                                )
    parser.add_argument(   '--months_increment', '-mi',
                                type = int,
                                required = False,
                                default=0,
                                help = ''' months increment'''

                                )
    parser.add_argument(   '--days_increment', '-di',
                                type = int,
                                required = False,
                                default=0,
                                help = ''' days increment'''

                                )
    parser.add_argument(   '--end___date', '-ed',
                                type = str,
                                required = False,
                                default="21000101-000000",
                                help = ''' starting date'''

                                )

    return parser.parse_args()

def create_Start_End_Times(starttime,endtime):
    fileout="Start_End_Times"

    f = open(fileout,'w')
    f.write(starttime)
    f.write("\n")
    f.write(endtime)
    f.close()

args = argument()

import os,sys
import glob
import datetime
from dateutil.relativedelta import relativedelta
import numpy as np


iteration=args.iteration # Iteration starts from 0



Exp_start_date_str=args.start_date
print("Scenario Simulation Starting date: " + Exp_start_date_str)
Exp___end_date_str=args.end___date
print("Scenario Simulation End      date: " + Exp___end_date_str)

Exp_start_date=datetime.datetime.strptime(Exp_start_date_str, "%Y%m%d-%H%M%S")
Exp___end_date=datetime.datetime.strptime(Exp___end_date_str, "%Y%m%d-%H%M%S")

delta_day=args.days_increment
delta_month=args.months_increment

if (  delta_day > 0 ) and (  delta_month > 0 ):
    print( " day increment and month increment both >0: Please choose one.")
    sys.exit()
    
if  delta_day > 0  :
    start_days=delta_day*iteration
    end___days=delta_day*(iteration+1)

    start_simulation_date = Exp_start_date + relativedelta(days=start_days)
    end___simulation_date = Exp_start_date + relativedelta(days=end___days)

if  delta_month > 0 :
    start_months=delta_month*iteration
    end___months=delta_month*(iteration+1)

    start_simulation_date = Exp_start_date + relativedelta(months=start_months)
    end___simulation_date = Exp_start_date + relativedelta(months=end___months)

start_simulation_date_str=start_simulation_date.strftime("%Y%m%d-%H%M%S")
end___simulation_date_str=end___simulation_date.strftime("%Y%m%d-%H%M%S")

print("Starting iteration #: "     + str(iteration)) 
print("Simulation Start    date: " + start_simulation_date_str)
print("Simulation end      date: "  + end___simulation_date_str)


create_Start_End_Times(start_simulation_date_str, end___simulation_date_str)

