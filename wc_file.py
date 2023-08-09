file1 = "example.txt"

file2 = "howler_text.txt"

filel = [ file1 , file2 ]

fh1 = open( file1 , 'rt' )

fh2 = open( file2 , 'rt' )

fhl = [ fh1 , fh2 ]

c = 0

nlines_t = 0
nwords_t = 0
nbytes_t = 0

for fh in fhl:

    nlines = 0
    nwords = 0
    nbytes = 0

    for line in fh:

        nlines += 1
        nwords += len(line.strip().split())
        nbytes += len(line)

    print( nlines , nwords , nbytes, filel[c])

    c = c + 1

    nlines_t += nlines
    nwords_t += nwords
    nbytes_t += nbytes

print( nlines_t , nwords_t , nbytes_t , "total" )