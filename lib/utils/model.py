from lib.model import *


def get_model(config):

    return hgnet(config)
    '''
    # TODO delete (transformer 已经合并了) get_hwt.py 和 get_hwto.py 其实可以删除

    if config.transformer:
        # 有 transformer情况下
        if config.head_type.upper() == 'WOO':
            # 不带offset
            return hgtnet(config)
        else:
            # 带offset transformer生成offset
            return hgtonet(config)

    else:
        return hgnet(config)

    '''