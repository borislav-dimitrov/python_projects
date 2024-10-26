class Challenge:
    def __init__(self, category, name, tier, description):
        self.category = category
        self.name = name
        self.tier = tier
        self.description = description

    def dump(self):
        return {
            'category': self.category,
            'name': self.name,
            'tier': self.tier,
            'description': self.description
        }