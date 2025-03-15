import random
import matplotlib.pyplot as plt
import simpy
import numpy as np

# RANDOM_SEED = 42
NEW_CUSTOMERS = 75
INTERVAL_CUSTOMERS = 10.0
MIN_PATIENCE = 4
MAX_PATIENCE = 8
Time_in_bank = 12
wait_time = 0
NumberOut = 0
workTime = 0
listwait = []
listreneged = []


def source(env, number, interval, counter):
    for i in range(number):
        c = customer(env, 'Customer%02d' % i, counter, Time_in_bank)
        env.process(c)
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)


def customer(env, name, counter, time_in_bank):
    arrive = env.now
    print('%7.4f %s: Here I am in bank' % (arrive, name))

    with counter.request() as req:
        patience = random.uniform(MIN_PATIENCE, MAX_PATIENCE)
        print(patience)
        results = yield req | env.timeout(patience)

        wait = env.now - arrive
        global wait_time
        global NumberOut
        global workTime
        global listwait
        global listreneged
        listwait.append(wait)
        wait_time += wait

        if req in results:
            print('%7.4f %s: Waited %6.3f' % (env.now, name, wait))
            listreneged.append(0)
            tib = random.expovariate(1.0 / time_in_bank)
            workTime += tib
            print(f"tib :{tib}")
            yield env.timeout(tib)
            print('%7.4f %s: Finished' % (env.now, name))

        else:
            NumberOut += 1
            listreneged.append(wait)
            print('%7.4f %s: RENEGED after %6.3f' % (env.now, name, wait))


print('Bank renege')
# random.seed(RANDOM_SEED)
env = simpy.Environment()

counter = simpy.Resource(env, capacity=3)
print(counter)
env.process(source(env, NEW_CUSTOMERS, INTERVAL_CUSTOMERS, counter))
env.run()
print(f"wait time :{wait_time}")
print(f"work time :{workTime}")
print(f"Number Out :{NumberOut}")
print(f"unused system :{env.now - workTime}")
x = np.arange(NEW_CUSTOMERS)
plt.plot(x, listwait)
plt.title("time wait")
plt.show()
plt.savefig('time_wait')
plt.plot(x, listreneged)
plt.title("time reneged")
plt.show()
plt.savefig("time_reneged")
