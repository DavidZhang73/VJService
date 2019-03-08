"""杭州电子科技大学"""

name = "HDU"

problem_url = "http://acm.hdu.edu.cn/showproblem.php?pid=%d"

encoding = "gbk"

regexp = {
    "title": r"<h1 style='color:#1A5CC8'>(.+?)<\/h1>",
    "time_limit": r"Time Limit: \d+\/(\d+) MS",
    "memory_limit": r"Memory Limit: \d+\/(\d+) K",
    "description": r"Problem Description<\/div> <div class=panel_content>([.\s\S]+?)<\/div><div class=panel_bottom>",
    "input": r"Input<\/div> <div class=panel_content>([.\s\S]+?)<\/div><div class=panel_bottom>",
    "output": r"Output<\/div> <div class=panel_content>([.\s\S]+?)<\/div><div class=panel_bottom>",
    "sample_input": r"Sample Input<\/div><div class=panel_content><pre>([.\s\S]+?)<\/pre><\/div><div class=panel_bottom>",
    "sample_output": r"Sample Output<\/div><div class=panel_content><pre>([.\s\S]+?)<\/pre><\/div><div class=panel_bottom>",
    "source": r"Source</div> <div class=panel_content> <a href=.+?>([.\s\S]+?)</a> </div>",
}


def replace_src(description):
    return description.replace(r"src=", r"src=http://acm.hdu.edu.cn/")
