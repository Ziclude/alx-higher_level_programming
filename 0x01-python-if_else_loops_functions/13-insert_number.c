#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: list head
 * @number: number to store in the new node
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *sprinter;
listint_t *nouv;
sprinter = *head;
nouv = malloc(sizeof(listint_t));
if (nouv == NULL)
return (NULL);
nouv->n = number;
if (*head == NULL || (*head)->n > number)
{
nouv->next = *head;
*head = nouv;
return (nouv);
}
while (sprinter->next != NULL)
{
if ((sprinter->next)->n >= number)
{
nouv->next = sprinter->next;
sprinter->next = nouv;
return (nouv);
}
sprinter = sprinter->next;
}
nouv->next = NULL;
sprinter->next = nouv;
return (nouv);
}
