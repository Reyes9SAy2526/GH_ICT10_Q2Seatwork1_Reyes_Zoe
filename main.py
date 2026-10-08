# Working with lists
from pyscript import display, document
countries = ['France', 'Germany', 'Denmark', 'Monaco', 'Romania', 'Russia', 'Ireland', 'Sweden', 'Switzerland', 'Netherlands']

nicknames = ['The Hexagon', 'The Land of Poets and Thinkers', 'Land of the Danes', 'The Billionaire\'s Playground', 'The Land of Count Dracula', 'Mother Russia', 'The Emerald Isle', '"Det avlånga landet" or The Elongated Country', 'The Land of the Alps', 'The Land of Windmills']

def get_nickname(e):
    country = document.getElementById("european_countries")
    country_result = country.value
    display(nicknames[countries.index(country_result)], target="result")