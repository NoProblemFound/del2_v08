from playwright.sync_api import Page, expect

test_page = "https://lejonmanen.github.io/timer-vue/"

def test_change_timer_to_5_minutes(page: Page):
    # Gå till sidan
    page.goto(test_page)

    # Skapa en timer
    page.get_by_role("button", name="Add timer").click()

    # Klicka på kugghjulet
    page.locator(".settings").click()

    # Skriv in 5 minuter
    minute_input = page.locator("input").nth(1)

    minute_input.fill("5")

    # Tryck Enter för att spara
    minute_input.press("Enter")

    # Klicka på Reset för att uppdatera timern
    # Det borde räcka att användaren trycker på Enter
    page.get_by_role("button", name="Reset").click()

    # Kontrollera att timern visar 05:00
    expect(page.get_by_text("05:00")).to_be_visible()

    # Starta timern
    page.get_by_role("button", name="Start").click()

    # Kontrollera att timern räknar ner
    expect(page.get_by_text("05:00")).not_to_be_visible()