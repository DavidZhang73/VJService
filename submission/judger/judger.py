import datetime

from oj.models import Language, Account
from submission.judger.support import HDU, POJ, SDUT
from submission.models import Submission


def judge(soj, sid, code, lang, id):
    lang_code = Language.objects.get(name=lang).code
    oj = {
        'POJ': POJ.Runner,
        'HDU': HDU.Runner,
        'SDUT': SDUT.Runner,
    }[soj]
    account = Account.objects.get(oj__name=soj)
    account_info = {
        "username": account.username,
        "password": account.password,
        "nickname": account.nickname,
    }
    print(account_info)
    result = oj(account=account_info,
                timeout=3,
                time_interval=0.2
                ).judge(sid=sid,
                        language=lang_code,
                        code=code
                        )
    #  (28490573, 'Compilation Error', 0, 0, '0_0_28490573_8835.cpp\r\n0_0_28490573_8835.cpp(1) : error C20
    # 59: 语法错误:“数字上的错误后缀”\r\n0_0_28490573_8835.cpp(1) : error C2059: 语法错误:“常量”\r\n')
    submission = Submission.objects.get(id=id)
    submission.runid = result[0]
    submission.status = result[1]
    submission.timeused = result[2]
    submission.memoryused = result[3]
    submission.errorinfo = result[4]
    submission.judge_datetime = datetime.datetime.now()
    submission.save()
