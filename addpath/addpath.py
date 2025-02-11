# addpath/addpath.py

import sys
import os


def add_parent_path(levels=1):
    """
    현재 실행 중인 스크립트의 상위 디렉토리를 sys.path에 추가합니다.

    :param levels: 추가할 상위 디렉토리 레벨 (기본값: 1)
    """
    current_path = os.path.abspath(os.getcwd())
    for _ in range(levels):
        current_path = os.path.dirname(current_path)

    if current_path not in sys.path:
        sys.path.insert(0, current_path)
