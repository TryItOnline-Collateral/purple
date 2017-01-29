#!/usr/bin/python2

A=__import__
s=A("sys")
d=A("collections").defaultdict
class Purple:
 def __init__(m,f):
  m.v=d(int);m.g=map(ord,"abi1oAB");
  for c in m.g:m.v[c]=0;m.v[49]=1
  try:o=open(f,"r");m.c=d(int,enumerate(map(ord,list(o.read()))));o.close()
  except IOError:print"File %s not found."%f;s.exit(1)
g=lambda h,y:ord(s.stdin.read(1))if y==111 else[h.v[y],h.c[h.v[y+32]]][0<y-64<3]
def run(h):
 while all([h.c[h.v[105]+x]in h.g for x in 0,1,2]):i=h.v[105];x=h.c[i];v=g(h,h.c[i+1])-g(h,h.c[i+2]);exec(["h.c[h.v[x+32]]=v","if 0<=v<256:s.stdout.write(chr(v))","h.c[i+3]=0","","h.v[x]=v","h.v[x]=v"][(x-3+x%2)%9]);h.v[105]+=3
if __name__=="__main__":
 if len(s.argv)<2:print"No filename to execute."
 else:run(Purple(s.argv[1]))
