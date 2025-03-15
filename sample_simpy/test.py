import simpy
import random
import matplotlib.pyplot as plt
import numpy as np

MIN_patince = 4
MAX_patince = 8
Time_in_bank = 12
Interval = 10
New_CUTUMER = 70
total_wait_time = 0
numberOUT = 0
worktime = 0
listwait = []
listrege = []


def source(env, number, interval, counter):
    for i in range(number):
        c = customer(env, "customer%02d" % i, counter, Time_in_bank)
        env.process(c)
        time = random.expovariate(1 / interval)
        yield env.timeout(time)


def customer(env, name, counter, time_in_bank):
    arrive = env.now
    print('%7.4f %s : here i am in bank' % (arrive, name))

    with counter.request() as req:
        patience = random.uniform(MIN_patince, MAX_patince)
        print("patience:", patience)
        results = yield req | env.timeout(patience)

        wait = env.now - arrive
        global total_wait_time
        global listrege
        global numberOUT
        global listwait
        global worktime
        global listrege
        total_wait_time += wait
        listwait.append(wait)

        if req in results:
            listrege.append(0)
            print('%7.4f %s : waited %6.3f' % (env.now, name, wait))

            temp = random.expovariate(1 / time_in_bank)
            worktime += temp
            print(temp)
            yield env.timeout(temp)
            print('%7.4f %s : finished' % (env.now, name))
        else:
            listrege.append(2)
            numberOUT += 1
            print('%7.4f %s : reneged after %6.3f' % (env.now, name, wait))


env = simpy.Environment()

counter = simpy.Resource(env, capacity=1)
env.process(source(env, New_CUTUMER, Interval, counter))
env.run()
print(f"total wait time is : {total_wait_time}")
print(f"total work time: {worktime}")
print(f"number out is : {numberOUT}")
print(f"unsused system : {env.now - worktime}")
x = np.arange(New_CUTUMER)
plt.plot(x, listwait)
plt.title("wait time")
plt.show()
