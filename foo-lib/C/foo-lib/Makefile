TARGET  = test_all
LIBS    = 
CC      = /opt/local/bin/gcc-mp-4.7
CFLAGS  = -std=c99 -g -Wall -DMOCK_NETWORK -DNODES_T_H=test_node_t.h
LDFLAGS = 

OBJECTS = $(patsubst %.c, %.o, $(wildcard *.c))
HEADERS = $(wildcard *.h)

default: clean $(TARGET)
	@./$(TARGET)

all: default
test: default

%.o: %.c $(HEADERS)
	@$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJECTS)
	@$(CC) $(LDFLAGS) $(OBJECTS) -Wall $(LIBS) -o $@

clean:
	@rm -f *.o
	@rm -f $(TARGET)

.PHONY: default all clean test
.PRECIOUS: $(TARGET) $(OBJECTS)
