def FA(s):
    if len(s)<3:
        return "Rejected"
    if s[0]=='1':
        if s[1]=='0':
            if s[2]=='1':
                for i in range(3,len(s)):
                    if s[i]!='1':
                        return "Rejected"
                return "Accepted" 
            return "Rejected" 
        return "Rejected" 
    return "Rejected" 
inputs=['1','10101','101','10111','01010','100','','10111101','1011111']
for i in inputs:
    print(FA(i))
