def product_of_array_elements(n, arr):
    product = 1
    for num in arr:
        product *= num
    return product

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    if len(arr) != n:
        raise ValueError("Number of elements provided doesn't match the array size!")

    result = product_of_array_elements(n, arr)
    print(result)
