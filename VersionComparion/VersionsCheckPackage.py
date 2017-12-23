# _*_coding:utf-8_*_
"""
ModelIntroduction:

CreateDate:

ModifyDate:

ModifiedByWho:

Author:

"""

def ver_size_auth(check_ver=None, checked_ver=None):
    """
    模块名称 ：版本高低校验
    参数： 校验版本与被校验版本
    """
    # logger.info("======================================版本高低校验======================================")
    try:
        if check_ver is None:
            check_ver = []
        if checked_ver is None:
            checked_ver = []
        check_ver_len = len(check_ver)
        checked_ver_len = len(checked_ver)
        if check_ver_len != checked_ver_len:
            raise ValueError
        else:
            for each_num in range(checked_ver_len):
                len_num = 0
                if len(str(checked_ver[each_num])) == len(str(check_ver[each_num])):
                    continue
                elif len(str(checked_ver[each_num])) > len(str(check_ver[each_num])):
                    len_num = len(str(checked_ver[each_num])) - len(str(check_ver[each_num]))
                    for each_ele in xrange(len_num):
                        check_ver[each_num] = '0' + check_ver[each_num]
                else:
                    len_num = len(str(check_ver[each_num])) - len(str(checked_ver[each_num]))
                    checked_ver[each_num] = str(checked_ver[each_num])
                    for each_ele in xrange(len_num):
                        checked_ver[each_num] = '0' + checked_ver[each_num]
            if int(''.join(checked_ver)) > int(''.join(check_ver)):
                return True
            else:
                return False
    except Exception as e:
        # logging.exception("<报错>|<版本高低校验失败> 详情:" + str(e))
        pass