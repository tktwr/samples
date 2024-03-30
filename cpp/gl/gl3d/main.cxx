#include "myglut.h"
#include <stdlib.h>

int did_init_gl = 0;
int g_w = 640;
int g_h = 480;
GLfloat lmodel_ambient[] = {0, 0, 0, 1};
GLfloat lit0_posW     [] = {0, 10, 0, 1}; // in the world coord
GLfloat lit0_ambient  [] = {1, 1, 1, 1};
GLfloat lit0_diffuse  [] = {1, 1, 1, 1};
GLfloat lit0_specular [] = {1, 1, 1, 1};
GLfloat mat0_ambient  [] = {.2, .2, .2, 1};
GLfloat mat0_diffuse  [] = {.8, .8, .8, 1};
GLfloat mat0_specular [] = {0, 0, 0, 1};
GLfloat mat0_shininess[] = {0};

void f_quit()
{
	exit(0);
}

void f_init_gl()
{
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lmodel_ambient);
	glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE);
	glLightfv(GL_LIGHT0, GL_AMBIENT,  lit0_ambient);
	glLightfv(GL_LIGHT0, GL_DIFFUSE,  lit0_diffuse);
	glLightfv(GL_LIGHT0, GL_SPECULAR, lit0_specular);
	glMaterialfv(GL_FRONT, GL_AMBIENT,   mat0_ambient);
	glMaterialfv(GL_FRONT, GL_DIFFUSE,   mat0_diffuse);
	glMaterialfv(GL_FRONT, GL_SPECULAR,  mat0_specular);
	glMaterialfv(GL_FRONT, GL_SHININESS, mat0_shininess);

	glDepthFunc(GL_LEQUAL);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_NORMALIZE);
	glDisable(GL_LIGHTING);
	glDisable(GL_TEXTURE_2D);
	glDisable(GL_BLEND);
}

void f_draw_objects()
{
	glPushMatrix();
	glTranslatef(0, .5, 0);
	glutSolidSphere(.5, 36, 18);
	glPopMatrix();
}

void f_draw_floor()
{
	glPushMatrix();
	glScalef(5, 5, 5);
	glBegin(GL_QUADS);
	glNormal3f(0, 1, 0);
	glVertex3f(-1, 0, -1);
	glVertex3f(-1, 0,  1);
	glVertex3f( 1, 0,  1);
	glVertex3f( 1, 0, -1);
	glEnd();
	glPopMatrix();
}

void f_draw_scene()
{
	float fovy = 60;
	float nearclip = .1;
	float farclip = 100;

	glClearColor(0, 0, 0, 1);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glViewport(0, 0, g_w, g_h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(fovy, float(g_w)/g_h, nearclip, farclip);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	float p[3] = {0, 0, 0};
	float t[3] = {0, 0, -1};
	float u[3] = {0, 1, 0};
	gluLookAt(p[0], p[1], p[2], t[0], t[1], t[2], u[0], u[1], u[2]);
	glTranslatef(0, -.5, -4);

	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glLightfv(GL_LIGHT0, GL_POSITION, lit0_posW);

	f_draw_objects();
	f_draw_floor();

	glDisable(GL_LIGHTING);
}

void DisplayFunc()
{
	if (!did_init_gl)
	{
		f_init_gl();
		did_init_gl = 1;
	}

	f_draw_scene();

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
	glutInitWindowSize(g_w, g_h);
	glutCreateWindow(argv[0]);

	glutDisplayFunc(DisplayFunc);
	glutMouseFunc(MouseFunc);
	glutMotionFunc(MotionFunc);
	glutKeyboardFunc(KeyFunc);
	//glutTimerFunc(100, TimerFunc, 0);
	glutMainLoop();
	return 0;
}

