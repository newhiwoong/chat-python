#AnalysisScore

import AnalysisLyrics

ReadScore=[]
#파일 받은 거 다 숫자 배열로 저장 GG
ReadAllScore=[[0]*5]
#문장 별 점수 GG
LineScore=[]

def start():
	global ReadScore
	#txt 파일 받기
	f = open("Score-record.txt", 'r')
	while True:
		line = f.readline()
		if not line: break
		ReadScore.append(line)
	f.close()
	return ReadScore

#나중에 1,2 같은 거 받아서 if else문으로 평균값만 출력할지 전체값 출력할지 고르게
def convert(): 
	global ReadScore
	global ReadAllScore
	global LineScore
	
	ReadScore = start()

	#나중에는 줄 수로 계산
	ScoreLen = len(AnalysisLyrics.start())

	#읽은 파일 줄 수 만큼 반복하면서 
	for i in range(len(ReadScore)):
		Slist = [i]*ScoreLen
		test = ReadScore[i]
		test = test.split(' ')
		#배열로 나누고 배열을 문자열로 바꿔서
		for i in range(0,ScoreLen):
			Slist[i] = int(test[i])
		#ReadAllScore에 저장
		ReadAllScore.append(Slist)

	for i in range(ScoreLen):
		### 문장 별로
		OneLine=0
		for j in range(len(ReadScore)+1):
			OneLine += ReadAllScore[j][i]
		LineScore.append(OneLine/len(ReadScore))
	return LineScore
