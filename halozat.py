halozatok=[]
with open('hálózat.txt','r',encoding='utf-8') as forras, \
    open('halozatok_api.txt','w',encoding='utf-8') as cel:
    halozati=forras.readline()
    for sor in forras:
            adat=sor.strip().split(',')
            hali={'nev/interfesz':adat[0],'ipcim':adat[1]}
            halozatok.append(hali)
            print(hali,file=cel)
print(f'{halozatok}')