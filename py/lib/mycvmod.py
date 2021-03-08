#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

class MyCv():
    def __init__(self):
        pass

    def hconcat(self, img_list, itp=cv2.INTER_CUBIC):
        l = []
        for i in img_list:
            if len(i.shape) == 3:
                l.append(i)
            else:
                bgr = cv2.cvtColor(i, cv2.COLOR_GRAY2BGR)
                l.append(bgr)
        h_min = min(i.shape[0] for i in l)
        img_list_resize = [cv2.resize(i, (int(i.shape[1] * h_min / i.shape[0]), h_min), interpolation=itp) for i in l]
        return cv2.hconcat(img_list_resize)

    def vconcat(self, img_list, itp=cv2.INTER_CUBIC):
        w_min = min(i.shape[1] for i in img_list)
        img_list_resize = [cv2.resize(i, (w_min, int(i.shape[0] * w_min / i.shape[1])), interpolation=itp) for i in img_list]
        return cv2.vconcat(img_list_resize)

    def tile(self, img_list_2d, itp=cv2.INTER_CUBIC):
        img_list_v = [self.hconcat(img_list_h, itp) for img_list_h in img_list_2d]
        return self.vconcat(img_list_v, itp)

