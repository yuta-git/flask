
s1 = {0, 1}
l1 = [1, 2]
t1 = (3, 4)

union = s1.union(l1, t1) # 和集合
# >> {0, 1, 2, 3, 4}

s1.update(l1, t1) # 和集合 上書き
# >> {0, 1, 2, 3, 4}

s2 = {0, 1}
l2 = [1, 2]
t2 = (3, 4)

set_difference = s2.difference(l2, t2) # 差集合("0"はs2にしか存在しない)
# >> {0}
print(set_difference)

s2.difference_update(l2, t2) # 差集合 上書き
# >> {0}

s3 = {0, 1, 2}
l3 = [1, 2, 3]
t3 = (2, 3, 4)

intersection = s3.intersection(l3, t3) # 積集合
# >> {2}

s3.intersection_update(l3, t3) #積集合 上書き
# >> {2}