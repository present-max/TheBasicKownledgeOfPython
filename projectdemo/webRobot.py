import requests#发送http请求
from lxml import html#解析html（支持xpath语法：定位html中标签的位置））
import csv#csv文件(就是一个表格，个数据以逗号隔开)操作
import re#正则表达式

URL_TOP="https://www.themoviedb.org/movie/top-rated"
URL_DETAIL="https://www.themoviedb.org"
URL_PAGE="https://www.themoviedb.org/discover/movie/items"
CSV_FILE="resourse/movie_top100.csv"

#获取电影的详细信息
def get_movie_detail(url):
    #请求电影详情
    response = requests.get(url,timeout=60)
    #解析电影详情     #将响应内容（就是http返回的html内容）转换为html文档
    document =html.fromstring(response.text)
    movie_names=document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/a/text()')#电影名
    movie_years=document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/h2/span/text()')#年份
    movie_times=document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[2]/text()')#上映时间
    movie_type=document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[3]/a/text()')#类型
    movie_cost_times=document.xpath('//*[@id="original_header"]/div[2]/section/div[1]/div/span[4]/text()')#时长
    movie_score=document.xpath('//*[@id="consensus_pill"]/div/div[1]/div/div/@data-percent')#评分
    movie_languages=document.xpath('//*[@id="media_v4"]/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()')#语言
    movie_directors=document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()')#导演
    movie_anchor=document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/ol/li[5]/p[1]/a/text()')#作者
    movie_slogans=document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/h3[1]/text()')#宣传语
    movie_discription=document.xpath('//*[@id="original_header"]/div[2]/section/div[3]/div/p/text()')#简介

    #将电影详情封装成字典
    movie_detail={
        "电影名":movie_names[0].strip() if movie_names else "",
        "年份":get_movie_year(movie_years),
        "上映时间":get_movie_publish(movie_times),
        "类型":",".join(movie_type)if movie_type else "",
        "时长":get_movie_time(movie_cost_times),
        "评分":movie_score[0].strip() if movie_score else "",
        "语言":movie_languages[0].strip() if movie_languages else "",
        "导演":movie_directors[0].strip() if movie_directors else "",
        "作者":movie_anchor[0].strip() if movie_anchor else "",
        "宣传语":movie_slogans[0].strip() if movie_slogans else "",
        "简介":movie_discription[0].strip() if movie_discription else "",
    }
    print(f"查询到电影：{movie_detail}")
    return movie_detail

#获取电影年份
def get_movie_year(movie_years):
    movie_year=movie_years[0].strip() if movie_years else ""
    movie_year.replace("(","")
    movie_year.replace(")","")
    return movie_year

#获取电影上映时间
def get_movie_publish(movie_times):
    movie_publish=movie_times[0].strip() if movie_times else ""
    #r表示原始字符串，不进行转义
    return re.search(r"\d{4}-\d{2}-\d{2}", movie_publish).group()

#获取电影时长
def get_movie_time(movie_cost_times):
    movie_time=movie_cost_times[0].strip() if movie_cost_times else ""
    hour=re.search(r"(\d+)h", movie_time)
    minute=re.search(r"(\d+)m", movie_time)
    h=int(hour.group(1)) if hour else 0
    m=int(minute.group(1)) if minute else 0
    return h*60+m

#保存所有电影信息到csv文件
def save_all_movie(all_movie):
    with open(CSV_FILE,'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['电影名', '年份', '上映时间', '类型', '时长', '评分', '语言', '导演', '作者', '宣传语', '简介']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_movie)

def main():
    all_movie = []
    # 循环请求电影列表
    for i in range(1, 6):
        # 请求电影列表
        if i == 1:
            response = requests.get(URL_TOP, timeout=60)
        else:
            response = requests.post(URL_PAGE ,
                                     f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={i}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-02-28&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400"
                                     ,timeout=60)
        # 解析电影列表
        document = html.fromstring(response.text)
        movie_list = document.xpath(
            f'//*[@id="page_{i}"]/div/div/div[@class="w-full overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-colors hover:border-gray-300"]')
        # 查询电影的详细信息
        for movie in movie_list:
            # 获取电影的url
            movie_url = movie.xpath('.//div/div/a/@href')
            if movie_url:
                movie_url = URL_DETAIL + movie_url[0]
                # 获取电影的详细信息
                movie_detail = get_movie_detail(movie_url)
                all_movie.append(movie_detail)
    #将数据保存到csv文件
    save_all_movie(all_movie)


if __name__ == '__main__':
    main()
