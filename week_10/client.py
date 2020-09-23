import cmd
import datetime
import httpx
import logging

class Client(cmd.Cmd):
    def do_hello(self, line):
        """say hello"""
        print(line)

    def do_time(self, line):
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))

    def do_exit(self, line):
        print("see you later")
        return True

    def do_parse_time(self, line):
        # line_split = line.split()

        try:
            time = datetime.datetime.strptime(line, "%Y/%m/%d %H:%M:%S")
        except ValueError as exc:
            print(f'error: {exc}')
        else:
            print(f'create time {time}')

    def do_get_time(self, line):
        if line.startswith("http://"):
            respons = httpx.get(line)
            print(f'time: {respons.json()}')
        else:
            logging.error("please enter http address")

if __name__ == "__main__":
    Client().cmdloop()