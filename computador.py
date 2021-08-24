import utils
import requests

class Computador:    
    def __init__(
        self,
        escola=None, 
        local=None, 
        tipo=None, 
        marca=None,
        modelo=None,
        numero_serie=None,
        numero_inventario=None,
        sistema_operacional=None,
        funciona="funcionando",
        cpu_freq=None,
        ram=None,
        hostname=None,
        ip=None,
        mac_address=None
    ):
        self.escola = escola 
        self.local = local 
        self.tipo = tipo 
        self.marca = marca 
        self.modelo = modelo 
        self.numero_serie = numero_serie 
        self.numero_inventario = numero_inventario 
        self.sistema_operacional = sistema_operacional 
        self.funciona = funciona 
        self.cpu_freq = cpu_freq 
        self.ram = ram 
        self.hostname = hostname 
        self.ip = ip 
        self.mac_address = mac_address
    
    def autoInit(self):
        info = utils.getSystemInfo()
        self.sistema_operacional = info['sistema_operacional']
        self.cpu_freq = info['processador']
        self.ram = info['ram']
        self.hostname = info['hostname']
        self.ip = info['ip']
        self.mac_address = info['mac_address']
    
    def sendInfo(self):
        pc = vars(self)
        response = requests.post('http://127.0.0.1:8000/api/computador/', data = pc) 
        return response