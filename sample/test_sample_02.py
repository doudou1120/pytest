def test_one():
    print("开始执行test one 方法")
    x='this'
    assert 'h' in x

def test_two():
    print("开始执行test two 方法")
    x='hello'
    assert 'e' in x

def test_three():
    print("开始执行test three 方法")
    a='hello'
    b='hello world'
    assert a in b