#include <Python.h>
/**
 * print_python_list_info - Prints basic info about python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
int sz, alc, a;
PyObject *oj;
sz = Py_SIZE(p);
alc = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", sz);
printf("[*] Allocated = %d\n", alc);
for (a = 0; a < sz; a++)
{
printf("Element %d: ", a);
oj = PyList_GetItem(p, a);
printf("%s\n", Py_TYPE(oj)->tp_name);
}
}
