"""
    weasyprint.tests.test_draw.svg.test_shapes
    ------------------------------------------

    Test how SVG simple shapes are drawn.

"""

from ...testing_utils import assert_no_logs
from .. import assert_pixels


@assert_no_logs
def test_rect_stroke():
    assert_pixels('rect_stroke', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RR___RR_
        _RR___RR_
        _RR___RR_
        _RRRRRRR_
        _RRRRRRR_
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="5" height="5"
              stroke-width="2" stroke="red" fill="none" />
      </svg>
    ''')


@assert_no_logs
def test_rect_fill():
    assert_pixels('rect_fill', 9, 9, '''
        _________
        _________
        __RRRRR__
        __RRRRR__
        __RRRRR__
        __RRRRR__
        __RRRRR__
        _________
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="5" height="5" fill="red" />
      </svg>
    ''')


@assert_no_logs
def test_rect_stroke_fill():
    assert_pixels('rect_stroke_fill', 9, 9, '''
        _________
        _RRRRRRR_
        _RRRRRRR_
        _RRBBBRR_
        _RRBBBRR_
        _RRBBBRR_
        _RRRRRRR_
        _RRRRRRR_
        _________
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect x="2" y="2" width="5" height="5"
              stroke-width="2" stroke="red" fill="blue" />
      </svg>
    ''')


@assert_no_logs
def test_rect_round():
    assert_pixels('rect_round', 9, 9, '''
        _zzzzzzz_
        zzzzzzzzz
        zzRRRRRzz
        zzRRRRRzz
        zzRRRRRzz
        zzRRRRRzz
        zzRRRRRzz
        zzzzzzzzz
        _zzzzzzz_
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect width="9" height="9" fill="red" rx="4" ry="4" />
      </svg>
    ''')


@assert_no_logs
def test_rect_round_zero():
    assert_pixels('rect_round_zero', 9, 9, '''
        RRRRRRRRR
        RRRRRRRRR
        RRRRRRRRR
        RRRRRRRRR
        RRRRRRRRR
        RRRRRRRRR
        RRRRRRRRR
        RRRRRRRRR
        RRRRRRRRR
    ''', '''
      <style>
        @page { size: 9px }
        svg { display: block }
      </style>
      <svg width="9px" height="9px" xmlns="http://www.w3.org/2000/svg">
        <rect width="9" height="9" fill="red" rx="0" ry="4" />
      </svg>
    ''')