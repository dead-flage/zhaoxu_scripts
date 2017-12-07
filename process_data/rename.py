import os
import glob
import argparse


def rename(path):
    list=os.listdir(path)
    for i in list:
		new_name=i.split('_')[0]
		os.rename(path+os.sep+i,path+os.sep+new_name)
		#print i
		print new_name


if __name__ == '__main__':
		path='D:\Share\data\json'
		rename(path)


