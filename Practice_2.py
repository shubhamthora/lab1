def countLines(name):
    with open(name, 'r') as file:
        lines = file.readlines()
        return len(lines)

def countChars(name):
    with open(name, 'r') as file:
        data = file.read()
        return len(data)

def test(name):
    lines = countLines(name)
    chars = countChars(name)
    print(f"{name} contains {lines} lines and {chars} characters.")




import mymod
mymod.countLines('example.txt')

mymod.countChars('example.txt')

mymod.test('example.txt')

