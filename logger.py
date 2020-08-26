from gpiozero import CPUTemperature

cpu = CPUTemperature()

ctemp = str(int(cpu.temperature))
ftemp = str(int(cpu.temperature * 1.8) + 32)
