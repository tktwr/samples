#include "myglut.h"
#include "glsl_util.h"
#include <stdlib.h>

GLSLProgram* glsl_prog = 0;

void f_quit()
{
	exit(0);
}

void DisplayFunc()
{
	glViewport(0, 0, 640, 480);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(0, 1, 0, 1);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	glDisable(GL_DEPTH_TEST);
	glDisable(GL_LIGHTING);
	glDisable(GL_BLEND);

	glClearColor(0, 0, 0, 1);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glsl_prog->useProgram();
	glColor3f(1, 0, 0);
	glBegin(GL_TRIANGLES);
	glVertex3f(0, 0, 0);
	glVertex3f(1, 0, 0);
	glVertex3f(0, 1, 0);
	glEnd();
	glsl_prog->unuseProgram();

	glutSwapBuffers();
}

void MouseFunc(int button, int state, int x, int y)
{
}

void MotionFunc(int x, int y)
{
}

void KeyFunc(unsigned char key, int x, int y)
{
	switch (key)
	{
		case ESC_KEY:
			f_quit();
			break;
	}
}

void TimerFunc(int val)
{
	glutPostRedisplay();
	glutTimerFunc(100, TimerFunc, 0);
}

int main(int argc, char *argv[])
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH);
	glutInitWindowPosition(0, 0);
	glutInitWindowSize(640, 480);
	glutCreateWindow(argv[0]);

	glewInit();

	glsl_prog = new GLSLProgram();
	glsl_prog->createProgram();
	glsl_prog->compileVertexShader("vert.glsl");
	glsl_prog->compileFragmentShader("frag.glsl");
	glsl_prog->linkProgram();

	glsl_prog->useProgram();
	float color[3] = {0, 1, 0};
	glsl_prog->setUniform3fv("color", 1, color);
	glsl_prog->unuseProgram();

	glutDisplayFunc(DisplayFunc);
	glutMouseFunc(MouseFunc);
	glutMotionFunc(MotionFunc);
	glutKeyboardFunc(KeyFunc);
	glutTimerFunc(100, TimerFunc, 0);
    glutMainLoop();

	delete glsl_prog;

	return 0;
}

