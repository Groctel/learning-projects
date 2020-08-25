MAKEDIR = .
BIN     = $(MAKEDIR)/bin
SRC     = $(MAKEDIR)/src

.PHONY: all dir

all: dir \
     $(BIN)/ruins.z5

dir:
	@mkdir -p $(BIN)

$(BIN)/ruins.z5: $(SRC)/ruins.inf
	inform $(SRC)/ruins.inf $(BIN)/ruins.z5
