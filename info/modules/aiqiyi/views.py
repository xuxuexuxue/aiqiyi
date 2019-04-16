from _curses import flash

from flask import current_app
from flask import render_template
from flask import request

from info import redis_store, db
from info.models import CategoryMovie, MovieList, MovieDetail, MoviePerformer, PerformerDetail
from info.modules.aiqiyi import index_blu



@index_blu.route('/movielist/')
def index():

    # 獲取參數
    args_dict = request.args
    page = args_dict.get("p", '1')  # 非必須參數 表示分頁第幾頁 默認1
    per_page = args_dict.get("per_page", "12")  # 非必須參數 表示每頁顯示幾個 默認12
    category_id = args_dict.get("cid", '0')  # 非必須參數 表示電影列表對應的哪個分類 默認全部

    try:
        page = int(page)
        per_page = int(per_page)
        category_id = int(category_id)
    except Exception as e:
        current_app.logger.error(e)

    # 查詢分類數據
    categories = []
    try:
        categories = CategoryMovie.query.all()
    except Exception as e:
        current_app.logger.error(e)
    category_dict = []
    for category in categories:
        category_dict.append(category.to_dict())

    # 查詢電影數據
    movies = []
    title = []
    total_page = None
    current_page = None
    performer_li = []
    mov_per = ""
    mov_dict = {}
    paginate = None
    # 用戶不傳分類id或者傳入默認cid==0則分頁返回所有電影數據
    if category_id is None or category_id == 0:
        items = []
        try:
            paginate = MovieList.query.paginate(page, per_page, False)
            items = paginate.items
            total_page = paginate.pages
            current_page = paginate.page
        except Exception as e:
            current_app.logger.error(e)

        for movie in items:
            movie_id = movie.id
            mov_dict = movie.to_dict()  # 對象轉化爲電影字典
            # 從moviedetailtable表中查詢主演數據
            try:
                # 獲取每個電影對應的主演數據
                mov_per = MoviePerformer.query.filter(MoviePerformer.id == movie_id)[0]
                performer = mov_per.performer
                # 電影字典設置數據
                mov_dict['performer'] = performer
            except Exception as e:
                current_app.logger.error(e)

            movies.append(mov_dict)

    else:
        # 用戶如果傳了分類id則根據此id獲取對應的電影數據
        # 很據分類id獲取CategoryMovie表裏相應的對象
        cat_id = category_id
        cat = CategoryMovie.query.filter(CategoryMovie.numid == cat_id)

        # 查詢MovieDetail表把表裏的categroy字段包含有上述title的對象filter出來
        items = []
        # 查詢所有地區的電影
        if category_id == 28:
            for cat_id in range(31, 38):
                cat = CategoryMovie.query.filter(CategoryMovie.numid == cat_id)
                # 獲取對象對應的title數據
                title = cat[0].title
                # 查詢MovieDetail表把表裏的categroy字段包含有上述title的對象filter出來

                try:
                    paginate = MovieDetail.query.filter(MovieDetail.categroy.contains(title)).paginate(page, per_page,False)

                    items = paginate.items
                    total_page = paginate.pages
                    current_page = paginate.page
                except Exception as e:
                    current_app.logger.error(e)

                # 返回分類id所對應的電影數據
                for movie in items:
                    movie_id = movie.id  # 取出每個電影的id
                    # 用此id從MovieList中查詢每個id對應的電影對象
                    movies_obj_list = MovieList.query.filter(MovieList.id == movie_id)
                    mov = movies_obj_list[0]
                    # 添加到返回數據中
                    mov_dict = mov.to_dict()
                    try:
                        mov_per = MoviePerformer.query.filter(MoviePerformer.id == movie_id)[0]
                        performer = mov_per.performer
                        mov_dict['performer'] = performer
                    except Exception as e:
                        current_app.logger.error(e)

                    movies.append(mov_dict)

            title = '全部'
        # 查詢所有類型的電影
        elif category_id == 75:
            for cat_id in range(38, 52):
                cat = CategoryMovie.query.filter(CategoryMovie.numid == cat_id)
                # 獲取對象對應的title數據
                title = cat[0].title
                # 查詢MovieDetail表把表裏的categroy字段包含有上述title的對象filter出來

                try:
                    paginate = MovieDetail.query.filter(MovieDetail.categroy.contains(title)).paginate(page, per_page, False)

                    items = paginate.items
                    total_page = paginate.pages
                    current_page = paginate.page
                except Exception as e:
                    current_app.logger.error(e)

                # 返回分類id所對應的電影數據
                for movie in items:
                    movie_id = movie.id  # 取出每個電影的id
                    # 用此id從MovieList中查詢每個id對應的電影對象
                    movies_obj_list = MovieList.query.filter(MovieList.id == movie_id)
                    mov = movies_obj_list[0]
                    # 添加到返回數據中
                    mov_dict = mov.to_dict()
                    try:
                        mov_per = MoviePerformer.query.filter(MoviePerformer.id == movie_id)[0]
                        performer = mov_per.performer
                        mov_dict['performer'] = performer
                    except Exception as e:
                        current_app.logger.error(e)
                    movies.append(mov_dict)

            title = '全部'
        # 查詢所有規格的電影
        elif category_id == 76:
            for cat_id in range(54, 65):
                cat = CategoryMovie.query.filter(CategoryMovie.numid == cat_id)
                # 獲取對象對應的title數據
                title = cat[0].title
                # 查詢MovieDetail表把表裏的categroy字段包含有上述title的對象filter出來

                try:
                    paginate = MovieDetail.query.filter(MovieDetail.categroy.contains(title)).paginate(page, per_page,False)

                    items = paginate.items
                    total_page = paginate.pages
                    current_page = paginate.page
                except Exception as e:
                    current_app.logger.error(e)

                # 返回分類id所對應的電影數據
                for movie in items:
                    movie_id = movie.id  # 取出每個電影的id
                    # 用此id從MovieList中查詢每個id對應的電影對象
                    movies_obj_list = MovieList.query.filter(MovieList.id == movie_id)
                    mov = movies_obj_list[0]
                    # 添加到返回數據中
                    mov_dict = mov.to_dict()
                    try:
                        mov_per = MoviePerformer.query.filter(MoviePerformer.id == movie_id)[0]
                        performer = mov_per.performer
                        mov_dict['performer'] = performer
                    except Exception as e:
                        current_app.logger.error(e)
                    movies.append(mov_dict)

            title = '全部'
        # 查詢所有年代的電影
        elif category_id == 65:
            for cat_id in range(65, 74):
                cat = CategoryMovie.query.filter(CategoryMovie.numid == cat_id)
                # 獲取對象對應的title數據
                title = cat[0].title
                # 查詢MovieDetail表把表裏的categroy字段包含有上述title的對象filter出來

                try:
                    paginate = MovieDetail.query.filter(MovieDetail.categroy.contains(title)).paginate(page, per_page,False)

                    items = paginate.items
                    total_page = paginate.pages
                    current_page = paginate.page
                except Exception as e:
                    current_app.logger.error(e)

                # 返回分類id所對應的電影數據
                for movie in items:
                    movie_id = movie.id  # 取出每個電影的id
                    # 用此id從MovieList中查詢每個id對應的電影對象
                    movies_obj_list = MovieList.query.filter(MovieList.id == movie_id)
                    mov = movies_obj_list[0]
                    # 添加到返回數據中
                    mov_dict = mov.to_dict()
                    try:
                        mov_per = MoviePerformer.query.filter(MoviePerformer.id == movie_id)[0]
                        performer = mov_per.performer
                        mov_dict['performer'] = performer
                    except Exception as e:
                        current_app.logger.error(e)
                    movies.append(mov_dict)

            title = '全部'
        #查詢具體每個分類下的電影
        else:
            # 獲取對象對應的title數據
            title = cat[0].title
            try:
                paginate = MovieDetail.query.filter(MovieDetail.categroy.contains(title)).paginate(page, per_page, False)
                items = paginate.items
                total_page = paginate.pages
                current_page = paginate.page
            except Exception as e:
                current_app.logger.error(e)

            # 返回分類id所對應的電影數據
            for movie in items:
                movie_id = movie.id  # 取出每個電影的id
                # 用此id從MovieList中查詢每個id對應的電影對象
                movies_obj_list = MovieList.query.filter(MovieList.id == movie_id)
                mov = movies_obj_list[0]
                # 添加到返回數據中
                mov_dict = mov.to_dict()
                try:
                    mov_per = MoviePerformer.query.filter(MoviePerformer.id == movie_id)[0]
                    performer = mov_per.performer
                    mov_dict['performer'] = performer
                except Exception as e:
                    current_app.logger.error(e)
                movies.append(mov_dict)


    data={
        'movies':movies,
        'categories':category_dict,
        'title':title,
        'cat_id':category_id,
        'total_page':total_page,
        'current_page':current_page,
        "paginate": paginate,

    }

    return render_template('aiqiyi/index.html',data=data)




# 播放详情页
@index_blu.route('/playmovie',methods=['GET','POST'])
def playmovie():
    # 获取点击的电影id
    mov_id = request.args.get('id')

    # 从数据库查询数据
    try:
        mov_obj = MovieList.query.filter(MovieList.id == mov_id).first()
        mov_detail_obj = MovieDetail.query.filter(MovieDetail.id == mov_id).first()
        mov_cat_obj = CategoryMovie.query.filter(CategoryMovie.numid == mov_id).first()
        mov_performer_obj = MoviePerformer.query.filter(MoviePerformer.id == mov_id).first()
    except Exception as e:
        current_app.logger.error(e)

    # print(mov_obj)
    # print(mov_detail_obj.director)

    # 获取相应数据
    titls = "http://yun.baiyug.cn/vip/?url="
    mov_url_ori = mov_obj.url  # 原始url
    mov_url = titls + mov_url_ori # 拼接url
    score = mov_obj.score  # 评分
    director = mov_detail_obj.director  # 导演
    performer = mov_performer_obj.performer  # 主演
    des = mov_detail_obj.des.split(',')  # 看点 需要做切割处理
    keyword = mov_detail_obj.keyword  # 简介
    name = mov_obj.moviename  # 获取名字
    category = mov_detail_obj.categroy.split(",")  # 獲取電影分類 分割處理

    # 根据分类获取分类id
    cat_id = []
    if category:
        try:
            for i in range(0,3):
                cat_obj = CategoryMovie.query.filter(CategoryMovie.title == category[i]).first()
                cat_id.append(cat_obj.numid)
        except Exception as e:
            current_app.logger.error(e)

    data = {
        "mov_url": mov_url,
        "score": score,
        "name": name,
        "category": category,
        "director": director,
        "keyword": keyword,
        "des": des,
        "performer": performer,
        "cat_id": cat_id
    }

    return render_template('aiqiyi/playmovie.html',data=data)



# 演员详情页
@index_blu.route('/performerdetail',methods=['GET','POST'])
def performerdetail():
    # 获取参数
    name = request.args.get('name')
    try:
        performer = PerformerDetail.query.filter(PerformerDetail.name == name).first()
    except Exception as e:
        print('error')
        current_app.logger.error(e)

    data = {}
    if performer:
        data = {
            "name":performer.name if performer.name else None,
            "e_name":performer.e_name if performer.e_name else None,
            "alias": performer.alias if performer.name else None,
            "sex": performer.sex if performer.name else None,
            "bloodtype": performer.bloodtype if performer.name else None,
            "height": performer.height if performer.name else None,
            "address": performer.address if performer.name else None,
            "birthday": performer.birthday if performer.name else None,
            "constellation": performer.constellation if performer.name else None,
            "loaction": performer.location if performer.name else None,
            "ResidentAgency": performer.ResidentialAddress if performer.name else None,
            "fameyear": performer.fameyear if performer.name else None,
            "hobby": performer.hobby if performer.name else None,
            "occupation": performer.Occupation if performer.name else None,
            "weight": performer.weight if performer.name else None,
            "image": performer.image if performer.name else None,
            "des": performer.des if performer.name else None,


        }
    else:
        print('查询数据库失败')


    return render_template('aiqiyi/performerdetail.html', data=data)














