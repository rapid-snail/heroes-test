
# {
#     "birthDate": "2019-02-21",
#     "city": "New York",
#     "fullName": "Doctor Strange",
#     "gender": "F",
#     "id": 122,
#     "mainSkill": "Magic",
#     "phone": "+74998884433"
#   }


class Hero:
    def __init__(self, id=None, birth_date=None, city=None, full_name=None, gender=None, main_skill=None, phone=None):

        self.id = id
        self.birth_date = birth_date
        self.city = city
        self.full_name = full_name
        self.gender = gender
        self.main_skill = main_skill
        self.phone = phone

    def init_from_dict(self, obj):
        self.id = obj.get("id")
        self.birth_date = obj.get("birthDate")
        self.city = obj.get("city")
        self.full_name = obj.get("fullName")
        self.gender = obj.get("gender")
        self.main_skill = obj.get("mainSkill")
        self.phone = obj.get("phone")
        return self

    def to_dict(self):
        res = dict()
        res["birthDate"] = self.birth_date
        res["city"] = self.city
        res["fullName"] = self.full_name
        res["gender"] = self.gender
        res["mainSkill"] = self.main_skill
        res["phone"] = self.phone
        return res

    def __repr__(self):
        s = "Hero{id=%s birth_date=%s city=%s full_name=%s gender=%s main_skill=%s phone=%s }" % (self.id,
                                                                self.birth_date,
                                                                self.city,
                                                                self.full_name,
                                                                self.gender,
                                                                self.main_skill,
                                                                self.phone)
        return s
