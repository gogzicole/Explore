def test_top_n():

    assert module.top_n([2,3,6,4,8,1,9],4) == [9,8,6,3], 'Incorrect'
    assert module.top_n([0,5,4,1,8,6],3) == [8,6,5], 'Incorrect'
    assert module.top_n([1,7,5,3,6],3) == [7,6,5], 'Incorrect'
    assert module.top_n([2,9,4,7,6,0,1],5) == [9,7,6,4,2], 'Incorrect'