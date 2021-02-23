point_dic = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
trans_dic = {0:(-1,-2),1:(-2,-1),2:(2,-1),3:(1,-2),4:(-2,1),5:(-1,2),6:(1,2),7:(2,1)}
inp=input()
pos=(point_dic[inp[0]], int(inp[1]))
count=0
for i in trans_dic.values():
    if 1<=pos[0]+i[0]<=8 and 1<=pos[1]+i[1]<=8:
        count+=1
print(count)