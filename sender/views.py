# Create your views here.
from django.views import View
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from django.shortcuts import render


def teplosteti(account_number, account_surname, account_phone_number, hot_water):
    driver = webdriver.Firefox()
    try:
        driver.get('http://teploseti.zp.ua')
        wait = WebDriverWait(driver, 10)
        send_values_button = driver.find_element_by_xpath("//a[@class='root-item'][@href='/ua/abonent/']")
        send_values_button.click()
        account_number_field = wait.until(expected_conditions.presence_of_element_located((By.ID, 'account_input')))
        account_number_field.send_keys(account_number)
        account_surname_field = driver.find_element_by_id('name_input')
        account_surname_field.send_keys(account_surname)
        check_button = \
            driver.find_element_by_xpath("//input[@value='Перевірити відповідності'][@type='submit'][@tabindex='3']")
        check_button.click()
        counter_field = wait.until(expected_conditions.presence_of_element_located((By.ID, 'val_input')))
        counter_field.send_keys(hot_water)
        phone_number_field = driver.find_element_by_id('phone_input')
        phone_number_field.send_keys(account_phone_number)
        submit_button = \
            driver.find_element_by_xpath("//input[@type='submit'][@tabindex='4'][@value='Надати показання']")
        submit_button.click()
        logout_button = wait.until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Завершити роботу')))
        logout_button.click()
        return True
    except Exception:
        return False
    finally:
        driver.quit()


def oblenergo(account_number, account_phone_number, elektro):
    driver = webdriver.Firefox()
    try:
        driver.get('http://www.zoe.com.ua/pokazania.php')
        wait = WebDriverWait(driver, 10)
        organization_dropdown = wait.until(expected_conditions.presence_of_element_located((By.ID, 'rem')))
        organization_choose = Select(organization_dropdown)
        organization_choose.select_by_visible_text('Запорізькі міські електричні мережі')
        counter_field = driver.find_element_by_id('pokazaniya_p')
        counter_field.send_keys(elektro)
        account_number_field = driver.find_element_by_id('nomber_facture_p')
        account_number_field.send_keys(account_number)
        phone_number_field = driver.find_element_by_id('phonenumber_p')
        phone_number_field.send_keys(account_phone_number)
        submit_button = driver.find_element_by_id('submit')
        submit_button.click()
        return True
    except Exception:
        return False
    finally:
        driver.quit()


def elektropostachannya(account_email, elektropostachannya_password, elektro):
    driver = webdriver.Firefox()
    try:
        driver.get('https://billing.zpep.com.ua/')
        wait = WebDriverWait(driver, 10)
        login_field = driver.find_element_by_id('Email')
        login_field.send_keys(account_email)
        password_field = driver.find_element_by_id('Password')
        password_field.send_keys(elektropostachannya_password)
        login_button = \
            driver.find_element_by_xpath("//input[@type='submit'][@class='btn btn-primary btn-block'][@value='Увійти']")
        login_button.click()
        details_button = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//html//body//div[1]//div[2]//div[2]//div[1]//div[3]//div//div[3]//a[3]")))
        details_button.click()
        add_indication_button = wait.until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//html//body//div[1]//div[2]//div[1]//div[1]//a[1]")))
        add_indication_button.click()
        counter_field = wait.until(expected_conditions.presence_of_element_located(
            (By.ID, 'CounterMeterages_0__CurrentValue')))
        counter_field.send_keys(elektro)
        save_button = driver.find_element_by_xpath("//button[@class='btn btn-primary'][@type='submit']")
        save_button.click()
        driver.execute_script("$('#logoutForm').submit();")
        return True
    except Exception:
        return False
    finally:
        driver.quit()


def vodokanal(account_email, vodokanal_password, cold_water):
    driver = webdriver.Firefox()
    try:
        driver.get('http://cpp.vodokanal.zp.ua')
        wait = WebDriverWait(driver, 10)
        login_field = wait.until(expected_conditions.presence_of_element_located((By.ID, 'textfield-1012-inputEl')))
        login_field.send_keys(account_email)
        password_field = driver.find_element_by_id('textfield-1013-inputEl')
        password_field.send_keys(vodokanal_password)
        login_button = driver.find_element_by_id('button-1022')
        login_button.click()
#       login_button click twice: first time get focus second time logged in
        login_button.click()
        wait.until(expected_conditions.presence_of_element_located((By.ID, 'messagebox-1001')))
        wait.until(expected_conditions.invisibility_of_element_located((By.ID, 'messagebox-1001')))

        # Java code
        # -------------------------
        #        WebElement popupMessageButton = driver.findElement(By.xpath("//a[@id='button-1007']"));
        #        if (popupMessageButton.isDisplayed()) popupMessageButton.click();
        # -------------------------
        counter = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'tab-1245')))
        counter.click()
        table = driver.find_element_by_id('gridview-1109-record-16')
        tbody = table.find_element_by_tag_name('tbody')
        tr = tbody.find_element_by_tag_name('tr')
        td = tr.find_element_by_xpath("//td[contains(@class, 'x-grid-cell-gridcolumn-1108')]")
        div = td.find_element_by_class_name('x-grid-cell-inner')
        button = div.find_element_by_tag_name('div')
        button.click()
        driver.execute_script("document.getElementById('numberfield-1269-inputEl').value = '{}';".format(cold_water))
        save_value_button = driver.find_element_by_id('button-1120')
        save_value_button.click()
        confirm_save_value_button = driver.find_element_by_id('button-1006')
        confirm_save_value_button.click()
        logout_button = driver.find_element_by_id('button-1032')
        logout_button.click()
        return True
    except Exception:
        return False
    finally:
        driver.quit()


class MyIndexView(View):
    def get(self, request, *args, **kwargs):
        result = dict()
        result['result_teploseti'] = ''
        result['result_oblenergo'] = ''
        result['result_elektropostach'] = ''
        result['result_vodokanal'] = ''
        result['label_teploseti'] = 'label'
        result['label_oblenergo'] = 'label'
        result['label_elektropostach'] = 'label'
        result['label_vodokanal'] = 'label'
        return render(request, 'index.html', {'result': result})

    def post(self, request, *args, **kwargs):
        result = dict()
        account_number = request.POST['account_number']
        account_email = request.POST['account_email']
        account_phone_number = request.POST['account_phone_number']
        checkbox_teploseti = request.POST.get('check_teploseti', 'false')
        checkbox_oblenergo = request.POST.get('check_oblenergo', 'false')
        checkbox_elektropostach = request.POST.get('check_elektropostach', 'false')
        checkbox_vodokanal = request.POST.get('check_vodokanal', 'false')
        if checkbox_teploseti != 'false':
            account_surname = request.POST['account_surname']
            hot_water_counter = request.POST['hot_water_counter']
#            result_teploseti = teplosteti(account_number, account_surname, account_phone_number, hot_water_counter)
            result_teploseti = True
            if result_teploseti:
                result['result_teploseti'] = 'Показники лічильника відправленні успішно'
                result['label_teploseti'] = 'greenlabel'
            else:
                result['result_teploseti'] = 'Не вдалося відправити показники лічильника'
                result['label_teploseti'] = 'redlabel'
        else:
            result['result_teploseti'] = ''
            result['label_teploseti'] = 'label'
        if checkbox_oblenergo != 'false':
            electricity_counter = request.POST['electricity_counter']
#            result_oblenergo = oblenergo(account_number, account_phone_number, electricity_counter)
            result_oblenergo = True
            if result_oblenergo:
                result['result_oblenergo'] = 'Показники лічильника відправленні успішно'
                result['label_oblenergo'] = 'greenlabel'
            else:
                result['result_oblenergo'] = 'Не вдалося відправити показники лічильника'
                result['label_oblenergo'] = 'redlabel'
        else:
            result['result_oblenergo'] = ''
            result['label_oblenergo'] = 'label'
        if checkbox_elektropostach != 'false':
            elektropostach_password = request.POST['elektropostach_password']
            electricity_counter = request.POST['electricity_counter']
#            result_elektropostach = elektropostachannya(account_email, elektropostach_password, electricity_counter)
            result_elektropostach = True
            if result_elektropostach:
                result['result_elektropostach'] = 'Показники лічильника відправленні успішно'
                result['label_elektropostach'] = 'greenlabel'
            else:
                result['result_elektropostach'] = 'Не вдалося відправити показники лічильника'
                result['label_elektropostach'] = 'redlabel'
        else:
            result['result_elektropostach'] = ''
            result['label_elektropostach'] = 'label'
        if checkbox_vodokanal != 'false':
            vodokanal_password = request.POST['vodokanal_password']
            cold_water_counter = request.POST['cold_water_counter']
#            result_vodokanal = vodokanal(account_email, vodokanal_password, cold_water_counter)
            result_vodokanal = True
            if result_vodokanal:
                result['result_vodokanal'] = 'Показники лічильника відправленні успішно'
                result['label_vodokanal'] = 'greenlabel'
            else:
                result['result_vodokanal'] = 'Не вдалося відправити показники лічильника'
                result['label_vodokanal'] = 'redlabel'
        else:
            result['result_vodokanal'] = ''
            result['label_vodokanal'] = 'label'
        return render(request, 'index.html', {'result': result})
