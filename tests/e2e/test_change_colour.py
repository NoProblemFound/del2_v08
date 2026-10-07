import re
from playwright.sync_api import Page, expect

test_page = "https://lejonmanen.github.io/timer-vue/"
def test_change_theme_to_dark(page: Page):

    # Går till webbsidan
    page.goto(test_page)

    # Letar upp en knapp som heter Dark och klickar på den.
    page.get_by_role("button", name="Dark").click()

    # Hitta webbsidans html-element
    ett_html = page.locator("html")

    # Kontrollera att html-elementet har attributet "data-theme"
    # och har värdet "dark"
    expect(ett_html).to_have_attribute("data-theme", "dark")

def test_change_theme_to_forest(page: Page):
    page.goto(test_page)
    page.get_by_role("button", name="Forest").click()
    html = page.locator("html")
    expect(html).to_have_attribute("data-theme", "forest")

def test_change_theme_to_light(page: Page):
    page.goto(test_page)
    page.get_by_role("button", name="Light").click()
    html = page.locator("html")
    expect(html).to_have_attribute("data-theme", "")