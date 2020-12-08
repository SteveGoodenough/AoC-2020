from src.day8 import count1, count2


def test_part_one():
    input_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    data = [line.split() for line in input_data.split('\n')]
    assert count1(data) == 5


def test_part_one_gets_to_end():
    input_data = """nop +0
jmp +2
acc +1
nop +0
nop +0
acc +6"""
    data = [line.split() for line in input_data.split('\n')]
    assert count1(data) == -6


def test_part_two():
    input_data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    data = [line.split() for line in input_data.split('\n')]
    assert count2(data) == 8
