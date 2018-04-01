#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
import bs4
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s[%(levelname)s]: %(message)s')
logging.disable(logging.CRITICAL) ##调试完成后添加，禁用log

SCRIPT_PAHT = os.path.realpath(__file__)
MUSIC_DIR_ROOT = os.path.split(SCRIPT_PAHT)[0] + '/.luooer_music'
MP3_FILE_FULL_NAME = MUSIC_DIR_ROOT + '/downing.mp3'
MUSIC_LIST_HTML =  MUSIC_DIR_ROOT + '/buf.html'

def download_music_list(peri_num):
    url = 'http://www.luoo.org/music.php?id=' + peri_num
    print('正在下载' + str(peri_num) + '期刊音乐列表，请稍等!')
    if (not os.path.exists(MUSIC_DIR_ROOT)):
        os.mkdir(MUSIC_DIR_ROOT)

    res = requests.get(url)
    res.raise_for_status()   
    music_list_html = open(MUSIC_LIST_HTML, 'wb')
    for buf in res.iter_content(100000):
        music_list_html.write(buf)
    music_list_html.close()

def download_music_file(down_list, peri_num):
    '''
    根据期刊的音乐列表，下载音乐
    '''
    print('落网期刊' + str(peri_num) + '总共有' + str(len(down_list)) + '首音乐，下载会花一些时间，请耐心等待...')
    for index in range(len(down_list)):
        print('正在下载第' + str(index + 1) + '首音乐：' + down_list[index])
        index = index + 1
        if(index < 10):
            index = '0' + str(index)
        else:
            index = str(index)
        url = 'http://mp3-cdn.luoo.net/low/luoo/radio' + peri_num +'/' + index + '.mp3'
        res = requests.get(url)
        res.raise_for_status()

        mp3file = open(MP3_FILE_FULL_NAME, 'wb')
        for buf in res.iter_content(100000):
            mp3file.write(buf)
        mp3file.close()

        file_rename(down_list, int(index) - 1, peri_num)

def file_rename(down_list, index, peri_num):
    dst_name = MUSIC_DIR_ROOT + '/' + peri_num + '/' 
    if (not os.path.exists(dst_name)):
        os.mkdir(dst_name)
    dst_name = dst_name + down_list[index]
    dst_name = dst_name.strip()  + '.mp3' 
    logging.debug(dst_name)
    os.rename(MP3_FILE_FULL_NAME, dst_name)

def parse_luooer_html(file, peri_num):
    if file is None:
        return

    file_obj = open(file, 'rb')
    soup = bs4.BeautifulSoup(file_obj,'lxml')
    div_body = soup.body
    main_div = div_body.find('div', {'class': 'musiclist'})

    try:
        all_text = main_div.get_text()
    except AttributeError:
        print('在落网上未找到有关' + str(peri_num) + '期刊的音乐！')
        sys.exit()
    
    full_music_str = all_text.split('\n')
    del full_music_str[0]
    del full_music_str[0]
    logging.debug(full_music_str)
    music_list = full_music_str[0].split('[download]')
    del music_list[-1]
    logging.debug(music_list)

    for music_index in range(len(music_list)):
        if(music_list[music_index] != None):
            music_name = music_list[music_index].split('. ')
            del music_name[0]
            music_list[music_index] = music_name[0]

    logging.debug(music_list)

    return music_list

def get_periodical_number():
    '''
    从命令行获取期刊号
    '''
    if (len(sys.argv) > 1):
        #从命令行获取待查询的命令
        cmd = ''.join(sys.argv[1])
        logging.debug('cmd = ' + str(cmd))
        return cmd
    else:
        print('请输入想听的专辑号，例如：luomoc 969')
        sys.exit()

def download_periodical_music(peri_num):
    download_music_list(peri_num)
    down_list = parse_luooer_html(MUSIC_LIST_HTML, peri_num)
    download_music_file(down_list, peri_num)


def is_exist_music(peri_num):  
    '''
    判断本地是否已存有该专辑音乐
    ''' 
    if (os.path.exists(MUSIC_DIR_ROOT + '/' + peri_num + '/')):
        print('本地已存有落网'+ str(peri_num) + '期刊的音乐！')
        return True
    else:
        print('本地未找到落网'+ str(peri_num) + '期刊的音乐,正从落网下载...')
        return False

def main():
    peri_num = get_periodical_number()
    if not is_exist_music(peri_num):
        download_music_list(peri_num)
        down_list = parse_luooer_html(MUSIC_LIST_HTML, peri_num)
        download_music_file(down_list, peri_num)
    os.system('mocp ' + MUSIC_DIR_ROOT + '/' + peri_num)
    
if __name__ == '__main__':
    main()