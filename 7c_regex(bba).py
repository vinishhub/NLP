def FA(s):
    size=0
    for i in s:
        if i=='a' or i=='b':
            size+=1
        else:
            return "Rejected"
        if size>=3:
            if s[size-3]=='b':
                if s[size-2]=='b':
                    if s[size-1]=='a':
                        return "Accepted"
                    return "Rejected"
                return "Rejected"
            return "Rejected"
    return "Rejected" 
inputs=['bba', 'ababbba', 'abba','abb', 'baba','bbb','']
for i in inputs:
    print(FA(i))
