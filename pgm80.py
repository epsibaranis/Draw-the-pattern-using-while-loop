# -*- coding: utf-8 -*-
"""
pgm no 80
Created on Mon Dec 27 17:39:16 2021
draw the Pattern
@author: tt
"""
c=0
q=1
n=6
while c<=5:
          x=0
          while x<q:
                   print(' ',end='')
                   x=x+1
          s=0
          while s<n:
                   print('*',end='')
                   s=s+1
          print()
          q=q+1
          n=n-1
          c=c+1