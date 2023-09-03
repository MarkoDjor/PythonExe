vremes = float(input( "How long did it take for a run?:"))

n = 0

sum_vreme = 0

while vremes != "":

    vreme = float(vremes)

    n = n + 1

    sum_vreme += vreme

    vremes = input( "How long did it take for a run?:")

srednje = sum_vreme/n

print( f"Average time is {srednje:0.2f} from {n} runs")