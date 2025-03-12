class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str)\
            -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self, clean_power: int, distance_from_city_center: int,
        average_rating: float, count_of_ratings: int
    ) -> None:
        self.clean_power = clean_power
        self.distance_from_city_center = distance_from_city_center
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings
