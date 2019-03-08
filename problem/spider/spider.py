"""爬虫模块"""
import re

import requests

from oj.models import OJ
from problem.models import Problem
from problem.spider.backends import *


def get_problem(oj, sid):
    """爬取一道题目并返回该题目的dict"""
    # 下载题目页面
    r = requests.get(oj.problem_url % sid, timeout=10)
    r.encoding = oj.encoding
    html = r.text
    # 创建题目dict
    problem = {
        "soj": oj.name,
        "sid": sid,
    }
    # 遍历regexp进行正则提取
    for key, reg in oj.regexp.items():
        match = re.findall(reg, html)
        if not match:
            problem[key] = ""
        else:
            # 保存该字段的值
            problem[key] = match[0]
    # 替换description的相对地址为绝对地址
    problem["description"] = oj.replace_src(problem["description"])
    return problem


def crawl(oj_name):
    """爬取某oj所有题目并保存到数据库"""
    oj_backend = {
        HDU.name: HDU,
        POJ.name: POJ,
        SDUT.name: SDUT
    }[oj_name]

    oj = OJ.objects.get(name=oj_name)

    if oj.start_sid > oj.end_sid:
        raise ValueError("end_sid 不能小于 start_sid")

    # 自动探测最大sid，检测30个空白题目
    blank_cnt = 0
    sid = oj.end_sid
    while True:
        p = Problem.objects.filter(sid=sid, soj=oj_backend.name)
        if p:
            print(f'(跳过)-{p[0]}')
        else:
            problem = get_problem(oj_backend, sid)
            if not problem['title']:
                print(f'(无信息) {problem["soj"]}-{problem["sid"]}')
                blank_cnt += 1
                if blank_cnt == 30:
                    oj.end_sid = sid - 30
                    oj.save()
                    break
            else:
                blank_cnt = 0
                print(f'(新增) {Problem.objects.create(**problem)}')
                oj.end_sid = sid
                oj.save()
        sid += 1
