import numpy as np
import matplotlib.pyplot as plt

# تعریف توزیع زمان خدمت دهی به مشتریان با توزیع نمایی
service_time_distribution = np.random.exponential(scale=12, size=20)

# تعریف توزیع زمان معطلی مشتریان که تصمیم به ترک بانک می‌گیرند با توزیع یکنواخت
abandonment_time_distribution = np.random.uniform(low=4, high=8, size=20)

# تابع شبیه‌سازی سیستم مراجعه کارکنان بانک
def simulate_bank_system(num_customers, num_tellers):
    # شبیه‌سازی زمان خدمت دهی به هر مشتری
    service_times = np.random.exponential(scale=12, size=num_customers)
    # شبیه‌سازی زمان معطلی مشتریان
    abandonment_times = np.random.uniform(low=4, high=8, size=num_customers)

    # محاسبه مدت زمان انتظار هر مشتری
    wait_times = np.zeros(num_customers)
    for i in range(1, num_customers):
        wait_times[i] = max(0, wait_times[i-1] + service_times[i-1] - abandonment_times[i-1])

    # محاسبه مجموع مدت زمان انتظار همه مشتریان
    total_wait_time = np.sum(wait_times)

    # محاسبه زمانی که مشتریان تصمیم به ترک بانک می‌گیرند
    abandonment_decision_times = np.cumsum(abandonment_times)

    # محاسبه تعداد مشتریانی که بانک را بدون دریافت خدمات ترک کرده‌اند
    num_abandoned_customers = np.sum(abandonment_times < service_times)

    # محاسبه مدت زمانی که سیستم در حال کار بوده است
    total_system_time = np.sum(service_times)

    # محاسبه مدت زمان بیکاری سیستم
    idle_time = total_system_time - total_wait_time

    # نمودار مدت زمان انتظار مشتریان
    plt.plot(wait_times, label='Wait Time')
    plt.xlabel('Customer')
    plt.ylabel('Wait Time')
    plt.title('Customer Wait Time')
    plt.legend()
    plt.show()

    # نمودار مدت زمان انتظار افرادی که از سیستم خارج شدند
    plt.plot(abandonment_decision_times, range(1, num_customers + 1), 'ro')
    plt.xlabel('Time')
    plt.ylabel('Customer')
    plt.title('Customers Who Abandoned the System')
    plt.show()

    return total_wait_time, num_abandoned_customers, total_system_time, idle_time

# تست تابع شبیه‌سازی با تعداد مشتریان و تعداد کارکنان مشخص
simulate_bank_system(20, 1)
import numpy as np
import matplotlib.pyplot as plt

# تعریف توزیع زمان خدمت دهی به مشتریان با توزیع نمایی
service_time_distribution = np.random.exponential(scale=12, size=20)

# تعریف توزیع زمان معطلی مشتریان که تصمیم به ترک بانک می‌گیرند با توزیع یکنواخت
abandonment_time_distribution = np.random.uniform(low=4, high=8, size=20)

# تابع شبیه‌سازی سیستم مراجعه کارکنان بانک
def simulate_bank_system(num_customers, num_tellers):
    # شبیه‌سازی زمان خدمت دهی به هر مشتری
    service_times = np.random.exponential(scale=12, size=num_customers)
    # شبیه‌سازی زمان معطلی مشتریان
    abandonment_times = np.random.uniform(low=4, high=8, size=num_customers)

    # محاسبه مدت زمان انتظار هر مشتری
    wait_times = np.zeros(num_customers)
    for i in range(1, num_customers):
        wait_times[i] = max(0, wait_times[i-1] + service_times[i-1] - abandonment_times[i-1])

    # محاسبه مجموع مدت زمان انتظار همه مشتریان
    total_wait_time = np.sum(wait_times)

    # محاسبه زمانی که مشتریان تصمیم به ترک بانک می‌گیرند
    abandonment_decision_times = np.cumsum(abandonment_times)

    # محاسبه تعداد مشتریانی که بانک را بدون دریافت خدمات ترک کرده‌اند
    num_abandoned_customers = np.sum(abandonment_times < service_times)

    # محاسبه مدت زمانی که سیستم در حال کار بوده است
    total_system_time = np.sum(service_times)

    # محاسبه مدت زمان بیکاری سیستم
    idle_time = total_system_time - total_wait_time

    # نمودار مدت زمان انتظار مشتریان
    plt.plot(wait_times, label='Wait Time')
    plt.xlabel('Customer')
    plt.ylabel('Wait Time')
    plt.title('Customer Wait Time')
    plt.legend()
    plt.show()

    # نمودار مدت زمان انتظار افرادی که از سیستم خارج شدند
    plt.plot(abandonment_decision_times, range(1, num_customers + 1), 'ro')
    plt.xlabel('Time')
    plt.ylabel('Customer')
    plt.title('Customers Who Abandoned the System')
    plt.show()

    return total_wait_time, num_abandoned_customers, total_system_time, idle_time

# تست تابع شبیه‌سازی با تعداد مشتریان و تعداد کارکنان مشخص
simulate_bank_system(20, 1)
