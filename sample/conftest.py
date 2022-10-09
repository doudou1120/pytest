import pytest
@pytest.fixture()# 不带参数的fixture默认参数为scope=function
def login():
    print("这是一个登录方法")

def pytest_configure(config):
    marker_list=["search","login"]#标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers",markers
        )