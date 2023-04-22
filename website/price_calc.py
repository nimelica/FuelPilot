from models import db, UserCredentials, ClientInformation, FuelQuote


def calculatePricing():
    ...
    
    # 查询数据库是否有 ClientInformation 的记录
    client_info_exists = db.session.query(ClientInformation.query.exists()).scalar()

    # 查询数据库是否有 FuelQuote 的记录
    fuel_quote_exists = db.session.query(FuelQuote.query.exists()).scalar()

    if client_info_exists:
    # 执行您想要的操作
        pass

    if fuel_quote_exists:
    # 执行您想要的操作
        pass
    
    
    session = db.session()
    gallons_requested = session.query(FuelQuote.gallons_requested).filter_by(id=your_fuelquote_id).first()
    if gallons_requested > 1000:
    # do something
        10####
    else:
    # do something else
        1000####


