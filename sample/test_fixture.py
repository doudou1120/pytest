import pytest
#以下移入conftest.py
# @pytest.fixture()
# def login():
#     print("这是一个登录方法")

def test_case1(login):
    print("test_case1需要登录")
    pass

def test_case2():
    print("test_case2不需要")
    pass

def test_case3(login):
    print("test_case3需要登录")
    pass

if __name__ == '__main__':
    pytest.main()