import re
filename = '../syllabi/sample1.txt'
def findMidterm(filename):
	Day = ['Mon','Tue','Wed','Thur','Fri']
	Month = ['Jan','January','Feb','February','Mar','March','Apr','April','May','June','July','Aug','August','Sep','September','Oct','October','Nov','November','Dec','December']
	keyword = ['Midterm','midterm','final','Final','Exam','exam']
	f = open(filename,'r')
	line = f.readline()

	month_set = set(Month)
	keyword_set = set(keyword)

	already_read_midterm1 = False
	already_read_midterm2 = False
	already_read_final = False

	Month_buffer = ''
	Date_buffer = ''

	while(line!=''):
		split_line = re.split('\W+',line)
		split_line_set = set(split_line)



		if(keyword_set.intersection(split_line_set)):
			#print(line)
			if((re.search('[0-9]',line))==None):
				line = f.readline()
				continue
			result = ''
			for j in range(0,len(split_line)):
				if(split_line[j] in keyword):
					result = result + split_line[j] + ' '
				if(split_line[j] in Month):
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
