# python

### #1 출력하기: print()

#### 출력하기

- print()는 값을 출력해주는 함수입니다.
- 입력한 메시지나 값을 출력합니다.
- 문자나 숫자 등을 출력할 수 있습니다.
- 쉼표(,)로 여러 값을 출력할 수 있습니다.
- 괄호(()) 안의 값을 출력합니다.

```python
>>> print()

>>> print('Hello world!')
Hello world!
>>> print(1)
1
>>> print([1, 2, 3])
[1, 2, 3]
```

```python
>>> print(1)
1
>>> print(1, 2, 3)
1 2 3
>>> print(1,2,3)
1 2 3
>>> print(123)
123
>>> print('python')
python
>>> print('My name is', 'Bob')
My name is Bob
```

### #2 입력하기: input()

#### 입력하기

- 실행 중 사용자의 입력을 받습니다.
- 입력 값은 항상 문자열로 받아옵니다.
- 프로그램에게 정보를 전달할 수 있습니다.
- 괄호 안에 문자열을 넣으면 프롬프트의 역할을 수행합니다.
- 입력 받은 값을 변수에 저장할 수 있습니다.

```python
>>> name = input('What is your name?')
What is your name?
```

### #3 변수와 변수이름

#### 변수

- 변수에는 값을 할당할 수 있습니다.
- 파이썬에서 =은 할당을 의미합니다.
- 할당된 값은 변할 수 있습니다.

```python
>>> my_int = 1
>>> my_str = 'Python'
>>> count = 1  # 1
>>> count = count + 1  # 2
```

- http://www.pythontutor.com/

#### 변수의 이름

- 아주 예전에는 메모리에 저장되어 있는 값을 불러오기 위해 번호를 사용했습니다.
- 번호가 많아지면서 관리가 어려워지고 숫자 대신 이름을 붙이기 시작했습니다.
- 변수의 이름은 다른 사람들과 함께 쓰기에 편한 이름으로 짓는 것이 좋습니다.
- 나 뿐만 아니라 모두가 이해할 수 있게 작성하는 것을 권장합니다.
- 글자나 밑줄 문자를 사용합니다.
- 대문자와 소문자를 구분합니다.

```python
>>> python = 1
>>> PYTHON = 2
```

- 숫자로 시작하는 이름은 쓸 수 없습니다.
- 띄어쓰기를 포함할 수 없습니다. 보통 띄어쓰기 대신 밑줄 문자를 사용합니다.
- 유니코드 방식을 사용하기 때문에 한글 변수명도 지원합니다.

```python
>>> 파이썬 = 1
>>> 김왼손 = 20
```

- 하지만 대부분의 경우 영어 변수명을 사용합니다.

### #4 기본재료 1 : 숫자형, 문자열, 불린

#### 숫자형 (Numeric)

- 숫자로 이루어진 자료형입니다.
- 정수나 실수 등을 다룰 수 있습니다.
- 숫자끼리 연산도 가능합니다.

```python
>>> my_int1 = 1
>>> my_int2 = -2
>>> my_int3 = 4096
>>> my_float1 = 1.0
>>> my_float2 = 2.0
>>> my_float3 = 3.14
```

#### 문자열 (String)

- 문자나 문자들을 늘어놓은 것입니다.
- 큰따옴표와 작은따옴표로 구분합니다.
- 리스트와 함께 시퀀스 자료형입니다.
- 작은따옴표(' ') 또는 큰따옴표(" ")로 구분합니다.

```python
>>> my_str1 = 'a'
>>> my_str2 = '3.14'
>>> my_str3 = 'coding'
>>> my_str4 = "coding"
```

#### 불린 (Boolean)

- 참(True)과 거짓(False)을 말합니다.
- 비교나 논리연산자의 결과입니다.

```python
>>> my_bool1 = True  # True
>>> my_bool2 = False  # False
>>> my_bool3 = 1 < 2  # True
>>> my_bool4 = 1 == 2  # False
```

### #5 기본재료 2 : 리스트, 튜플, 딕셔너리

#### 리스트 (List)

- 여러 값을 함께 모아서 저장합니다.
- 값을 변경할 수 있으며 순서가 있습니다.

```python
>>> my_list = []  # []
>>> my_list.append(123)  # [123]
>>> my_list.append('abc') # [123, 'abc']
>>> my_list.append(True)  # [123, 'abc', True]
```

#### 튜플 (Tuple)

- 여러 값을 함께 모아서 저장합니다.
- 값을 변경할 수 없으며 순서가 있습니다.

```python
>>> my_tuple1 = ()
>>> my_tuple2 = (1,)
>>> my_tuple3 = ('a', 'b', 'c')
>>> my_tuple4 = 3.14, 'Python', True
```

#### 딕셔너리 (Dictionary)

- 관련된 정보를 서로 연관시켜 놓은 것입니다.
- 키와 값의 쌍으로 이루어져 있습니다.

```python
>>> my_dict = {}  # {}
>>> my_dict[1] = 'a'  # {1: 'a'}
>>> my_dict['b'] = 2  # {1: 'a', 'b': 2}
>>> my_dict['c'] = 'd'  # {1: 'a', 'b': 2, 'c': 'd'}
```

### #6 자료형 변환하기

- 자료형끼리 변환할 수 있는 함수도 있습니다.
- 내장함수란 파이썬에서 기본으로 제공하는 함수를 말합니다.
- int(): 정수형으로 변환합니다.

```python
>>> print(int(3.14))
3
```

- float(): 실수형으로 변환합니다.

```python
>>> print(float(3))
3.0
```

- str(): 문자열로 변환합니다.

```python
>>> print(str(3.0))
3.0
>>> print(type(str(3.0)))
<class 'str'>
```

- list(): 리스트로 변환합니다.

```python
>>> print(list('3.0'))
['3', '.', '0']
```

### #7 주석

- 사람을 위한 설명을 메모합니다.
- 코멘트(comment)라고도 합니다.
- 컴퓨터는 주석을 무시합니다.
- \#을 사용합니다.
- 지나치게 많거나 코드와 상관없는 주석은 오히려 방해가 될 수 있습니다.

```python
>>> print('Hello Python!')  # 문자열을 출력합니다.
Hello Python!
>>> print(12345)  # 숫자를 출력합니다.
12345
>>> print(2 + 3)  # 계산결과를 출력합니다.
5
```

### #8 문자열

- 문자나 문자들을 나열한 것입니다.
- 값을 변경할 수 없으며 순서가 있습니다.
- 큰따옴표(" ")나 작은따옴표(' ')로 구분합니다.

```python
>>> my_str = 'python'
>>> print(my_str)
python
>>> type(my_str)
<class 'str'>
```

- 문자열 안에 큰따옴표나 작은따옴표를 넣고 싶을 때는 서로 다른 따옴표를 함께 씁니다.

```python
>>> print("Let's go!")
>>> print('I said, "Hello!"')
```

- 같은 따옴표를 세 번씩 쓰면 여러 줄을 표현할 수 있습니다.

```python
>>> my_str = """버스
지하철
택시
"""
```

### #9 문자열 포맷팅

- % 연산자를 이용해 문자열에 숫자, 문자열 등을 대입합니다.
- 문자열을 자유롭게 표현하는 방법입니다.

```python
>>> print('My name is %s' % 'Tom')
My name is Tom
>>> print('x = %d, y = %d' % (1, 2))
x = 1, y = 2
>>> print('%d x %d = %d' % (2, 3, 2 * 3))
2 x 3 = 6
```

- %d : 정수형 숫자를 대입할 수 있습니다.

```python
>>> print('%d %d' % (1, 2))
1 2
```

- %f : 실수형 숫자를 대입할 수 있습니다.

```python
>>> print('%f' % 3.14)
3.14
```

- %s : 문자열을 대입할 수 있습니다.

```python
>>> print('%s' % 'coding')
coding
```

### #10 format()

- 포맷팅을 수행하는 문자열의 메소드입니다.
- 중괄호 { }를 이용해 값을 대입합니다.
- % 연산자보다 파이썬스러운 방법입니다.
- 괄호 안에 숫자를 넣어 순서도 지정할 수 있습니다.

```python
>>> print('My name is %s' % 'Tom')
My name is Tom
>>> print('My name is {}'.format('Tom'))
My name is Tom
>>> print('{} x {} ={}'.format(2, 3, 2 * 3))
2 x 3 = 6
>>> print('{1} x {0} ={2}'.format(2, 3, 2 * 3))  # 괄호 안의 숫자는 순서를 지정
3 x 2 = 6
```

### #11 문자열 인덱싱

- 위치(index)를 이용해 각 문자에 접근할 수 있습니다.
- 위치는 0부터 시작합니다. 공백도 포함합니다.

```python
>>> alphabet = 'abcde'
>>> print(alphabet[0])
a
>>> print(alphabet[3])
d
>>> print(alphabet[5])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(alphabet[5])
IndexError: string index out of range
>>> my_name = '김왼손의 왼손코딩'
>>> my_name[3]
의
>>> my_name[8]
딩
```

- 음수를 인덱스로 사용할 수 있습니다.
- 가장 뒤의 값을 -1부터 해서 거꾸로 세어갑니다.

```python
>>> my_name = '김왼손의 왼손코딩'
>>> my_name[-1]
딩
```

- 리스트 자료형에서도 거의 비슷합니다.

### #12 문자열 슬라이싱

- 문자열에서 여러 값을 한꺼번에 잘라옵니다.
- 콜론(:)을 이용해 여러 값을 한꺼번에 가져올 수 있습니다.
- 기존 문자열은 그대로 두고 복사해서 사용합니다.

```python
>>> my_str = 'Hello Python!'
>>> print(my_str[0:1])
H
>>> print(my_str[0:2])
He
>>> print(my_str[3:7])
lo P
>>> my_name = '김왼손의 왼손코딩'
>>> print(my_name[5:7])
왼손
```

- 앞이나 뒤 숫자를 생략할 수도 있습니다.

```python
>>> my_name = '김왼손의 왼손코딩'
>>> my_name[:2]
김왼
>>> my_name[7:]
코딩
```

### #13 문자열 메서드

- 특정한 기능을 수행하기 위한 코드를 모아두고 이름을 붙인 것을 함수라고 합니다.
- 메서드는 특정 객체만 사용할 수 있는 함수를 말합니다.
- string.split(): 문자열을 공백 기준으로 분리하는 메서드입니다.

```python
>>> fruit_str = 'apple banana lemon'
>>> fruits = fruit_str.split()
>>> print(fruits[0])
apple
>>> print(fruits[1])
banana
>>> my_name = '김왼손의 왼손코딩'
>>> print(my_name.split())
['김왼손의', '왼손코딩']
```

### #14 독스트링

- 문서화 문자열(Documentation string)입니다.
- 함수가 어떤 일을 수행하는지 설명합니다.
- 보통 큰따옴표(" ") 세 개를 사용합니다.

```python
def 함수이름(인자1, ...):
    """함수에 대한 설명"""
    실행할 명령1
    실행할 명령2
    ...
    return 결과
```

### #15 end, 이스케이프 코드

- end: print() 함수에서 출력의 끝을 지정합니다.
- 파이썬에서는 줄 바꿈(\n)이 기본 값입니다.
- 특정한 기능을 수행하기 위해 미리 정해둔 문자 조합을 이스케이프 코드라고 합니다.

```python
>>> print(' ', end='')

>>> print('집단지성', end='/')
집단지성/
>>> print('집단지성', end='미운코딩새끼')
집단지성미운코딩새끼
```

### #16 리스트

#### 기본구조

- 여러 값을 한꺼번에 모을 수 있습니다.
- 값들은 변경할 수 있고 순서가 있습니다.
- 가변과 불변
  - 가변(mutable) : 값을 변경할 수 있습니다. 리스트, 딕셔너리 등이 해당됩니다.
  - 불변(immutable) : 값을 변경할 수 없습니다. 문자열, 튜플 등이 해당됩니다.
- 빈 리스트 만들기

```python
>>> my_list = []
[]
>>> type(my_list)
<class 'list'>
```

- 값을 가지고 있는 리스트 만들기

```python
>>> my_list = [1, 2, 3]
>>> print(my_list)
[1, 2, 3]
```

### #17 리스트 값 추가하기

- 리스트의 메서드 list.append()를 사용해서 값을 추가할 수 있습니다.

```python
>>> students = ['Tom', 'Alice', 'Sally']
>>> students.append('Betty')
>>> students.append('Angela')
>>> print(students)
['Tom', 'Alice', 'Sally', 'Betty', 'Angela']
```

- 리스트는 마치 그릇과 같습니다. 그릇이 없는 상태에서 식재료를 쏟을 수 없습니다.
- 리스트(그릇)가 없는 상태로 append()를 이용해 값을 추가할 수 없습니다.

```python
>>> humans.append('David')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    humans.append('David')
NameError: name 'humans' is not defined
```

### #18 리스트 인덱싱, 슬라이싱

- 인덱싱, 슬라이싱은 문자열의 방법과 상당히 유사합니다.
- 위치를 이용해서 값에 접근하는 것을 인덱싱이라고 합니다.

```python
>>> animals = ['코알라', '하이에나', '바다소', '땅다람쥐', '바다코끼리', '스컹크', '아나콘다']
>>> print(animals[1])
['하이에나']
```

### #19 리스트 메서드

- 리스트도 다양한 메서드를 가지고 있습니다.
- 메서드들을 외우는 건 중요하지 않습니다. 필요할 때 검색해서 사용할 수 있으면 됩니다.
- list.sort(): 리스트 안의 값을 정렬합니다.

```python
>>> animals =['코알라', '하이에나', '바다소', '땅다람쥐', '바다코끼리', '스컹크', '아나콘다']
>>> animals.sort()
>>> print(animals)
['땅다람쥐', '바다소', '바다코끼리', '스컹크', '아나콘다', '코알라', '하이에나']
```

- list.count(): 해당 값의 개수를 셉니다.

```python
>>> animals =['코알라', '하이에나', '바다소', '땅다람쥐', '바다코끼리', '스컹크', '아나콘다']
>>> print(animals.count('바다소'))
1
```

- 더 많은 리스트의 메서드를 알고 싶다면 구글에 검색해보세요.

### #20 튜플

#### 기본구조

- 튜플은 리스트와 거의 유사합니다.
- 여러 값을 한꺼번에 모을 수 있습니다.
- 값을 변경할 수 없다는 점이 리스트와 다릅니다.
- 튜플은 괄호를 쓰지 않아도 됩니다.

```python
>>> my_tuple = (1, 2, 3)
>>> type(my_tuple)
<class 'tuple'>
>>> my_tuple = 1, 2, 3
>>> type(my_tuple)
<class 'tuple'>
```

### #21 패킹, 언패킹

- 패킹(packing) : 여러 개의 값을 한꺼번에 묶는 것을 말합니다.
- 언패킹(unpacking) : 묶여 있는 값을 풀어놓는 것을 말합니다.

```python
>>> my_tuple = (1, 2, 3)
>>> num1, num2, num3 = my_tuple
>>> print(num1)
1
>>> print(num2)
2
```

- 두 변수의 값을 서로 바꿀 때도 사용할 수 있습니다.

```python
>>> num1 = 1
>>> num2 = 2
>>> num1, num2 = num2, num1
>>> print(num1)
2
>>> print(num2)
1
```

### #22 for

#### 반복문

- 반복되는 지루한 작업을 처리하기 위해 사용합니다.
- 파이썬에는 for와 while 두 가지 반복문이 있습니다.
- for는 횟수를 기준으로, while은 조건을 기준으로 반복합니다.

#### 기본구조

```python
for 변수 in 컨테이너:
    실행할 명령1
    실행할 명령2
    ...
```

- 컨테이너 안의 값을 전부 순회할 때까지 반복합니다.
- 반복하는 부분을 코드블럭이라고 합니다.
- 코드블럭을 구분하기 위해 콜론(:)과 들여쓰기를 사용합니다.

```python
animals = [땅다람쥐, 바다코끼리, 스컹크, 아나콘다, 코알라, 하이에나, 바다소]
for animal in animals:
    print(animal)

땅다람쥐
바다코끼리
스컹크
아나콘다
코알라
하이에나
바다소
for num in [1, 2, 3]:
    print(num)

1
2
3
for ch in '김왼손':
    print(ch)

김
왼
손
```

#### 들여쓰기

- 파이썬에서는 들여쓰기가 선택이 아닌 필수입니다.
- 띄어쓰기의 종류는 하나로 통일해야 합니다.
- 보통 띄어쓰기 4칸을 권장합니다.

### #23 range()

- for와 함께 자주 사용되는 내장함수입니다.
- range(stop)은 0부터 stop 전까지의 숫자를 나열합니다.
- range(start, strop)는 start부터 stop 전까지의 숫자를 나열합니다.

```python
for n in range(3):
    print(n)

0
1
2
for n in range(4, 6):
    print(n)

4
5
```

### #24 for x 2

- 반복문을 중첩해서도 사용할 수 있습니다.
- 아래는 for를 이용해 구구단 2단을 출력하는 예제입니다.

```python
for i in range(1, 10):
    print('{}x{}={}'.format(2, i, 2 * i))
```

- for를 중첩해서 사용하면 2단부터 9단까지 모두 출력할 수도 있습니다.

```python
for j in range(2, 10):
    for i in range(1, 10):
        print('{}x{}={}'.format(j, i, j * i))
```

### #25 컴프리헨션

- 리스트를 만드는 강력하고 간결한 방법입니다.
- 초보자에게는 쉽지 않을 수 있지만 많이 사용됩니다.
- 주어진 리스트에서 홀수만 뽑아내는 코드를 작성해봅시다.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = []

for number in numbers:
    if number % 2 == 1:  # 2로 나눴을 때 1이 남으면 홀수입니다.
        odd_numbers.append(number)
```

- 다음은 컴프리헨션을 이용한 방법입니다.

```python
>>> odd_numbers = [number for number in numbers if number % 2 == 1]
```

### #26 할당 연산자

- 수학에서 =는 같다는 뜻입니다.
- 파이썬에서 =은 할당 연산자입니다.
- 오른쪽의 값을 왼쪽의 변수에 할당합니다.

```python
>>> my_int = 1
>>> my_float = 2.0
>>> my_list = []
```

- +=와 같은 것들을 복합 할당 연산자라고 합니다.

```python
>>> count = 0
>>> count = count + 1
>>> print(count)
1
>>> count += 1  # count = count + 1과 같습니다.
>>> print(count)
2
```

### #27 산술 연산자

- 숫자끼리 연산을 할 수 있게 하는 연산자입니다.
- 아래와 같이 더하기, 빼기, 곱하기, 나누기를 할 수 있습니다.

```python
>>> print(3 + 3)
6
>>> print(20 - 5)
15
>>> print(6 * 2)
12
>>> print(12 / 3)
4.0
```

- 아래는 특수 연산자입니다.

```python
>>> print(3 ** 2)  # 3의 2제곱
9
>>> print(4 ** 3)  # 4의 3제곱
64
>>> print(7 / 3)  # 7 나누기 3
2.3333333333333335
>>> print(7 // 3)  # 7 나누기 3의 몫
2
>>> print(7 % 3)  # 7 나누기 3의 나머지
1
```

### #28 %로 홀짝 구분하기

- %의 경우에는 홀수, 짝수의 구분에도 사용할 수 있습니다.
- 아래 코드는 %를 이용해 홀짝 구분을 하는 코드입니다.

```python
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number % 2 == 1:
        print(number, ': 홀수')
    else:
        print(number, ': 짝수')

1 : 홀수
2 : 짝수
3 : 홀수
4 : 짝수
5 : 홀수
6 : 짝수
7 : 홀수
```

### #29 문자열 연산자

- 문자열에도 연산자가 있습니다.
- \+ : 문자열끼리 연결합니다.

```python
>>> print('김왼손'+ 'X' + '집단지성들')
김왼손X집단지성들
>>> print('안녕하세요' + ' ' + '반갑습니다')
안녕하세요 반갑습니다
```

- \* : 문자열을 해당 수만큼 반복합니다.

```python
>>> print('안녕' * 3)
안녕안녕안녕
>>> print('안녕 ' * 5)
안녕 안녕 안녕 안녕 안녕 
```

### #30 비교 연산자

- 말 그대로 비교를 할 때 사용 되는 연산자입니다.
- 비교의 결과는 참(True)과 거짓(False)입니다.
- == : 왼쪽과 오른쪽이 같은 지 비교
- != : 왼쪽과 오른쪽이 다른 지 비교
- \> : 왼쪽이 더 큰 지 비교
- < : 오른쪽이 더 큰 지 비교
- \>= : 왼쪽이 더 크거나 같은 지 비교
- <= : 오른쪽이 더 크거나 같은 지 비교

```python
>>> print(1 < 2)
True
>>> print(1 > 2)
False
>>> print(1 == 1)
True
>>> print(1 != 1)
False
>>> print(4 <= 6)
True
>>> print(5 <= 5)
True
```

### #31 논리 연산자

- 파이썬의 논리 연산자에는 and, or, not이 있습니다.
- and : 둘 다 True일 때에만 True
- or : 한 쪽이라도 True면 True
- not : True면 False, False면 True

```python
>>> print(True)
True
>>> print(False)
False
>>> print(True and True)
True
>>> print(True and False)
False
>>> print(False and True)
False
>>> print(False and False)
False
>>> print(True or True)
True
>>> print(True or False)
True
>>> print(False or True)
True
>>> print(False or False)
False
>>> print(not False)
True
>>> print(not True)
False
```

- 놀이동산의 청룡 열차를 타기 위해서는 키와 나이 제한을 넘겨야 합니다.
- 키가 140cm 이상이면서 나이도 10살 이상이어야 청룡 열차를 탈 수 있다고 해봅시다.
- 일단 키도 120cm 이하면서 나이가 8살이면 결과는 어떻게 될까요?
- 키와 나이 조건 모두 False이기 때문에 결과는 False입니다.

```python
>>> my_height = 120
>>> my_age = 8
>>> print(my_height > 140 and my_age > 10)
False
```

- 키가 190cm이면서 나이가 9살이면 어떨까요?
- 키 조건은 True이지만 나이 조건은 False이므로 결과는 False입니다.

```python
>>> my_height = 190
>>> my_age = 9
>>> print(my_height  > 140 and my_age > 10)
False
```

- 키가 150cm이면서 나이가 32살이면 어떨까요?
- 키와 나이 조건 모두 True이므로 결과는 True입니다.

```python
>>> my_height = 150
>>> my_age = 32
>>> print(my_height > 140 and my_age > 10)
True
```

### #32 멤버쉽 연산자

- 리스트, 튜플 등의 안에 해당 값이 있는 지 확인합니다.
- in과 not in 키워드를 사용합니다.

```python
>>> fruits = ['사과', '딸기', '망고', '브로콜리', '바나나']
>>> print(fruits)
['사과', '딸기', '망고', '브로콜리', '바나나']
>>> print('딸기' in fruits)
True
>>> print('딸기' not in fruits)
False
>>> print('상추' in fruits)
False
>>> print('상추' not in fruits)
True
```

### #33 if

```python
if 조건:
    실행할 명령1
    실행할 명령2
    ...
```

- 조건이 참인지 거짓인지 판단합니다.
- 조건에 따라 처리의 흐름을 바꿉니다.
- if 키워드를 사용합니다.
  - 참일 경우 코드블럭을 실행합니다.
  - 거짓일 경우 코드블럭을 넘어갑니다.

```python
name = 'Edwin'
if name == 'Edwin':
    print('당신이 Edwin이군요.')
    print('만나서 반가워요 Edwin.')

당신이 Edwin이군요.
만나서 반가워요 Edwin
```

### #34 else, elif

```python
if 조건:
    실행할 명령1
    실행할 명령2
else:
    실행할 명령3
    실행할 명령4
```

- if와 함께 사용할 수 있는 친구들입니다.
- else: 이전의 if나 elif가 모두 거짓일 경우 else로 넘어갑니다.

```python
name = 'Bob'
if name == 'Alice':
    print('당신이 Ailce이군요.')
else:
    print('아니 당신은!?')

아니 당신은!?
```

- elif : 이전의 if나 elif가 거짓일 경우 elif의 조건문으로 넘어갑니다.

```python
if 조건:
    실행할 명령1
    실행할 명령2
elif 조건:
    실행할 명령3
    실행할 명령4
name = 'Bob'
if name == 'Alice':
    print('당신이 Ailce이군요.')
elif name == 'Bob':
    print('당신이 Bob이군요.')
else:
    print('아니 당신은!?')

당신이 Bob이군요.
```

### #35 while

```python
while 조건:
    실행할 문장 1
    실행할 문장 2
    ...
```

- 반복문은 반복되는 지루한 작업을 처리합니다.
- 코드의 양이 줄어들고 읽기 쉬워집니다.
- while은 조건을 기준으로 반복합니다.

```python
count = 0
whlie count < 3:
    print('횟수: ', count)
    count += 1

횟수: 0
횟수: 1
횟수: 2
```

### #36 continue, break

- continue : 다시 조건으로 돌아갑니다.
- break : 반복문을 끝내 버립니다.

```python
count = 0
while count < 10:
    count += 1
    if count < 4:
        continue
    if count == 8:
        break
```

### #37 딕셔너리

```python
{key1: value1, key2: value2, key3: value3 ...}
```

- 딕셔너리를 말 그대로 해석하면 사전입니다.
- 키(key)와 값(value)을 쌍으로 갖는 자료형입니다.
- 리스트와의 차이점은 관련된 정보를 연관시킨다는 것입니다.
- 리스트는 값을 다루기 위해 인덱스를 사용하지만 딕셔너리는 키를 사용합니다.

```python
>>> my_dict = {}  # {}
>>> my_dict[1] = 'a'  # {1: 'a'}
>>> my_dict['b'] = 2  # {1: 'a', 'b': 2}
>>> my_dict['c'] = 'd'  # {1: 'a', 'b': 2, 'c': 'd'}
```

### #38 딕셔너리 메서드

- 메서드는 특정 객체만 사용할 수 있는 함수를 말합니다.
- 아래는 딕셔너리가 사용할 수 있는 메서드들입니다.
- dict.values(): 딕셔너리에서 값만 뽑아 돌려줍니다.

```python
students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
for student in students.values():
    print(student)

Tom
Sally
Betty
```

- dict.keys(): 딕셔너리에서 키만 뽑아 돌려줍니다.

```python
students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
for key in students.keys():
    print(key)

학생1
학생2
학생3
```

- dict.items(): 딕셔너리에서 키와 값 쌍을 뽑아 돌려줍니다.

```python
students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
for key, val in students.items():
    print(key, val)

학생1 Tom
학생2 Sally
학생3 Betty
```

### #39 함수

- 수학에도 함수가 있고, 엑셀에도 함수가 있습니다.
- 우리가 사용해왔던 print(), input() 등도 모두 함수입니다.
- 반복되는 코드에 이름을 붙여서 다시 사용할 수 있게 합니다.
- 필요할 때 함수의 이름을 불러서 사용할 수 있습니다.
- 통나무가 마술모자에 들어가면 마술빗자루가 나옵니다.
- 이와 유사하게 입력 값이 함수에 들어가면 출력 값이 나옵니다.

```python
def 함수이름(인자1, ...):
    실행할 명령1
    실행할 명령2
    ...
    return 결과
```

- 함수에게 전달하는 값을 인자 혹은 매개변수라고 합니다.
- 굳이 따지자면 다른 용어이지만 보통 혼용해서 사용합니다.
- 함수에게 받아오는 값을 리턴 값, 반환 값, 결과 값이라고 합니다.
- 마치 내가 함수와 함께 캐치볼을 하는 것과 같습니다.
- 인자와 결과 값은 있을 수도 있고 없을 수도 있습니다.

### #40 함수를 사용하는 이유

- 다시 사용할 수 있습니다.
- 코드를 관리하기 쉬워집니다.
- 조립해서 사용할 수 있습니다.

### #41 여러개 돌려주기

- 콤마(,)를 사용해서 여러 개의 값을 돌려받을 수 있습니다.
- 여러 개를 돌려줄 때는 하나의 튜플로 묶어서 전달합니다.

```python
def add_mul(num1, num2):
    return num1 + num2, num1 * num2

my_add, my_mul = add_mul(1, 2)  # 3, 2
```

### #42 모듈

- 비슷한 기능의 함수들을 모아둔 파일입니다.
- 직접 만들 수도 있고 가져와서 사용할 수도 있습니다.
- import 키워드로 모듈을 가져옵니다.
- 마침표(.)를 이용해 함수를 사용합니다.

```python
import 모듈이름
```

- 제품을 구매했을 때 배터리가 포함되어 있어 따로 구매할 필요가 없는 경우가 있습니다.
- 파이썬은 제공하는 라이브러리들이 많아서 구현할 필요 없이 바로 가져다 쓸 수 있습니다.
- 보통 이런 라이브러리들은 충분히 되어 있을 확률이 높습니다.

### #43 랜덤

- 난수를 만들거나 무작위와 관련된 함수를 포함합니다.
- 아래 random 모듈이 포함하고 있는 함수들입니다.
- random.choice(): 리스트의 값 중 하나를 랜덤하게 선택합니다.

```
>>> import random
>>> students = ['Tom', 'Sally', 'Betty', 'Eric', 'Angela', 'Stephany'] 
>>> print(random.choice(students))
Betty
>>> print(random.choice(students))
Eric
>>> print(random.choice(students))
Tom
```

- random.sample(): 리스트의 값 중에서 지정한 개수만큼 랜덤하게 선택합니다.

```
import random
fruits = ['apple', 'banana', 'lemon']
my_fruit = random.sample(fruits, 2)
print(my_fruit) # ['apple', 'banana'] or ['banana', 'lemon'] or ...
```

- random.randint(): 특정 범위의 정수 중 하나를 랜덤하게 선택합니다.

```
import random
my_int = random.randint(0, 10)
print(my_int)  # 0~10
```

### #44 객체

- 현실의 물건, 물체, 사물을 컴퓨터 안에 재현하는 것입니다.
- 함수와 데이터를 한꺼번에 묶어둔 것을 말합니다.
- 파이썬에서는 대부분의 것들이 객체입니다.
- 통기타 객체
  - 데이터: 이름, 색깔, 종류
  - 함수: 핑거스타일로 연주하기, 스트럼으로 연주하기
- 게임 속 용사 객체
  - 데이터: 성별, 이름, 레벨
  - 함수: 앞으로 가기, 때리기, 점프 뛰기
- http://pythontutor.com/

### #45 코딩 스타일

#### PEP8

- 코드를 작성하다 보면 나보다 다른 사람들이 보는 경우가 더 많습니다.
- 일관된 기준을 가지고 코드를 작성하면 다른 사람들과의 협업에 도움이 됩니다.
- PEP8은 파이썬 제작자인 귀도 반 로썸이 제안하는 코딩 스타일 가이드입니다.
  - 원본 : https://www.python.org/dev/peps/pep-0008/
  - 번역본 : https://b.luavis.kr/python/python-convention
- 코드를 일관성 있게 작성할 수 있게 하는 기준이자 약속입니다.
- 하지만 무리하게 일관성을 지키는 것은 별로 현명한 행동이 아닙니다.