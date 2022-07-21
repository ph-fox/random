
#By: Anikin Luke. 
# EHEH
#def random(value)->exec:(random=lambda value:''.join(list(set(str(value)))) if(int(value))else ''.join(list(set(str(value)))))
#random=lambda value:''.join(list(set(str(value)))) if(int(value))else ''.join(list(set(str(value))))

def random(value)->exec:return int(''.join(list(set(str(value))))) if(type(value) is int)else ''.join(list(set(str(value))))


#print(value(12))
x = 1234
print(random(x))
print(type(random(x)))
