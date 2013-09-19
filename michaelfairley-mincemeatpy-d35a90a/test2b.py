__author__ = 'luiscunha'

a={'Giuseppe Omodei Sal\xc3\xa8-dynamics': 1, 'P. J. Ryan-Low': 1, 'P. J. Ryan-high': 1,'Tomi Janhunen-of': 3, 'C. M. Laprano-Noise': 1, 'J. T. Saccoman-reliable': 1}

r={}
for a,b in a.items():
    k=a.split("-")
    word=k[1].rstrip(".")
    name=k[0]
    if name not in r:
        r[name]={}
    r[name][word]=b
print(r)

filename=open('output.txt', "a")

for key, value in r.items():
    string=str(key)+":"+str(value)+"\n"
    print string
    filename.write(string)
filename.close()






