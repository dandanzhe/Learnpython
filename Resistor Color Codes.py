import math
dit={0: 'black', 1: 'brown', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green', 6: 'blue', 7: 'violet', 8: 'gray', 9: 'white'}
def encode_resistor_colors(ohms_string):
    a=ohms_string.split()[0]
    if a[-1]=='k':
        st=float(a[:-1])*1000
    elif a[-1]=='M':
        st=float(a[:-1])*1000000
    else:
        st=float(a)
    num1=int(str(st)[0])
    num2=int(str(st)[1])
    num3=math.log10(st/(num1*10+num2))
    print dit[num1]+" "+dit[num2]+" "+dit[num3]+" gold"
encode_resistor_colors("1k ohms")
encode_resistor_colors("4.7k ohms")
encode_resistor_colors("10k ohms")
encode_resistor_colors("1M ohms")