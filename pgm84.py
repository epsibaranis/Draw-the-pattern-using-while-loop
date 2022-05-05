# -*- coding: utf-8 -*-
"""
84
Created on Mon Dec 27 14:31:46 2021

@author: tt
"""
c=0
n=5
q=1
r=1
while c<=5:
    s=0
    while s<n:
        print('',end=(''))
        s=s+1
        print()
    x=0
    while x<q:
        print('*',end=(''))
        q=q+1
        print()
    y=0
    while y<r:
        print('*',end=(''))
        y=y+1
        print()
    n=n-1
    q=q+1
    c=c+1
    
    