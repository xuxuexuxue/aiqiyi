from info import db


class MovieForm(db.Model):
    """电影分类列表"""
    __tablename__ = "categroyMovieTable"
    numid = db.Column(db.Integer,primary_key=True)
    categroy = db.Column(db.String(100))
    url = db.Column(db.String(100))
    title = db.Column(db.String(100))


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


class MovieShow(db.Model):
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
