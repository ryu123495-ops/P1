def add(a,b) : 
    print(a+b)

add(5,7)
add(111, 222)


def mux(c,b) : 
    print(c*b)

mux(5,7)

def divide(a,b) : 
    print(a/b)
    print("나누기 끝!")

divide(11,2)

def add(a,b) : 
    return a+b

result = add(5,7)

print(result)


import random
random_num = random.random()

print(random_num)


if random_num > 0.6 : 
    print("0.6보다 큽니다.")
elif 0.4 < random_num < 0.6 :
    print("0.4~6입니다.")
else :
    print("0.4보다 작습니다.")


my_portfolio = [[1,2,3],"삼성전자", "SK하이닉스", "google", "tesla", "apple"]

print(my_portfolio[0][1])

for item in my_portfolio : 
    print(item)

a_person = {
    "name" : "홍길동",
    "age" : 20,
    "address" : "서울시 강남구",
    "phone" : "010-1234-5678"
}

b_person = {
    "name" : "엘리스", 
    "age" : 25,
    "job" : "student",
    "nationality" : ["Korean", "america"]
}

print(a_person["name"])
print(b_person["nationality"])