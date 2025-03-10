n = int(input()) # 참가자의 수.
sizeList = list(map(int, input().split())) # 티셔츠 사이즈별 신청자 수.
t, p = map(int, input().split()) # 티셔츠 묶음 수, 펜의 묶음 수.

# S, M, L, XL, XXL, XXXL
# 같은 사이즈의 5장 묶음으로만 주문 가능.
# 티셔츠는 남아도 됨.부족하면 안되고 신청한 사이즈대로 나눠줘야함.
bundle = 0
for sz in sizeList:
    if sz == 0: #size가 0인 경우.
        continue
    elif sz <= t: #size가 5보다 작은 경우 +1.
        bundle += 1 
    elif sz % t == 0: #size가 5로 나누어 떨어지는 경우
        bundle += sz//t
    else: #size가 5로 나누어 떨어지지 않는 경우
        bundle += sz//t + 1

pen_bundle = n//p
pen = n%p

print(bundle)
print(pen_bundle, pen)