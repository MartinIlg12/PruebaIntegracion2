from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoAlertPresentException


driver = webdriver.Chrome()


driver.get("https://www.demoblaze.com/index.html")
sleep(2)


registro = driver.find_element(By.XPATH, '//*[@id="signin2"]')
registro.click()
sleep(1)


user = driver.find_element(By.XPATH, '//*[@id="sign-username"]')
user.send_keys("IlguanItsqmet12")
sleep(1)

password = driver.find_element(By.XPATH, '//*[@id="sign-password"]')
password.send_keys("usuario1")
sleep(1)


botonRegistro = driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]')
botonRegistro.click()
sleep(2)  


try:
    alert = driver.switch_to.alert
    alert.accept()
    print("Alerta aceptada.")
except NoAlertPresentException:
    print("No apareció ninguna alerta.")


iniciarSesion = driver.find_element(By.XPATH, '//*[@id="login2"]')
iniciarSesion.click()
sleep(1)


loginUser = driver.find_element(By.XPATH, '//*[@id="loginusername"]')
loginUser.send_keys("IlguanItsqmet12")
sleep(1)

loginPassword = driver.find_element(By.XPATH, '//*[@id="loginpassword"]')
loginPassword.send_keys("usuario1")
sleep(1)


botonLogin = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
botonLogin.click()
sleep(2)

producto1 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/a/img')
producto1.click()
sleep(2)

productoCompra1 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
productoCompra1.click()
sleep(2)

try:
    alert = driver.switch_to.alert
    alert.accept()
    print("Alerta aceptada.")
except NoAlertPresentException:
    print("No apareció ninguna alerta.")

home = driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
home.click()
sleep(2)

producto2 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a/img')
producto2.click()
sleep(2)

productoCompra2 = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a')
productoCompra2.click()
sleep(2)

try:
    alert = driver.switch_to.alert
    alert.accept()
    print("Alerta aceptada.")
except NoAlertPresentException:
    print("No apareció ninguna alerta.")

carrito = driver.find_element(By.XPATH, '//*[@id="cartur"]')
carrito.click()
sleep(2)

comprar = driver.find_element(By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button')
comprar.click()
sleep(2)

nombre = driver.find_element(By.XPATH, '//*[@id="name"]')
nombre.send_keys("Martin Ilguan")
sleep(2)

pais = driver.find_element(By.XPATH, '//*[@id="country"]')
pais.send_keys("Ecuador")
sleep(2)

ciudad = driver.find_element(By.XPATH, '//*[@id="city"]')
ciudad.send_keys("Quito")
sleep(2)

card = driver.find_element(By.XPATH, '//*[@id="card"]')
card.send_keys("1725582587")
sleep(2)

mes = driver.find_element(By.XPATH, '//*[@id="month"]')
mes.send_keys("Mayo")
sleep(2)

año = driver.find_element(By.XPATH, '//*[@id="year"]')
año.send_keys("2024")
sleep(2)

compraHecha = driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]')
compraHecha.click()
sleep(2)

okFinal = driver.find_element(By.XPATH, '/html/body/div[10]/div[7]/div/button')
okFinal.click()
sleep(2)

salir = driver.find_element(By.XPATH, '//*[@id="logout2"]')
salir.click()
sleep(2)

sleep(5)
driver.close()
