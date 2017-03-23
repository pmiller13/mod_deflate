import requests
import sys

def automate(site,num):
    tot = 0
    times = []
    max_time = 0
    for i in range(num):

        response = requests.get(site)
        tot = tot + response.elapsed.total_seconds()
        times.append(response.elapsed.total_seconds())

        if max_time < response.elapsed.total_seconds():
            max_time = response.elapsed.total_seconds()

    avg = tot/num
    print("Avg time: " + str(avg) + " sec")
    print("Max time: " + str(max_time) + " sec")

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        ip = sys.argv[1]
        num = int(sys.argv[2])
        site = sys.argv[3]
        site = 'http://' + ip + '/' + site + '/'
        automate(site,num)
    else:
        print("Usage: python use.py xxx.xxx.xxx.xxx number_of_requests site_path")
