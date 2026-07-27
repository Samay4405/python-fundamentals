# # 1)

# lst = [1, 2, 3, 4, 5, 6]

# new_lst = []

# for x in lst:
#     if x % 2 != 0:
#         new_lst.append(x)

# print(new_lst)

# # 2)

# lst = [1, 2, 3, 4, 5, 6]

# for x in lst[:]:        # lst[:] creates a copy
#     if x % 2 == 0:
#         lst.remove(x)

# print(lst)

# # 3)

# lst = [1, 2, 3, 4, 5, 6]

# lst = [x for x in lst if x % 2 != 0]

# print(lst)

IST = [1,22,52,14,3,5,88,7,65,5,0,45,6,3]

X_IST = []

for x in IST:
    if x < 10:
        X_IST.append(x)
        
print(X_IST)
    
    
A️⃣ Reverse a list manually (no built-in methods)


B️⃣ Find second largest element safely
C️⃣ Remove duplicates while preserving order