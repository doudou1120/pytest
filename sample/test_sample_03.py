import pytest

class TestDemo():
    def test_one(self):
        print("开始执行test one 方法")
        x='this'
        # assert 'h' in x
        pytest.assume('h' not in x)
        pytest.assume(1==2)
        pytest.assume('x' in 'xxx')

    def test_two(self):
        print("开始执行test two 方法")
        x='hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行test three 方法")
        a='hello'
        b='hello world'
        assert a in b


class TestDemo1():
    def test_a(self):
        print("开始执行test 方法")
        x='this'
        assert 'h' in x

    def test_b(self):
        print("开始执行test b 方法")
        x='hello'
        assert 'e' in x

    def test_c(self):
        print("开始执行test c 方法")
        a='hello'
        b='hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main("-v -x TestDemo")
    pytest.main("-v -s TestDemo")
