import time,datetime
from info import db

# 爱奇艺的模型类
class CategoryMovie(db.Model):
    """电影分类列表"""
    __tablename__ = "categroyMovieTable"
    numid = db.Column(db.Integer,primary_key=True)
    categroy = db.Column(db.String(100))
    url = db.Column(db.String(100))
    title = db.Column(db.String(100))
    source = db.Column(db.String(100))

    def to_dict(self):
        resp_dict = {
            "numid": self.numid,
            "categroy": self.categroy,
            "source": self.source,
            "url": self.url,
            "title":self.title,
        }
        return resp_dict


class MovieDetail(db.Model):
    """电影详情页"""
    __tablename__ = "moviedetailtable"
    id = db.Column(db.Integer,primary_key=True)
    director = db.Column(db.String(100))
    keyword = db.Column(db.String(500))
    categroy = db.Column(db.String(500))
    des = db.Column(db.String(3000))


class MoviePerformer(db.Model):
    """演员列表"""
    __tablename__ = "movieperformertable"
    id = db.Column(db.Integer,primary_key=True)
    performer = db.Column(db.String(100))
    role = db.Column(db.String(255))


class MovieList(db.Model):
    """电影列表"""
    __tablename__ = "movietable"
    id = db.Column(db.Integer,primary_key=True)
    moviename = db.Column(db.String(100))
    time = db.Column(db.String(100))
    url = db.Column(db.String(500))
    imagepath = db.Column(db.String(2000))
    saveimagepath = db.Column(db.String(500))
    score = db.Column(db.Float(10, 1))
    status = db.Column(db.Integer)
    source = db.Column(db.String(10))

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "moviename": self.moviename,
            "time": self.time,
            "url": self.url,
            "imagepath": self.imagepath if self.imagepath else None,
            "saveimagepath": self.saveimagepath if self.saveimagepath else None,
            "score": self.score,
            "status": self.status,
            "source": self.source,
            "performer": "",
        }
        return resp_dict


class MovieUrl(db.Model):
    """电影URL"""
    __tablename__ = "movieurl"
    id = db.Column(db.Integer,primary_key=True)
    movieurl = db.Column(db.String(255))


class PerformerDetail(db.Model):
    """演员详情"""
    __tablename__ = "performerdetailtable"
    name = db.Column(db.String(100),primary_key=True)
    e_name = db.Column(db.String(100))
    alias = db.Column(db.String(200))
    sex = db.Column(db.String(10))
    bloodtype = db.Column(db.String(5))
    height = db.Column(db.String(10))
    address = db.Column(db.String(500))
    birthday = db.Column(db.String(50))
    constellation = db.Column(db.String(500))
    location = db.Column(db.String(200))
    ResidentialAddress = db.Column(db.String(100))
    school = db.Column(db.String(200))
    BrokerageAgency = db.Column(db.String(200))
    fameyear = db.Column(db.String(200))
    hobby = db.Column(db.String(1000))
    Occupation = db.Column(db.String(500))
    weight = db.Column(db.String(500))
    image = db.Column(db.String(1000))
    des = db.Column(db.String(200))



# mmonly的模型类
class TagTable(db.Model):
    """分类标签"""
    __tablename__ = "TagTable"

    NUMID = db.Column(db.Integer,primary_key=True)
    CATEGROY = db.Column(db.String(100))  # 大分类
    TAG = db.Column(db.String(100))  # 小分类
    TAGDES = db.Column(db.String(1000))  # 分类描述
    TITLE = db.Column(db.String(1000))  # 标题
    IMAGEPATH = db.Column(db.String(300))  # 文件地址

    def to_dict(self):
        resp_dict = {
            "numid": self.NUMID,
            "categroy": self.CATEGROY,
            "tag": self.TAG,
            "tagdes": self.TAGDES,
            "title": self.TITLE,
            "imagepath": self.IMAGEPATH,

        }
        return resp_dict

    def to_simple_dict(self):
        resp_dict = {
            "categroy": self.CATEGROY,
            "tag": self.TAG,
            "title": self.TITLE,
        }
        return resp_dict


class GroupIDTable(db.Model):
    """分類及標籤"""
    __tablename__ = "GroupIDTable"

    GROUPID = db.Column(db.Integer, primary_key=True)
    HEADERIMAGEPATH = db.Column(db.String(200))  # 大分類
    PHOTODES = db.Column(db.String(200))  # 小分類
    CREATERTIME = db.Column(db.String(200))  # 描述
    SIZE = db.Column(db.String(2000))  # 標題
    PATH = db.Column(db.String(200))  # 文件地址
    SAVEIMAGEPATH = db.Column(db.String(200))
    USERID = db.Column(db.String(10))
    STATUS = db.Column(db.String(10))
    SOURCE = db.Column(db.String(100))
    MYGROUPID = db.Column(db.Integer)


    def to_dict(self):
        resp_dict = {
            "groupid": self.GROUPID,
            "headerimagepath": self.HEADERIMAGEPATH,
            "photodes": self.PHOTODES,
            # 時間戳與時間元祖與格式化時間的轉換
            "creatertime": time.strftime("%Y--%m--%d %H:%M:%S",  time.localtime(int(self.CREATERTIME))),
            "size": self.SIZE,
            "path": self.PATH,
            "saveimagepath": self.SAVEIMAGEPATH,
            "userid": self.USERID,
            "status": self.STATUS,
            "source": self.SOURCE,
            "mygroupid": self.MYGROUPID,
        }
        return resp_dict


class GroupAttTable(db.Model):
    """分類及標籤"""
    __tablename__ = "GroupAttTable"

    id = db.Column(db.Integer, primary_key=True)
    MYGROUPID = db.Column(db.String(100))
    TAG = db.Column(db.String(100))  # 大分類
    TAGDES = db.Column(db.String(100))  # 小分類

    def to_dict(self):
        resp_dict = {
            "groupid": int(self.MYGROUPID),
            "tag": self.TAG,
            "tagdes": self.TAGDES,
        }
        return resp_dict


class SourceTable(db.Model):
    """分類及標籤"""
    __tablename__ = "SourceTable"

    id = db.Column(db.Integer, primary_key=True)
    MYGROUPID = db.Column(db.String(100))
    NETURL = db.Column(db.String(200))  # 大分類
    PHOTOSAVEPATH = db.Column(db.String(100))  # 小分類
    PICTUREDES = db.Column(db.String(1000))
    CREATETIME = db.Column(db.String(100))
    USERID = db.Column(db.String(100))
    SOURCE = db.Column(db.String(11))

    def to_dict(self):
        resp_dict = {
            "groupid": self.MYGROUPID,
            "neturl": self.NETURL,
            "photosavepath": self.PHOTOSAVEPATH,
            "picturedes": self.PICTUREDES,
            "createtime": time.strftime("%Y--%m--%d %H:%M:%S",  time.localtime(int(self.CREATETIME))),
            "userid": self.USERID,
            "source": self.SOURCE,

        }
        return resp_dict









