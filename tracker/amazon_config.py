from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from django.shortcuts import render,HttpResponse
from django.views import View

DIRECTORY = 'tracker/reports'


BASE_URL = "http://www.amazon.de/"


def get_chrome_web_driver(options):
    return webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')

def set_gpu_as_disabled(options):
    options.add_argument('--disable-gpu')

def set_no_sand_box(options):
    options.add_argument('--no-sandbox')

def get_chrome_binary(options):
    options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')