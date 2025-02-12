import grpc
from concurrent import futures
import playback_pb2
import playback_pb2_grpc

class PlaybackService(playback_pb2_grpc.PlaybackServiceServicer):
    def PlaySong(self, request, context):
        return playback_pb2.PlaybackResponse(message=f"Playing {request.song_name}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    playback_pb2_grpc.add_PlaybackServiceServicer_to_server(PlaybackService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
