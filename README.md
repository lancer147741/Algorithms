# Algorithms


1. Binary Search
[Задачи для тренировки](https://leetcode.com/tag/binary-search/)
---
## Бинарный поиск - это алгоритм поиска элемента в отсортированном списке данных. Он работает следующим образом:

```
1.Принимает на вход отсортированный список элементов.
2.Задает начальный и конечный индекс для этого списка.
3.Находит средний индекс между начальным и конечным индексом.
4.Сравнивает элемент по среднему индексу с целевым элементом, который мы ищем.
5.Если средний элемент равен целевому элементу, поиск завершается, и возвращается индекс среднего элемента.
6.Если средний элемент меньше целевого элемента, поиск продолжается в правой половине списка, иначе в левой половине списка.
7.Повторяет шаги 3-6, сужая интервал поиска до тех пор, пока не будет найден целевой элемент или интервал сужится до нуля.
            Время - O(log n)
(Алгоритм - бинарный поиск в файле с названием Binary_Search.py)
```

[Рассмотрим данную задачу](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
Тут надо найти минимальное число в отсортированном вращенном(сдвинутом) массиве:
```
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```
---
## ***Теперь разберем код где используется бинарный поиск для этой задачи:***

Изначально определяются два указателя: left (левый) и right (правый). left указывает на начало массива (индекс 0), а right указывает на его конец (индекс len(nums) - 1).
Затем начинается цикл while, который будет выполняться до тех пор, пока левый указатель left меньше правого указателя right.
Внутри цикла находится средний индекс [mid] массива, который вычисляется как среднее арифметическое между left и right.
Затем выполняется сравнение элемента nums[mid] с элементом nums[right]. Если значение в средней точке mid больше значения в правой точке right, это означает, что минимальный элемент должен быть в правой половине массива. Поэтому левый указатель left обновляется, чтобы указывать на mid + 1.
Если nums[mid] не больше nums[right], это означает, что минимальный элемент находится в левой половине массива или средний элемент mid может быть самым минимальным. В этом случае правый указатель right обновляется, чтобы указывать на mid.
Цикл продолжает выполняться до тех пор, пока левый указатель left не станет больше или равен правому указателю right.
После завершения цикла, левый указатель left указывает на минимальный элемент в массиве, и функция возвращает nums[left], который и является минимальным элементом.


## Также рассмотрим пример из жизни для подробного обьяснения: Допустим словарь - Он отсортирован поэтому бинарный поиск будет работать :)

Представьте себе большой алфавитный словарь с тысячами слов. Если пользователь хочет найти определенное слово в этом словаре, бинарный поиск может значительно ускорить этот процесс. Вот как это может работать поэтапно:
1.(Выбор диапазона): Пользователь начинает поиск с середины словаря, разделяя его на две части. Он смотрит на слово, которое находится примерно посередине словаря.
2.(Сравнение слова): Пользователь сравнивает искомое слово с словом в середине. Если искомое слово идет раньше в алфавитной последовательности, чем слово, с которым оно сравнивается в алфавитном порядке, чем слово в середине словаря, он знает, что искомое слово должно находиться в левой половине словаря.
3.(Уточнение диапазона): Теперь пользователь оставляет только левую половину словаря и повторяет шаг 1, выбирая снова средний элемент этой половины.
4.(Повторение сравнения и сокращение диапазона): Пользователь продолжает сравнивать и уточнять диапазон до тех пор, пока не найдет искомое слово.


