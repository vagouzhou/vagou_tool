import subprocess
import sys

def otool(s):
    o = subprocess.Popen(['/usr/bin/otool', '-L', s], stdout=subprocess.PIPE)
    for l in o.stdout:
        if l[0] == '\t':
            yield l.split(' ', 1)[0][1:]

need = set([sys.argv[1]])
done = set()

while need:
    needed = set(need)
    need = set()
    for f in needed:
        print f + "="
        need.update(otool(f))
        print "<<<" + repr(need) + ">>>" + "\r\n"
    done.update(needed)
    need.difference_update(done)

for f in sorted(done):
    print f
