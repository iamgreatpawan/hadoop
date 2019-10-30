import sys
current_gender=None
avg_age_m=0
avg_age_f=0
count_m=0
count_f=0
gender=None
for line in sys.stdin:
	line=line.strip()
	x=line.split('\t')
	try:
		if len(x)==2:
			gender=x[0]
			age=x[1]
			age=int(age)
			#print(gender,age)
			current_gender=gender
	except ValueError:
                continue
	if current_gender=='male':
		avg_age_m+=age
		count_m+=1
	if current_gender=='female':
		avg_age_f+=age
		count_f+=1
	
                        
			
print("Male:",avg_age_m/count_m)
print("Female:",avg_age_f/count_f)
