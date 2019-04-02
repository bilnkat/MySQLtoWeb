from pkg import db



class Computer(db.Model):
    __tablename__ = 'AllComputers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable = False)
    managed = db.Column(db.String(20), unique=False, nullable = False)
    username = db.Column(db.String(20), unique=False, nullable = False)
    model = db.Column(db.String(100), unique=False, nullable = False)
    department = db.Column(db.String(20), unique=False, nullable = True)
    building = db.Column(db.String(20), unique=False, nullable = True)
    mac_address = db.Column(db.String(20), unique=False, nullable = False)
    udid = db.Column(db.String(20), unique=False, nullable = False)
    serial_number = db.Column(db.String(20), unique=False, nullable = False)
    report_date_utc = db.Column(db.String(20), unique=False, nullable = False)
    report_date_epoch = db.Column(db.String(20), unique=False, nullable = False)

    def __repr__(self):
        return '{} {}'.format(self.id, self.username)