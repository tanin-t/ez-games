from rest_framework.views import APIView
from rest_framework.response import Response

from bingo.serializers import PlayerSerializer
from .models import BingoNumber, Player
import random


class ResetGameAPIView(APIView):
    def post(self, request):
        BingoNumber.objects.all().delete()
        Player.objects.all().delete()
        return Response('OK')


class PlayerListCreateAPIView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request):
        validator = PlayerSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        player = Player.objects.create(**validator.validated_data)

        serializer = PlayerSerializer(player)
        return Response(serializer.data)


class GenerateBingoNumber(APIView):
    def post(self, request):
        max_loop = 20
        count_loop = 0

        while True:
            random_num = random.randint(1, 100)
            if not BingoNumber.objects.filter(number=random_num).exists():
                break
            
            count_loop += 1
            if count_loop >= max_loop:
                raise Exception('Max loop reached')

        BingoNumber.objects.create(number=random_num)

        return Response({ 'number': random_num })


class CheckBingoNumberAPI(APIView):
    def post(self, request):
        number = request.data['number']
        bingo_number = BingoNumber.objects.filter(number=number).first()

        if bingo_number:
            return Response({ 'ok': True })
        
        return Response({ 'ok': False })
        
