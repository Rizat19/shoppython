with open('sentences.txt','r') as f:
    a=f.read()
    s=a.split()
    s.sort(key=str.casefold)
    print(s)
    
with open('ri','w',encoding='utf-8') as f1:
    for soz in s:
        f1.write(soz+'\n')







