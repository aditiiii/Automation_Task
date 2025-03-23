import re
import time

import playwright
from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_run(playwright:Playwright) :
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Products").click()
    page.get_by_role("textbox", name="Search Product").click()
    page.get_by_role("textbox", name="Search Product").fill("women")
    page.get_by_role("textbox", name="Search Product").press("Enter")
    page.get_by_role("button", name="").click()
    time.sleep(5)



def test_run2(playwright: Playwright) :
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://automationexercise.com/")
    page.get_by_role("link", name="Home").click()
    page.locator("div:nth-child(4) > .product-image-wrapper > .choose > .nav > li > a").click()
    page.get_by_role("heading", name="Men Tshirt").click()
    page.get_by_text("Rs.").click()
    page.locator("#quantity").click()
    page.locator("#quantity").fill("4")
    time.sleep(5)
    page.get_by_text("Availability: In Stock").click()
    page.get_by_role("button", name="Add to cart").click()
    page.get_by_role("link", name="View Cart").click()
    page.get_by_role("link", name="Product Image").click()
    page.get_by_role("button", name="4").click()
    time.sleep(5)

