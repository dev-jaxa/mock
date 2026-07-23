# 1 - vazifa

# lst = [[10, 20], [40], [30, 56, 25], [10, 20], [33]]
# natija = []
# for element in lst:
#     if element not in natija:
#         natija.append(element)
# print(natija)

# 2 - vazifa

# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]
# C = [[A[i][j] + B[i][j] for j in range(len(A[i]))] for i in range(len(A))]
# print(C)

# 3 - vazifa


# def count_passing_students(grades: list[int], passingGrade: int) -> int:
#     return sum(element >= passingGrade for element in grades)


# grades = [45, 60, 75, 30, 90]
# passingGrade = 60
# print(count_passing_students(grades, passingGrade))


# 4 - vazifa


# def ends_with_gram(words: list[str]) -> list[str]:
#     return list(element for element in words if element.lower().endswith("gram"))


# words = ["telegram", "Instagram", "hello", "program", "diagram", "world"]
# print(ends_with_gram(words))


# 5 - vazifa


# def get_phone_number(contacts: dict[str, str], search_name: str) -> str:
#     for name in contacts:
#         if name.lower() == search_name.lower():
#             return contacts[name]
#     return "Topilmadi"


# contacts = {"Ali": "+998901112233", "Vali": "+998909998877", "Hasan": "+998938889900"}
# search_name = "Vali"
# print(get_phone_number(contacts, search_name))
