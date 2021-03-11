class BasePage():
    def __init__ (self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


# print(type(open))
# print(type(BasePage))

# class Car():
#
#     wheelsAmount = 4
#     def __init__(self, make, color, year):
#         self.make = make
#         self.color = color
#         self.year = year
#
#
# carMazda = Car("Mazda", "red", "2019")
# carNissan = Car("Nissan", "silver", "2015")
#
# print(carNissan.wheelsAmount)
# paulcamperLoginPage = BasePage(browser, "url")
# paulcamperLoginPage.open()