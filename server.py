import grpc
from concurrent import futures
import time 

#import the generated class
import calculator_pb2
import calculator_pb2_grpc

#import the calculator.py 
import calculator

#now create the server function that will defind by the other structure 
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
#now lets take the values from the other calculator funciton 

    def SquareRoot(self,request,context):
        response=calculator_pb2.Number()
        response.value=calculator.square_root(request.value)
        return response


server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(),server)

#create grpc server
print('grpc server start with port 50051')
server.add_insecure_port('[::]:50051')
server.start()


#now lets create time buffer for the server 

try:
    while True:
        time.sleep(84210)
    
except KeyboardInterrupt:
    server.stop(0)