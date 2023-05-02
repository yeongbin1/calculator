def add(x, y):
    return x + 1y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return x / y

print("사칙연산을 선택하세요.")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")

while True:
    choice = input("선택하세요(1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        break
    else:
        print("잘못된 선택입니다. 다시 입력해주세요.")

while True:
    num1 = input("첫 번째 숫자를 입력하세요: ")
    if num1.isnumeric():
        num1 = float(num1)
        break
    else:
        print("숫자를 입력해주세요.")

while True:
    num2 = input("두 번째 숫자를 입력하세요: ")
    if num2.isnumeric():
        num2 = float(num2)
        break
    else:
        print("숫자를 입력해주세요.")

if choice == '1':
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")

elif choice == '2':
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")

elif choice == '3':
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")

elif choice == '4':
    try:
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    except ValueError as e:
        print(e)

else:
    print("잘못된 선택입니다.")