#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CMSeeK, check the LICENSE file for more information
# Copyright (c) 2018 - 2019 Tuhinshubhra

def start(id, url, ua, ga, source, ga_content, detection_method=''):
    if id == "wp":
        # for now this is the only cms... but not for long!
        import deepscans.wp.init as wpscan
        wpscan.start(id, url, ua, ga, source, detection_method)
    if id == 'joom':
        # told ya... not for long
        import deepscans.joom.init as joomscan
        joomscan.start(id, url, ua, ga, source)
