from rest_framework import serializers


class Validators:

    @staticmethod
    def number_ram(data):

        num_slots = data['mother_board_id'].ram_slots
        num_ram = len(data['memory_id'])

        if num_slots < num_ram:
            raise (
                serializers.ValidationError(
                    f"Número de ram selecionada maior do que a suportada pela placa mãe. Suportada: {num_slots} Pedida: {num_ram}")
            )
    