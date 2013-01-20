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
# `d`. For example:


def test1():
    assert hex_in_direction([3, 5, 0], 1) == [3, 5, 1]
    assert hex_in_direction([3, 5, 0], 2) == [3, 5, 2]
    assert hex_in_direction([3, 5, 0], 3) == [3, 5, 3]
    assert hex_in_direction([3, 5, 0], 4) == [3, 5, 4]
    assert hex_in_direction([3, 5, 0], 5) == [3, 5, 5]
    assert hex_in_direction([3, 5, 0], 6) == [3, 5, 6]


# You can see that in this diagram:
#        __________
#       /\        /\
#      /  \  6   /  \
#     /    \____/    \
#    /  5  /    \  1  \
#   /_____/   0  \_____\
#   \     \      /     /
#    \  4  \____/  2  /
#     \    /    \    /
#      \  /  3   \  /
#       \/________\/
#
#
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


# From the diagram we can see other specific directions:
#
# from .1, .6 is in direction 5 and .2 is in direction 3
# from .2, .1 is in direction 6 and .3 is in direction 4
# from .3, .2 is in direction 1 and .4 is in direction 5
# from .4, .3 is in direction 2 and .5 is in direction 6
# from .5, .4 is in direction 3 and .6 is in direction 1
# from .6, .5 is in direction 4 and .1 is in direction 2

def test4():
    assert hex_in_direction([3, 5, 1], 5) == [3, 5, 6]
    assert hex_in_direction([3, 5, 2], 6) == [3, 5, 1]
    assert hex_in_direction([3, 5, 3], 1) == [3, 5, 2]
    assert hex_in_direction([3, 5, 4], 2) == [3, 5, 3]
    assert hex_in_direction([3, 5, 5], 3) == [3, 5, 4]
    assert hex_in_direction([3, 5, 6], 4) == [3, 5, 5]
    assert hex_in_direction([3, 5, 1], 3) == [3, 5, 2]
    assert hex_in_direction([3, 5, 2], 4) == [3, 5, 3]
    assert hex_in_direction([3, 5, 3], 5) == [3, 5, 4]
    assert hex_in_direction([3, 5, 4], 6) == [3, 5, 5]
    assert hex_in_direction([3, 5, 5], 1) == [3, 5, 6]
    assert hex_in_direction([3, 5, 6], 2) == [3, 5, 1]

# Notice that the .1 in direction 5 is the same as the .5 in the direction 1
# and so on.
#
# .1 -5-> == .5 -1-> == .6
# .2 -6-> == .6 -2-> == .1
# .3 -1-> == .1 -3-> == .2
# .4 -2-> == .2 -4-> == .3
# .5 -3-> == .3 -5-> == .4
# .6 -4-> == .4 -6-> == .5
#
# The result is just the number "in between", with the proviso that 6 is
# between 5 and 1 and 1 is between 6 and 2.
#
# if we call the tail address t and the direction d then:
#
#     if (t - d) == 2, result is d + 1 (== t - 1)
#     if (t - d) == -2, result is d - 1 (== t + 1)


# We're now handling 24 out of 36 possible situations.

# Here is our solution so far:

def hex_in_direction(start, direction):
    if start[-1] == 0:
        return start[:-1] + [direction]
    if start[-1] == opposite(direction):
        return start[:-1] + [0]
    if start[-1] - direction == 2:
        return start[:-1] + [direction + 1]
    if start[-1] - direction == -2:
        return start[:-1] + [direction - 1]
    if abs(start[-1] - direction) == 4:
        return start[:-1] + [mod6((start[-1] + 6 + direction) / 2)]


# Because our directions go 1 thru 6 rather than 0 thru 5, we can't just
# use % 6 so we instead use the following:

def mod6(n):
    return ((n - 1) % 6 + 1)

# Let's prove it passes the tests:

test1()
test2()
test3()
test4()


print("all tests passed.")
