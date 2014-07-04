#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from bowling import bowling

def test_total_miss():
    assert_equals(bowling("--------------------"),0)
    
def test_karin_miss():
    assert_equals(bowling("1-1-1-1-1-1-1-1-1-1-"),10)

def test_low_score():
    assert_equals(bowling("11111111111111111111"),20)

def test_final_spare():
    assert_equals(bowling("1111111111111111111/1"),29)
    
def test_slash_irnxwo():
    assert_equals(bowling("1/11111111111111111/1"),38)

def test_final_x():
    assert_equals(bowling("111111111111111111X11"),30)

def test_good_game():
    assert_equals(bowling("1111X111111111111X11"),40)

def test_last_frame_full():
    assert_equals(bowling("11 11 X 11 11 11 11 11 11 XXX"),58)

def test_perfect_game():
    assert_equals(bowling("X X X X X X X X X XXX"),300)
    
def test_fast_perfect_game():
    assert_equals(bowling("X X 3/ X X X X X X XXX"),273)

def test_999():
    assert_equals(bowling("9-9-9-9-9-9-9-9-9-9-"), 90)

def test_5slash():
    assert_equals(bowling("5/5/5/5/5/5/5/5/5/5/5"), 150)

def test_168():
    assert_equals(bowling("X7/729/XXX236/7/3"), 168)

def test_final():
    assert_equals(bowling("111111111111111111X--"),28)

def test_final2():
    assert_equals(bowling("1111111111111111111/-"),28)

def test_final677():
    assert_equals(bowling("111111111111111111X-/"),38)

