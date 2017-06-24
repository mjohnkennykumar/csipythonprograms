from sklearn import tree
#features=[[230,"smooth"],[220,"smooth"],[170,"rough"],[150,"rough"]]
#labels=["apple", "apple", "orange", "orange"]
features=[[230,0],[220,0],[170,1],[150,1]]
labels=[0, 0, 1, 1]
clf=tree.DecisionTreeClassifier();
clf=clf.fit(features,labels);
print(clf.predict([[170,0]]));