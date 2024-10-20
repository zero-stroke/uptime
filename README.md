# uptime.py

A Python script to check internet uptime by pinging DNS servers.

## Prerequisites

For running with python, follow the below steps. Otherwise, I've also compiled it into an exe that you can point and click to run, so that is an alternative as well. 

1. **Python**: Make sure Python is installed on your computer, version 3.10 or up
   - Download from: https://www.python.org/downloads/ make sure to check the box that says to add it to your "PATH".
   - Verify installation in terminal/command prompt: 
```shell 
python --version
``` 

2. **Git** (Optional - Choose one method below):
   - **With Git:**
     - Install Git from: https://git-scm.com/downloads
     - Clone: 
```bash 
git clone https://github.com/zero-stroke/uptime.git
```
   - **Without Git:**
     - Click the green "Code" button on GitHub
     - Select "Download ZIP"
     - Extract the ZIP file

## Running the Script

1. Open your terminal/command prompt
2. Navigate to script location: `cd path/to/script`. For example, `cd C:/Users/you/Downloads/uptime/`

3. Run by opening your command prompt/terminal and entering the following command: 
```shell
python uptime.py
```

## Usage 
It logs instances at which all three ping attempts are not successful and tracks them as outages, and records how long these outages go on for.

Output while running should look something like this:
```
                      Quad9            Cloudflare       Google
2024-10-19 14:12:56 - ✅ 53.08 ms      ✅ 51.03 ms      ✅ 49.53 ms
2024-10-19 14:12:59 - ✅ 54.06 ms      ✅ 48.04 ms      ✅ 61.24 ms
2024-10-19 14:13:02 - ✅ 51.64 ms      ✅ 49.06 ms      ✅ 47.54 ms
2024-10-19 14:13:05 - ✅ 52.53 ms      ✅ 48.53 ms      ✅ 50.10 ms
2024-10-19 14:13:09 - ✅ 52.23 ms      ✅ 49.17 ms      ✅ 46.52 ms
2024-10-19 14:13:12 - ✅ 51.81 ms      ✅ 48.03 ms      ✅ 48.54 ms
2024-10-19 14:13:15 - ✅ 51.53 ms      ✅ 48.02 ms      ✅ 49.08 ms
2024-10-19 14:13:18 - ✅ 52.62 ms      ✅ 48.02 ms      ✅ 48.92 ms
2024-10-19 14:13:21 - ✅ 52.55 ms      ✅ 48.54 ms      ✅ 47.01 ms
2024-10-19 14:13:25 - ✅ 264.02 ms     ✅ 62.03 ms      ✅ 70.94 ms
2024-10-19 14:13:28 - ✅ 52.12 ms      ✅ 48.03 ms      ✅ 48.57 ms
2024-10-19 14:13:31 - ✅ 52.55 ms      ✅ 66.36 ms      ✅ 52.02 ms
2024-10-19 14:13:34 - ✅ 52.03 ms      ✅ 48.51 ms      ✅ 47.41 ms
2024-10-19 14:13:41 - ❌               ✅ 48.56 ms      ✅ 47.54 ms
2024-10-19 14:13:44 - ✅ 51.51 ms      ✅ 50.07 ms      ✅ 48.00 ms
2024-10-19 14:13:47 - ✅ 71.09 ms      ✅ 75.09 ms      ✅ 71.58 ms
2024-10-19 14:13:50 - ✅ 52.67 ms      ✅ 48.10 ms      ✅ 48.03 ms


Host    | Uptime  | Average  | Low      | High
--------+---------+----------+----------+----------
9.9.9.9 | 99.89%  | 58.78 ms | 50.53 ms | 646.77 ms
1.1.1.1 | 100.00% | 51.76 ms | 46.67 ms | 152.50 ms
8.8.8.8 | 100.00% | 51.62 ms | 45.53 ms | 214.64 ms

No outages
```

During an outage it might look something like this:
```shell
                      Quad9            Cloudflare       Google
2024-10-19 16:33:09 - ✅ 55.09 ms      ✅ 48.22 ms      ✅ 47.16 ms
2024-10-19 16:33:24 - ❌❌❌❌❌❌❌ Internet Outage ❌❌❌❌❌❌❌
2024-10-19 16:33:39 - ❌❌❌❌❌❌❌ Internet Outage ❌❌❌❌❌❌❌
2024-10-19 16:33:54 - ❌❌❌❌❌❌❌ Internet Outage ❌❌❌❌❌❌❌
2024-10-19 16:34:09 - ❌❌❌❌❌❌❌ Internet Outage ❌❌❌❌❌❌❌


Host    | Uptime | Average  | Low      | High
--------+--------+----------+----------+---------
9.9.9.9 | 73.33% | 54.48 ms | 50.81 ms | 58.62 ms
1.1.1.1 | 73.33% | 51.04 ms | 47.92 ms | 59.84 ms
8.8.8.8 | 73.33% | 49.16 ms | 47.08 ms | 55.12 ms

Ongoing outage since 2024-10-19 16:34:05

                      Quad9            Cloudflare       Google
2024-10-19 16:34:24 - ❌❌❌❌❌❌❌ Internet Outage ❌❌❌❌❌❌❌
2024-10-19 16:34:27 - ✅ 60.69 ms      ✅ 56.15 ms      ✅ 52.74 ms
2024-10-19 16:34:30 - ✅ 53.58 ms      ✅ 49.60 ms      ✅ 47.72 ms
2024-10-19 16:34:33 - ✅ 52.66 ms      ✅ 49.94 ms      ✅ 46.73 ms
2024-10-19 16:34:36 - ✅ 56.55 ms      ✅ 52.60 ms      ✅ 58.75 ms
2024-10-19 16:34:39 - ✅ 52.66 ms      ✅ 49.94 ms      ✅ 46.73 ms
2024-10-19 16:34:42 - ✅ 56.55 ms      ✅ 52.60 ms      ✅ 58.75 ms

Host    | Uptime | Average  | Low      | High
--------+--------+----------+----------+---------
9.9.9.9 | 75.00% | 54.85 ms | 50.81 ms | 60.69 ms
1.1.1.1 | 75.00% | 51.31 ms | 47.92 ms | 59.84 ms
8.8.8.8 | 75.00% | 49.78 ms | 46.73 ms | 58.75 ms

Total outages: 1
Outage Log:
Start               | End                 | Duration
--------------------+---------------------+----------------------
2024-10-19 16:33:24 | 2024-10-19 16:34:27 | 63.17s (1.05 minutes)
```

## Support

If you encounter issues:
- Check Python is installed correctly
- Ensure you're in the correct directory
- For help, create an issue on GitHub

## License
This project is licensed under the Apache NON-AI License, Version 2.0 - see the [LICENSE](LICENSE.txt) file for details


