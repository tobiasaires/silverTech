from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.


class ApiTest(APITestCase):

    def test_list_all_processors(self):
        request = self.client.get("/api/processors/")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 4)

    def test_list_all_memories(self):
        request = self.client.get("/api/memories/")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 5)

    def test_list_all_mother_board(self):
        request = self.client.get("/api/mother-boards/")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 3)

    def test_list_all_video_board(self):
        request = self.client.get("/api/video-boards/")

        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(len(request.data), 3)

    def test_not_create_computer_with_more_ram_then_slots(self):
        request = self.client.get("/api/computers/", {'mother_board_id': 1, "video_board_id": 'null',
                                                      "processor_id": 1,
                                                      "memory_id": [
                                                          1, 2, 3]}, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_create_computer_with_more_ram_size_then_supported(self):
        request = self.client.get("/api/computers/", {'mother_board_id': 1, "video_board_id": 'null',
                                                      "processor_id": 1,
                                                      "memory_id": [
                                                          4]}, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_create_computer_with_processor_not_supported_by_mother_board(self):
        request = self.client.get("/api/computers/", {'mother_board_id': 1, "video_board_id": 'null',
                                                      "processor_id": 3,
                                                      "memory_id": [
                                                          4]}, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_create_computer_with_processor_not_supported_by_mother_board(self):
        request = self.client.get("/api/computers/", {'mother_board_id': 1, "video_board_id": 'null',
                                                      "processor_id": 3,
                                                      "memory_id": [
                                                          1]}, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_create_computer_with_not_default_video_board(self):
        request = self.client.get("/api/computers/", {'mother_board_id': 1, "video_board_id": 'null',
                                                      "processor_id": 1,
                                                      "memory_id": [
                                                          1]}, format='json')
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_computer_with_default_video_board(self):
        request = self.client.get("/api/computers/", {'mother_board_id': 3, "video_board_id": '',
                                                      "processor_id": 1,
                                                      "memory_id": [
                                                          1]}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_create_computer_with_video_board(self):

        request = self.client.get("/api/computers/", {'mother_board_id': 2, "video_board_id": 1,
                                                      "processor_id": 1,
                                                      "memory_id": [
                                                          1]}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_create_an_order(self):

        request = self.client.get("/api/orders/", {'computer_id': 2, "user_id": 1}, format='json')
        self.assertEqual(request.status_code, status.HTTP_200_OK)
