import re


with open('11_12.txt','r',encoding='utf-8') as f:
    content = f.read()
    movies_name = re.findall('<a href="https://movie.douban.com/subject/\d+/"  class="">(.*?)/', content, re.S)
    movie_year = re.findall('<span class="rating_nums">(.*?)</span>', content, re.S)

    with open('movie_name.txt', 'w') as m_n:
        if len(movie_year) == len(movies_name):
            for i in range(0, len(movies_name)):
                m_n.write(movies_name[i] + '----' + movie_year[i] + '\n')
                i += 1