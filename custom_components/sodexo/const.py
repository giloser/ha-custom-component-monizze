from typing import Dict

DOMAIN = "monizze"
PLATFORM = "sensor"
DOMAIN_DATA = f"{DOMAIN}_data"

DEFAULT_ICON = "mdi:credit-card"
UNIT_OF_MEASUREMENT = "€"

ATTRIBUTION = "Data provided by https://my.monizze.be/"

LOGIN_URL = "https://my.monizze.be/en/login"
MYACCOUNT_URL = "https://my.monizze.be/en/mymonizze"

COUNTRY_PT = "Belgium"

CONF_COUNTRY = "country"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

CONF_COUNTRIES = [
    "Australia",
    "Belgium",
    "Brasil",
    "Canada",
    "Chile",
    "China",
    "Colombia",
    "Czech Republic",
    "Denmark",
    "Finland",
    "France",
    "India",
    "Indonesia",
    "Ireland",
    "Israel",
    "Italy",
    "Malaysia",
    "Mexico",
    "Middle East",
    "Netherlands",
    "Norway",
    "Peru",
    "Philippines",
    "Poland",
    COUNTRY_PT,
    "Qatar",
    "Romania",
    "Singapore",
    "South Africa",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Thailand",
    "Turkey",
    "United Arab Emirates",
    "United States",
    "United-Kingdom",
    "Vietnam"
]