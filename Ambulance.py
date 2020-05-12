class Brigade:
    def __init__(self, x_coordinate, y_coordinate, driver, doctor, id):
        self.id = id
        self.x = x_coordinate
        self.y = y_coordinate
        self.driver = driver
        self.doctor = doctor

class Ambulance:
    def __init__(self):
        self.brigades = []

    def add_brigade(self, x_coordinate, y_coordinate, driver, doctor):
        self.brigades.append(Brigade(x_coordinate, y_coordinate, driver, doctor, len(self.brigades) + 1))


Ambul = Ambulance()
Ambul.add_brigade(61,67, 'Васильев Семен Петрович', 'Антонов Вадим Семенович')
Ambul.add_brigade(240,349, 'Круглов Виктор Дмитриевич', 'Липин Леонид Валентинович')
Ambul.add_brigade(952,367, 'Дегтярёв Дмитрий Владимирович', 'Горов Кирилл Виталиевич')
Ambul.add_brigade(60,951, 'Сидоров Александр Степанович', 'Длиноногов Василий Евгеньевич')
Ambul.add_brigade(480,107, 'Омельченкко Антон Владиславович', 'Товин Яков Александрович')
Ambul.add_brigade(128,670, 'Субботин Денис Дмитрьевич', 'Зыков Пантелей Эльдарович')
Ambul.add_brigade(803,452, 'Егоров Леонид Романович', 'Фокин Виталий Аристархович')
Ambul.add_brigade(829,717, 'Гордеев Иван Мэлсович', 'Белов Ростислав Витальевич')
Ambul.add_brigade(534,403, 'Сорокин Тихон Кимович', 'Григорьев Севастьян Ильяович')
Ambul.add_brigade(850,553, 'Фомин Осип Богуславович', 'Лаврентьев Май Альбертович')
Ambul.add_brigade(860,610, 'Муравьёв Соломон Артёмович', 'Сысоев Август Ильяович')
Ambul.add_brigade(982,926, 'Борисов Илларион Еремеевич', 'Зуев Карл Юлианович')