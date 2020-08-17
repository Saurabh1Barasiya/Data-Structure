def display(array,size):
    for i in array:
        print(i,end=' ')

def array_deletion(array,size,element):
    try:
        array.remove(element)
        return 1
    except ValueError:
        print(f"The value {element} is not present in the array ")
if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6] 
    element = 6
    size = len(array)
    val = array_deletion(array, size ,element)
    if val == 1:
        size = size - 1
        print(f"Deletion successful  array size is {size}")
        display(array,size)
