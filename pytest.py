import inc_dec

def test_increment():
    assert inc_dec.increment(3) == 4

# 这个测试用例一定会失败，是刻意做的
def test_decrement():
    assert inc_dec.decrement(3) == 4
