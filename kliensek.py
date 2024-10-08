kliensek=[]
with open('kliensek.txt','r',encoding='utf-8') as forras, \
    open('kliensek_api.txt','w',encoding='utf-8') as cel:
    kliensi=forras.readline()
    for sor in forras:
            adat=sor.strip().split(',')
            klien={'nev':adat[0],'ipcim':adat[1],'mac-cim':adat[2],'interfesz':adat[3]}
            kliensek.append(klien)
            print(klien,file=cel)
print(f'{kliensek}')