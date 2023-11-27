from random import randint

def longest_sequence(num_list, difference):
    old_result_list = []
    end_result_list = [num_list[0]]
    end_list_start_index = 0
    index = 1
    max_length = 0
    while index<len(num_list):
        if num_list[index]<=num_list[index-1] and abs(num_list[index]-num_list[index-1])<=difference:
            end_result_list.append(num_list[index])
            index+=1
            continue
        else:
            if len(end_result_list)>=len(old_result_list) or abs(num_list[index]-num_list[index-1])>difference:
                if len(end_result_list)>=len(old_result_list):
                    end_list_start_index = index - len(old_result_list)
                    old_result_list = end_result_list
            end_result_list = [num_list[index]]
            index+=1
            continue    
    print('Последняя (!) из наибольших невозрастающих последовательностей с различием', difference, ': ', old_result_list, ' (начинается с ', end_list_start_index, '-го элемента стартового массива)')
    return old_result_list

list_length = int(input('Введите размер массива: '))
numbers_list = []                #создаём и заполняем рандомными целыми числами от -10 до 10 список длины listLength
for i in range(list_length):
    numbers_list.append(randint(-10, 10))    
print('Сгенерированный массив: ', numbers_list)
difference = int(input('Введите (зафиксируйте) различие между элементами в подпоследовательности: '))
print(longest_sequence(numbers_list, difference))