def format_emtpy_strings(lt):
    result=[]

    for a,b,c,d in lt:
        try:
            e=a,float(b), float(c), float(d)
            result.append(e)
        except:
            if b=='':
                b=0
            else:
                b=float(b)
            if c=='':
                c=0
            else:
                c=float(c)
            if d=="":
                d=0
            else:
                d=float(d)
            e=a,b,c,d
            result.append(e)
    return result

# def list_merge(lt1,lt2):
#     counter=-1
#     for members in lt1:
#         counter+=1
#         for names in lt2:
#             if members[0]==names[0]:
#                 a=members[1]+names[1]
#                 b=members[2]+names[2]
#                 c=members[3]+names[3]
#                 e=members[0],a,b,c
#                 lt1.pop(counter)
#                 lt1.insert(counter, e)
#     return lt1
