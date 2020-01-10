# n2000 = int(input("Enter number of 2000 notes = "))
# n500 = int(input("Enter number of 500 notes = "))
# n100 = int(input("Enter number of 100 notes = "))

amo = int(input("Enter Amount = "))

temp=0
p2000=0
p500=0
p100=0
f100=0
f500=0
f2000=0
# if amo>=2000:
#     p2000 = int(amo/2000)
#     if n2000<p2000:
#         p2000 = n2000
#     amo = amo-(p2000*2000)
# if amo>=500:
#     p500 = int(amo/500)
#     if n500<p500:
#         p500 = n500
#     amo = amo-(p500*500)
#
# if amo>=100:
#     p100 = int(amo/100)
#     if n100<p100:
#         p100 = n100
#     amo = amo-(p100*100)
#
# if 0<amo<100:
#     temp=1
# if amo>=100:
#     temp=2
#
# if temp==1:
#     print("Please Enter in multiple of 100")
# elif temp==2:
#     print("No Sufficient amount in ATM")
# else:
#     print("2000={0}, 500={1}, 100={2}".format(p2000,p500,p100))

if amo>=100:
    f100=1
    amo=amo-100
if amo>=500:
    f500=1
    amo=amo-500
if amo>=2000:
    p2000 = int(amo/2000)
    amo = amo-(p2000*2000)
    f2000=f2000 + p2000
if amo>=500:
    p500 = int(amo/500)
    amo = amo-(p500*500)
    f500 = f500 + p500
if amo>=100:
    p100 = int(amo/100)
    amo = amo-(p100*100)
    f100 = f100 + p100

if amo!=0:
    temp=2

if temp==2:
    print("Invalid amount in ATM")
else:
    print("2000={0}, 500={1}, 100={2}".format(f2000,f500,f100))

