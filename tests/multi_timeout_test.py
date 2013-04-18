#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-
# vi:ts=4:et

import pycurl
import unittest

class MultiTimeoutTest(unittest.TestCase):
    def test_multi_timeout_small(self):
        m = pycurl.CurlMulti()
        m.setopt(pycurl.M_PIPELINING, 1)
        print(m.timeout())
