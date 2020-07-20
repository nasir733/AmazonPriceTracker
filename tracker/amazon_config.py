from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from django.shortcuts import render,HttpResponse
from django.views import View

DIRECTORY = 'tracker/reports'


BASE_URL = "http://www.amazon.de/"


def get_chrome_web_driver(options):
    return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)


def get_web_driver_options():
    return webdriver.FirefoxOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')
