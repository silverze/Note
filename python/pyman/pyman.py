#!/usr/bin/env python3
import requests
import logging
import bs4
import os
import sys


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s[%(levelname)s]: %(message)s')
logging.disable(logging.CRITICAL) ##调试完成后添加，禁用log

'''
使用getcwd()获取的路径，是当前的工作路径，如果将该脚本做成一个linux系统中的命令时，
用户执行时，会出现在当前的目录中创建文件夹，创建文件。
CUR_PATH = os.getcwd()
LOCAL_CMD_DIR = CUR_PATH + '/' + 'man_linuxde/'
'''

SCRIPT_PAHT = os.path.realpath(__file__)
logging.debug(SCRIPT_PAHT)
LOCAL_CMD_DIR = os.path.split(SCRIPT_PAHT)[0] + '/.man_linuxde/'
logging.debug(LOCAL_CMD_DIR)

def get_lookup_cmd():
	if (len(sys.argv) > 1):
		#从命令行获取待查询的命令
		cmd = ''.join(sys.argv[1])
		logging.debug('cmd = ' + str(cmd))
		return cmd
	else:
		print('使用方法: pyman your_lookup_cmd, 例如：./pyman find 或者 pyman find')

def create_cmd_dir():
    try:
        os.mkdir(LOCAL_CMD_DIR)
        logging.debug('.man_linuxde创建成功！')
    except Exception as FileExistsError:
        logging.debug('.man_linuxde目录已经存在')

def download_cmd_file(cmd_name):
    url = 'http://man.linuxde.net/' + cmd_name
    print('正在下载 URL:' + url + ' 的内容，请稍等 ...')
    res = requests.get(url)
    res.raise_for_status()
    html_file = LOCAL_CMD_DIR + cmd_name + '.html'
    logging.debug(html_file)
    playFile = open(html_file, 'wb')
    for buf in res.iter_content(100000):
        playFile.write(buf)
    playFile.close()
    return html_file

def get_cmd_file(cmd_name):
    if cmd_name is None:
        return

    local_cmd = os.listdir(LOCAL_CMD_DIR)
    local_html_file =  cmd_name + '.html'
    if local_html_file in local_cmd:
        logging.debug(LOCAL_CMD_DIR + local_html_file)
        return (LOCAL_CMD_DIR + local_html_file)
    else:
       dcf = download_cmd_file(cmd_name)
       return dcf

def parse_linuxde_html(cmd_file):
    if cmd_file is None:
        return

    file_obj = open(cmd_file)
    soup = bs4.BeautifulSoup(file_obj,'lxml')
    div_body = soup.body
    main_div = div_body.find('div', {'class': 'main'})

    post_hd = main_div.find('h1', {'class': 'l'})
    cmd_descr = main_div.find('p')
    all_text = main_div.get_text()
    text_list = all_text.split('\n')

    #截取有用的文本
    tail_num = len(text_list)
    for index in range(0, len(text_list)):
        if '最近更新的命令' == text_list[index]:
            tail_num = index

    text_list = text_list[2:tail_num]

    all_text = '\n'.join(text_list)
    print(all_text)

def main():
    lookup_cmd = get_lookup_cmd()
    create_cmd_dir()
    cmd_file = get_cmd_file(lookup_cmd)
    parse_linuxde_html(cmd_file)


if __name__ == '__main__':
    main()

