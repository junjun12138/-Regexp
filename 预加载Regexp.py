import re
lst = re.findall(r"\d+","1100,发表危害我的004")
print(lst)

lse = re.finditer(r"\d+","1133,翠收到了儿科绿色034")
print(lse)
for i in lse:
    print(i.group())
print("--------------------------")
les = re.search(r"\d+","hsd好地方额332，骄傲了的993")
print(les)
print("--------------------------")
lles = re.match(r"\d+","999 ,try to apply 1111")
print(lles)
print("--------------------------")
#预加载正则表达式对象
Obj = re.compile(r"\d+")
le = Obj.findall("笨蛋22，涵涵234")
lee = Obj.finditer("改动44，ww33")
leee = Obj.search("iij33,442vv")
leeee = Obj.match("99,222")
print(le,lee,leee,leeee)


