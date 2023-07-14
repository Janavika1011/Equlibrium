def find_equilibrium_index(A):
    n = len(A)
    total_sum = sum(A)
    left_sum = 0
    right_sum = total_sum
    for i in range(n):
        right_sum -= A[i]
        if left_sum == right_sum:
            return i
        left_sum += A[i]
        return -1
arr = list(map(int,input("Enter: ").split()))
equilibrium_index = find_equilibrium_index(arr)
print(equilibrium_index)
