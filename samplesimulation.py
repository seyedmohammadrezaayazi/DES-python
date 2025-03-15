import simpy
import random
import matplotlib.pyplot as plot
import numpy

rand=43
new_customer = 70
time_in_bank = 12
interval = 10
min_patince = 4
max_patince = 8
worktime = 0
numberout = 0
total_wait_time = 0
listwait = []
list_n=[]


def source(env, number, counter, interval):
    for i in range(number):
        c = customer(env, "customer%02d" % i, counter, time_in_bank)
        env.process(c)
        time = random.expovariate(1 / interval)
        yield env.timeout(time)


def customer(env, name, counter, time_in_bank):
    arrive = env.now
    print('%7.4f %s : here i am in bank' % (arrive, name))
    with counter.request() as req:
        patience = random.uniform(min_patince, max_patince)
        print("patience ", patience)
        results = yield req | env.timeout(patience)

        wait = env.now - arrive
        global total_wait_time
        global listwait
        global worktime
        global numberout
        global list_n
        total_wait_time += wait
        listwait.append(wait)

        if req in results:
            list_n.append(0)
            print("%7.4f %s : waited %6.3f" % (env.now, name, wait))
            temp = random.expovariate(1 / time_in_bank)
            worktime += temp
            print("work time", temp)
            yield env.timeout(temp)
            print("%7.4f %s  finished " % (env.now, name))
        else:
            list_n.append(2)
            numberout += 1
            print("%7.4f %s  reneged after  %6.3f" % (env.now, name, wait))

random.seed(2)
env = simpy.Environment()

counter = simpy.Resource(env, capacity=3)

env.process(source(env, new_customer, counter, interval))
env.run()

print(f"total wait time is :{total_wait_time}")
print(f"work time is :{worktime}")
print(f"number out is :{numberout}")

x = numpy.arange(new_customer)
plot.plot(x, listwait)
plot.title("wait time")
plot.show()
plot.plot(x, list_n)
plot.title("out")
plot.show()

