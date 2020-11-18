# python3.6
# coding: utf-8

# store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"
# store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

## Store AA pKR values and N/C-terms in dictionaries:
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
## Count the occurrence of each pKR AA in the sequence, and append N/C-terms:
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)
## Compute the net charge according to the Henderson-Hesselbach equation:
pH = 0
while pH <= 14:
    posCharge = 0
    for x in ['k', 'h', 'r']:
        posCharge += seqCount[x]*(10**pKR[x])/((10**pH)+(10**pKR[x]))
    negCharge = 0
    for x in ['y', 'c', 'd', 'e']:
        negCharge += seqCount[x]*(10**pH)/((10**pH)+(10**pKR[x]))
    netCharge = posCharge - negCharge
    print(f"{pH} {netCharge}")
    pH += 1
