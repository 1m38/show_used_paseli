# coding: utf-8

import os
import sys
import codecs
import re
import collections


import selenium
from selenium import webdriver
from bs4 import BeautifulSoup


def create_driver():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("intl.accept_languages", "ja")
    profile.update_preferences()
    driver = webdriver.Firefox(profile)
    return driver


def open_payment_page(driver):
    # login
    driver.get("https://my.konami.net/index.html")
    input("Press Enter After Login:")

    # paseli login page
    driver.find_element_by_id("service-paseli").find_element_by_link_text("チャージ").click()
    # paseli payment page
    driver.find_element_by_xpath("//a[@href='payinfo.kc']").click()
    return


def retrieve_payment_data(driver):

    total = {}

    while True:
        h = driver.find_element_by_class_name("buy_table").get_attribute("innerHTML")
        soup = BeautifulSoup(h, "html.parser")
        trs = soup.find_all("tr")
        for tr in trs[2:]:
            tds = tr.find_all("td")
            day = tds[0].text
            tp = tds[1].text
            cash = int(tds[2].text.strip("円").replace(",", ""))

            if day not in total:
                total[day] = {"pay": 0, "charge": 0}
            if tp == "チャージ":
                total[day]["charge"] += cash
            else:
                total[day]["pay"] += cash

        try:
            driver.find_element_by_xpath("//input[@value='進む']").click()
        except selenium.common.exceptions.NoSuchElementException:
            break

    # print total
    print("day\t\tpay\tcharge")
    print("------------------------")
    for day in sorted(total.keys()):
        print("{}\t{}\t{}".format(day, total[day]["pay"], total[day]["charge"]))


def main(args):
    driver = create_driver()
    open_payment_page(driver)
    retrieve_payment_data(driver)


def _main():
    import argparse
    parser = argparse.ArgumentParser()

    args = parser.parse_args()
    main(args)

    return 0


if __name__ == "__main__":
    sys.exit(_main())
