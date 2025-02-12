import grpc
import playback_pb2
import playback_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = playback_pb2_grpc.PlaybackServiceStub(channel)

response = stub.PlaySong(playback_pb2.PlaybackRequest(song_name="Bohemian Rhapsody"))
print(f"Server Response: {response.message}")
