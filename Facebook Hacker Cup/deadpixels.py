from __future__ import division
import re

def split_string(m, k):
    return re.findall('.'*(len(k)/m), k)

class Memoize:
	def __init__ (self, f):
		self.f = f
		self.mem = {}
	def __call__(self, *args, **kwargs):
		if (args, str(kwargs)) in self.mem:
			return self.mem[args, str(kwargs)]
		else:
			tmp = self.f(*args, **kwargs)
			self.mem[args, str(kwargs)] = tmp
			return tmp


class Monitor(object):
    def __init__(self, W,H,P,Q,N,X,Y,a,b,c,d):
        #print locals()
        for varname, value in list(locals().iteritems()):
            if varname != 'self':
                setattr(self, varname, value)

        self.deadxdict = {}
        self.deadydict = {}
        self.dead_pixels = set(self._deadpixel(i) for i in range(1,N))

    def monitor_size(self):
        print "Monitor: {} W by {} H".format(self.W, self.H)

    def image_size(self):
        print "Image: {} W by {} H".format(self.P, self.Q)

    def _deadx(self, i):
        if i in self.deadxdict:
            return self.deadxdict[i]
        else:
            if i == 0:
                return self.X
            else:
                out = (self._deadx(i-1)*self.a + self._deady(i-1)*self.b + 1) % self.W
                self.deadxdict[i] = out
                return out

    def _deady(self, i):
        if i in self.deadydict:
            return self.deadydict[i]
        else:
            if i == 0:
                return self.Y
            else:
                out = (self._deadx(i-1)*self.c + self._deady(i-1)*self.d + 1) % self.W
                self.deadydict[i] = out
                return out

    def _deadpixel(self, i):
        return (self._deadx(i), self._deady(i))

    def check_if_image_shows(self, xcor, ycor):
        maxx = xcor + self.P - 1
        maxy = ycor + self.Q - 1
        print 'Image: X {}-{} Y {}-{}'.format(xcor, maxx, ycor, maxy)
        print self.dead_pixels
        for x, y in self.dead_pixels:
            if xcor <= x <= maxx and ycor <= y <= maxy:
                print 'DEAD'
                return False
        else:
            return True

    def checkall(self):
        end = 0
        for x in range(self.W - self.P + 1):
            for y in range(self.H - self.Q + 1):
                if self.check_if_image_shows(x,y):
                    end += 1
        return end

def test():
    return Monitor(*map(int,'4 4 2 2 1 0 2 1 2 3 4'.split(' ')))
    
def main():
    infile = open(r'C:/FB/input.txt', 'r')
    outfile = open(r'C:/FB/out.txt', 'w')
    lines = [x.strip() for x in infile][1:]
    for index, line in enumerate(lines):
        m = Monitor(*map(int,line.split(' ')))
        m.monitor_size()
        m.image_size()
        outfile.write('Case #{}: {}'.format(index+1, m.checkall()))
    outfile.close()
        
##    print m.dead_pixels
##    m.monitor_size()
##    m.image_size()
##    print m.checkall()

if __name__ == '__main__':
    main()
