f1=open("./data02.txt", "r", encoding = 'utf-8-sig') #읽기목적 파일열기
answer = []
for quest in f1 :
    if quest != "" : 
        answer.append(input(quest)+"\n")
f1.close()

f2=open("./result02.txt", "w", encoding = 'utf-8-sig') #쓰기목적 파일열기 
f2.write("[응답결과] \n")
f2.writelines(answer)
f2.close() 

print("\n[응답 결과]") 
for ele in answer :  print(ele, end="") 
