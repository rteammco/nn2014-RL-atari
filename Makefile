# Makefile for NN Project


# Only parts you might have to change:
SRC_FILES = main.cpp
ALE_DIR = $(shell pwd)/ale_0.4.4/ale_0_4


# specify flags and compiler variables
EXE = proj
CXX = g++
#FLAGS = -DNDEBUG -g -O3 -ffast-math -fopenmp -std=c++0x
SRC_DIR = src
OBJ_DIR = obj
OS = $(shell uname)


# specify source files
OBJ = $(addprefix obj/, $(SRC_FILES:.cpp=.o))
SRC = $(addprefix $(SRC_DIR)/, $(SRC_FILES))


# specify libraries, links and include sources
LIBSO = libale.so
LIBRARIES = -L$(ALE_DIR)
INCLUDES = -I$(ALE_DIR)/src
LINKS = -lale -lz
#LINKS = -pthread -ldl


# specify custom macros
PREPROC_VARS = -D ROM_DIRECTORY="\"$(ALE_DIR)/roms\""


all: prep compile

prep:
	@mkdir -p $(OBJ_DIR)

# if OS X, just make a symlink to the .so file...
ifeq ($(OS),Darwin)
	@if [ ! -f "./$(LIBSO)" ]; then ln -s $(ALE_DIR)/$(LIBSO) .; echo "Created symlink to \"$(LIBSO)\"."; fi
# if on a real Unix system, add the runtime path
else
LIBRARIES += -Wl,-rpath=$(ALE_DIR)
endif

#compile:
#	$(CXX) $(FLAGS) $(INCLUDES) $(LIBRARIES) $(PATHS) $(SRC) $(LINKS) -o $(EXE) $(PREPROC_VARS)
$(OBJ): $(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@echo "Compiling $@..."
	@$(CXX) $(FLAGS) $(INCLUDES) -c -o $@ $< $(PREPROC_VARS)

compile: $(OBJ)
	@echo "\nBuilding executable:"
	$(CXX) $(FLAGS) $(LINKS) $(LIBRARIES) $? -o $(EXE)
	@echo "\nCompilation complete: success!\n"


# Remove the executable and object files
clean:
	@echo "Deleting object files and executable:"
	rm -f $(EXE)
	rm -rf $(OBJ_DIR)
	rm -f $(LIBSO)


# Run and debug scripts
run:
	@./$(EXE) space_invaders
