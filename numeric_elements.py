listn = [22,18,34,55,11,78,99]

#listn_s = sorted(listn)

listn.sort()

print( f'This is sorted in usual order {listn}')

listn.sort(reverse=True)

print( f'This list is sorted in reverse order {listn}')

listnew = list( reversed( listn ) )

print( f'This list is sorted in reverse order {listnew}')
