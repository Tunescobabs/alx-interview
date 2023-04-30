#!/usr/bin/python3
import sys

total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
lines_read = 0

for line in sys.stdin:
    try:
        words = line.split()
        size = int(words[-1])
        status_code = int(words[-2])
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        total_size += size
        lines_read += 1
        if lines_read % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in sorted(status_codes_count.items()):
                if count != 0:
                    print("{}: {}".format(code, count))
    except Exception:
        pass

