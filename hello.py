print(1)
print(1+2)

print(~~~5)

def demo_string():
    stra = '   \n\rhello welcome\r\n'
    strb = 'hello usst'
    print(1,stra.lstrip())
    print(2,stra.rstrip())
    for str in strb.split(' '):
        print(str)
    print(3,strb.startswith('h'))
    print(4,strb.endswith('x'))

if __name__ == '__main__':
    demo_string()