from models import Parada


def conversion(old):
    new = old.replace('  ', ' ')
    new = new.split(' ')
    if int(new[0]) < 0:
        return "%.6f" % (int(new[0]) - int(new[1]) / 60.0 - float(new[2]) / 3600.0)
    else:
        return "%.6f" % (int(new[0]) + int(new[1]) / 60.0 + float(new[2]) / 3600.0)


def migrar_paradas():
    arquivo_paradas = open(
        "/home/jamerson/Projetos/hackercidadao/paradao/paradao_server/paradao/rest_server/CTMGrandeRecife_RuasParadasOnibus_dado.csv", 'r')
    arquivo_paradas.readline()
    for parada in arquivo_paradas.readlines():
        parada = parada.rstrip().split(";")
        try:
            p = Parada(codigo=parada[0],  # Codigo
                    logradouro=parada[1],  # Logradouro
                    bairro=parada[2],  # Bairro
                    cidade=parada[3],  # Cidade
                    latitude=conversion(parada[4]),  # Latitude
                    longitude=conversion(parada[5]))  # Longitude
            p.save()
            print "passou!"
        except:
            pass

migrar_paradas()
