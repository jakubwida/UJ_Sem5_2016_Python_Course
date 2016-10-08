list=[111,22,3,444,55,6,777,88,9]
strlist=map(str,list)
out = [e.zfill(3) for e in strlist]
out="".join(out)
print(out)

