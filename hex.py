# We'll start off addressing a hex as a list, e.g. `[3, 5, 0, 2, 1]`.
#
# Each number in the list must range from 0 to 6 inclusive and the meaning
# is described in `addressing.txt`
#
# To find the sub-hex (i.e. the hex one level finer) in any direction is
# trivial. The sub-hex in the `3` direction from `[4, 2]` is `[4, 2, 3]`.
#
# A more involved question is what's the same-level hex's address in a given
# direction?
#
# In one case, this is still trivial. If we're on a hex ending in a `0` the
# same-level hex in direction `d` has an address just replacing the `0` with
# `d`. For example


def test1():
    assert hex_in_direction([3, 5, 0], 1) == [3, 5, 1]
    assert hex_in_direction([3, 5, 0], 2) == [3, 5, 2]
    assert hex_in_direction([3, 5, 0], 3) == [3, 5, 3]
    assert hex_in_direction([3, 5, 0], 4) == [3, 5, 4]
    assert hex_in_direction([3, 5, 0], 5) == [3, 5, 5]
    assert hex_in_direction([3, 5, 0], 6) == [3, 5, 6]


# By considering the inverse we can see that if the hex addresses ends in a
# number that is the "opposite" of the direction we want to go, the new
# address just replaces the last digit with a `0`.
#
# By opposite here, we mean:
#
# 1 <-> 4
# 2 <-> 5
# 3 <-> 6


def test2():
    assert opposite(1) == 4
    assert opposite(2) == 5
    assert opposite(3) == 6
    assert opposite(4) == 1
    assert opposite(5) == 2
    assert opposite(6) == 3


def opposite(direction):
    return direction + 3 if direction < 4 else direction - 3


# and so:


def test3():
    assert hex_in_direction([3, 5, 1], 4) == [3, 5, 0]
    assert hex_in_direction([3, 5, 2], 5) == [3, 5, 0]
    assert hex_in_direction([3, 5, 3], 6) == [3, 5, 0]
    assert hex_in_direction([3, 5, 4], 1) == [3, 5, 0]
    assert hex_in_direction([3, 5, 5], 2) == [3, 5, 0]
    assert hex_in_direction([3, 5, 6], 3) == [3, 5, 0]


def hex_in_direction(start, direction):
    if start[-1] == 0:
        return start[:-1] + [direction]
    if start[-1] == opposite(direction):
        return start[:-1] + [0]


test1()
test2()
test3()

print("all tests passed.")
