preamble = """\
M48
FMAT,2
ICI,OFF
METRIC,TZ,000.000
{0}%
G90
M71
{1}M30
"""

class Excellon:
    preamble = """\nM48\nFMAT,2\nICI,OFF\nMETRIC,TZ,000.000\n{0}%\nG90\nM71\n{1}M30\n"""
    
    def __init__(self,f,holes):
        tools = sorted(holes.keys())
        p0 = "".join(["T%dC%.3f\n" % (i + 2, d) for (i, d) in enumerate(tools)])
        p1 = "".join([self.hits(i, holes[t]) for (i, t) in enumerate(tools)])
        f.write(preamble.format(p0, p1))
    
    def number(self,n):
        i = int(round(n * 1000))
        return "%03d" % i
    
    def hits(self,i,xys):
        return (("T%d\n" % (i + 2)) + 
                "".join(["X%sY%s\n" % (self.number(xy[0]), self.number(xy[1])) for xy in xys]))
