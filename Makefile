# Makefile for NN Project


# Only parts you might have to change:
SRC_FILES = main.cpp
ALE_DIR = $(shell pwd)/ale_with_obj
MAT_DIR = /u/mhollen/sift
MAT_SDL_DIR = $(MAT_DIR)/SDL
MAT_HNEAT_DIR = $(MAT_DIR)/HyperNEAT
# .../lib


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
LIBRARIES = -L$(ALE_DIR)
# LINUX ONLY: -Wl,-rpath stuff
LIBRARIES += -Wl,-rpath=$(ALE_DIR)
LIBRARIES += -Wl,-rpath=$(MAT_SDL_DIR)/lib
LIBRARIES += -L/u/mhauskn/local/lib
INCLUDES = -I$(ALE_DIR)/src
INCLUDES += -I$(MAT_SDL_DIR)/include
LINKS = -lale -lz
LINKS += -lSDL -lSDL_gfx -lSDL_image 
LINKS += -lboost_thread-mt -lboost_serialization -lboost_system -lboost_filesystem
#LINKS += -pthread -ldl


# specify custom macros
PREPROC_VARS = -D ROM_DIRECTORY="\"$(ALE_DIR)/roms\""


all: prep compile

prep:
	@mkdir -p $(OBJ_DIR)


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


# Run and debug scripts
run:
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$(MAT_SDL_DIR)/lib:$(MAT_HNEAT_DIR)/SDL2_image-2.0.0
	export LIBRARY_PATH=$LIBRARY_PATH:$(MAT_SDL_DIR)/lib:$(MAT_HNEAT_DIR)/SDL2_image-2.0.0
	./$(EXE) space_invaders
