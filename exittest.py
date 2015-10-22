# -*- coding:utf-8 -*-  '
'''
Created on 2015年9月22日

@author: Administrator
'''
import time

def test_exit(self):
    dr = self.dr
    dr.find_element_by_xpath("/html/body/div[2]/div/div[2]/form/input[3]").click()
    time.sleep(1)
    errorstr3 = dr.find_element_by_id("flash-notice").text
    if errorstr3 == u"成功退出":
        flag = 1
    else:
        flag = 0
    self.assertEqual(flag,1,"Exit------failed")