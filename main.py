import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e_c
from selenium.webdriver.support.ui import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación."
                            )
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    btn_solicitar_taxi = (By.CSS_SELECTOR, "button.button.round")
    btn_seleccion_comfort = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    input_num_telefono = (By.CLASS_NAME, "np-button")
    agregar_num_telefono = (By.ID, 'phone')
    btn_siguiente_telefono = (By.CSS_SELECTOR, ".button.full")
    input_ingresar_codigo = campo_ingresar_codigo = (By.ID, "code")
    btn_validar_codigo = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    clic_modo_de_pago = (By.CSS_SELECTOR, '.pp-button.filled')
    clic_adicionar_tarjeta = (By.CSS_SELECTOR, '.pp-row.disabled')
    completar_campo_tarjeta = (By.ID, 'number')
    completar_campo_codigo = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    clic_salir_foco = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[2]')
    btn_agregar_tarjeta = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    btn_cerrar_popup = (By.CSS_SELECTOR,
                        '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    conseguir_modo_pago = (By.CLASS_NAME, "pp-value-text")
    mensaje_conductor = (By.ID, "comment")
    opcion_manta_y_panuelo = (By.CSS_SELECTOR, ".slider.round")
    btn_adicionar_helado = (By.CLASS_NAME, 'counter-plus')
    conseguir_total_helados = (By.CLASS_NAME, 'counter-value')
    solicitar_taxi = (By.CLASS_NAME, 'smart-button')
    pop_up_solicitud_realizada = (By.CLASS_NAME, 'order-header-title')


def __init__(self, driver):
    self.driver = driver


def set_from(self, from_address):
    from_field_element = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.from_field))
    from_field_element.send_keys(from_address)


def set_to(self, to_address):
    to_field_element = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.to_field))
    to_field_element.send_keys(to_address)


def set_route(self, address_from, address_to):
    self.set_from(address_from)
    self.set_to(address_to)


def get_from(self):
    return (WebDriverWait(self.driver, 10)
            .until(e_c.presence_of_element_located(self.from_field)).get_property('value'))


def get_to(self):
    return (WebDriverWait(self.driver, 10)
            .until(e_c.presence_of_element_located(self.to_field)).get_property('value'))


def set_hacer_clic_btn_pedir_taxi(self):
    pedir_Taxi = (WebDriverWait(self.driver, 10)
                  .until(e_c.presence_of_element_located(self.btn_solicitar_taxi)))
    pedir_Taxi.click()


def set_clic_btn_comfort(self):
    seleccion_comfort = (WebDriverWait(self.driver, 10)
                         .until(e_c.presence_of_element_located(self.btn_seleccion_comfort)))
    seleccion_comfort.click()


def get_btn_comfort(self):
    tarifa_comfort = (WebDriverWait(self.driver, 10)
                      .until(e_c.presence_of_element_located(self.btn_seleccion_comfort)).text)
    return tarifa_comfort


def set_btn_num_telefono(self):
    clicNumTelefono = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.input_num_telefono))
    clicNumTelefono.click()


def set_ingresar_num_telefono(self, numero):
    agregarNumTelefono = WebDriverWait(self.driver, 10).until(
        e_c.presence_of_element_located(self.agregar_num_telefono))
    agregarNumTelefono.send_keys(numero)


def set_clic_btn_siguient_telefono(self):
    btnSiguiente = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.btn_siguiente_telefono))
    btnSiguiente.click()


def set_agregar_codigo(self, codigo):
    agregarCodigo = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.input_ingresar_codigo))
    agregarCodigo.send_keys(codigo)


def set_validar_codigo(self):
    validarCodigo = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.btn_validar_codigo))
    validarCodigo.click()


def get_num_telefono(self):
    numTelefono = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.input_num_telefono))
    return numTelefono.text


def set_ejecutar_agregar_num_telefono(self, numero):
    self.set_btn_num_telefono()
    self.set_ingresar_num_telefono(numero)
    self.set_clic_btn_siguient_telefono()


def set_codigo_num_telefono(self, codigo):
    self.set_agregar_codigo(codigo)
    self.set_validar_codigo()


def set_clic_modo_pago(self):
    seleccionar_tarjeteCredito = WebDriverWait(self, 10).until(e_c.presence_of_element_located(self.clic_modo_de_pago))
    seleccionar_tarjeteCredito.click()


def set_adicionar_tarjeta_credito(self):
    WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(By.CSS_SELECTOR, '.pp-row.disabled')).click()


def set_clic_modo_pago_y_agregar_tarjeta(self):
    self.set_clic_modo_pago()
    self.set_adicionar_tarjeta_credito()


def set_completar_campo_tarjeta_credito(self, numeroTarjeta):
    agregarTarjetaCredito = (WebDriverWait(self.driver, 10)
                             .until(e_c.presence_of_element_located(self.completar_campo_tarjeta)))
    agregarTarjetaCredito.send_keys(numeroTarjeta)


def set_completar_codigo_tarjeta_Credito(self, numCodigo):
    completarCodigo = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.completar_campo_codigo))
    completarCodigo.send_keys(numCodigo)


def set_completar_campos_tarjeta_y_codigo(self, numeroTarjeta, numCodigo):
    self.set_completar_campo_tarjeta_credito(numeroTarjeta)
    self.set_completar_codigo_tarjeta_Credito(numCodigo)


def get_obtener_tarjeta_credito(self):
    agregarTarjeta = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.completar_campo_tarjeta))
    return agregarTarjeta.get_property('value')


def get_obtener_codigo(self):
    agregarCodigo = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.completar_campo_codigo))
    return agregarCodigo.get_property('value')


def set_salir_de_foco(self):
    clic_SalirFoco = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.clic_salir_foco))
    clic_SalirFoco.click()


def set_clic_agregar_tarjeta_credito(self):
    clic_AgregarTajeta = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.btn_agregar_tarjeta))
    clic_AgregarTajeta.click()


def set_clic_cerrar_pop_up(self):
    cerrar_popUp = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.btn_cerrar_popup))
    cerrar_popUp.click()


def set_clic_salir_foco_agregar_tarjeta_cerrar_pop_up(self):
    self.set_salir_de_foco()
    self.set_clic_agregar_tarjeta_credito()
    self.set_clic_cerrar_pop_up()


def get_conseguir_modo_pago(self):
    validarTexto = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.conseguir_modo_pago))
    return validarTexto.text


def set_adicionar_mensaje(self, mensaje_para_el_conductor):
    adicionarMensaje = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.mensaje_conductor))
    adicionarMensaje.send_keys(mensaje_para_el_conductor)


def get_validar_mensaje_conductor(self):
    validarMensaje = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.mensaje_conductor))
    return validarMensaje.get_attribute('value')


def set_clic_manta_y_panuelo(self):
    clicOpcion_MyP = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.opcion_manta_y_panuelo))
    clicOpcion_MyP.click()


def get_validar_opcion_m_y_p_esta_seleccionado(self):
    presionarOpcion = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(By.XPATH,
         "//div[@class='r-sw-container']/*[contains(text(),'Manta')]/..//div[@class='switch']//input[@class='switch-input']"))
    return presionarOpcion.is_selected()


def set_adicionar_helado(self):
    adicionar_helado = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.btn_adicionar_helado))
    adicionar_helado.click()
    adicionar_helado.click()


def get_conseguir_total_helados(self):
    total_helado = WebDriverWait(self.driver, 10).until(e_c.presence_of_element_located(self.conseguir_total_helados))
    return total_helado.text


def set_clic_solicitar_taxi(self):
    solicitarTaxi = self.driver.find_element(*self.solicitar_taxi)
    solicitarTaxi.click()


def get_validar_pop_up_solicitud_realizada(self):
    popUp_solicitud = (WebDriverWait(self.driver, 10)
                       .until(e_c.presence_of_element_located(self.pop_up_solicitud_realizada)))
    return popUp_solicitud.text


def set_espera_confirmacion(self):
    ventana_emergente = (WebDriverWait(self.driver, 40)
                         .until(e_c.presence_of_element_located(self.pop_up_solicitud_realizada),
                                'El conductor llegará en'))

def get_validar_datos_conductor(self):
    dato_conductor = (WebDriverWait(self.driver, 60)
                      .until(e_c.presence_of_element_located(self.pop_up_solicitud_realizada)))
    return dato_conductor.text


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
