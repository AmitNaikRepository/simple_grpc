import grpc
import calculator_pb2
import calculator_pb2_grpc

#create teh channel first 
channel=grpc.insecure_channel('localhost: 50081')

#create grpc client request 
stub=calculator_pb2_grpc.CalculatorStub(channel)

#create teh valid request for the server 
number=calculator_pb2.Number(value=16)

# make a call 
response=stub.SquareRoot(number)

print(response.value)
