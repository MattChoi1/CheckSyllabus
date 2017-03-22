import re
filename = '../syllabi/sample2.txt'
def findMidterm(filename):
	Day = ['Mon','Tue','Wed','Thur','Fri']
	Month = ['Jan','January','Feb','February','Mar','March','Apr','April','May','June','July','Aug','August','Sep','September','Oct','October','Nov','November','Dec','December']
	keyword = ['Midterm','midterm','final','Final','Exam','exam']
	f = open(filename,'r')
	line = f.readline()
	concateMonth = ''.join(Month)
	month_set = set(Month)
	keyword_set = set(keyword)
	while(line!=''):	
			
		split_line = re.split('\W+',line)
		split_line_set = set(split_line)
		if(keyword_set.intersection(split_line_set)):
			if((re.search('[0-9]',line))==None):
				line = f.readline()
				continue
			
			result = ''
			for j in range(0,len(split_line_set)):
				if(len(split_line_set)==0):
					line = f.readline
					continue
				curr = split_line_set.pop()
				if(curr in keyword):
					result = result + curr + ' '

				while(len(split_line_set)!=0):
					curr = split_line_set.pop()
					print(curr)
					if(curr in month_set):
						result = result + curr + ' '
						if(len(split_line_set) != 0):
							curr = split_line_set.pop()
							if(curr.isdigit()):
								result += curr 
								print(result)
				line = f.readline()
				continue
		line = f.readline()

	f.close()
