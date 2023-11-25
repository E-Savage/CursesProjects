import curses as cur 
cur.setupterm('xterm') 
bold = cur.getstr('bold').decode('ascii') 
cls = cur.getstr('clear').decode('ascii') 
normal = cur.getstr('sgr0').decode('ascii') 
print(cls) 
name = input("Hello, what's your name? ") 
print("Nice to meet you ", bold, name, normal) 
input("\nHit enter to exit")
