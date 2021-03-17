from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import csv
import re
import passwords

def getPostion(employee_number, school):
    if '1A' in school or '1B' in school:
        print(employee_number + ' School:' + school + ' Will Be set to: 1st Yr')
        position_field.select_by_visible_text('1st Year Apprentice')
    elif '2A' in school or '2B' in school:
        print(employee_number + ' School:' + school + ' Will Be set to: 2nd Yr')
        position_field.select_by_visible_text('2nd Year Apprentice')
    elif '3A' in school or '3B' in school:
        print(employee_number + ' School:' + school + ' Will Be set to: 3rd Yr')
        position_field.select_by_visible_text('3rd Year Apprentice')
    elif '4A' in school or '4B' in school:
        print(employee_number + ' School:' + school + ' Will Be set to: 4th Yr')
        position_field.select_by_visible_text('4th Year Apprentice')
    else:
        print(employee_number + ' School:' + school + ' Hit the else, will be set to 4th Yr')
        position_field.select_by_visible_text('4th Year Apprentice')

    # try:
    #     split_school = school.split('-')
    #     year_in_school = split_school[0]
    #     semester = split_school[2]
    #     if '1' in year_in_school and '2021' in semester:
    #         print('School: ' + school + ' Will Be set to: 1st Yr')
    #         position_field.select_by_visible_text('1st Year Apprentice')
    #     elif '2' in year_in_school and '2021' in semester:
    #         print('School: ' + school + ' Will Be set to: 2nd Yr')
    #         position_field.select_by_visible_text('2nd Year Apprentice')
    #     elif '3' in year_in_school and '2021' in semester:
    #         print('School: ' + school + ' Will Be set to: 3rd Yr')
    #         position_field.select_by_visible_text('3rd Year Apprentice')
    #     elif '4' in year_in_school and '2021' in semester:
    #         print('School: ' + school + ' Will Be set to: 4th Yr')
    #         position_field.select_by_visible_text('4th Year Apprentice')
    # except:
    #     if school == '':
    #         print('School: ' + school + ' Will be set to: 4th Yr')
    #         position_field.select_by_visible_text('4th Year Apprentice')

desktop = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop'))
driver = webdriver.Firefox(executable_path=desktop + '\\geckodriver.exe')
username = passwords.username
password = passwords.password

driver.get('http://127.0.0.1:8001/accounts/login/?next=/manpower/employees/create/')
username_field = driver.find_element_by_id('id_username')
password_field = driver.find_element_by_id('id_password')
sign_in_button = driver.find_element_by_xpath('/html/body/div/div/div/div/form/div/div[4]/input[1]')

username_field.send_keys(username)
password_field.send_keys(password)
sign_in_button.click()

with open('manpower.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        employee_number = row[0].strip()
        first_name = row[1].strip()
        last_name = row[2].strip()
        if row[3] and row[4]:
            phone = row[4].strip()
        elif row[3] and not row[4]:
            phone = row[3].strip()
        else:
            phone = row[4].strip()
        email = row[5].strip()
        address = row[7].strip()
        city = row[8].strip()
        state = row[9].strip()
        zip_code = row[10].strip()
        date_of_birth = row[11].strip()
        spouse = row[12].strip()
        drivers_license_number = row[14].strip()
        drivers_license_state = row[15].strip()
        driving_release = row[16].strip()
        drive = row[17].strip()
        electrical_license_level = row[22].strip()
        electrical_license_number = row[23].strip()
        electrical_license_expiration = row[24].strip()
        date_hired = row[25].strip()
        cost_center = row[35].strip()
        school = row[36].strip()

        driver.get('http://127.0.0.1:8001/manpower/employees/create/')
        password_field = driver.find_element_by_id('id_password')
        confirm_password_field = driver.find_element_by_id('id_repeat_password')
        first_name_field = driver.find_element_by_id('id_first_name')
        last_name_field = driver.find_element_by_id('id_last_name')
        employee_number_field = driver.find_element_by_id('id_employee_number')
        hire_date_field = driver.find_element_by_id('id_hire_date')
        date_of_birth_field = driver.find_element_by_id('id_date_of_birth')
        street_address_field = driver.find_element_by_id('id_street_address')
        city_field = driver.find_element_by_id('id_city')
        state_field = Select(driver.find_element_by_id('id_state'))
        zip_code_field = driver.find_element_by_id('id_zip_code')
        email_address_field = driver.find_element_by_id('id_email_address')
        phone_number_field = driver.find_element_by_id('id_phone_number')
        spouse_name_field = driver.find_element_by_id('id_spouse_name')
        drivers_license_state_field = Select(driver.find_element_by_id('id_drivers_license_state'))
        drivers_license_number_field = driver.find_element_by_id('id_drivers_license_number')
        drivers_license_expiration_field = driver.find_element_by_id('id_drivers_license_expiration')
        electrical_license_number_field = driver.find_element_by_id('id_electrical_license_number')
        electrical_license_level_field = Select(driver.find_element_by_id('id_electrical_license_level'))
        electrical_license_expiration_field = driver.find_element_by_id('id_electrical_license_expiration')
        position_field = Select(driver.find_element_by_id('id_position'))
        school_field = Select(driver.find_element_by_id('id_school'))
        assigned_job_field = Select(driver.find_element_by_id('id_assigned_job'))
        create_button = driver.find_element_by_xpath('/html/body/div/div/div/form/div/div/input')

        password_field.send_keys(passwords.profile_password)
        confirm_password_field.send_keys(passwords.profile_password)
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        employee_number_field.send_keys(employee_number)
        hire_date_field.clear()
        hire_date_field.send_keys(date_hired)
        date_of_birth_field.send_keys(date_of_birth)
        street_address_field.send_keys(address)
        city_field.send_keys(city)
        state_field.select_by_visible_text('Utah')
        if '-' in zip_code:
            zip_split = zip_code.split('-')
            zip_code_field.send_keys(zip_split[0])
        else:
            zip_code_field.send_keys(zip_code)
        email_address_field.send_keys(email)
        phone_number_field.send_keys(re.sub("[^0-9]", "", phone))
        if spouse == 'Single' or spouse == 'Divorced':
            pass
        else:
            spouse_name_field.send_keys(spouse)
        drivers_license_number_field.send_keys(drivers_license_number)
        electrical_license_number_field.send_keys(electrical_license_number)
        if electrical_license_level == 'Apprentice' or electrical_license_level == 'Journeyman' or electrical_license_level == 'Master':
            electrical_license_level_field.select_by_visible_text(electrical_license_level)
        else:
            pass
        electrical_license_expiration_field.send_keys(electrical_license_expiration)
        if electrical_license_level == 'Journeyman' or electrical_license_level == 'Master':
            position_field.select_by_visible_text('Journeyman')
        else:
            getPostion(employee_number, school)
        if 'SLCC' in school:
            school_field.select_by_visible_text('Salt Lake Community College')
        elif 'IEC' in school:
            school_field.select_by_visible_text('IEC')
        elif 'Tooele' in school:
            school_field.select_by_visible_text('Tooele Technical College')
        elif 'MATC' in school:
            school_field.select_by_visible_text('Mountainland Technical College')
        elif 'OWTC' in school or 'Ogden' in school or 'OgdenTech' in school or 'OWATC' in school:
            school_field.select_by_visible_text('Ogden-Weber Technical College')
        elif 'David' in school or 'DATC' in school or 'DATA' in school:
            school_field.select_by_visible_text('Davis Technical College')
