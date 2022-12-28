class incident:
    def __init__(self, data):
        self.key = list(data.values())[list(data.keys()).index("INCIDENT_KEY")]
        self.code = list(data.values())[list(data.keys()).index("JURISDICTION_CODE")]


class victim:
    def __init__(self, data):
        self.age_group = list(data.values())[list(data.keys()).index("VIC_AGE_GROUP")]
        self.sex = list(data.values())[list(data.keys()).index("VIC_SEX")]
        self.race = list(data.values())[list(data.keys()).index("VIC_RACE")]


class occurence:
    def __init__(self, data):
        self.occur_date = list(data.values())[list(data.keys()).index("OCCUR_DATE")]
        self.occur_time = list(data.values())[list(data.keys()).index("OCCUR_TIME")]
        self.murder_flag = list(data.values())[list(data.keys()).index("STATISTICAL_MURDER_FLAG")]
        self.borough = list(data.values())[list(data.keys()).index("BOROUGH")]
        self.precinct = list(data.values())[list(data.keys()).index("PRECINCT")]


class union(occurence, victim, incident):
    def __init__(self, data):
        occurence.__init__(self, data=data)
        incident.__init__(self, data=data)
        victim.__init__(self, data=data)

