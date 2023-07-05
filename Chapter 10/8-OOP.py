class Sample:
    a = "ARJUN"

obj = Sample()
obj.a = "VOEO"

print(Sample.a)
print(obj.a)

# Sample.a = "VOEO" # To change class attribute



class See:
    def __init__(slf, name):  # slf ki jagah kuch bhi daal sakte ho
        slf.name = name
    
obj = See("ARJUU")
print(obj.name)