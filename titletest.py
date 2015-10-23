# -*- coding:utf-8 -*-  
def test_title(self):
    dr = self.dr
    print u"open the website...........pass"
    flagstr = dr.title
    assert"wulliam site" in dr.title
    """
    if flagstr == "wulliam site":
        print u"open the website............passed"
    else:
        print u"open the website............failed"
    """