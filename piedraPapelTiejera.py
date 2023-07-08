import random
import os
j=True

opciones=('piedra','papel','tijera')
def clear(turnos):
    if turnos!=0:
       os.system('Pause')
    os.system('cls')if os.name=='nt'else os.system('clear')
def tur():
    sw=True
    while sw:
        turnos=input('ingrese los puntos en disputa: ')
        if turnos.isdigit() and int(turnos)>0:
            sw=False
        else:
            print('solo numeros > 0')
    return int(turnos)
while j:
    u,b,e,p=0,0,0,0
    print('''
     _____________________________________________________
    |                PIEDRA PAPEL O TIJERA                | 
    |                                                     |
    |                        _.-._           .-.          |   
    |                      _| | | |          | |    / )   |  
    |                     | | | | |          | |   / /    |   
    |                     | | | | |          | |  / /     |   
    |        _.-.-.-.     | 1 ' 1 | ,-,   _.-| |_/ /      |         
    |       ;_|_|_|_|_    |       |/ /   ; \( \   /       |    
    |       |_|_|\__  \   |     ,-' /    |\_)\ \  |       |         
    |       |    . '  |   |    ;    |    |    )   |       | 
    |       |   (    /    |        /     |   (    /       |        
    |        \_____ /      \_____ /       \_____ /        |  
     _____________________________________________________ 
              Solo las victorias cuentan               
    ''')
    turnos=tur()  
    while turnos>0: 
        clear(turnos)  
        print(f'''     
        ________________________________________________
       |Opciones:     |1.-Piedra |2.- Papel |3.- Tijera |
        ________________________________________________     
       |Puntuacion:   |tu: {u}   VS bot: {b} |  Partidas: {p} |
        ________________________________________________
            ''')
        manobot=random.choice(opciones)   
        mano=input('        tu mano: ').lower()
        print('        ________________________________________________')
        if len(mano)>0 and mano in opciones or len(mano)>0 and int(mano) <= len(opciones)and int(mano)>0:
            if mano.isdigit():
                mano=opciones[int(mano)-1]
            print(f'''        bot: {manobot}
        ________________________________________________''')
            if mano!=manobot:
                if (manobot=='papel'and mano=='piedra') or(manobot=='tijera' and mano=='papel')or(manobot=='piedra' and mano=='tijera'):
                    print('       |               gana bot                         |')
                    print('        ________________________________________________')
                    turnos-=1
                    b+=1
                else:           
                    print('       |               ganas tu                         |')
                    print('        ________________________________________________')
                    turnos-=1
                    u+=1
            else:
                e+=1
                print('       |                     empate                     |')
                print('        ________________________________________________')
        else:
            print('       | solo se permite piedra papel o tijera          |')
            p-=1
        p+=1
    clear(0)
    print(f'''         ___________________________________________________     
        |Puntuacion:|tu: {u} VS bot: {b} empate:{e}|  Partidas: {p} |
         ___________________________________________________
            ''')
    j = True if input('          ¿quieres jugar otra vez?(s)').upper()=='S' else False
    print(j)
