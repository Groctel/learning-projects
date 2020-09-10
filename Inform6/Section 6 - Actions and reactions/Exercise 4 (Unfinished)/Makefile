MAKEDIR = .
BIN     = $(MAKEDIR)/bin
SRC     = $(MAKEDIR)/src

.PHONY: all dir

all: dir \
     $(BIN)/door.z5

dir:
	@mkdir -p $(BIN)

$(BIN)/door.z5: $(SRC)/door.inf
	inform $(SRC)/door.inf $(BIN)/door.z5
