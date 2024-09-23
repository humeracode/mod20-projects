def calculate_product(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# Example usage
nums = (4, 3, 2, 2, -1, 18)
print("Original Tuple:", nums)
print("Product of all numbers in the tuple:", calculate_product(nums))
