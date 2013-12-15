
# t black paint
# rings 1 cm

def c(inner_ring):
    # pi cancels out b/c 1 ml covers pi cm^2 area
    
    #return ((inner_ring + 1)**2 - inner_ring**2)
    outer_ring = inner_ring + 1
    return (outer_ring + inner_ring) * (outer_ring-inner_ring)


##infile = open(r'C:\Users\JJ Fliegelman\Downloads\a.in', 'r')
infile = open(r'C:\in.txt', 'r')
text = infile.read()
text = text.split('\n')[1:]
outfile = open(r'C:\out.txt', 'w')

case = 0
for line in text:
    r, t = map(int, line.split(' '))
    black_rings = 0
    paint_used = 0
    current_r = r
    while paint_used <= t:
        paint_used += c(current_r)
        black_rings += 1
        current_r += 2
    else:
        black_rings -= 1
    case += 1

    outfile.write('Case #{}: {}\n'.format(case, black_rings))
    print 'Case #{}: {}\n'.format(case, black_rings)

outfile.close()
