from app.main import Car

def calculate_car_washing_price(self, car: Car) -> float:
    return round(
        car.comfort_class * (self.clean_power - car.clean_mark)
        * self.average_rating / self.distance_from_city_center,
        1
    )


def wash_single_car(self, car: Car) -> None:
    if car.clean_mark < self.clean_power:
        car.clean_mark = self.clean_power


def serve_cars(self, cars: list[Car]) -> float:
    total_income = 0.0
    for car in cars:
        if car.clean_mark < self.clean_power:
            total_income += self.calculate_car_washing_price(car)
            self.wash_single_car(car)
    return round(total_income, 1)


def rate_service(self, new_rating: int) -> None:
    total_score = self.average_rating * self.count_of_ratings + new_rating
    self.count_of_ratings += 1
    self.average_rating = round(total_score / self.count_of_ratings, 1)
