import time
from tqdm import tqdm

# تعداد مراحل کاری که باید انجام شود
total_steps = 10000000000

# شروع زمان
start_time = time.time()

# استفاده از tqdm برای نمایش نوار پیشرفت و زمان باقی‌مانده
for i in tqdm(range(total_steps), desc="Processing", unit="step"):
    # شبیه‌سازی کار (مثلاً یک محاسبه ساده)
    _ = i * i  # انجام یک عملیات ساده برای شبیه‌سازی

    # به محض اینکه بخواهید کاری انجام دهید، زمان باقی‌مانده به طور خودکار محاسبه می‌شود
    # `tqdm` به طور خودکار زمان باقی‌مانده را نمایش می‌دهد.

# پایان زمان
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total time taken: {elapsed_time:.2f} seconds")
