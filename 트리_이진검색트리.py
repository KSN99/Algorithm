#이진 검색 트리 구현

from __future__ import annotations
from typing import Any, Type

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key, value, left, right) -> None:
        """생성자(constructor)"""
        self.key = key #key
        self.value = value # value
        self.left = left # left pointer
        self.right = right # right pointer

class BinarySearchTree:
    """이진 검색 트리"""

    def __init__(self) -> None:
        self.root = None #root

    def search(self, key):
        """키가 key인 노드를 검색"""
        p=self.root # 루트에 주목
        while True:
            if p is None:
                return None
            
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right
    
    def add(self, key, value):
        def add_none(node, key, value):
            if key== node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None,None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True