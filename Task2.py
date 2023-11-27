from random import randint

def max_sum_sequence(nums):
    end_sum = 0
    current_sum = 0
    end_sublist = []
    current_sublist = []
    for i in range(len(nums)):
        if nums[i]>=0:
            current_sublist.append(nums[i])
            current_sum+=nums[i]
        else:
            if current_sum>end_sum:
                end_sum = current_sum
                end_sublist = current_sublist
            current_sum = 0
            current_sublist = []
    print('Подпоследовательность с наибольшей суммой: ', end_sublist, ', сумма элементов = ', end_sum)

list_length = int(input('Введите размер массива: '))
numbers_list = []                #создаём и заполняем рандомными целыми числами от -10 до 10 список длины listLength
for i in range(list_length):
    numbers_list.append(randint(-10, 10))    
print('Сгенерированный массив: ', numbers_list)
max_sum_sequence(numbers_list)