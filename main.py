from yandex_music import Client
import random as rd
import time
import configparser as cf
import os
from art import tprint
import token_ya as ya

tprint("Power by dev Grib.pw")
print("#################################")
print("Скрипт скачивания с Яндекс Музыки")
print("#################################\n")
start_prog = time.time()

print("Создание файла конфигурации\n")
ya.ya_token()

config = cf.ConfigParser()
config.read("settings.ini") # Файл конфигурации где лежит ваш токен
try:
    TOKEN = config["Yandex"]["TOKEN"]
except KeyError:
    os.remove("settings.ini")
    ya.ya_token()
option = int(input("Выберете опция загрузки:\nВариант 1 - присвоить номер треку по порядку\nВариант 2 - присвоить номер треку рандомно\nВвод номера варианта: "))
dir_mp3 = input("Введите название папки куда скачивать файлы: ")
 
try:
    os.mkdir(dir_mp3)
    print(f'Папка {dir_mp3} создана!')
except FileExistsError:
    print(f'Папа {dir_mp3} существует!')

client = Client(TOKEN).init()


    

def random_dw_mp3():
    track = client.users_likes_tracks().fetch_tracks()

    nums = 0

    for num in track:
        nums += 1

    rd_list = list(range(1, nums+1))
    rd.shuffle(rd_list)
    rd_array = []

    for l in rd_list:
    
        if l <= 9:
            t_id_rd = "00"+str(l)
            rd_array.append(t_id_rd)
        elif l >= 10 and l <= 99:
            t_id_rd = "0" + str(l)
            rd_array.append(t_id_rd)
        else:
            t_id_rd = str(l)
            rd_array.append(t_id_rd)

            

    for i in range(nums):
        
        start_dw = time.time()
        
        if i+1 <= 9:
            t_id = "00"+str(i+1)
        elif i+1 >= 10 and i+1 <= 99:
            t_id = "0" + str(i+1)
        else:
            t_id = str(i+1)

        track = client.users_likes_tracks()[i].fetch_track()
        art = []
        
        for artist in track.artists_name():
            str_artist = str(artist)
            artists = ""
            for j in str_artist:
                if j == "/":
                    j = "_"
                artists += j
            art.append(artists)
            
        track.download(f'{dir_mp3}/{rd_array[i]}_{", ".join(art)} - {track.title}.mp3')
        end_dw = time.time() - start_dw
        end_dw = float('{:.2f}'.format(end_dw))
        print("################################################################################################")
        print(f"Скачивание трека - {t_id}/{nums}\nПрисвоен рандомный номер - {rd_array[i]}\nВремя скачивание трека: {end_dw} Сек.")
        print(f'Название файлы: {rd_array[i]}_{", ".join(art)} - {track.title}.mp3')
        print("################################################################################################\n")    
        
    end_prog = time.time() - start_prog
    end_prog /= 60
    print(f"Загрузка завершена! Количество загруженных треков - {nums}\nВремя выполнения скрипта: {float('{:.2f}'.format(end_prog))} Мин!\n")

def dw_mp3():
    track = client.users_likes_tracks().fetch_tracks()

    nums = 0

    for num in track:
        nums += 1            

    for i in range(nums):
        
        start_dw = time.time()
        
        if i+1 <= 9:
            t_id = "00"+str(i+1)
        elif i+1 >= 10 and i+1 <= 99:
            t_id = "0" + str(i+1)
        else:
            t_id = str(i+1)

        track = client.users_likes_tracks()[i].fetch_track()
        art = []
        
        for artist in track.artists_name():
            str_artist = str(artist)
            artists = ""
            for j in str_artist:
                if j == "/":
                    j = "_"
                artists += j
            art.append(artists)
            
        track.download(f'{dir_mp3}/{t_id}_{", ".join(art)} - {track.title}.mp3')
        end_dw = time.time() - start_dw
        end_dw = float('{:.2f}'.format(end_dw))
        print("################################################################################################")
        print(f"Скачивание трека - {t_id}/{nums}\nВремя скачивание трека: {end_dw} Сек.")
        print(f'Название файлы: {t_id}_{", ".join(art)} - {track.title}.mp3')
        print("################################################################################################\n")    
        
    end_prog = time.time() - start_prog
    end_prog /= 60
    print(f"Загрузка завершена! Количество загруженных треков - {nums}\nВремя выполнения скрипта: {float('{:.2f}'.format(end_prog))} Мин!\n")

def main():
    if option == 1:
        dw_mp3()
    elif option == 2:
        random_dw_mp3()
    else:
        break

if __name__ == "__main__":
    main()