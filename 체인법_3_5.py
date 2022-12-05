#체인법으로 해시함수 구현

from __future__ import annotations
from typing import Any,Type
import hashlib

class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key:Any,value: Any, next:Node) -> None:
        """초기화"""
        self.key = key #key
        self.value=value #value
        self.next = next #뒤쪽 노드를 참조.