from flask import current_app
from flask import render_template
from flask import request

from info.models import TagTable, GroupIDTable, GroupAttTable, SourceTable
from info.modules.mmonly import mmonly_blu



# 标签页面
@mmonly_blu.route("/tag/", methods=['GET', 'POST'])
def index():
    # 查出标签数据
    try:
        tags = TagTable.query.all()
    except Exception as e:
        current_app.logger.error(e)

    tags_li = []
    categroies = []
    for tag in tags:
        tags_li.append(tag.to_dict())
        categroies.append(tag.CATEGROY)

    data = {
        "tag":tags_li,
        "categroies":categroies
    }


    return render_template("mmonly/tag.html",data = data)

    # CATEGROY是大分类 TITLE是小分类标签


# 标签组图
@mmonly_blu.route("/tagdetail/", methods=['GET', 'POST'])
def getTagDetail():
    # 获取参数
    tag = request.args.get('tag')
    print(tag)
    page = request.args.get('p',1)
    per_page =  request.args.get('per_page',12)

    try:
        page = int(page)
        per_page = int(per_page)
    except Exception as e:
        current_app.logger.error(e)

    # 根据传入的tag 查询出tagtable对象 进一步查出categroy
    if tag:
        tag_obj = TagTable.query.filter(TagTable.TAG==tag).first()

        categroy = tag_obj.CATEGROY # 大分类
        tag_now = tag_obj.to_dict()

    # 通过大分类获取大分类下的小分类
    rec_li = []
    cat_obj = TagTable.query.filter(TagTable.CATEGROY == categroy).all()
    for cat in cat_obj:
        rec_li.append(cat.to_simple_dict())


    """获取对应标签数据"""
    source = []
    group_id = []
    total_page = None
    current_page = None
    Source_obj = []

    # 从GroupAttTable中获取mygroupid
    group_att_obj = GroupAttTable.query.filter(GroupAttTable.TAG == tag).all()
    for i in group_att_obj:
        group_id.append(i.MYGROUPID)
    # 根据mygroupid从GroupIDTable中获取数据

    paginate = GroupIDTable.query.filter(GroupIDTable.MYGROUPID.in_(group_id)).paginate(page, per_page, False)
    total_page = paginate.pages
    current_page = paginate.page
    for source_obj in paginate.items:
        source.append(source_obj.to_dict())


    data = {
        "rec" : rec_li,
        "source" : source,
        "tag": tag_now,
        "total_page": total_page,
        "current_page": current_page,
        "paginate" : paginate,
    }

    return render_template('mmonly/tagdetail.html', data=data)


# 组图详情
@mmonly_blu.route('/picdetail')
def picDetail():
    # 获得参数
    group_id = request.args.get('myGroupId') # 组图id
    page = request.args.get('p', "1")
    per_page = request.args.get("per_page", "1")

    try:
        group_id = int(group_id)
        page = int(page)
        per_page = int(per_page)
    except Exception as e:
        current_app.logger.error(e)

    paginate = SourceTable.query.filter(SourceTable.MYGROUPID == group_id).paginate(page, per_page, False)
    total_page = paginate.pages
    current_page = paginate.page
    img_li = []
    for item in paginate.items:
        img_li.append(item.to_dict())

    # 根據mygroupid通過GroupAttTable查詢對應的tagdes
    tagdes_li = []
    tagdes_obj = GroupAttTable.query.filter(GroupAttTable.MYGROUPID == group_id).all()
    for tagdes in tagdes_obj:
        tagdes_li.append(tagdes.to_dict())

    data = {
        "total_page": total_page,
        "current_page": current_page,
        "list": img_li,
        "tagdes_li": tagdes_li,
        "mygroupid": group_id,
        "paginate": paginate,
    }

    return render_template('mmonly/picdetail.html', data=data)












