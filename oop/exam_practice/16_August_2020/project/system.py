from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def get_hardware_info(hardware: Hardware):
        memory_for_all_software = sum(x.memory_consumption for x in hardware.software_components)
        capacity_for_all_software = sum(x.capacity_consumption for x in hardware.software_components)

        software_names = []
        if hardware.software_components:
            for software in hardware.software_components:
                software_names.append(software.name)
        else:
            software_names.append("None")

        result = [f"Hardware Component - {hardware.name}",
                  f"Express Software Components: {len([x for x in hardware.software_components if x.software_type == 'Express'])}",
                  f"Light Software Components: {len([x for x in hardware.software_components if x.software_type == 'Light'])}",
                  f"Memory Usage: {memory_for_all_software} / {hardware.memory}",
                  f"Capacity Usage: {capacity_for_all_software} / {hardware.capacity}",
                  f"Type: {hardware.hardware_type}",
                  f"Software Components: {', '.join(software_names)}"]

        return "\n".join(result)

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception as error:
            raise Exception(error)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        express_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception as error:
            raise Exception(error)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        found_hardware = [x for x in System._hardware if x.name == hardware_name]
        found_software = [x for x in System._software if x.name == software_name]

        if found_hardware and found_software:
            hardware = found_hardware[0]
            software = found_software[0]

            hardware.uninstall(software)
            System._software.remove(software)

        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        memory_consumption_for_software = sum(x.memory_consumption for x in System._software)
        capacity_consumption_for_software = sum(x.capacity_consumption for x in System._software)
        memory_for_hardware = sum(x.memory for x in System._hardware)
        capacity_for_hardware = sum(x.capacity for x in System._hardware)

        result = ["System Analysis",
                  f"Hardware Components: {len(System._hardware)}",
                  f"Software Components: {len(System._software)}",
                  f"Total Operational Memory: {memory_consumption_for_software} / {memory_for_hardware}",
                  f"Total Capacity Taken: {capacity_consumption_for_software} / {capacity_for_hardware}"]

        return "\n".join(result)

    @staticmethod
    def system_split():
        result = []

        for hardware in System._hardware:
            result.append(System.get_hardware_info(hardware))

        return "\n".join(result)
