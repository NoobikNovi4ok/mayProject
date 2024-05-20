from playwright.sync_api import Page, expect
import time

def test_registration(page: Page):
    page.goto('http://127.0.0.1:8000/user/registration')
    page.fill('input[name="username"]', 'Delss28')
    page.fill('input[name="email"]', 'deliss2008@mail.ru')
    page.fill('input[name="password1"]', 'Gigachad123')
    page.fill('input[name="password2"]', 'Gigachad123')
    time.sleep(5)

    page.click('button[type="submit"]')
    expect(page.get_by_text('вы успешно создали в аккаунт')).to_be_visible()
    time.sleep(10)

def test_login(page: Page):
    page.goto('http://127.0.0.1:8000/user/login')
    page.fill('input[name="username"]', 'Delss28')
    page.fill('input[name="password"]', 'Gigachad123')
    time.sleep(5)

    page.click('button[type="submit"]')
    expect(page.get_by_text('вы успешно вошли в аккаунт')).to_be_visible()
    time.sleep(10)

def test_order(page: Page):
    page.goto('http://127.0.0.1:8000/catalog')
    link = page.locator('a')
    href = link.get_attribute('href')
    assert href == 'http://127.0.0.1:8000/product/pitahajya'
    page.click('a[href="product/pitahajya"]')
    page.goto('http://127.0.0.1:8000/profile')
    page.get_by_role('link', name='Оформить заказ').click()
    page.fill('input[name="full_name"]', 'Мешков Максим Михайлович')
    page.fill('input[name="date"]', '12.12.2005')
    page.fill('input[name="address"]', 'г.Владимир ул.Горького д.49')
    page.get_by_role('link', name='Заказать').click()


    time.sleep(10)
def test_choose(page: Page):
    page.goto('http://127.0.0.1:8000/catalog')
    page.locator("xpath=/html/body/div[1]/div/div[2]/div[2]/div/a[2]").click()
    expect(page.get_by_text('Питахайя')).to_be_visible()
    time.sleep(10)

def test_catalog(page: Page):
    page.goto('http://127.0.0.1:8000')
    page.get_by_role('link', name='Каталог').click()
    expect(page.get_by_text('Дуриан')).to_be_visible()

    time.sleep(10)
def test_about(page: Page):
    page.goto('http://127.0.0.1:8000')
    page.get_by_role('link', name='О нас').click()
    expect(page.get_by_text('2015 год')).to_be_visible()
    time.sleep(10)

def test_contact(page: Page):
    page.goto('http://127.0.0.1:8000')
    page.get_by_role('link', name='Контакты').click()
    expect(page.get_by_text('Сотрудничество с поставщиками')).to_be_visible()

    time.sleep(10)