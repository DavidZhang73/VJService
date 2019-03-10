from celery import shared_task

from submission.judger import judger


@shared_task
def submit(soj, sid, code, lang, id):
    judger.judge(soj, sid, code, lang, id)
