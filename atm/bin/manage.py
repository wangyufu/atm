# __author__:"wangyufu"
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from core import manage_main


if __name__ == '__main__':
    manage_main.interactive()