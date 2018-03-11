#ifndef myglut_h
#define myglut_h

#define GLEW_STATIC
#include <GL/glew.h>

#if defined(WIN32)
#    include <GL/glut.h>
#elif defined(__APPLE__) || defined(MACOSX)
#    include <GLUT/glut.h>
#else
#    define UNIX
#    include <GL/glut.h>
#endif

#ifdef _MSC_VER
#    ifdef NDEBUG
#        pragma comment(linker, "/SUBSYSTEM:WINDOWS /ENTRY:mainCRTStartup")
#    else
#        pragma comment(linker, "/SUBSYSTEM:CONSOLE")
#    endif
#endif

#define CTRL_KEY(x) ((x)-'A'+1)
#define ESC_KEY 27
#define BS_KEY 8
#define ENTER_KEY 13

#endif  // myglut_h
