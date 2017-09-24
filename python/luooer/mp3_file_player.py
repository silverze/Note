import pygame 
import os 
import time

def play_current_dir_mp3():
    file_list = os.listdir(os.getcwd())
    print(file_list)
    pygame.mixer.init()
    for mp3file in file_list:   
        if ".mp3" in mp3file:
            mp3file = mp3file.encode('utf_8')#加入编码转换避免pygame.mixer_music.load()错误   
            pygame.mixer_music.load(mp3file)
            pygame.mixer_music.play()
            while (pygame.mixer_music.get_busy()):
                time.sleep(0.01)

def main():
    print("播放当前目录下的mp3音乐")
    play_current_dir_mp3()

if __name__ == "__main__":
    main()
