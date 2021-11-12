import json
import showtime_pb2
import showtime_pb2_grpc
import grpc
from concurrent import futures

class ShowtimeServicer(showtime_pb2_grpc.ShowtimeServicer):
    def __init__(self):
        with open('{}/databases/times.json'.format("."), "r") as jsf:
            self.times = json.load(jsf)["schedule"]

    # Get all times in a list
    def GetListTimes(self, request, context):
        print("GetListTimes")

        for time in self.times:
            for movie in time["movies"]:
                yield showtime_pb2.TimesData(date=time["date"], movies=movie)

    # Get times for a specific date
    def GetTimesByDate(self, request, context):
        print("GetTimesByDate")
        for time in self.times:
            if str(time["date"]) == str(request.date):
                return showtime_pb2.TimesData(date=time["date"], movies=time["movies"])
        return showtime_pb2.TimesData(date="", movies="")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_ShowtimeServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    print("Showtime serv on port 3003...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
