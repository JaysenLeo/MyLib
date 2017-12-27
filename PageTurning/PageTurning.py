# -*- coding: utf-8 -*-
"""
ModelIntroduction:

CreateDate:

ModifyDate:

ModifiedByWho:

Author:

"""
import logging
import logging.config
from LogModule.conf import logconf
logging.config.fileConfig(logconf.L_URL.get('log_url_upTool'))
logger = logging.getLogger("root")
def page_generator(page_content=None, page_size=9, page_current=1, page_opt='', page_jump=None):
    '''
    参数:
            page_content : 以列表形式组织成的页内容
            page_size : length of each page (how many items of list)
            page_current : position of current page
            page_option :
                            page_first 翻到首页
                            page_last 翻到最后一页
                            page_up 翻到上一页
                            page_down 翻到下一页
                            page_jump 跳到某一页
    '''
    #logger.info("\x1B[1;32;40m********************PageTurning********************\x1B[0m")
    logger.info("********************PageTurning********************")
    try:
        # 初始化页内容
        if page_content is None:
            page_content = []
        if not isinstance(page_content, list):
            pass
            # raise
        page_count = len(page_content)
        # 统计总页数
        if page_count % page_size > 0:
            page_total = (page_count / page_size) + 1
        else:
            page_total = (page_count / page_size)

        if page_current is not None:
            page_current_int = int(page_current)
        else:
            page_current_int = 1

        # 总页数为1
        if page_total is 1:
            page_current_int = 1
        # 总页数超过1
        elif page_jump is None and page_total > 1:
            if page_opt == 'page_first':
                page_current_int = 1
            elif page_opt == 'page_last':
                page_current_int = page_total
            elif page_opt == 'page_up':
                if page_current_int is 1:
                    page_current_int = 1
                else:
                    page_current_int -= 1
            elif page_opt == 'page_down':
                if page_current_int is page_total:
                    page_current_int = page_total
                else:
                    page_current_int += 1
        elif page_jump is not None:
            page_current_int = page_jump
        else:
            pass

        # The content of the page to obtain the corresponding pages.
        if len(page_content) < page_size:
            res = page_content
        elif len(page_content[(page_current_int - 1) * page_size:]) > page_size:
            res = page_content[(page_current_int - 1) * page_size:page_current_int * page_size]
        else:
            res = page_content[(page_current_int - 1) * page_size:]

        logging.info("[Normal]|<PageTurning>Turing Page Finish")
        return {'data_list': res,
                'page_msg': {'page_count': page_count, 'page_total': page_total, 'page_current': str(page_current_int)}}
    except Exception as e:
        logging.exception("[Errors]|<PageTurning>Turing Page Errors:" + str(e))


def page_content_sort():
    pass


if __name__ == '__main__':
    test_list = range(33)
    # while True:
    # print "\x1B[1;32;40m" +str(test_list) +"\x1B[0m"
    print '\033[1;31;40m' +str(test_list) +'\033[0m'
    # page_size = int(raw_input('page_size:'))
    # page_current = int(raw_input('page_current:'))
    page_opt=None
    page_jump=2
    """ page_first;page_last;page_up;page_down;page_jump
    """
    print page_generator(test_list,page_size=3,page_current=1,page_opt=page_opt,page_jump=page_jump)





            # # The current page is the last page
            # if page_current_int is page_total:
            #     if page_opt == 'page_first':
            #         page_current_int = 1
            #     elif page_opt == 'page_last':
            #         page_current_int = page_total
            #     elif page_opt == 'page_up':
            #         page_current_int -= 1
            #     elif page_opt == 'page_down':
            #         page_current_int = page_total
            # # The current page is the first page
            # elif page_current_int is 1:
            #     if page_opt == 'page_first':
            #         page_current_int = 1
            #     elif page_opt == 'page_last':
            #         page_current_int = page_total
            #     elif page_opt == 'page_up':
            #         page_current_int = 1
            #     elif page_opt == 'page_down':
            #         page_current_int += 1
            # else:
            #     if page_opt == 'page_first':
            #         page_current_int = 1
            #     elif page_opt == 'page_last':
            #         page_current_int = page_total
            #     elif page_opt == 'page_up':
            #         page_current_int -= 1
            #     elif page_opt == 'page_down':
            #         page_current_int += 1