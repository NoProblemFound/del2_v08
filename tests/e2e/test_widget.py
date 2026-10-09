from playwright.sync_api import Page, expect

test_page = "https://lejonmanen.github.io/timer-vue/"

def test_create_timer_widget(page: Page):
    # Gå till timer-vue sidan
    page.goto(test_page)

    # Hitta knappen Add timer och klicka på den
    page.get_by_role("button", name="Add timer").click()

    # Letar efter ett element som innehåller texten: "15.00"
    # Spara resultet i variable timer
    timer = page.get_by_text("15:00")

    # Kontrollera att elementet är synligt på websidan.
    expect(timer).to_be_visible()

def test_create_note_widget(page: Page):
    # Gå till timer-vue sidan
    page.goto(test_page)

    # Hitta knappen Add note och klicka på den
    page.get_by_role("button", name="Add note").click()

    # Letar efter ett element som innehåller texten: "Click to change text"
    # Spara resultet i variable note
    note = page.get_by_text("Click to change text")

    # Kontrollera att elementet är synligt på websidan.
    expect(note).to_be_visible()


def test_remove_timer_widget(page: Page):

    page.goto(test_page)

    page.get_by_role("button", name="Add timer").click()
    expect(page.get_by_role("button", name="Start")).to_be_visible()

    # Ta bort timern
    # Hitta ett element som har klassen close och klicka på den
    page.locator(".close").click()
    # Kontrollera att timern inte längre finns
    expect(page.get_by_role("button", name="Start")).not_to_be_visible()

def test_remove_note_widget(page: Page):

    page.goto(test_page)

    page.get_by_role("button", name="Add note").click()
    note = page.get_by_text("Click to change text")
    # Kontrollera att elementet är synligt på websidan.
    expect(note).to_be_visible()

    # Ta bort anteckningswidget
    # Hitta ett element som har klassen close och klicka på den
    page.locator(".close").click()
    # Kontrollera att anteckmingswidget inte längre finns
    expect(page.get_by_text("Click to change text")).not_to_be_visible()

