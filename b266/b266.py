# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:06:35 2022.

@author: grant
"""
# import pprint
matrixOri = []
matrixtemp = []
opra = []
row = []

while True:
    try:
        matrixOri = []
        matrixtemp = []
        opra = []
        row = []
        r, c, m = map(int, input().strip().split())
        for i in range(r):
            row = list(map(int, input().split()))
            matrixOri.append(row)
        opra = list(input().split(" "))
        opra = opra[::-1]
        for i in range(len(opra)):
            # print(f"Operation:{opra[i]}:")
            if opra[i] == "0":
                # print("旋轉")
                temp = []
                matrixtemp = []
                for j in range(len(matrixOri[0]) - 1, -1, -1):
                    for k in range(len(matrixOri)):
                        temp.append(matrixOri[k][j])
                    matrixtemp.append(temp.copy())
                    temp = []
                matrixOri = matrixtemp
                # print(*matrixOri)
            else:
                # print("翻轉")
                matrixOri.reverse()
                # for j in range(len(matrixOri)//2):
                #     matrixOri[j], matrixOri[len(
                #         matrixOri)-j-1] = matrixOri[len(matrixOri)-j-1], matrixOri[j]

                # print(*matrixOri)

        print(len(matrixOri), len(matrixOri[0]))
        # print(matrixOri)
        for i in range(len(matrixOri)):
            for j in range(len(matrixOri[0])):
                print(matrixOri[i][j], end="")
                if j != (len(matrixOri[0])-1):
                    print(' ', end="")
            print("")
        # for i in range(len(matrixOri)):
        #     print(' '.join(str(matrixOri[i])))

    except:
        break


# pprint.pprint(matrixOri)
# pprint.pprint(opra)

# while True:
#     try:
#         r, c, m = map(int, input().strip().split())
#         templst = []
#         for i in range(r):
#             templst.append(list(map(int, input().split())))
#         lst = list(map(int, input().split()))
#         for i in lst[::-1]:
#             if i == 1:
#                 templst.reverse()
#             else:
#                 anslst = []
#                 for i in range(c-1, -1, -1):
#                     anslst.append([])
#                     for j in range(r):
#                         anslst[-1].append(templst[j][i])
#                 c, r = r, c
#                 templst = anslst

#         print(r, c)
#         for i in range(r):
#             for j in range(c):
#                 print(templst[i][j], end = '')
#                 if j != c-1:
#                     print(' ', end = '')
#             if i != r-1:
#                 print()
#         print()
#     except:
#         break
