"""
ISCG5421 Practice Test - Semester 2 2020

Kris Pritchard - @krp

pytest -v test_contact_tracer.py
"""

import pytest
import contact_tracer


def test_that_location_id_is_added_to_visited_set():
    brown = contact_tracer.Person('brown@unitec.ac.nz')
    brown.visit(123)
    assert 123 in brown.visited
    
def test_that_invalidlocation_is_raised_if_negative_location_id():
    brown = contact_tracer.Person('brown@unitec.ac.nz')
    with pytest.raises(contact_tracer.InvalidLocation):
        brown.visit(-1)

def test_num_visited_locations_is_zero_if_no_visits():
    ben = contact_tracer.Person('ben@unitec.ac.nz')
    num_location_visited = ben.num_locations_visited()
    assert num_location_visited == 0

def test_num_locations_visited_gt_zero_if_visited_locations():
    wipun = contact_tracer.Person('wipun@unitec.ac.nz')
    wipun.visit(1000)
    num_locations_visited = wipun.num_locations_visited()
    assert num_locations_visited == 1

def test_assert_has_contact_returns_true_for_two_people_with_contact():
    wipun = contact_tracer.Person('wipun@unitec.ac.nz')
    ben = contact_tracer.Person('ben@unitec.ac.nz')
    wipun.visit(500)
    ben.visit(500)
    wipun_has_had_contact_with_ben = wipun.has_contact(ben)
    assert wipun_has_had_contact_with_ben == True

def test_assert_has_contact_returns_false_for_two_people_without_contact():
    wipun = contact_tracer.Person('wipun@unitec.ac.nz')
    ben = contact_tracer.Person('ben@unitec.ac.nz')
    wipun.visit(1000)
    ben.visit(500)
    wipun_has_had_contact_with_ben = wipun.has_contact(ben)
    assert wipun_has_had_contact_with_ben == False

def test_notify_returns_all_caps():
    wipun = contact_tracer.Person('wipun@unitec.ac.nz')
    notification = wipun._notify()
    assert notification == 'WIPUN@UNITEC.AC.NZ'

