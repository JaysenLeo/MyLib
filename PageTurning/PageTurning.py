# _*_coding:utf-8_*_
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
    """
    :param
            page_content : content of page that is list
            page_size : length of each page (how many items of list)
            page_current : position of current page
            page_option :
                            page_first
                            page_last
                            page_up
                            page_down
                            page_jump
    """
    #logger.info("\x1B[1;32;40m********************PageTurning********************\x1B[0m")
    logger.info("********************PageTurning********************")
    try:
        # Initialize the page content
        if page_content is None:
            page_content = []

        page_count = len(page_content)
        # Statistics of the total number of pages
        if page_count % page_size > 0:
            page_total = (page_count / page_size) + 1
        else:
            page_total = (page_count / page_size)

        if page_current is not None:
            page_current_int = int(page_current)
        else:
            page_current_int = 1

        # The total number of pages 1
        if page_total is 1:
            page_current_int = 1
        # More than 1 of the total number of pages
        else:
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
        pass

def page_content_sort():
    pass


if __name__ == '__main__':
    test_list = range(33)
    while True:
        # print "\x1B[1;32;40m" +str(test_list) +"\x1B[0m"
        print '\033[1;31;40m' +str(test_list) +'\033[0m'
        # page_size = int(raw_input('page_size:'))
        # page_current = int(raw_input('page_current:'))
        page_opt = raw_input('page_option:')
        page_jump=None
        """ page_first;page_last;page_up;page_down;page_jump
        """
        print page_generator(test_list,page_size=3,page_current=1,page_opt=page_opt,page_jump=None)





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