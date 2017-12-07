import  os

def go_next(path):
	file = os.listdir(path)
	a_close_num = 0
	glass_close_num = 0
	a_open_num = 0
	glass_open_num = 0
	ac =0
	ao =0
	go =0
	gc =0
	if 'a_close' in file:
		print 1
		ac = 1
		pic_list = os.list(path + os.sep + 'a_close')
		a_close_num = len(pic_list)
		
	if 'glass_close' in file:
		pic_list = os.list(path + os.sep + 'glass_close')
		glass_close_num = len(pic_list)
		gc = int(1)
	if 'a_open' in file:
		pic_list = os.list(path + os.sep + 'a_open')
		a_open_num = len(pic_list)
		ao = int(1)
	if 'glass_open' in file:
		pic_list = os.list(path + os.sep + 'glass_open')
		glass_open_num = len(pic_list)
		go = int(1)
	print ac ,ao,gc,go
	#if ac + ao + gc +go >=2:
	print  path ,'                    ', a_close_num,' ', glass_open_num,' ',a_open_num,' ',glass_open_num
	if ac + ao + gc +go <2:
		try:
			for ele in file:
				print ele
				go_next(path +os.sep +ele)
		except:
			a = 0
path = 'E:\\work\\eye_data\\source_eye_data\\data_1109\\CEs_10-25\\11-30_finished\\'
go_next(path)