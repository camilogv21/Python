class awoo:
    
    def __init__(self,cont):
        self.id = cont
                        
        
if __name__ == "__main__":
    
    
    obj = int(input("cuantos objectos quiere crear?: "))   
    a = []
    
    for i in range(1, obj+1):
        
        obej = awoo(i)
        a.append(obej)
        
    for x in a:
        print(f"objetos creados: {x.id}")
        
    print(a[0].id) 