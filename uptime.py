"""
Can be run for days to see how often the internet is up.
"""
import subprocess
import time
from dataclasses import dataclass, field
from datetime import datetime
import sys

from Utils.string_formatting import format_seconds

sys.stdout.reconfigure(encoding='utf-8')


@dataclass(slots=True)
class Outage:
    _start: float
    _end: float

    @property
    def start(self) -> float:
        return round(self._start, 2)

    @start.setter
    def start(self, value: float):
        self._start = value

    @property
    def end(self) -> float:
        return round(self._end, 2)

    @end.setter
    def end(self, value: float):
        self._end = value

    @property
    def duration(self) -> float:
        return round(self.end - self.start, 2)


@dataclass(slots=True)
class Host:
    address: str
    success_pings: int = 0
    failed_pings: int = 0
    total_pings: int = 0
    response_times: list[float] = field(default_factory=list)
    total_response_time: float = 0.0
    high_response_time: float = 0
    low_response_time: float = float('inf')
    uptime_percentage: float = 0
    avg_response_time: float = 0

    def update_response_time(self, time_: float):
        self.response_times.append(time_)
        self.total_response_time += time_
        self.high_response_time = max(self.high_response_time, time_)
        self.low_response_time = min(self.low_response_time, time_)

    def calculate_stats(self):
        total_pings = self.success_pings + self.failed_pings
        if total_pings > 0:
            self.uptime_percentage = (self.success_pings / total_pings) * 100
        if self.response_times:
            self.avg_response_time = sum(self.response_times) / len(self.response_times)


def main() -> None:
    all_host_ips = ["9.9.9.9", "1.1.1.1", "8.8.8.8"]  # Quad9, Cloudflare, Google DNS servers (could do 208.67.222.222)
    all_hosts: list[Host] = [Host(address=host_ip) for host_ip in all_host_ips]

    ping_interval_seconds = 3
    info_print_interval_seconds = 40
    ljust_num = 12
    num_outages = 0
    timeout_limit = 4.8
    outage_start = 0.0
    outages: list[Outage] = []

    print(" " * 5 + "Monitoring internet uptime by pinging DNS servers:\n" + "-" * 60 + "\n")
    print(" " * 22 + "Quad9            Cloudflare       Google")
    script_start = time.time()

    try:
        while True:
            all_failed = True
            ping_result_output = []
            for host in all_hosts:
                start_time = time.time()
                host.total_pings += 1
                try:
                    ping_result = subprocess.run(["ping", "-n", "1", host.address], stdout=subprocess.PIPE,
                                                 stderr=subprocess.PIPE, timeout=timeout_limit)
                    end_time = time.time()
                    response_time = (end_time - start_time) * 1000  # Convert to milliseconds
                except subprocess.TimeoutExpired:
                    host.failed_pings += 1
                    ping_result_output.append("⏱️ timeout".ljust(ljust_num + 1))
                    continue

                if ping_result.returncode == 0:
                    all_failed = False
                    host.success_pings += 1
                    host.update_response_time(response_time)
                    ping_result_output.append(f"✅ {response_time:.2f} ms".ljust(ljust_num))
                else:
                    host.failed_pings += 1
                    ping_result_output.append("❌".ljust(ljust_num))

            if all_failed:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - ❌❌❌❌❌❌❌❌❌ Internet Outage ❌❌❌❌❌❌❌❌❌ ")
                if not outage_start:
                    outage_start = time.time()
            else:
                if outage_start:
                    outage_end = time.time()
                    num_outages += 1
                    outage = Outage(outage_start, outage_end)
                    outages.append(outage)
                    outage_start = 0.0
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {'    '.join(ping_result_output)}"[:-2])  # noqa

            if all_hosts[0].total_pings % info_print_interval_seconds == 0:  # Every x seconds
                for host in all_hosts:
                    host.uptime_percentage = host.success_pings / host.total_pings * 100
                    host.avg_response_time = host.total_response_time / len(host.response_times)

                calulate_stats(all_hosts)
                if outages:
                    print_outage_info(outages)
                else:
                    print("\nNo outages")
                print("\n                      Quad9            Cloudflare       Google")

            time.sleep(ping_interval_seconds)

    except KeyboardInterrupt:
        print("\nFinal Uptime and Response Times:", end='')
        calulate_stats(all_hosts)
        script_end = time.time()
        total_time = script_end - script_start
        message = format_seconds(total_time)
        if outages:
            print_outage_info(outages)
        else:
            print("\nNo outages")
        print(f"\nProgram ran for: {message}\n")


def print_outage_info(all_outages: list[Outage]) -> None:
    print(f"\nTotal outages: {len(all_outages)}")
    print("Outage Log:")
    column_names = ["Start", "End", "Duration"]

    stats: list[list] = []
    for outage in all_outages:
        stats.append([datetime.fromtimestamp(outage.start).strftime('%Y-%m-%d %H:%M:%S'),
                      datetime.fromtimestamp(outage.end).strftime('%Y-%m-%d %H:%M:%S'),
                      format_seconds(outage.duration)])

    print_formatted_stats(stats, column_names)


def calulate_stats(all_hosts: list[Host]) -> None:
    print("\n")
    column_names = ["Host", "Uptime", "Average", "Low", "High"]

    stats: list[list] = []
    for host in all_hosts:
        uptime = f"{host.uptime_percentage:.2f}%"
        high = f"{host.high_response_time:.2f} ms"
        low = f"{host.low_response_time:.2f} ms"
        average = f"{host.avg_response_time:.2f} ms"
        stats.append([host.address, uptime, average, low, high])

    print_formatted_stats(stats, column_names)


def print_formatted_stats(stats: list[list], column_names: list) -> None:
    # Determine column widths for alignment
    col_widths = [max(len(str(item)) for item in col) for col in zip(*stats, column_names)]

    # Print header
    print(" | ".join(header.ljust(width) for header, width in zip(column_names, col_widths)))
    print("-+-".join('-' * width for width in col_widths))

    # Print stats
    for stat in stats:
        print(" | ".join(str(item).ljust(width) for item, width in zip(stat, col_widths)))


if __name__ == '__main__':
    main()
