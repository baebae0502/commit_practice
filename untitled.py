# 06-1
def gugu(n) :
    result = []
    i = 1
    while i < 10 :
        result.append(i * n)
        i += 1
    return result
print(gugu(3))

# 06-2 : 3과 5의 배수 합하기
""" 
3의 배수, 5의 배수 나열하고 lcm 제외시키기.
"""
result = 0
for n in range(1, 1000) :
    if n % 3 == 0 or n % 5 == 0 :
        result += n
print(result)

# 06-3 : 게시판 페이징하기
def get_total_page(m, n) :
    if m % n == 0 :
        return m // n
    else :
        return m // n + 1
print(get_total_page(5, 10))
print(get_total_page(15, 10))
print(get_total_page(25, 10))
print(get_total_page(30, 10))

# 06-4 : 간단한 메모장 만들기
# C:/doit/ch6/memo.py

# 06-5 : 탭을 4개의 공백으로 바꾸기
# C:/doit/ch6/tabto4.py

# 06-6 : 하위 디렉터리 검색하기
# C:/doit/ch6/sub_dir_search.py

'''
추가한부분
'''
