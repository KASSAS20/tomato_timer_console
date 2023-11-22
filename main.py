import time
import os





if __name__ == '__main__':
    start = int(time.time())
    finish = start+int(input('Время ожидания: '))*60
    while True:
        time.sleep(1)
        os.system('clear')
        start+=1
        if finish-start == 0:
            print("Время вышло")
            break
        else:
            timer = finish-start
            hours = timer//60//60
            minute = (timer//60)-(hours*60)
            secound = timer-(hours*60*60)-(minute*60)
            formatted_time = '{:02}:{:02}:{:02}'.format(hours, minute, secound)
            print(formatted_time)

        
