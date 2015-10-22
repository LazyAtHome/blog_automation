# -*- coding:utf-8 -*-  '
'''
Created on 2015年9月22日

@author: Administrator
'''
import time

def test_delete(self):
    dr = self.dr
    dr.find_element_by_xpath("//a[@href='/admin/blog/61']").click()
    time.sleep(1)
    confirm  = dr.switch_to_alert()
    confirm.accept()
    time.sleep(1)
    try:
        dr.find_element_by_xpath("//a[@href='/admin/blog/61']")
        flag = 1
    except:
        flag = 0
    #self.verifyEquals(flag,0,"new's delete------failed")
    self.assertEquals(flag,0,"new's delete------failed")
    """
    try:
        dr.find_element_by_xpath("//a[@href='/admin/blog/48']")
        isdel = False
    except:
        isdel = True
    if isdel == True:
         print u"删除操作............passed"
    else:
         print u"删除操作............failed"
    """

