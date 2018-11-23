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