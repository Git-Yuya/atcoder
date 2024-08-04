# 入力
S = input()

# 空文字のT
T = ""
# 文字列Sのインデックス
index = 0

# 文字列Sの始めから部分文字列を判定
while index < len(S):
    if S[index:index + 5] == "dream":
        if S[index + 5:index + 8] == "era":
            T += "dream"
            index += 5
        elif S[index + 5:index + 7] == "er":
            T += "dreamer"
            index += 7
        else:
            T += "dream"
            index += 5

    elif S[index:index + 5] == "erase":
        if S[index + 5:index + 6] == "r":
            T += "eraser"
            index += 6
        else:
            T += "erase"
            index += 5
    
    else:
        break
    
# 出力
print("YES" if S == T else "NO")




##### 別解 #####
# # 入力
# S = input()

# # 文字列Sの部分文字列を順番に気を付け空文字に置換
# S = S.replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")

# # 出力
# if s:
#     print("NO")
# else:
#     print("YES")
