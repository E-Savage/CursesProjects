import curses as cur

cur.setupterm('xterm') 
bold = cur.tigetstr('bold').decode('utf-8') 
cls = cur.tigetstr('clear').decode('ascii') 
normal = cur.tigetstr('sgr0').decode('ascii') 
print(cls) 
name = input("Hello, what's your name? ") 
print("Nice to meet you ", bold, name, normal) 
input("\nHit enter to exit")
