############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType('musk', '1998', 'green', True, True, 'muskmelon')
    casaba = MelonType('cas', '2003', 'orange', False, False, 'casaba')
    crenshaw = MelonType('cren', '1996', 'green', False, False, 'crenshaw')
    yellow_watermelon = MelonType('yw', '2013', 'yellow', False, True, 'yellow watermelon')

    muskmelon.add_pairing(['mint'])
    casaba.add_pairing(['mint', 'strawberies'])
    crenshaw.add_pairing(['proscuitto'])
    yellow_watermelon.add_pairing(['ice cream'])

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"\n{melon.name.capitalize()} pairs well with")
        for food in melon.pairings: #<-----reference init
            print (f"- {food}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    return {m.code: m for m in melon_types}


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, type, shape_rating, color_rating, field, employee):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.employee = employee

    def is_sellable(self):
        """Calculates if a melon passes quality control"""

        shape_score = 5
        color_score = 5
        bad_field = 3

        return self.shape_rating > shape_score and self.color_rating > color_score and self.field != bad_field


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_codes = make_melon_type_lookup(melon_types)
    melons = [
        Melon(melon_codes['yw'], 8, 7, 2, 'Sheila'),
        Melon(melon_codes['yw'], 3, 4, 2, 'Sheila'),
        Melon(melon_codes['yw'], 9, 8, 3, 'Sheila'),
        Melon(melon_codes['cas'], 10, 6, 35, 'Sheila'),
        Melon(melon_codes['cren'], 8, 9, 35, 'Michael'),
        Melon(melon_codes['cren'], 8, 2, 35, 'Michael'),
        Melon(melon_codes['cren'], 2, 3, 4, 'Michael'),
        Melon(melon_codes['musk'], 6, 7, 4, 'Sheila'),
        Melon(melon_codes['yw'], 7, 10, 3, 'Sheila')
    ]

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for m in melons:
        sellable = "(CAN BE SOLD)" if m.is_sellable() else "(NOT SELLABLE)"
        print(f"Harvested by {m.employee} from Field {m.field} {sellable}")
