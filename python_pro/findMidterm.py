import re
filename = '../syllabi/sample2.txt'
def findMidterm(filename):
	Day = ['Mon','Tue','Wed','Thur','Fri']
	Month = ['Jan','January','Feb','February','Mar','March','Apr','April','May','June','July','Aug','August','Sep','September','Oct','October','Nov','November','Dec','December']
	keyword = ['Midterm','midterm','final','Final','Exam','exam']
	f = open(filename,'r')
	line = f.readline()
	concateMonth = ''.join(Month)
	while(line!=''):
		for i in range(0,len(keyword)):
			print(line)
			if(keyword[i] in line):
				if((re.search('[0-9]',line))==None):
					line = f.readline()
					continue
				split_line = re.split('\W+',line)
				result = ''
				for j in range(0,len(split_line)):
					if(split_line[j] in keyword):
							result = result + split_line[j] + ' '
					if(split_line[j] in concateMonth):
						result += split_line[j]
						result += ' '
						if(j+1>=len(split_line)):
							continue

						result += split_line[j+1]	
						print(result)
						line = f.readline()
						continue
				
		line = f.readline()

	f.close()
