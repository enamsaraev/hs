import multiprocessing

bind = "0.0.0.0:8080"
workers = 2 * multiprocessing.cpu_count() + 1
# log_level = "debug"
