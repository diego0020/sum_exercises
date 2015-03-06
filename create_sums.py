import jinja2
import os
import random

os.chdir('C:/Users/da.angulo39/Desktop')

digits=8
limit = 10**digits -1

def create_sum(limit):
    s1=random.randint(0,limit)
    s2=random.randint(0,limit)
    s_base="{:9}\n{}{:8}"
    op=random.choice(('+','-'))
    if op == '-' and s2 > s1:
        s2, s1 = s1, s2 
    s_line=s_base.format(s1,op,s2)
    return s_line

s_line = create_sum(limit)

sums=(create_sum(limit) for i in xrange(7*10*7*2))
    
with open('sumas.htm') as f:
    s=f.read()
t=jinja2.Template(s)
with open('sumas.htm') as f:
    s=f.read()
t=jinja2.Template(s)
t.render(suma=s_line)
s2=t.render(sumas=sums)
with open('sumas2.htm','w') as f:
    f.write(s2)
