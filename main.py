#!/bin/python 
import time
import sys
from rich.progress import Progress
if len(sys.argv)==1:
    print("Please pass argument")
    exit()

def timer(x):
    with Progress() as progress:

        task1 = progress.add_task("[green]Timer...", total=x)

        while not progress.finished:
            progress.update(task1, advance=0.5)
            time.sleep(0.5)

z= ['s','m','h']


x = sys.argv                            #main.py 1s best

y= sys.argv[1][-1]                      #s
argument = sys.argv[1]                  #1s
if y in z:
    timer_count=int(argument[:-1])       #1
    if y=='s':
        timer(timer_count)

    if y=='m':
        timer(timer_count*60)
    if y=='h':
        timer(timer_count*3600)

starttime= time.time()
print(starttime)
print(f"x=>{x} y=>{y} argument => {argument}")
