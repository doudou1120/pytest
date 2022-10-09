import pytest
def setup_module():
    print("这是个setup_module方法")

def teardown_module():
    print("这是个teardown_module方法")

def setup_function():
    print("setup_function")

def teardown_function():
    print("teardown_function")

def test_login():
    print("这是个外部方法")
class tearDemo():
    def setup_class(self):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def teardown_class(self):
        print("teardown_class")

    def teardwon_method(self):
        print("teardwon_method")

    def teardown(self):
        print("teardown")

    def test_one(self):
        print("开始执行test one 方法")
        x='this'
        assert 'h' in x

    def test_two(self):
        print("开始执行test two 方法")
        x='hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行test three 方法")
        a='hello'
        b='hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main()