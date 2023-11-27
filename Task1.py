from random import randint

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        middle = nums[int(len(nums)/2)]
        left_nums = []
        middle_nums = []
        right_nums = []
        for n in nums:
            if n < middle:
                left_nums.append(n)
            elif n > middle:
                right_nums.append(n)
            else:
                middle_nums.append(n)
        return quick_sort(left_nums) + middle_nums + quick_sort(right_nums)

list_length = int(input('Введите размер массива: '))
numbers_list = []                #создаём и заполняем рандомными целыми числами от -10 до 10 список длины listLength
for i in range(list_length):
    numbers_list.append(randint(-10, 10))    
print('Сгенерированный массив: ', numbers_list)
print('Отсортированный массив: ', quick_sort(numbers_list))