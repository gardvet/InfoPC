import platform
import psutil

print("\n INFORMAÇÕES DA MÁQUINA")
print("\n")

rede = platform.node()
maquina = platform.machine()
processador = platform.processor()
plataforma = platform.platform()
so = platform.system()
tipo = platform.release()
versao = platform.version()

# Nome da rede
print(f"Nome da rede: {rede}")
# Tipo de máquina
print(f"Tipo da Maquina: {maquina}")
# Modelo do Processador
print(f"Tipo do processador: {processador}")
# Tipo da plataforma
print(f"Tipo da plataforma: {plataforma}")
# Sistema Operacional
print(f"Sistema Operacional: {so} ")
# release
print(f"Realease: {tipo}")
# Versão do sistema
print(f"Versão do sistema: {versao}")

print("\n")
print("\n INFORMAÇÕES DE HARDWARE")
print("\n")

#Núcleos fisicos
print(f"Número de núcleos físicos: {psutil.cpu_count(logical=False)}")
# núcleos lógicos
print(f"Número de núcleos lógicos: {psutil.cpu_count(logical=True)}")
# Frequência da CPU
print(f"Frequência da CPU: {psutil.cpu_freq().current}")
# Frequência Miníma
print(f"Frequência mínima: {psutil.cpu_freq().min}")
# Frequência Maxima
print(f"Frequência máxima: {psutil.cpu_freq().max}")
# Utilização atual da CPU
print(f"Utiliz  percpu=True)")
# Informações da memória
print(f"Memória instalada na máquina: {round(psutil.virtual_memory().total/1000000000, 2)} GB")
print(f"Memória disponível: {round(psutil.virtual_memory().available/1000000000, 2)} GB")
print(f"Memória Usada: {round(psutil.virtual_memory().used/1000000000, 2)} GB")
print(f"Memória em uso: {psutil.virtual_memory().percent}%")