# uptime.py

A Python script to check internet uptime by pinging DNS servers.


## Prerequisites

For running with python, follow the below steps. If you don't want to use python, I've also compiled it into an .exe that you can point and click to run, but I recommend python for optimal stability. 

This has been tested to work on windows 10, 11, and Ubuntu. 

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
     - Select "Download ZIP", then extract the downloaded file

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
2024-10-19 14:13:31 - ✅ 52.55 ms      ✅ 66.36 ms      ✅ 52.02 ms
2024-10-19 14:13:34 - ✅ 52.03 ms      ✅ 48.51 ms      ✅ 47.41 ms
2024-10-19 14:13:41 - ❌               ✅ 48.56 ms      ✅ 47.54 ms
2024-10-19 14:13:44 - ✅ 51.51 ms      ✅ 50.07 ms      ✅ 48.00 ms
2024-10-19 14:13:47 - ✅ 71.09 ms      ✅ 75.09 ms      ✅ 71.58 ms


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

As it runs, it also writes the output to a .log file in the same directory that it was ran from.

You can also add your own hosts to ping by using the `--extra-hosts` or `e` flag when 
it's ran in the command line, giving each host's address and name. 
For example, 

```python uptime.py --extra-hosts 8.8.4.4 GoogleDNS 1.0.0.1 "Another Host"```

```python uptime.py -e 8.8.4.4 GoogleDNS```

```uptime.exe -e 8.8.4.4 GoogleDNS 208.67.222.222 "Another Host"```


Note that if using Windows 10 or below, the emojis are replaced by [✓] and [X].



## Support

If you encounter issues:
- Check Python is installed correctly
- Ensure you're in the correct directory
- For help, create an issue on GitHub


If you find this tool useful, consider giving it a ⭐ on GitHub to help others discover it!



## License
This project is licensed under the Apache NON-AI License, Version 2.0 - see the [LICENSE](LICENSE.txt) file for details
