lst=[11,22,33,44,55,11,22,33,44]
def count (lst,X):
  return lst.count(X)
X = int(input("enter the item you want to find out : "))
print("{} has occurred {} times". format(X,count(lst,X)))