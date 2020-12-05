import pytest
from src.day5 import count1, count2, calc_id


@pytest.mark.parametrize(
    "ticket, expected_id", [
        ('FBFBBFFRLR', 357),
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820),
        ('FFFFFFFLLL', 0),
        ('BBBBBBBRRR', 1023),
    ]
)
def test_calc_ticket_id(ticket, expected_id):
    id = calc_id(ticket)
    assert id == expected_id


def test_calc_max_id():
    tickets = [
        'FBFBBFFRLR',
        'BBFFBBFRLL',
        'BFFFBBFRRR',
        'FFFBBBFRRR',
        'FFFFFFFLLL',
    ]
    max_id = count1(tickets)
    assert max_id == 820


def test_calc_find_seat():
    tickets = _get_tickets(low=50, high=100, skip=88)
    id = count2(tickets)
    assert id == 88


def _get_tickets(low, high, skip):
    tickets = []
    for i in range(low, high):
        if i == skip:
            continue
        b_ticket = '{0:b}'.format(i).zfill(10)
        ticket = b_ticket[:7].replace('0', 'F').replace('1', 'B') + b_ticket[-3:].replace('0', 'L').replace('1', 'R')
        tickets.append(ticket)
    return tickets
