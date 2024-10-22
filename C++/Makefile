
CXX = g++


CXXFLAGS = -Wall -std=c++11


TARGET = main


SRCS = main.cpp fundo.cpp carro.cpp obstaculo.cpp


OBJS = $(SRCS:.cpp=.o)


$(TARGET): $(OBJS)
    $(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)


%.o: %.cpp
    $(CXX) $(CXXFLAGS) -c $< -o $@


clean:
    rm -f $(OBJS) $(TARGET)
