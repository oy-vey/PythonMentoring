import pytest
from tasks import *

namespace = dir()

@pytest.mark.skipif('task1' not in namespace,reason="Task hasn't been found...")
def test_task1():
    assert task1.cumsum([]) == [0]
    assert task1.cumsum([0]) == [0, 0]
    assert task1.cumsum([1,2,3]) == [0, 1, 3, 6]
    assert task1.cumsum([-1]) == [0, -1]
    test_l = list(range(1,1000))
    output_l = [0]
    for i in test_l[0:]:
        output_l.append(output_l[-1]+i)
    assert task1.cumsum(test_l) == output_l
    
@pytest.mark.skipif('task2' not in namespace,reason="Task hasn't been found...")
def test_task2():
    assert task2.trim([-1, 0, 2, 3], 1, 2) == [1, 1, 2, 2]
    assert task2.trim([-1, 0, 2, 3], 3, 4) == [3, 3, 3, 3]
    assert task2.trim([0], 0, 0) == [0]

@pytest.mark.skipif('task4' not in namespace,reason="Task hasn't been found...")
def test_task4():
    assert task4.factorize(12) == [(2,2),(3,1)]
    assert task4.factorize(2) == [(2,1)]
    assert task4.factorize(14) == [(2,1),(7,1)] 
    

@pytest.mark.skipif('task5' not in namespace,reason="Task hasn't been found...")
def test_task5():
    
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
    """
    assert task5.get_links(html_doc) == ["http://example.com/elsie", "http://example.com/lacie", "http://example.com/tillie"]