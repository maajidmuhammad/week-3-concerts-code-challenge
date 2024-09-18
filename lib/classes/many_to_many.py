class Band:
    _id_counter = 1
    all = []

    def __init__(self, name, hometown):
        self._id = Band._id_counter
        Band._id_counter += 1
        self.name = name
        self.hometown = hometown
        Band.all.append(self)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._hometown = value
        else:
            raise ValueError("Hometown must be a non-empty string.")

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.band == self]

    def venues(self):
        return list(set(concert.venue for concert in self.concerts()))

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        return Concert(date, self, venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]


class Concert:
    _id_counter = 1
    all_concerts = []

    def __init__(self, date, band, venue):
        self._id = Concert._id_counter
        Concert._id_counter += 1
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all_concerts.append(self)

    @property
    def id(self):
        return self._id

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string.")

    @property
    def band(self):
        return self._band

    @property
    def venue(self):
        return self._venue

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    _id_counter = 1
    all = []

    def __init__(self, name, city):
        self._id = Venue._id_counter
        Venue._id_counter += 1
        self.name = name
        self.city = city
        Venue.all.append(self)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string.")

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.venue == self]

    def bands(self):
        return list({concert.band for concert in self.concerts()})

    def concert_on(self, date):
        return next((concert for concert in self.concerts() if concert.date == date), None)
