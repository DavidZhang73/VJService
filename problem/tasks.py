from celery import shared_task

from .spider import spider


@shared_task
def crawl_HDU():
    spider.crawl('HDU')


@shared_task
def crawl_POJ():
    spider.crawl('POJ')


@shared_task
def crawl_SDUT():
    spider.crawl('SDUT')
