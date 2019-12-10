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

    @staticmethod
    def ram_size(data):

        ram_size_request = sum([memory.ram_size for memory in data['memory_id']])
        ram_size_suported = data['mother_board_id'].ram_max_size

        if ram_size_request > ram_size_suported:
            raise (
            serializers.ValidationError(
                f"Aplaca mãe selecioanada não suporta essa quantidade de Ram pedida. Suportada: {ram_size_suported} Pedida: {ram_size_request}"
            )
        )
