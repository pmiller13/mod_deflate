import requests
import sys

sites = ['gallery','opportunity','business-time']
iterations = 0
num = 0
ip = ''

def avg(list): return sum(list)/len(list)

def automate():
    tot = 0
    times = []
    total_bandwidth = 0
    max_time = 0
    #if len(ip) == 0:
    #    ip = '0.0.0.0'
    for site in sites:
        # Number of trials to run per site
        site = 'http://' + ip + '/' + site + '/'
        for i in range(iterations):
            # Number of requests to send
            for j in range(num):
                response = requests.get(site)
                times.append(response.elapsed.total_seconds())
                total_bandwidth = total_bandwidth + (len(response.content)/10000000.0)
        times.sort()

        print(str(iterations) + " trials  of " + str(num) + " complete for " + site + ":")
        print("Min: " + str(times[0]) + " sec")
        print("Max: " + str(times[len(times)-1]) + " sec")
        print("Avg: " + str(avg(times)) + " sec")
        foo = iterations + 0.0
        print("Bandwidth: " + str(total_bandwidth/foo))
        print('\n')



iterations = input("How many times would you like to test each site? ")
num = input("How many requests per site? ")
ip = raw_input("Enter site ip: ")
print('\n')
automate()
