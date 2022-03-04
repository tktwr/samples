include $(MY_LIBTT_WIN)/makefile.mk

PROJ_DIR=$(shell pwd)

APPS="\
sample_c++11.exe \
sample_c++14.exe \
sample_c++17.exe \
sample_c++20.exe \
sample_class.exe \
sample_cstdio.exe \
sample_fstream.exe \
sample_hello_world.exe \
sample_move.exe \
sample_stl.exe \
sample_stream.exe \
sample_string.exe \
sample_syntax.exe \
sample_template.exe \
sample_thread.exe \
sample_util.exe \
"

all: cmake build

run:
	@for i in "$(APPS)"; do\
		echo "=== [$$i] ===";\
		cd $(PROJ_DIR)/$(BUILD_DIR);\
		$(BUILD_CONFIG)/$$i;\
	done

