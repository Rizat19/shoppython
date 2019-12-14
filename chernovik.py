f_list = []
with open('data/log.txt', 'r') as f:
     data = f.read().split('\n')
     data.pop()
     for i in data:
          a = i.split(',')
          f_list.append(a)
print(f_list[len(f_list)-1][0],f_list[len(f_list)-1][1])