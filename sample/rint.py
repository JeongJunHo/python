from sklearn import svm

# xor 계산 데이터 실습
clf = svm.SVC()
# clf.fit(데이터, 답)
clf.fit(
    [
        [0,0],
        [1,0],
        [0,1],
        [1,1]
    ],
    [0,1,1,0]
)
results = clf.predict([
    [0,0],
    [1,0]
])
print(results)