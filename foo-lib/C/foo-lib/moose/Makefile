TARGET=test_all

PLATFORMS_PATH=../../../../platforms
INCLUDE_PATH=$(PLATFORMS_PATH)

MOOSE_DIR=$(PLATFORMS_PATH)/moose

MORE_SRC = $(MOOSE_DIR)/avr.c    \
           $(MOOSE_DIR)/clock.c  \
					 $(MOOSE_DIR)/serial.c \
					 $(MOOSE_DIR)/xbee.c   \
					 ../nodes.c            \
					 $(patsubst %.c, %.o, $(wildcard *.c))

MORE_OBJECTS = $(patsubst %.c, %.o, $(MORE_SRC))

MCU=atmega1284p
F_CPU=8000000

AVRDUDE_PROGRAMMER=jtag2

MORE_CDEFS += -DSERIAL_ON_USART1
MORE_CDEFS += -DNODES_T_H=test_node_t.h

include $(MOOSE_DIR)/Makefile

all: program

clean: clean_avr clean_more_objects

clean_avr:
	@(cd $(MOOSE_DIR); $(MAKE) clean)

clean_more_objects:
	@rm -f $(MORE_OBJECTS)

# setup and control targets

fuses:
	$(AVRDUDE) $(AVRDUDE_FLAGS) -U lfuse:w:0xE2:m

serial-digitus:
	screen /dev/tty.usbserial-FTSJ84AI 9600

serial-logilink:
	screen /dev/tty.usbserial 9600
