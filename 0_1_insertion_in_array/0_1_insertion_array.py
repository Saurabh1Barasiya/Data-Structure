def display(l1,size):
    print(f"Totel elements in the array is { size }")
    for i in l1:
        print(i,end=' ')

def insert_Elements(l1,size,index,element):
    l1.insert(index,element)
    return 1

if __name__ == "__main__":
    l = [10,20,40,60,70,4,2,3,7,1]    # 10 elements
    element = 100
    index = 0
    size = len(l) 
    val = insert_Elements(l, size , index,element)
    if val == 1:
        size += 1
        print("Inserton done successfully ")
        display(l, size)
