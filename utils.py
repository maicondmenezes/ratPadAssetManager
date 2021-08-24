import platform, socket, re, uuid, psutil, logging, cpuinfo, requests

LARGE_FONT= ("Verdana", 14)
NORMAL_FONT= ("Verdana", 10)
STATUS_LIST = ['funcionando', 'defeituoso']
TYPE_LIST = ['Desktop', 'Notebook', 'Mini-Desktop', 'Netbook']
LOCALS_LIST = ['Secretaria', 'Coordenação',	'Depósito', 'Direção', 'Laboratório de Informática', 'Sala de Aula', 'Sala de Leitura', 'Sala dos Professores']

def addSystemInfo(pc):
    response = requests.post('http://maicondmenezes.pythonanywhere.com/api/computador/', data = pc) 
    return(response)

def getSystemInfo():
    
    try:
        info={}        
        info['sistema_operacional']=str(platform.system()) + ' ' + str(platform.release())
        info['processador']=str(cpuinfo.cpu.info[0]['model name'])
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info['hostname']=socket.gethostname()
        info['ip']=socket.gethostbyname(socket.gethostname())
        info['mac_address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
                
        return info
    except Exception as e:
        logging.exception(e)