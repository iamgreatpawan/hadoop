import sys
for line in sys.stdin:
	line=line.strip()
	words=line.split(',')
	
	if words[1]=='1' and len(words)>=6 and words[5].isdigit():
                print('%s\t%s'%(words[4],words[5]))
