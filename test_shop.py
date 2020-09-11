from shop import judge_money


def test_judge_money_50yen():
    assert judge_money(50,100) == False

def test_judge_money_100yen():
    assert judge_money(100,100) == True    